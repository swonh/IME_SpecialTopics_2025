def frac_knapsack(start, remaining_size):
    """남은 물건들로 계산한 분수 knapsack의 upper bound"""
    items = [(P[i], S[i], i) for i in range(start, n)]
    items.sort(key=lambda item: item[0] / item[1], reverse=True)

    total_value = 0
    for p, s, i in items:
        if s <= remaining_size:
            total_value += p
            remaining_size -= s
        else:
            total_value += p * (remaining_size / s)
            break
    return total_value


def p_v():
    return sum(P[i] for i in range(n) if x[i] == 1)


def s_v():
    return sum(S[i] for i in range(n) if x[i] == 1)


def knapsack(i, size):
    global MP, best_x

    if i >= n or size <= 0:
        current_profit = p_v()
        if current_profit > MP:
            MP = current_profit
            best_x = x[:]
        return

    pv = p_v()

    # Case 1: x[i] = 1 (선택함)
    if S[i] <= size:
        bound = frac_knapsack(i + 1, size - S[i])
        if pv + P[i] + bound > MP:
            if pv + P[i] > MP:
                MP = pv + P[i]
                best_x = x[:i] + [1] + x[i + 1:]

            x[i] = 1
            knapsack(i + 1, size - S[i])

    # Case 2: x[i] = 0 (선택하지 않음)
    x[i] = 0
    bound = frac_knapsack(i + 1, size)
    if pv + bound > MP:
        knapsack(i + 1, size)


# 물건 정보: (가치 P[i], 무게 S[i])
P = [15, 16, 6]
S = [3, 4, 2]
n = len(P)
capacity = 5

# 현재까지 찾은 최대 이익
MP = 0
# 최적해에 대응하는 선택 벡터
best_x = [0] * n
# 현재 탐색 중 선택 벡터
x = [0] * n

# 실행
knapsack(0, capacity)

# 결과 출력
print("최대 이익:", MP)
print("선택된 물건 (0/1):", best_x)
