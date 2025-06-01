import time  # 시간 측정을 위한 모듈

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()
    print()


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None


def is_safe(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


# Node counter
node_counter = 0


def solve_sudoku(board):
    global node_counter
    node_counter += 1
    if node_counter % 10000 == 0:
        print(f"Visited nodes: {node_counter}")

    row, col = find_empty_cell(board)
    if row is None:
        return True

    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            
    board[row][col] = 0
    return False


# Sample board
sudoku_board = [
    [9, 0, 7, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 8, 5],
    [0, 0, 1, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 7, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 1, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 7, 3],
    [0, 0, 2, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 9]
]

print("Input Sudoku:")
print_board(sudoku_board)

start_time = time.time()

if solve_sudoku(sudoku_board):
    elapsed = time.time() - start_time
    print(f"\nSolved Sudoku (total visited nodes: {node_counter}):")
    print_board(sudoku_board)
    print(f"🕒 Solving time: {elapsed:.4f} seconds")
else:
    print("No solution found.")
