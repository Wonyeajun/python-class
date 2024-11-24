class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class MiniHeap:
    def __init__(self):
        self.root = None  # 루트 노드
        self.last = None  # 마지막 삽입된 노드


    def find_insertion_point(self):
        """새 노드를 삽입할 위치를 찾아 반환"""
        from collections import deque
        Que = deque()
        Que.append(self.root)
        while Que:
            current = Que.popleft()
            if not current.left:
                return current, "left"
            elif not current.right:
                return current, "right"
            else:
                Que.append(current.left)
                Que.append(current.right)

    def _find_last_node(self):
        """마지막 노드를 찾아 반환"""
        from collections import deque
        Que = deque()
        Que.append(self.root)
        last = None
        while Que:
            last = Que.popleft()
            if last.left:
                Que.append(last.left)
            if last.right:
                Que.append(last.right)
        return last

    def _heapify_up(self, node):
        """삽입 후 위로 올라가며 힙 속성을 유지"""
        while node.parent and node.data < node.parent.data:
            node.data, node.parent.data = node.parent.data, node.data
            node = node.parent

    def _heapify_down(self, node):
        """삭제 후 아래로 내려가며 힙 속성을 유지"""
        while node:
            smallest = node
            if node.left and node.left.data < smallest.data:
                smallest = node.left
            if node.right and node.right.data < smallest.data:
                smallest = node.right

            if smallest != node:
                node.data,smallest.data = smallest.data, node.data
                node = smallest
            else:
                break

    def insert(self, data):
        """새 노드를 힙에 삽입"""
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            self.last = new_node
        else:
            parent, direction = self.find_insertion_point()
            if direction == "left":
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self._heapify_up(new_node)
            self.last = new_node

    def remove(self):
        """최소값(루트 노드)을 제거하고 반환"""
        if not self.root:
            raise IndexError("Heap is empty")
        min_value = self.root.data
        if self.root == self.last:
            self.root = None
            self.last = None
        else:
            # 마지막 노드와 루트 노드 교체
            last_node = self._find_last_node()
            self.root.data, last_node.data = last_node.data, self.root.data

            # 마지막 노드 제거
            if last_node.parent.left == last_node:
                last_node.parent.left = None
            else:
                last_node.parent.right = None

            self.last = self._find_last_node()  # 새로운 마지막 노드 설정
            self._heapify_down(self.root)  # 루트에서 힙 속성 복구

        return min_value



data = [53, 1, 15, 47, 83, 90, 46, 26, 50, 2, 55, 78, 49, 63, 40, 33, 38, 39, 19, 45]
miniheap = MiniHeap()

# 데이터 삽입
for d in data:
    miniheap.insert(d)

# 최소값 제거 및 출력
for _ in range(len(data)):
    print(miniheap.remove(), end=' ')
