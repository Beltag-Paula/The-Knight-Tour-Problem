# Initialize the chessboard and it's size
chessboard_size = 8
chessboard = [[-1 for i in range(chessboard_size)] for i in range(chessboard_size)]

# Initialize the knight & it's 8 legal possible moves on the chessboard
move_row = [2, 1, -1, -2, -2, -1, 1, 2]
move_col = [1, 2, 2, 1, -1, -2, -2, -1]


def isValidKnightTour(row, col):
    # this function checks if the position[row][col] of the knight is valid inside our chessboard
    if row >= 0 and row >= 0 and row < chessboard_size and col < chessboard_size and chessboard[row][col] == -1:
        return True
    return False


def printKnightRoute():
    # this function will print the Route of the Knight on a chessboard[8][8]
    for i in range(chessboard_size):
        for j in range(chessboard_size):
            print('{:2d}'.format(chessboard[i][j]), end=' ')
        print()


def solveKnightTourBacktracking(current_row, current_col, move_row, move_col, counterKnightSteps):
    if counterKnightSteps == chessboard_size ** 2:
        return True

    # Try all the next moves from the current row and col
    for i in range(8):
        new_move_row = current_row + move_row[i]
        new_move_col = current_col + move_col[i]
        if isValidKnightTour(new_move_row, new_move_col):
            chessboard[new_move_row][new_move_col] = counterKnightSteps
            if solveKnightTourBacktracking(new_move_row, new_move_col, move_row, move_col, counterKnightSteps + 1):
                return True

            # Backtracking
            chessboard[new_move_row][new_move_col] = -1
    return False


def KnightTourMain():
    # This uses the function KnightTourBacktracking:
    # either it returns false if no complete tour is possible
    # or it returns true and prints the tour on the chessboard

    chessboard[0][0] = 0

    counterKnightSteps = 1

    # Checking if solution exists or not
    if not solveKnightTourBacktracking(0, 0, move_row, move_col, counterKnightSteps):
        print("Solution doesn't exist")
    else:
        printKnightRoute()


if __name__ == "__main__":

    KnightTourMain()
