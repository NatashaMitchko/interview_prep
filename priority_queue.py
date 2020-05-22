class MaxHeap:
    def __init__(self, items=[]):
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self._bubble_up()

    def peek(self):
        if self.heap[1]:
            return self.heap[1]

    def pop(self):
        if len(self.heap) > 2:
            self._swap(self.heap[1], self.heap[-1])
            self._float_down()
            return self.heap.pop()
        elif len(self.heap) == 2:
            return self.heap.pop(1)
        else:
            return
    
    def push(self, val):
        self.heap.append(val)
        self._bubble_up()
    
    def _swap(self, position1=1, position2=-1):
        self.heap[position1], self.heap[position2] = self.heap[position2], self.heap[position1]
    
    def _bubble_up(self, index=-1):
        parent = index // 2
        if parent <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.swap(index, parent)
            self._bubble_up(parent)

    def _float_down(self, index=1):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self._swap(index, largest)
            self._float_down(largest)