
# 코드 8.14: 최대힙의 삽입 알고리즘         참고 코드: ch08/MaxHeap.py
def heappush(heap, n) :
    heap.append(n)		    # 맨 마지막 노드로 일단 삽입
    i = len(heap)-1			# 노드 n의 위치
    while i != 1 :          # n이 루트가 아니면 up-heap 진행
        pi = i//2           # 부모 노드의 위치
        if n <= heap[pi]:   # 부모보다 작으면 up-heap 종료
            break
        heap[i] = heap[pi]	# 부모를 끌어내림
        i = pi			    # i가 부모의 인덱스가 됨
    heap[i] = n			    # 마지막 위치에 n 삽입


# 코드 8.15: 최대힙의 삭제 알고리즘         참고 코드: ch08/MaxHeap.py
def heappop(heap) :
    size = len(heap) - 1    # 노드의 개수
    if size == 0 :          # 공백상태
       return None

    root = heap[1]		    # 삭제할 루트 노드(사장)
    last = heap[size]	    # 마지막 노드(말단사원)
    pi = 1                  # 부모 노드의 인덱스
    i = 2                   # 자식 노드의 인덱스

    while (i <= size):	    # 마지막 노드 이전까지
        if i<size and heap[i] < heap[i+1]:  # right가 더 크면 i를 1 증가 (기본은 왼쪽 노드)
            i += 1          # 비교할 자식은 오른쪽 자식
        if last >= heap[i]: # 자식이 더 작으면 down-heap 종료
            break
        heap[pi] = heap[i]  # 아니면 down-heap 계속
        pi = i              
        i *= 2

    heap[pi] = last	        # 맨 마지막 노드를 parent위치에 복사
    heap.pop()		        # 맨 마지막 노드 삭제
    return root			    # 저장해두었던 루트를 반환

# 코드 12.3: 최대힙을 이용한 힙 정렬 알고리즘
def heapSort1(data):
    heap = [0]
    for e in data :			    # 모든 데이터를 힙에 삽입
        heappush(heap, e)

    for i in range(1, len(data)+1) :
        data[-i] = heappop(heap)


############################################################
# 코드 12.4: 배열을 최대힙으로 바꾸는 heapify 함수
def heapify(arr, n, i): 
    largest = i         # Initialize largest as root 
    l = 2 * i + 1       # left = 2*i + 1 
    r = 2 * i + 2       # right = 2*i + 2 
  
    if l < n and arr[i] < arr[l]: largest = l 
    if r < n and arr[largest] < arr[r]:  largest = r 
  
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        heapify(arr, n, largest) 
  
# 코드 12.5: 제자리 정렬로 구현된 힙 정렬
def heapSort(arr): 
    n = len(arr) 
  
    print("i=", 0, arr)
    for i in range(n//2, -1, -1): 
        heapify(arr, n, i) 
        print("i=", i, arr)
  
    print()
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 
        print("i=", i, arr)

############################################################
# 힙 테스트 프로그램
if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]		# 힙에 삽입할 데이터
    print("최대힙 이용")
    print("정렬전:", data)
    heapSort1(data)
    print("정렬후:", data)

    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]		# 힙에 삽입할 데이터
    print("\n제자리 정렬")
    print("정렬전:", data)
    heapSort(data)
    print("정렬후:", data)