# 코드 12.8: 퀵 정렬
# 퀵 정렬 알고리즘을 이용해 배열의 left ~ right 항목들을 오름차순으로 정렬하는 함수
def quick_sort(A, left, right) :
	if left<right :						    # 정렬 범위가 2개 이상인 경우
		q = partition(A, left, right)	    # 좌우로 분할 
		quick_sort(A, left, q - 1)		    # 왼쪽 부분리스트를 퀵 정렬
		quick_sort(A, q + 1, right)	    # 오른쪽 부분리스트를 퀵 정렬


# 코드 12.9: 퀵 정렬을 위한 partition() 함수
def partition(A, left, right):
    low = left + 1
    high = right
    pivot = A[left]  # 피벗 설정

    while low < high:  # low와 high가 역전되지 않는 한 반복
        while low <= right and A[low] < pivot:
            low += 1
        while high >= left and A[high] > pivot:
            high -= 1

        if low < high:  # 선택된 두 레코드 교환
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]  # high와 피벗 항목 교환
    return high

if __name__ == "__main__":
    data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
    print("Original  :", data)
    quick_sort(data, 0, len(data)-1)
    print("Quick     :", data)
