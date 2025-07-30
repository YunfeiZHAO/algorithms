""" dynamic programming"""
import math
from collections import deque

def maxSubsetSum(arr):
    n = len(arr)
    if n == 0:
        return 0
    elif n == 1:
        return max(0, arr[0])
    dp = [0] * n
    dp[0] = max(0, arr[0])
    dp[1] = max(arr[0], arr[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1] , dp[i-2] + max(0, arr[i]))
    return dp[-1]


def abbreviation(a, b):
    """
    Capitalize zero or more of a's lowercase letters.
    Delete all of the remaining lowercase letters in a.
    to make a == b. 
    check whether it is possible
        Args:
            a: ascii[A-Za-z]
            b: ascii[A-Z]
    """
    n, m = len(a), len(b)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(n):
        for j in range(m + 1):
            if dp[i][j]:
                # Option 1: Delete a lowercase letter
                if a[i].islower():
                    dp[i + 1][j] = True
                # Option 2: Match if possible
                if j < m and a[i].upper() == b[j]:
                    dp[i + 1][j + 1] = True

    return 'YES' if dp[n][m] else 'NO'


def candies(n, arr):
    """ Candies: give candies
        1. each student has at least one candy.
        2. between adjacent students, higher ranked student should have more candies.
        3. when two children have equal rating, they are allowed to have different number of candies    
        Args:
            n: number of students
            arr: students rank and position
        break the problem into two passes and only the last element will effect
        the next element.
    """
    nums = [1] * n  # Initialize all students with one candy
    for i in range(1, n):  # Forward pass
        if arr[i] > arr[i-1]:
            nums[i] = nums[i-1] + 1
    for i in range(n-2, -1, -1):  # Backward pass
        if arr[i] > arr[i+1] and nums[i] <= nums[i+1]:
            nums[i] = nums[i+1] + 1
    return sum(nums)


def decibinaryNumbers(x):
    """ Hackerrank: Decibinary Numbers
        get the xth 1-index decibinary number
        the 123: 1* 2^2 + 2* 2^1 + 3* 2^0
        if the converted to decimal value is the same, 2 and 10, they
        are ordered by decimal value of the representation string 10 > 2
        so 
        x = 3 we have 2
        x = 4 we have 10
    """
    deci_n = [0,1]
    

def coin_change(coins: list[int], amount: int) -> int:
    """ https://leetcode.com/problems/coin-change/
        Get the minimum number of coins to get the amount.
        [Datadog]
    """
    # Initialize the dp array. Use a large value (amount + 1) as infinity.
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0

    for i in range(1, amount + 1):
        for coin in coins:
            if (prev := i - coin) >= 0:
                # get the min coins we can use in current step
                # based on the coins we already get before.
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1


def rob1(nums: list[int])-> int:
    """ House robber
        https://leetcode.com/problems/house-robber/
        [Datadog]
        idea:
            robs: is a list contain the max rob I can achieve since the first house
            robs[i] = max(robs[i-1],  robs[i-2]+nums[i])
            which means, for each state, we decide either not to steal or we steal it 
            but do not steal the last one.
    """
    n = len(nums)
    r1, r2 = 0, 0
    for i in range(0, n):
        r = max(r2, r1 + nums[i])
        r1 = r2
        r2 = r
    return r


def rob2(nums: list[int])-> int:
    """ House robber 2
        https://leetcode.com/problems/house-robber-ii
        The houses are arranged in a circle this time.
        [Datadog]
        idea:
            robs: is a list contain the max rob I can achieve since the first house
            robs[i] = max(robs[i-1],  robs[i-2]+nums[i])
            which means, for each state, we decide either not to steal or we steal it 
            but do not still the last one.
    """
    n = len(nums)
    cur_nums = nums[0: n-1]
    r1 = rob1(cur_nums)
    cur_nums = nums[1:]
    r2 = rob1(cur_nums)
    return max(r1, r2)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rob3(root: TreeNode|None) -> int:
    """ House robber 3
        https://leetcode.com/problems/house-robber-iii/description/
        The house is formed as a binary tree
        idea:
            The first sight, use the bfs, but it is not working as children grand children
            can be seleced at same time as long as they are
            not on the same sub branch of the parent.
    """
    def dfs(node: TreeNode|None) ->tuple[int, int]:
        """
        Returns (rob_this, skip_this)
        - rob_this:  max money if we rob node
        - skip_this: max money if we skip node
        """
        if not node:
            return 0, 0

        l_rob, l_skip = dfs(node.left)
        r_rob, r_skip = dfs(node.right)

        rob_this = node.val + l_skip + r_skip
        skip_this = max(l_rob, l_skip) + max(r_rob, r_skip)

        return rob_this, skip_this

    return max(dfs(root))


def triangle_min_sum(triangle: list[list[int]]):
    """ Ge the minimum path sum from top to bottom of the triangle
        https://leetcode.com/problems/triangle
    """
    n = len(triangle)
    dp = triangle[-1][:]
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
    return dp[0]


    




if __name__ == '__main__':
    # arr = [2,1,5,8,4]
    # print(maxSubsetSum(arr))

    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    # triangle = [[-10]]
    print(triangle_min_sum(triangle))


