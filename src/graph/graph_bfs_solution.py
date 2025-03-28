""" Graph bfs problems solution """
from collections import defaultdict, deque
from typing import List


class SnakesAndLadders:
    """ 909 https://leetcode.com/problems/snakes-and-ladders/ """
    def get_index(self, x, y):
        n = self.n
        line = n - x
        pair = line % 2
        base = n * (line - 1)
        index = base + y + 1 if pair == 1 else base + n - y
        return index

    def get_pos(self, index):
        n = self.n
        line = (index - 1) // n + 1
        m = (index - 1)  % n
        pair = line % 2
        y = m if pair == 1 else n - m -1
        x = n - line
        return (x, y)

    def next(self, cur, step):
        index = min(cur + step, self.n ** 2)
        x, y = self.get_pos(index)
        index = slide if (slide := self.board[x][y]) != -1 else index
        return index

    def bfs(self):
        queue = deque([1])
        visited = set([1])
        rolls = 0
        while queue:
            for _ in range(len(queue)):
                cur_index = queue.popleft()
                if cur_index == self.n ** 2:
                    return rolls
                next_steps = [
                    next_index
                    for i in range(1,7)
                    if (next_index := self.next(cur_index, i)) not in visited]
                queue.extend(next_steps)
                visited.update(next_steps)
            rolls += 1
        return -1

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        self.n = len(board)
        self.board = board
        return self.bfs()

