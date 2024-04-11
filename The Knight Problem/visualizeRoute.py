import tkinter as tk

# Initialize the chessboard size
chessboard_size = 8

# Initialize the knight & its 8 legal possible moves on the chessboard
move_row = [2, 1, -1, -2, -2, -1, 1, 2]
move_col = [1, 2, 2, 1, -1, -2, -2, -1]


def isValidKnightTour(row, col, chessboard):
    # Check if the position (row, col) of the knight is valid inside the chessboard
    if 0 <= row < chessboard_size and 0 <= col < chessboard_size and chessboard[row][col] == -1:
        return True
    return False


def solveKnightTourBacktracking(current_row, current_col, move_row, move_col, counterKnightSteps, chessboard, canvas):
    if counterKnightSteps == chessboard_size ** 2:
        return True

    # Try all the next moves from the current row and col
    for i in range(8):
        new_move_row = current_row + move_row[i]
        new_move_col = current_col + move_col[i]
        if isValidKnightTour(new_move_row, new_move_col, chessboard):
            chessboard[new_move_row][new_move_col] = counterKnightSteps
            canvas.create_text(new_move_col * 50 + 25, new_move_row * 50 + 25, text=str(counterKnightSteps),
                               fill="black", font=("Arial", 12, "bold"))
            canvas.update()  # Update the canvas to show the change

            if solveKnightTourBacktracking(new_move_row, new_move_col, move_row, move_col, counterKnightSteps + 1,
                                           chessboard, canvas):
                return True

            # Backtracking
            canvas.create_rectangle(new_move_col * 50, new_move_row * 50, (new_move_col + 1) * 50,
                                     (new_move_row + 1) * 50, fill="white")
            chessboard[new_move_row][new_move_col] = -1
            canvas.update()  # Update the canvas to show the change

    return False


def KnightTourMain():
    # Initialize the chessboard
    chessboard = [[-1 for _ in range(chessboard_size)] for _ in range(chessboard_size)]
    chessboard[0][0] = 0

    # Create a Tkinter window
    root = tk.Tk()
    root.title("Knight's Tour Backtracking")

    # Create a canvas to draw the chessboard and knight's tour
    canvas = tk.Canvas(root, width=chessboard_size * 50, height=chessboard_size * 50)
    canvas.pack()

    # Draw the chessboard
    for i in range(chessboard_size):
        for j in range(chessboard_size):
            color = "white" if (i + j) % 2 == 0 else "blue"
            canvas.create_rectangle(j * 50, i * 50, (j + 1) * 50, (i + 1) * 50, fill=color)

    # Start the knight's tour
    solveKnightTourBacktracking(0, 0, move_row, move_col, 1, chessboard, canvas)

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    KnightTourMain()
