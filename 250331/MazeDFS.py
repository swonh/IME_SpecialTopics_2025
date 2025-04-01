# 코드 4.7: 미로의 깊이우선탐색 (참고 파일: ch04/MazeStack.py)
from ArrayStack import ArrayStack

map =[[ '1', '1', '1', '1', '1', '1' ],
	  [ 'e', '0', '0', '0', '0', '1' ],
	  [ '1', '0', '1', '0', '1', '1' ],
	  [ '1', '1', '1', '0', '0', 'x' ],
	  [ '1', '1', '1', '0', '1', '1' ],
	  [ '1', '1', '1', '1', '1', '1' ]]
MAZE_SIZE = 6


# 코드 4.7: 갈 수 있는 위치인지를 판단하는 알고리즘 (참고 파일: ch04/MazeStack.py)
def isValidPos(x, y) :		# (x,y)가 갈 수 있는 방인지 검사하는 함수
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE :
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False


def DFS() :			# 깊이우선탐색 함수
    print('DFS: ')
    stack = ArrayStack(100)	# 사용할 덱 객체를 준비
    stack.push((0,1))		# 후단에 시작위치 삽입. (0,1)은 튜플

    while not stack.isEmpty(): 	# 공백이 아닐 동안 
        here = stack.pop()      # 후단에서 항목을 꺼냄(pop) 
        print(here, end='->')
        (x,y) = here

        if (map[y][x] == 'x') :	# 출구이면 성공. True 반환
            return True
        else :
            map[y][x] = '.'	# 현재위치를 지나왔다고 ’.’표시
            if isValidPos(x, y - 1): stack.push((x, y - 1)) # 상
            if isValidPos(x + 1, y): stack.push((x + 1, y)) # 우
            if isValidPos(x, y + 1): stack.push((x, y + 1)) # 하
            if isValidPos(x - 1, y): stack.push((x - 1, y)) # 좌
        print(' 현재 스택: ', stack)
    return False

result = DFS()
if result : print(' --> 미로탐색 성공')
else : print(' --> 미로탐색 실패')