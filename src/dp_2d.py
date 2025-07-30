""" 2D Dynamic Programming problems. """
from collections import defaultdict


def max_points(points: list[list[int]]) -> int:
    """ Find the maximum points that can be collected from a grid.
        Each row can only be traversed once, and you can only move to the next row.
        There is a panalty of the distence between the points in the current row and the next row.
        https://leetcode.com/problems/maximum-number-of-points-with-cost
        Args:
            points: 2D list of points, where points[i][j] is the point at cell (i, j).
        Returns:
            Maximum points that can be collected.

    """
    # 1. simple dp, got TLE error
    # Transition function: dp[i][j] = max_k(points[i][j] + dp[i-1][k] - abs(k-j))
    # speed: O(m*n^2) mem: O(m)

    # n, m = len(points), len(points[0])
    # dp = points[0]
    # for i in range(1, n):
    #     new_dp = [0] * m
    #     for j in range(m):
    #         val = points[i][j]
    #         max_cur = float('-inf')
    #         for k in range(m):
    #             cur = val + dp[k] - abs(k - j)
    #             if cur > max_cur:
    #                 max_cur = cur
    #         new_dp[j] = max_cur
    #     dp = new_dp
    # return max(dp)

    # 2. double dynamic programming.
    # Each time we do a dp, we use memory to trade for 
    # the time to reduce one linear level of complexity.
    # when we compute the  max_k(dp[i-1][k] + points[i][j] - abs(k-j)), we can use the dp with
    # left and right pass throughs.
    # dp_l[i][j] = points[i][j] + max(dp_l[i][j-1] - 1, dp_l[i-1][j]) from left to right
    # dp_r[i][j] = points[i][j] + max(dp_r[i][j+1] - 1, dp_r[i-1][j]) from right to left
    # dp[i][j] = max(dp_l[i][j], dp_r[i][j])
    # n, m = len(points), len(points[0])
    # dp = points[0][:]
    # for i in range(1, n):
    #     dp_l = [0] * m
    #     dp_r = [0] * m

    #     dp_l[0] = dp[0]
    #     dp_r[-1] = dp[-1]
    #     for j in range(1, m):
    #         dp_l[j] = max(dp_l[j-1] - 1, dp[j])
    #         dp_r[m-1-j] = max(dp_r[m-j] - 1, dp[m-1-j])

    #     for j in range(m):
    #         dp[j] = points[i][j] + max(dp_l[j], dp_r[j])
    # return max(dp)

    n, m = len(points), len(points[0])
    dp = [[0] * m for _ in range(n)]
    
    # Initialize the first row
    for j in range(m):
        dp[0][j] = points[0][j]
    
    # Fill the dp table
    for i in range(1, n):
        for j in range(m):
            max_prev = max(dp[i-1])  # Get the maximum from the previous row
            dp[i][j] = points[i][j] + max_prev - abs(j - dp[i-1].index(max_prev))
    
    return max(dp[-1])  # Return the maximum from the last row


def max_vacation_days(flights: list[list[int]], days: list[list[int]]) -> int:
    """ Maximum vacation days
        https://leetcode.com/problems/maximum-vacation-days
        [Datadog]
        Think week by week. Each Monday you may stay in your current city or fly to another reachable city.
        For that chosen city you add that week’s available vacation days.

        dp[w][c] = max vacation days you can have after finishing week w while ending in city c.
        but we depend on only the last week, so it can be reduced to a 1d array
    """
    n = len(flights)      # cities
    k = len(days[0])      # weeks

    # trans[j] = cities you can come FROM to arrive in city j this week
    trans = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if flights[i][j] == 1 or i == j:
                trans[j].append(i)

    dp_from = [-1] * n
    dp_from[0] = 0  # start in city 0

    for w in range(k):
        dp_to = [-1] * n
        for c in range(n):
            best = -1
            for f in trans[c]:
                if dp_from[f] >= 0:
                    best = max(best, dp_from[f] + days[c][w])
            dp_to[c] = best
        dp_from = dp_to

    return max(dp_from)
