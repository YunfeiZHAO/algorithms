""" dynamic programming"""

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
    






if __name__ == '__main__':
    arr = [2,1,5,8,4]
    print(maxSubsetSum(arr))


