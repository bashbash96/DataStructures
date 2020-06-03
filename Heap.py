class MinHeap:
    def __init__(self):
        self.heap = [0]

    def insert(self, data):
        self.heap.append(data)
        self.bottomUpHeapify()

    def extractMin(self):
        if len(self.heap) < 2:
            return None
        elif len(self.heap) == 2:
            return self.heap.pop()

        data = self.heap[1]

        self.heap[1] = self.heap.pop()

        self.topDownHeapify()

        return data

    def bottomUpHeapify(self):
        currIdx = len(self.heap) - 1
        parent = currIdx // 2

        while parent > 0 and self.heap[parent] > self.heap[currIdx]:
            self.heap[parent], self.heap[currIdx] = self.heap[currIdx], self.heap[parent]
            currIdx = parent
            parent = currIdx // 2

    def topDownHeapify(self):
        curr = 1
        left, right = curr * 2, (curr * 2) + 1

        while left < len(self.heap) or right < len(self.heap):

            minIdx = self.getMin(curr, left, right)

            if minIdx == curr:
                return

            self.heap[curr], self.heap[minIdx] = self.heap[minIdx], self.heap[curr]

            curr = minIdx
            left, right = curr * 2, (curr * 2) + 1

    def getMin(self, curr, left, right):
        minIdx = curr
        if left < len(self.heap) and self.heap[left] < self.heap[minIdx]:
            minIdx = left
        if right < len(self.heap) and self.heap[right] < self.heap[minIdx]:
            minIdx = right

        return minIdx

    def peek(self):
        if len(self.heap) < 2:
            return None

        return self.heap[1]

    def size(self):
        return len(self.heap) - 1

    def printHeap(self):

        for i in range(1, len(self.heap)):
            print(self.heap[i], end=' ')
        print()


def heapSort(arr):
    H = MinHeap()
    while len(arr) > 0:
        H.insert(arr.pop)

    while H.size() > 0:
        arr.append(H.extractMin())

    # time O(n log(n))
    # space O(1)
