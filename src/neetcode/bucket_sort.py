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

if __name__ == "__main__":
    nums = [1,2,2,3,3,3]
    k = 2
    print(topKFrequent(nums, k))
