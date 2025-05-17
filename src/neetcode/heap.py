""" Heap """
from typing import List


class KthLargest:
    """ https://neetcode.io/problems/kth-largest-integer-in-a-stream
        Implementation of heapq
    """

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        self.heapify(nums)
    
    def up(self):
        i = len(self.heap) - 1
        while (parent := (i-1)//2) >= 0:
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                return

    def down(self):
        i = 0
        n = len(self.heap)
        while True:
            smallest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and self.heap[l] < self.heap[smallest]:
                smallest = l
            if r < n and self.heap[r] < self.heap[smallest]:
                smallest = r
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def heapify(self, l):
        for x in l:
            self.heap.append(x)
            self.up()
            if len(self.heap) > self.k:
                self.heap[0] = self.heap.pop()
                self.down()

    def heappush(self, x):
        self.heap.append(x)
        self.up()

    def add(self, val: int) -> int:
        self.heappush(val)
        if len(self.heap) > self.k:
            self.heap[0] = self.heap.pop()
            self.down()
        return self.heap[0]
