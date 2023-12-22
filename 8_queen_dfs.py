import tkinter as tk
import random
import time

board_size = 8

# checking current queen position to see if it is safe
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n, canvas):
    board = [-1] * n
    initial_state = list(range(n)) # random starting point on first row
    random.shuffle(initial_state)
# dfs/backtracking to work through to find solution
    def dfs(row):
        if row == n:
            return board[:]
        for col in initial_state:
            if is_safe(board, row, col):
                board[row] = col
                canvas.delete("queens")
                draw_chessboard(canvas, board)
                canvas.update()
                time.sleep(0.1) 
                solution = dfs(row + 1)
                if solution is not None:
                    return solution
                board[row] = -1
        return None

    solution = dfs(0)
    return solution
# referenced a lot of online code to figure out how to draw this
def draw_chessboard(canvas, board):
    for row in range(board_size):
        for col in range(board_size):
            color = "light blue" if (row + col) % 2 == 0 else "light gray"
            canvas.create_rectangle(col * 40, row * 40, (col + 1) * 40, (row + 1) * 40, fill=color)

    for row, col in enumerate(board):
        x = col * 40 + 20
        y = row * 40 + 20
        canvas.create_text(x, y, text="♕", font=("Helvetica", 40), fill="red")
# solve button to start a new solution
def solve():
    solution = solve_n_queens(board_size, canvas)
    draw_chessboard(canvas, solution)

root = tk.Tk()
root.title("8-Queens Visualizer")

canvas = tk.Canvas(root, width=board_size * 40, height=board_size * 40)
canvas.pack()

solve_button = tk.Button(root, text="Solve", command=solve)
solve_button.pack()

root.mainloop()