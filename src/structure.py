""" Some data structure implementation """

class MyCircularQueue:
    """ Design circular queue
    https://leetcode.com/problems/design-circular-queue/
    [Datadog]
    The circular queue is a linear data structure in which
    the operations are performed based on FIFO (First In First Out) principle,
    and the last position is connected back to the first position to make a circle.
    It is also called "Ring Buffer".
    """
    def __init__(self, k: int):
        self.front = 0
        self.back = -1
        self.k = k
        self.size = 0
        self.q = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): # cannot enqueue
            return False

        self.back = (self.back + 1) % self.k
        self.q[self.back] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): # cannot dequeue
            return False
        
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]    

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.back]  

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k