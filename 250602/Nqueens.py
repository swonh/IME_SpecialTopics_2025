def is_safe(x, row, col):
    # x[0] ~ x[row-1]까지는 이미 배치된 퀸의 열 정보
    for prev_row in range(row):
        # 같은 열이거나, 대각선에 있으면 false
        if x[prev_row] == col or abs(x[prev_row] - col) == abs(prev_row - row):
            return False
    return True

def NQueens(k, x, N, solutions):
    if k == N:
        # 모든 퀸이 배치됨 (0~N-1까지)
        solutions.append(x[:])  # 깊은 복사
        return

    for c in range(N):
        if is_safe(x, k, c):
            x[k] = c  # k행에 c열에 퀸을 놓음
            NQueens(k + 1, x, N, solutions)


def solve_n_queens(N):
    x = [-1] * N        # 각 행마다 퀸이 위치한 열 정보를 저장
    solutions = []      # 가능한 모든 해
    NQueens(0, x, N, solutions)
    return solutions


def print_solution(sol):
    N = len(sol)
    board = [["."] * N for _ in range(N)]
    for row in range(N):
        board[row][sol[row]] = "Q"
    for row in board:
        print(" ".join(row))
    print()


# 예시 실행
N = 8
all_solutions = solve_n_queens(N)
print(f"총 해 수: {len(all_solutions)}개")

# 첫 번째 해 출력
print("첫 번째 해:")
print_solution(all_solutions[0])
