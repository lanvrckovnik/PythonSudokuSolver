import numpy as np
#----------YOUR-SUDOKU:--------------------------------------
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]
#-----------OR-FILL-IT-IN-IN-THE-PROGRAM------------------------

g = input("Do you want to overwrite the grid?[y/n]")
if g == "y":
        for j in range(9):
            correct = False
            while not correct:
                row = input(f"Row {j+1}:")
                if len(row) == 9:
                    correct = True
                else:
                    print("Incorrectly written, please try again.")
            count = 0
            for i in row:
                grid[j][count] = int(i)
                count += 1
else:
        ""

print("YOUR GRID: ")
print(np.matrix(grid))

def possible(y, x, n):
        global grid
        for i in range(0,9):
                if grid[y][i] == n:
                        return False
        for i in range(0,9):
                if grid[i][x] == n:
                        return False
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0,3):
                for j in range(0,3):
                        if grid[y0+i][x0+j] == n:
                                return False
        return True

def solve():
        global grid
        for y in range(9):
                for x in range(9):
                        if grid[y][x] == 0:
                                for n in range(1,10):
                                        if possible(y,x,n):
                                                grid[y][x] = n
                                                solve()
                                                grid[y][x] = 0
                                return
        print()
        print("SOLUTION:")
        print(np.matrix(grid))
        input("More solutions?")
solve()

print("No more solutions!")
input("Press ENTER to continue...")


