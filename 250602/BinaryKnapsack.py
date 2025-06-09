def frac_knapsack(start, remaining_size):
    """남은 Item들로 계산한 fractional knapsack의 upper bound"""
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
    # 전역변수를 수정하기 위해 global 키워드 사용 (MP, best_x)
    global MP, best_x

    if i >= n or size <= 0:
        current_profit = p_v()
        if current_profit > MP:
            MP = current_profit # MP 값 업데이트
            best_x = x[:] # 최종 솔루션 도출
        return

    pv = p_v() # 현재 총 가치 계산

    # Case 1: x[i] = 1 (선택함)
    if S[i] <= size:
        bound = frac_knapsack(i + 1, size - S[i]) # Fractional knapsack 문제를 풀어 목적함수 값의 상한 계산
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

# 코드 실행 부분
# Item 정보: (가치 P[i], 무게 S[i])
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
print("선택된 Item (0/1):", best_x)
