def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if A[j] < A[least] :
                least = j
        A[i], A[least] = A[least], A[i] # 배열 항목 교환
        print(A, i+1)   # 중간 관정 출력용 
        
def insertion_sort(A):
    n = len(A)
    # round: n-1
    for i in range(1, n):
        key = A[i]
        j = i-1
        while j>=0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
        print(A, i)
        
def bubble_sort(A):
    n = len(A)
    # Round: n-1
    for i in range(n-1, 0, -1):
        bChanged = False
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                bChanged = True
                
        if not bChanged: break;
        print(A, n-i)
            
        

        
        
org = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]

data = list(org)
# print("Original  :", org)
# selection_sort(data)
# print("Selection :", data)

# print("Original  :", org)
# insertion_sort(data)
# print("Insertion :", data)


print("Original  :", org)
bubble_sort(data)
print("Bubble :", data)