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


if __name__ == '__main__':
    print(climbStairs(4))


