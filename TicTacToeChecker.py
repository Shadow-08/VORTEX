# tic-tac-toe board checker
# returns 1 if 'X' won
# returns 2 if 'O' won
# returns 0 if it's a draw
# returns -1 if board is unsolved
# coded by Ahad Ulla Baig

def checker(arr):

    for n in range(3):
        if arr[n][0] == arr[n][1] == arr[n][2] != 0:  # horizontal check
            return arr[n][0]
        if arr[0][n] == arr[1][n] == arr[2][n] != 0:  # vertical check
            return arr[0][n]

    if arr[0][0] == arr[1][1] == arr[2][2] != 0:  # right diagonal check
        return arr[0][0]

    if arr[0][2] == arr[1][1] == arr[2][0] != 0:  # left diagonal check
        return arr[0][2]

    if 0 not in arr[0] and 0 not in arr[1] and 0 not in arr[2]:  # draw check
        return 0

    return -1
