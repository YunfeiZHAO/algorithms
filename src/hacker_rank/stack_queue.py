"""question related to stacks and queues"""
from collections import namedtuple, deque

def largestRectangle(h):
    """ h is an array of heights, find the larges surface that
        you can achieve with k consecutive elements in h
        k * min(h[i], h[i+1],...,h[i+k-1])

        This is a two pointer method, that for each element,
        we find the farest left and right side that is bigger or equal
        to the element and calculate the surface.
        O(n^2)
        the worst case is all elements are equal.
    """
    n = len(h)
    max_surf = 0
    for i, v in enumerate(h):
        l = i
        r = i
        while l >= 0 and h[l] >= v:
            l -= 1
        while r < n and h[r] >=v:
            r += 1
        cur_surf = (r-l-1) * v
        if cur_surf > max_surf:
            max_surf = cur_surf
    return max_surf

def calculate_spans(arr):
    """
        Given an integer array of size , 
        find the maximum of the minimum(s) of every window size in the array.
        The window size varies from 1 to len(arr).
    """
    n = len(arr)
    left_span = [-1] * n
    right_span = [n] * n
    
    stack = []

    # Calculate left span
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        left_span[i] = stack[-1] if stack else -1
        stack.append(i)
        
    stack = []

    # Calculate right span
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        right_span[i] = stack[-1] if stack else n
        stack.append(i)
        
    return left_span, right_span

def riddle(arr):
    n = len(arr)
    left_span, right_span = calculate_spans(arr)
    
    result = [0] * (n + 1)
    
    for i in range(n):
        length = right_span[i] - left_span[i] - 1
        result[length] = max(result[length], arr[i])

    # Fill the result for each window size where there isn't a direct minimum.
    for i in range(n - 1, 0, -1):
        result[i] = max(result[i], result[i + 1])
        
    return result[1:]



Pos = namedtuple('Position', ['x', 'y'])

def minimumMoves(grid, startX, startY, goalX, goalY):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    q = deque()
    
    q.append(Pos(startX, startY))
    visited[startX][startY] = True
    steps = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        for _ in range(len(q)):
            current = q.popleft()
            if current.x == goalX and current.y == goalY:
                return steps

            for dx, dy in directions:
                x, y = current.x, current.y
                while True:
                    x += dx
                    y += dy
                    if not (0 <= x < n and 0 <= y < n):
                        break
                    if grid[x][y] == 'X':
                        break
                    if visited[x][y]:
                        continue
                    visited[x][y] = True
                    q.append(Pos(x, y))
        steps += 1

    return -1


if __name__ == '__main__':
    grid = ['.X.','.X.', '...']
    startX, startY, goalX, goalY = 0,0,0,2
    print(minimumMoves(grid, startX, startY, goalX, goalY))