""" binary tree """
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    """ https://neetcode.io/problems/kth-smallest-integer-in-bst
        in order traversal with bfs iterative way
    """
    stack = []
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right