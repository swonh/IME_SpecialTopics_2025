# 최대값 찾기
def find_max(A):
    max_val = 0
    for i in range(len(A)):
        if max_val < A[i]:
            max_val = A[i]
    return max_val

A = [1, 20, 30, 3]
print(find_max(A))

