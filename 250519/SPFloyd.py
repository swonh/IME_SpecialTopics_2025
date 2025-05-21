# 코드 11.16: Floyd 알고리즘
INF = 9999
def printA(A):
    vsize = len(A)
    print("====================================")
    for i in range(vsize) :
        for j in range(vsize) :
            if (A[i][j] == INF) :
                print(" INF ", end='')
            else :
                print("%4d "%A[i][j], end='')
        print("");

def shortest_path_floyd(vertex, adj) :
    vsize = len(vertex)         # 정점의 개수

    A = list(adj)			    # 2차원 배열(리스트의 리스트)의 복사
    for i in range(vsize) :
        A[i] = list(adj[i])

    for k in range(vsize) :
        for i in range(vsize) :
            for j in range(vsize) :
                if (A[i][k] + A[k][j] < A[i][j]) :
                    A[i][j] = A[i][k] + A[k][j]
        printA(A)				# 진행상황 출력용 


if __name__ == "__main__":
    # Shortest Path를 위한 Weighted Graph
    vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
    weight = [ [0,	    7,		INF,	INF,	3,      10,		INF],
               [7,		0,	    4,		10,	    2,	    6,	    INF],
               [INF,	4,		0,	    2,		INF,	INF,	INF],
               [INF,	10,     2,		0,      11,		9,	    4   ],
               [3,	    2,	    INF,   11,		0,      13,		5   ],
               [10,		6,	    INF,	9,      13,		0,	    INF],
               [INF,    INF,	INF,   4,		5,		INF,	0   ]]    

    print("Shortest Path By Floyd's Algorithm")
    shortest_path_floyd(vertex, weight)