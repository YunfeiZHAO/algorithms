""" union and find is a good algoritmn to group the nodes (linked) in a undirected graph
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
        
    
