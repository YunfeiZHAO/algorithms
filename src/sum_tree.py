""" Different kind of tree """


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bstToGst(root: TreeNode|None) -> TreeNode|None:
    """ How to convert binary search tree to greater sum tree
        https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
        Given the root of a Binary Search Tree (BST),
        convert it to a Greater Tree such that every key of the original BST is
        changed to the original key plus the sum of all keys
        greater than the original key in BST.
        [Datadog]
        idea: in-order traversal
    """
    def dfs(node, acc):
        """ dfs to update the value
            Args:
                root: parent root
                acc: the accumulated sum
        """
        if not node:
            return acc
        acc = dfs(node.right, acc)
        acc = node.val + acc
        node.val = acc
        acc = dfs(node.left, acc)
        return acc
    dfs(root, 0)
    return root


def has_path_sum(root: TreeNode|None, targetSum: int) -> bool:
    """ Whether there is a path from root to a leaf that the sum is target_sum
        https://leetcode.com/problems/path-sum/
        [Datadog]
    """
    if not root:
        return False

    def dfs(node, cur_sum):
        if not node:
            return False

        cur_sum += node.val

        # Check only at leaves
        if not node.left and not node.right:
            return cur_sum == targetSum

        return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)

    return dfs(root, 0)

        
