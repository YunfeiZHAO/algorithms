""" Tree related question"""
import sys
import math
from collections import defaultdict, deque


def lca(root, v1, v2):
    """
    class Node:
        def __init__(self,info): 
            self.info = info  
            self.left = None  
            self.right = None 
    root is the root of a binary search tree, find the lowest common ancestor of v1, v2
    v1, v2 are values and they are in the tree        
    """
    while root:
        val = root.info
        if val > v1 and val > v2:
            root = root.left
        elif val < v1 and val < v2:
            root = root.right
        else:
            return root


def decode_huff(root, s):
    """ Huffman coding assigns variable-length codewords to fixed-length input characters based on their frequencies.
        1. Building the Tree: 
            The algorithm constructs a binary tree using the frequency of each character.
            Each character is represented at the leaf level of the tree to ensure that 
            no encoding for a character is a subsequence of another.

        2. Tree Construction: 
            Begin with the two characters that have the smallest frequencies.
            The character with the lower frequency becomes the left leaf,
            and the one with the higher frequency becomes the right leaf.
            A new node is created as the parent of these two leaves,
            with its frequency equal to the sum of their frequencies.
            This node is used to iteratively link other characters,
            continuing the process based on frequency.

        3. Assigning Codes:
            Once the tree is built, traverse it to assign code values:
            each left path from the root is assigned a '0',
            and each right path is assigned a '1'.
            To obtain the encoding of a character,
            trace the path from the root to the leaf representing that character.
        Args:
            root: root of the Huffman tree "1001011"
            s: decoded encoded string "ABACA"

        class Node:
            def __init__(self, freq,data):
                self.freq= freq
                self.data=data
                self.left = None
                self.right = None
    """
    p = root
    d = []
    for c in s:
        if c == '0':
            p = p.left
        else:
            p = p.right
        if p.left is None and p.right is None:
            d.append(p.data)
            p = root
    return ''.join(d)


def balanced_forest(c, edges):
    """ Given a tree, we want to cut two edges and add a node with value w to one of the three children trees
        so that the sum of three trees are equal. We want to find the min(w) or -1 if it is not possible. 
        w and all nodes values are positive
        Args:
            c: is the node value and the position is the node number (start with 1) [5, 8, 5].
            edges: the edges that link the nodes [[1,2] [1,3]].
    """
    # build a tree graph
    min_w = math.inf
    c = [0] + c # padding the 0 index

    def get_graph(edges):
        """ break the link between u v"""
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def sum_subtree(graph, root, parent):
        """ calculate the subtree sum
            Args:
                root: root node of the subtree
                parent: the parent of this node and also the other
                        element that we get when cut the edge
        """
        s = c[root]
        children = graph[root]
        if len(children) == 0:
            return s
        for child in children:
            if child != parent:
                s += sum_subtree(graph, child, root)
        return s

    def possible_sum(edges, graph):
        p_s = []
        for u,v in edges:
            sum_u = sum_subtree(graph, u, v)
            sum_v = sum_subtree(graph, v, u)
            p_s.append((sum_u, sum_v))
        return p_s

    for i in range(len(edges)):
        new_edges = edges.copy()
        u, v = new_edges.pop(i)
        new_graph = get_graph(new_edges)
        sum_u = sum_subtree(new_graph, u, v)
        sum_v = sum_subtree(new_graph, v, u)
        if sum_u == sum_v:
            if min_w > sum_u:
                min_w = sum_u
        else:
            # all possible sum in the remain graph
            p0 = min(sum_u, sum_v)
            big_sum = max(sum_u, sum_v)
            p_sum = possible_sum(new_edges, new_graph)
            for p1, p2 in p_sum:
                if p1 + p2 == big_sum:
                    # only split the big one can give faisable solution
                    values = [p0, p1, p2]
                    counts = {x: values.count(x) for x in set(values)}
                    for value, count in counts.items():
                        if count == 2:
                            third_value = sum(values) - 2 * value
                            if value > third_value:
                                w = value - third_value
                                if w < min_w:
                                    min_w = w
    if min_w < math.inf:
        return min_w
    return -1



class TreeNode():
    """ Tree node class """
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def construct_tree(l):
    """ construct a tree from l.
        Args:
            l: complet tree the root 1 is not there
    """
    root = TreeNode(1)
    queue = deque()
    queue.append(root)
    for l, r in l:
        node = queue.popleft()
        if l != -1:
            node.left = TreeNode(l)
            queue.append(node.left)
        if r != -1:
            node.right = TreeNode(r)
            queue.append(node.right)
    return root


def swap(root, k, level, r):
    if root:
        if level % k == 0:
            root.left, root.right = root.right, root.left
        
        # inorder traversal
        swap(root.left, k, level+1, r)
        r.append(root.val)
        swap(root.right, k, level+1, r)


def swapNodes(indexes, queries):
    """ swap nodes in a binary three
        Args:
            indexes: binary tree, presented in list in level order, empty leaf value is -1 otherwise increase value.
            queries: each k in queries, swap the the left and right children of element in level h in [k , 2k, ...]
            the root of tree take value 1, it is not in indexes. the level of root is 1.
            We need to save the tree in result by in-order traversal after each swap.
        Two many recursions problem!!!
    """
    sys.setrecursionlimit(len(indexes)+3)
    results = []
    if len(indexes) == 0 or len(queries) == 0:
        return results
    tree = construct_tree(indexes)
    for k in queries:
        r = []
        swap(tree, k, 1, r)
        results.append(r)
    return results


def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    if not (min_val < node.data < max_val):
        return False
    return (is_bst(node.left, min_val, node.data) and
            is_bst(node.right, node.data, max_val))

def checkBST(root):
    """ check whether a tree is BST"""
    return is_bst(root)



def diameter_of_binaryTree(root: TreeNode|None) -> int:
    """ Calculate the diameter of a binary tree.
        https://neetcode.io/problems/binary-tree-diameter
        The diameter is the length of the longest path between any two nodes in the tree.
        This path may or may not pass through the root.

        idea: check the depth of left and right subtrees for each node, and for the root,
        the diameter is also the sum of the depth of left and right subtrees.

        Args:
            root: root of the binary tree
        Returns:
            int: the diameter of the binary tree
    """
    max_diameter = 0

    def dfs(node: TreeNode|None) -> int:
        nonlocal max_diameter
        if not node:
            return 0

        left_depth = dfs(node.left)
        right_depth = dfs(node.right)

        # Update the maximum diameter found so far
        max_diameter = max(max_diameter, left_depth + right_depth)

        # Return the depth of this subtree
        return max(left_depth, right_depth) + 1

    dfs(root)
    return max_diameter


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


def maxDepth(self, root: 'Node') -> int:
    """ Get the maximum depth of N-ary tree
        https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
        [Datadog]
    """
    if not root:
        return 0
    if not root.children:
        return 1
    return 1 + max(map(self.maxDepth, root.children))


if __name__ == '__main__':
    c = [12,10,8,12,14,12]
    edges = [[1,2],[1,3],[1,4],[2,5],[4,6]]
    print(balanced_forest(c, edges))


