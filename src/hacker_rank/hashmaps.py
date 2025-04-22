""" dictionary and hashmaps related questions"""
from collections import defaultdict


def sherlockAndAnagrams(s):
    """ Given a string, find number of substring pairs that can get each other by shuffle
        complexity: O(n^2 logn)
    """
    n = len(s)
    count = 0
    # Dictionary to store substring signatures
    substring_map = defaultdict(int)
    # Iterate over all possible substring lengths
    for length in range(1, n):
        for i in range(n - length + 1):
            # Frequency signature of the current substring
            signature = tuple(sorted(s[i: i+length]))
            # Update the count for this signature
            substring_map[signature] += 1
    # Count pairs based on frequencies of signatures
    for frequency in substring_map.values():
        if frequency > 1:
            count += (frequency * (frequency - 1)) // 2  # Number of pairs in nC2
    
    return count


def countTriplets(arr, r):
    """
    You are given an array and you need to find number of tripets of indices (i, j, k)
    such that the elements at those indices are in geometric progression 
    for a given common ratio r  and i<j<k.

    You can utilize hash tables (dictionaries) to keep track of potential triplets 
    as you iterate, reducing lookup time.
    This approach leverages the fact that once you know a number,
    you only need to store how many times it appears as part of a triplet.
    """
    count = 0
    v2_count = defaultdict(int)
    v3_count = defaultdict(int)

    for v in arr:
        # If v appears as the third element of the triplet
        count += v3_count[v]
        # If v can be the second element,
        # increase the count for v*r as the third element
        v3_count[v * r] += v2_count[v]
        # v can be part of a pair,
        # increase the possibility of v*r being second.
        v2_count[v * r] += 1
    return count


if __name__ == "__main__":
    sherlockAndAnagrams('ifailuhkqq')
