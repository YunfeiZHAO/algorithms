""" dynamic programming"""
def climbStairs(n: int) -> int:
    """ You are given an integer n representing the number of steps to reach the top of a staircase. 
        You can climb with either 1 or 2 steps at a time.
        Return the number of distinct ways to climb to the top of the staircase.
    """
    if n < 3:
        return n
    prev1 = 1
    prev2 = 2
    ways = 0
    for _ in range(n-2):
        ways = prev1 + prev2
        prev1 = prev2
        prev2 = ways
    return ways


def perfect_squares(n):
    """https://leetcode.com/problems/perfect-squares/description/
        O((n*n)^(1/2))
    """
    dp = [n] * (n+1) # worst case where n will be add with n of 1
    dp[0] = 0 # base case

    for target in range(1, n+1):
        for s in range(1, target + 1):
            square = s * s
            if target - square < 0:
                break
            dp[target] = min(dp[target], dp[target - square] + 1)
    return dp[n]


if __name__ == '__main__':
    # print(climbStairs(4))
    print(perfect_squares(5))


