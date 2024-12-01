""" Graph problems solution """
from collections import defaultdict, deque
from typing import List

class EvaluateDivision:
    """ 399 https://leetcode.com/problems/evaluate-division/"""
    def bfs(self, query):
        c, d = query
        if c not in self.adj or d not in self.adj:
            return -1
        queue, visit = deque(), set()
        queue.append((c, 1))
        while queue:
            s, v = queue.popleft()
            if s == d:
                return v
            for n, w in self.adj[s]:
                if n not in visit:
                    queue.append((n, w*v))
                    visit.add(n)
        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a,b = eq
            val = values[i]
            adj[a].append((b, val))
            adj[b].append((a, 1/val))
        self.adj = adj
        return [self.bfs(q) for q in queries]


class CourseSchedule:
    """ Course Schedule problems"""
    def dfs_canFinish(self, crs):
        if crs in self.cycle_set:
            return False
        if not self.preMap[crs]:
            return True
        self.cycle_set.add(crs)
        for pre in self.preMap[crs]:
            if not self.dfs_canFinish(pre):
                return False
        # checked, so no longer in the circle_set
        self.cycle_set.remove(crs)
        # checked, no need in the preMap
        self.preMap[crs] = []
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """ 207 https://leetcode.com/problems/course-schedule/ """
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        self.cycle_set = set()
        self.preMap = preMap
        for crs in range(numCourses):
            if not self.dfs_canFinish(crs):
                return False
        return True

    def dfs_findOrder(self, crs):
        # If the course is in the cycle set, we've detected a cycle
        if crs in self.cycle_set:
            return False
        # If the course has already been visited, skip it
        if crs in self.visited:
            return True
        # Mark the course as part of the current cycle
        self.cycle_set.add(crs)
        # Visit all prerequisites
        for pre in self.preMap[crs]:
            if not self.dfs_findOrder(pre):
                return False
        # No cycle detected, mark this course as processed
        self.cycle_set.remove(crs)
        self.visited.add(crs)
        self.result.append(crs)
        self.preMap[crs] = []
        
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """ 210 https://leetcode.com/problems/course-schedule-ii/ """
        # Build the adjacency list
        self.preMap = defaultdict(list)
        for crs, pre in prerequisites:
            self.preMap[crs].append(pre)
        
        # Initialize sets and result list
        self.cycle_set = set()  # To track courses in the current recursion stack
        self.visited = set()    # To track fully processed courses
        self.result = []        # To store the valid course order
        
        # Attempt to visit all courses
        for crs in range(numCourses):
            if crs not in self.visited:
                if not self.dfs_findOrder(crs):
                    return []  # Return an empty list if a cycle is detected
        
        # The result list contains the courses in reverse order
        return self.result