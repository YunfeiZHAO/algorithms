""" graphe problem"""
from collections import defaultdict, Counter, deque
import math

def find_linked_subgraph(graph, start, remain_cities):
    """ dfs update all linked elements of start into visited set """
    stack = [start]
    while stack:
        city = stack.pop()
        if city in remain_cities:
            remain_cities.remove(city)
            stack.extend(graph[city])


def roadsAndLibraries(n, c_lib, c_road, cities):
    """ build library to give all cites access to the library
        Args:
            n: number of cities.
            c_lib: cost of building a library.
            c_road: cost of building a road.
            cities list[list]: the potentially routes to build between two cites.
        we want to minimize the cost to give access if library to all cites.
        bfs method
    """
    # find all linked cities groups
    # each group of size m need m - 1 number of roads
    if c_lib <= c_road:
        return n * c_lib
    remain_cities = {i for i in range(1,n+1)}
    n_group = 0
    graph = defaultdict(list)
    for u, v in cities:
        graph[u].append(v)
        graph[v].append(u)
    while remain_cities:
        next_city = next(iter(remain_cities))
        find_linked_subgraph(graph, next_city, remain_cities)
        n_group += 1
    n_road = n - n_group

    p1 = n_road * c_road + c_lib * n_group
    p2 = c_lib * n

    return min(p1, p2)

def roadsAndLibraries_uf(n, c_lib, c_road, cities):
    """ union and find method"""
    # the first element is the placeholder
    parents = [0] + list(range(1, n+1))
    weights = {i:1 for i in range(1, n+1)}

    def find(c):
        while parents[c] != c:
            parents[c] = parents[parents[c]]
            c = parents[c]
        return c

    def union(u, v):
        p_u = find(u)
        p_v = find(v)
        if p_u == p_v:
            return
        p_uw = weights[p_u]
        p_vw = weights[p_v]
        if p_uw > p_vw:
            p_u, p_v = p_v, p_u
        parents[p_v] = p_u
        weights[p_u] = p_uw + p_vw
        del weights[p_v]
    for u,v in cities:
        union(u,v)

    n_group = len(weights)
    n_road = n - n_group
    p1 = n_road * c_road + c_lib * n_group
    p2 = c_lib * n
    return min(p1, p2)




def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    """ find the shortest path between two nodes in a graph with val
        Args:
            graph_nodes int: node from 1...graph_nodes
            graph_from and graph_to: map these two to get undirected links
            ids: the value of each node
            val: value to search in graph
    """
    # check whether we have two nodes of this value
    dest = [i + 1 for i, v in enumerate(ids) if v == val]
    if len(dest) < 2:
        return -1
    # build the graph
    graph = defaultdict(list)
    for i, v in enumerate(graph_from):
        v_to = graph_to[i]
        graph[v].append(v_to)
        graph[v_to].append(v)
    # get the start node
    min_step = math.inf
    for start in dest[:-1]: # if we have n dest, we set as start for the first n-1
        # BFS to find the path, use bfs to count the steps
        visited = set()
        queue = deque([start])
        step = 0
        while queue:
            child_queue = deque()
            for node in queue:
                if node not in visited:
                    visited.add(node)
                    if ids[node - 1] == val and step > 0:
                        min_step = min(step, min_step)
                    child_queue.extend(graph[node])
            queue = child_queue
            step += 1
    return min_step
                        


                
