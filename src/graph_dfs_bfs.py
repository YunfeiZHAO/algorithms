"""graph questions"""
from collections import defaultdict

def min_clique(num_nodes, num_edges):
    """ given a node number and edges number, return the 
        minimum clique in the graphe
        Turán's Theorem
    """
    pass


def maximum_detonation(bombs: list[list[int]]) -> int:
    """ https://leetcode.com/problems/detonate-the-maximum-bombs
        We can not union find here as this a directional graph.
        The explosion radius are different.
    """
    # build graph
    n = len(bombs)
    graph = defaultdict(list)
    for i in range(n - 1):
        for j in range(i+1, n):
            x1, y1, r1 = bombs[i]
            x2, y2, r2 = bombs[j]
            dist_2 = (x2-x1)**2 + (y2-y1)**2
            if dist_2 <= r1**2:
                graph[i].append(j)
            if dist_2 <= r2**2:
                graph[j].append(i)
    # count generated explosion
    def dfs(node, visited):
        """ count the number of bombs that will explode"""
        if node in visited:
            return 0
        children = graph[node]
        cur = 1
        visited.add(node)
        if children:
            for child in graph[node]:
                cur += dfs(child, visited)
        return cur

    max_count = 1
    for i in range(n):
        count = dfs(i, set())
        max_count = max(count, max_count)
    return max_count


def count_battleships(board: list[list[str]]) -> int:
    """ count boats
        https://leetcode.com/problems/battleships-in-a-board
        mark the visited place on the board
    """
    mark = "_"
    m = len(board)
    n = len(board[0])
    count = 0
    def dfs(x, y):
        # edge check
        if x < 0 or y <0 or x >=m or y>=n:
            return
        val = board[x][y]
        # if visited or not a battleship
        if val in {".", mark}:
            return
        if val == "X":
            # mark as visited
            board[x][y] = mark
            # check the neighbors
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
    for i in range(m):
        for j in range(n):
            if board[i][j] == "X":
                count += 1
                dfs(i, j)
    return count
