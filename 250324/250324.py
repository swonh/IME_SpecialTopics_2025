class ArrayList:
    # 리스트의 데이터: 생성자에서 정의 및 초기화
    def __init__(self, capacity=100):
        self.capcity = capacity
        self.array = [None]*capacity
        self.size = 0
    
    # 리스트의 연산: 클래스의 메소드
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else: return None
        
    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1
        else : pass
    