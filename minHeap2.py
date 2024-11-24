class MinHeap:
    def __init__(self):
        self.heap = [float('-inf')]
        self.size = 0

    def insert(self,data):
        self.size += 1
        # 1. 제일 마지막 터미널 노드에 데이터 삽입, 터미널 노드 = 자식 노드가 없는 가장 낮은 레이어의 노드
        self.heap.append(data)
        # 2. 삽입 노드와 부모 노드 비교 및 교환
        idx = len(self.heap) - 1 # 삽입 노드의 인덱스
        while self.heap[idx//2] > self.heap[idx]:
            self.heap[idx], self.heap[idx//2] = self.heap[idx//2], self.heap[idx]
            idx //= 2

    def remove(self):
        # 트리가 비어있는 경우 None 리턴
        if len(self.heap) == 1:
            return None
        self.size -= 1
        # 1. 루트 노드의 값을 저장
        data = self.heap[1]

        #2. 가장 마지막 터미널 노드의 값을 루트 노드에 복사
        self.heap[1] = self.heap[-1]
        self.heap.pop()

        #3. 루트 노드부터 출발하여 자식과 비교해 더 작은 자식들과 위치를 교환
        idx = 1 #현재 노드의 인덱스
        while True:
            #왼쪽 자식 노드의 인덱스
            c_idx = idx * 2
            # 오른쪽 자식 노드가 존재하면서 더 작으면 오른쪽 자식 노드 선택
            if c_idx +1 < len(self.heap):
                if self.heap[c_idx] > self.heap[c_idx +1]:
                    c_idx += 1

            # 인덱스 범위가 벗어나거나 자식보다 부모가 더 작으면 멈춤
            if c_idx >= len(self.heap) or self.heap[c_idx] > self.heap[idx]:
                break
            # 선택한 자식 노드와 현재 노드 교환
            self.heap[idx], self.heap[c_idx] = self.heap[c_idx], self.heap[idx]
            idx = c_idx

        # 마지막으로 데이터 반환
        return data

    def getSize(self):
        return self.size

data = [53, 1, 15, 47, 83, 90, 46, 26, 50, 2, 55, 78, 49, 63, 40, 33, 38, 39, 19, 45]
miniheap = MinHeap()

# 데이터 삽입
for d in data:
    miniheap.insert(d)

# 최소값 제거 및 출력
for _ in range(len(data)):
    print(miniheap.remove(), end=' ')
