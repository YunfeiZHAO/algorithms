""" recursive questions"""
from collections import Counter

def subsets(nums: list[int]) -> list[list[int]]:
    """ https://leetcode.com/problems/subsets
        Given an integer array nums of unique elements,
        return all possible subsets (the power set).
        there is only for loop, but it using recursive idea,
        each time we update the subsets and reuse it.
    """
    subsets = [[]]
    for e in nums:
        new_subsets = []
        for s in subsets:
            new_s = s.copy()
            new_s.append(e)
            new_subsets.append(new_s)
        subsets += new_subsets
    return subsets


def subset2(nums: list[int]) -> list[list[int]]:
    """ https://leetcode.com/problems/subsets-ii
        This time, there are duplicated elements.
    """
    subsets = [[]]
    counts = Counter(nums)
    for e, count in counts.items():
        new_subsets = []
        for s in subsets:
            for c in range(count):
                new_s = s.copy()
                new_s += [e] * (c + 1)
                new_subsets.append(new_s)
        subsets += new_subsets
    return subsets




if __name__ == "__main__":
    print(subset2([1,2,2,2,3]))