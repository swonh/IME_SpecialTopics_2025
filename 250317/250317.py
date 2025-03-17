# Deep copy 실습

# 1. Deepcopy 모듈 사용
import copy
a = [1,2,[3,4]]
b = copy.deepcopy(a)

# 2. Deepcopy 모듈 사용하지 않고 구현하는 방법 (예시시)
a = [1,2,[3,4]]
b = []

for i in range(len(a)):
    if isinstance(a[i], list):
        list = []
        for k in range(len(a[i])):
            list.append(a[i][k])
        b.append(list)
    else:
        b.append(a[i])

b[2][0] = 99


# 코딩 인터뷰 문제 #1: two sum

# 1. Brute force (O(n^2)), 가장 비효율적인 방법
def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = [2, 7, 11, 15]
target = 9

print(two_sum_brute_force(nums, 9))