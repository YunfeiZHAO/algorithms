""" bucket sort"""
from collections import Counter
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    """ https://neetcode.io/problems/top-k-elements-in-list 
        get top K frequence element in a list
    """
    n = len(nums)
    counts = Counter(nums)
    freq = [[] for i in range(n + 1)]
    for num, count in counts.items():
        freq[count].append(num)
    res = []
    for i in range(n, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res

def findMinDifference(timePoints: list[str]) -> int:
    """
    https://leetcode.com/problems/minimum-time-difference
    When we need to sort and we have limited type of elements, we should think of bucket sort.
    BUCKET SORT:
    IDEA: 
        We have at most 24 * 60 = 1440 possible times.
        Instead of sorting the list (which is slow), just mark which times exist using a bool[1440] array.  
        --> That is bucket sort: you make an array where each index is a "bucket" that tracks whether a time appears.
    Algo: 
        1) Convert everything to minutes
        2) Use a boolean[1440] to track visited times (bucket sort)
        3) Linear scan to compute min diff between visited minutes
        4) Edge Case: circular time difference (last → first)
    """
    seen = [False] * 1440
    for t in timePoints:
        minutes = int(t[:2]) * 60 + int(t[3:])
        if seen[minutes]:
            return 0
        seen[minutes] = True

    # Find first time for circular calculation
    first = last = prev = None
    min_diff = 1440

    # Two pointers: prev (previous time), curr (current time, as we scan)
    for curr in range(1440):
        if seen[curr]:
            if prev is not None:
                min_diff = min(min_diff, curr - prev)
            else:
                first = curr
            prev = curr
            last = curr

    # Wrap-around difference (from last to first across midnight)
    min_diff = min(min_diff, (first + 1440 - last))

    return min_diff

if __name__ == "__main__":
    nums = [1,2,2,3,3,3]
    k = 2
    print(topKFrequent(nums, k))
