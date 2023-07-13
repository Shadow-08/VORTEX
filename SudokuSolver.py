# sudoku solver using recursions and backtracking
# coded by - Ahad Ulla Baig

def solve(grid, row, col):  # function to solve the puzzle

    # this stops backtracking if we reach 8th row and 9th column
    if row == 8 and col == 9:
        return True

    # if we reach 9th column then move to the next row
    if col == 9:
        row += 1
        col = 0

    # if position is not empty then go to the next position
    if grid[row][col] > 0:
        return solve(grid, row, col + 1)

    for n in range(1, 10):

        if valid(grid, row, col, n):  # check for number validity

            # assigning the number to that position
            grid[row][col] = n

            if solve(grid, row, col + 1):  # check other possibilities
                return True

        grid[row][col] = 0  # assign 0 to the wrongly assumed value

    return False


def valid(grid, row, col, n):  # function to check the numbers validity

    for x in range(9):  # check for row validity
        if grid[row][x] == n:
            return False

    for x in range(9):  # check for column validity
        if grid[x][col] == n:
            return False

    # check for 3x3 grid validity
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == n:
                return False

    return True


def answer(arr):  # function to print the grid
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=' ')
        print()


# 0 stands for an empty cell
puzzle = [[0, 3, 6, 0, 0, 5, 0, 0, 0],
          [7, 8, 0, 0, 0, 0, 0, 0, 4],
          [0, 0, 0, 0, 0, 0, 8, 6, 9],
          [9, 0, 0, 0, 5, 0, 0, 4, 0],
          [0, 0, 0, 1, 0, 7, 0, 0, 0],
          [0, 1, 0, 0, 9, 0, 0, 0, 3],
          [1, 9, 3, 0, 0, 0, 0, 0, 0],
          [2, 0, 0, 0, 0, 0, 0, 1, 5],
          [0, 0, 0, 2, 0, 0, 7, 9, 0]]

if solve(puzzle, 0, 0):
    answer(puzzle)
else:
    print('no solution exists')
