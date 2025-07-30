""" 
union and find is a good algoritmn to group the nodes (linked) in a undirected graph
For Weighted Union Find (also know as, union find by rank) without path compression, 
    time complexity for both union() and find() = O(logN).
For Weighted Union Find (also known as, union find by rank) with path compression,
    time complexity for both union() and find() = O(α(N)) ≈ O(1), 
    where α is the inverse of the Ackerman function.

https://www.thealgorists.com/Algo/UsefulDataStructures/UnionFind
"""

class UnionFind():
    """ Weighted Union Find with Path Compression OR Union Find by Rank with Path Compression"""
    def __init__(self):
        """ create the dict to store parent and weights"""
        self.parents = {}
        self.weights = {}

    def add(self, item):
        """ Initialise the parent to itself and weight to 1"""
        self.parents[item] = item
        self.weights[item] = 1


def max_difference(g_nodes:int, g_from:list, g_to:list):
    """
    In an undirected graph, a connected component of the graph is any group of connected nodes.
    For each connected component, the differece is the max_value - min_value in the component.
    Find the maximum difference
    Args:
        g_nodes: the nodes [0,1,2,3, ... , g_nodes - 1]
        g_from: [0, 2]
        g_to: [1, 5]
        node 0,1 are connected 2,5 are connected
    Use union and find to get the connected components and their parents.

    g_node = 5
    g_from = [0,0,4,3]
    g_to = [1,3,2,4]
    print(max_difference(g_node, g_from, g_to))
    """
    # parents store the parent of each element (index)
    parents = list(range(g_nodes))
    weights = [1] * g_nodes
    max_value = list(range(g_nodes))
    min_value = list(range(g_nodes))

    def find(node):
        """find the parent of a node"""
        while node != parents[node]:
            parents[node] = parents[parents[node]]
            node = parents[node]
        return node

    def union(u, v):
        """ union nodes u and v as one group"""
        p_u = find(u)
        p_v = find(v)
        if p_u == p_v:
            return
        w_p_u = weights[p_u]
        w_p_v = weights[p_v]
        if w_p_u < w_p_v:
            w_p_u, w_p_v = w_p_v, w_p_u
        parents[p_v] = p_u
        weight = w_p_u + w_p_v
        weights[p_u] = weight
        weights[p_v] = weight
        max_value[p_u] = max(max_value[p_u], max_value[p_v])
        min_value[p_v] = min(min_value[p_u], min_value[p_v])

    for u, v in zip(g_from, g_to):
        union(u, v)
    max_diff = 0
    for mx, mi in zip(max_value, min_value):
        diff =  mx - mi
        if diff > max_diff:
            max_diff = diff
    return max_diff










if __name__ == "__main__":
    pass
