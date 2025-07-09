""" String manipulation"""
from collections import Counter

def strStr(haystack: str, needle: str) -> int:
    """ Return the index of first occurrence of needle in haystack, or -1 if not found
        This is the implementation of find() function in Python.
        time O(n*m) memory O(1)
    """
    n_needle = len(needle)
    for i in range(len(haystack) - n_needle + 1):
        match = True
        for j, v in enumerate(needle):
            if haystack[i+j] != v:
                match = False
                break
        if match:
            return i
    return -1


def isValid(s):
    """ For a string, check if remove at most 1 char, all frequences of chars are equal"""
    counts = Counter(s)
    freq_of_freq = Counter(counts.values())
    common_freq = max(freq_of_freq, key=freq_of_freq.get)
    diff = 0
    for v in counts.values():
        diff += abs(common_freq - v)
    if  diff > 1:
            return "NO"
    return "YES"

if __name__ == "__main__":
    s = "aaaabbcc"
    print(isValid(s))


def substrCount(n, s):
    count = 0
    for i in range(1, n-1):
        # find all same but middle one cases
        if s[i - 1] == s[i + 1] and s[i] != s[i-1]:
            count += 1
            k = 2
            while i - k > 0 and i + k < n and s[i-k] == s[i-1] and s[i+k] == s[i-1]:
                count += 1
                k += 1
    # count all consequent chars
    i = 0
    while i < n:
        count_char = 0
        while i + count_char < n and s[i + count_char] == s[i]:
            count_char += 1
        count += ((count_char+1)*count_char)//2
        i += count_char
    return count

def commonChild(s1, s2):
    """ find longest common child of s1, s2. All chars in this child can
        be found both in s1 and s2 and should be in original order.

        # Todo: get the memory optimised version
    """
    m = len(s1)
    n = len(s2)
    # dp[i][j] store the LCS  from s1[:i+1] s2[:j+1]
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[m][n]


