# 최대값 찾기
# A = [1, 2, 4, 10, 3]
# 0 ~ 4 
def find_max(A):
    max = 0
    for i in range(A):
        if max < A[i]:
            max = A[i]
    return max

        
