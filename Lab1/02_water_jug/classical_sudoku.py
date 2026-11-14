import tkinter as tk
import random
def valid(board, r, c, n):
    for i in range(9):
        if board[r][i] == n or board[i][c] == n:
            return False

    sr = (r // 3) * 3
    sc = (c // 3) * 3

    for i in range(sr, sr + 3):
        for j in range(sc, sc + 3):
            if board[i][j] == n:
                return False

    return True


def generate(board):

    for r in range(9):
        for c in range(9):

            if board[r][c] == 0:

                numbers = list(range(1, 10))
                random.shuffle(numbers)

                for n in numbers:

                    if valid(board, r, c, n):
                        board[r][c] = n

                        if generate(board):
                            return True

                        board[r][c] = 0

                return False

    return True


def new_game():

    global board, solution, original, steps

    solution = [[0 for j in range(9)] for i in range(9)]
    generate(solution)

    board = [row[:] for row in solution]

    empty = random.sample(range(81), 40)

    for x in empty:
        r = x // 9
        c = x % 9
        board[r][c] = 0

    original = [row[:] for row in board]

    steps = 0
    count.config(text="Steps: 0")
    status.config(text="New game started!", fg="blue")

    display()


def display():

    for r in range(9):
        for c in range(9):

            cells[r][c].config(state="normal")
            cells[r][c].delete(0, tk.END)

            if board[r][c] != 0:
                cells[r][c].insert(0, str(board[r][c]))

            if original[r][c] != 0:
                cells[r][c].config(state="disabled")
            else:
                cells[r][c].config(fg="blue")


def submit():

    global steps

    try:
        r = int(row_entry.get()) - 1
        c = int(col_entry.get()) - 1
        n = int(num_entry.get())

    except ValueError:
        status.config(text="Enter valid numbers!", fg="red")
        return

    if r < 0 or r > 8 or c < 0 or c > 8 or n < 1 or n > 9:
        status.config(text="Enter values from 1 to 9!", fg="red")
        return

    if original[r][c] != 0:
        status.config(text="Cannot change original numbers!", fg="red")
        return

    if board[r][c] != 0:
        status.config(text="Cell already filled! Erase it first.", fg="red")
        return

    if valid(board, r, c, n):

        board[r][c] = n
        steps += 1

        display()

        count.config(text="Steps: " + str(steps))

        if board == solution:
            status.config(text="Congratulations! Sudoku completed!", fg="green")
        else:
            status.config(text="Correct move!", fg="green")

    else:
        status.config(text="Invalid move!", fg="red")


def erase():

    try:
        r = int(row_entry.get()) - 1
        c = int(col_entry.get()) - 1

    except ValueError:
        status.config(text="Enter valid row and column!", fg="red")
        return

    if r < 0 or r > 8 or c < 0 or c > 8:
        status.config(text="Row and column must be 1 to 9!", fg="red")
        return

    if original[r][c] != 0:
        status.config(text="Cannot erase original numbers!", fg="red")
        return

    if board[r][c] == 0:
        status.config(text="Cell is already empty!", fg="red")
        return

    board[r][c] = 0
    display()

    status.config(text="Number erased!", fg="blue")


root = tk.Tk()
root.title("Sudoku Game")
root.geometry("550x700")
root.resizable(False, False)

title = tk.Label(root, text="SUDOKU",
                 font=("Arial", 25, "bold"))
title.pack(pady=15)

grid = tk.Frame(root)
grid.pack(pady=15)

cells = []

for r in range(9):

    row = []

    for c in range(9):

        cell = tk.Entry(
            grid,
            width=3,
            font=("Arial", 16, "bold"),
            justify="center",
            relief="solid",
            bd=1
        )

        cell.grid(
            row=r,
            column=c,
            padx=(2 if c % 3 == 0 else 0,
                  2 if c % 3 == 2 else 0),
            pady=(2 if r % 3 == 0 else 0,
                  2 if r % 3 == 2 else 0),
            ipady=7
        )

        row.append(cell)

    cells.append(row)


input_frame = tk.Frame(root)
input_frame.pack(pady=15)

tk.Label(input_frame, text="Row:").grid(row=0, column=0)
row_entry = tk.Entry(input_frame, width=5)
row_entry.grid(row=0, column=1, padx=5)

tk.Label(input_frame, text="Column:").grid(row=0, column=2)
col_entry = tk.Entry(input_frame, width=5)
col_entry.grid(row=0, column=3, padx=5)

tk.Label(input_frame, text="Number:").grid(row=0, column=4)
num_entry = tk.Entry(input_frame, width=5)
num_entry.grid(row=0, column=5, padx=5)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Submit",
          command=submit, width=12).grid(row=0, column=0, padx=5)

tk.Button(button_frame, text="Erase",
          command=erase, width=12).grid(row=0, column=1, padx=5)

tk.Button(button_frame, text="New Game",
          command=new_game, width=12).grid(row=0, column=2, padx=5)


status = tk.Label(root, text="Welcome to Sudoku!",
                  font=("Arial", 12))
status.pack(pady=10)

count = tk.Label(root, text="Steps: 0",
                 font=("Arial", 12, "bold"))
count.pack(pady=5)

new_game()
root.mainloop()
