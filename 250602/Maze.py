def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 0 and not visited[x][y]


def find_way(x, y):
    if x == n - 1 and y == n - 1:
        path.append((x, y))
        return True

    if not is_valid(x, y):
        return False

    visited[x][y] = True
    path.append((x, y))

    # ↓ 아래로 이동
    if find_way(x + 1, y):
        return True
    # → 오른쪽으로 이동
    if find_way(x, y + 1):
        return True

    # dead end → backtrack
    path.pop()
    return False

# 0: 이동 가능, 1: 벽
maze = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 0]
]

n = len(maze)
visited = [[False] * n for _ in range(n)]
path = []  # 지나온 경로 저장

# 실행
if find_way(0, 0):
    print("✅ 경로 찾음:")
    print(" -> ".join(map(str, path)))
else:
    print("❌ 탈출 경로 없음.")