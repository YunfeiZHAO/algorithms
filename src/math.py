""" Math related questions. """
import random
import bisect
import numpy as np



def pickIndex(weights) -> int:
    """ Pick an index based on the probability distribution.
        https://leetcode.com/problems/random-pick-with-weight/
    """
    # 1.
    # np.random.choice(len(self.prob), p=self.prob)
    # This method uses numpy's random.choice to select an index based on the given probabilities.
    # However, it is not efficient for large arrays as it requires O(n) space and time complexity.

    # 2.
    # create a new array, the new array is the cumulative sum of the weights.
    # weight = [2, 2, 1]  new wights = [0,0,1,1,2] and the normalized version [0.4, 0.4, 0.2]
    # cumulative sum: [0.4, 0.8, 1.0]
    # then we use the binary search to find the index of the random number generated
    # in the cumulative sum array.
    # the complexity is O(n) for creating the cumulative sum array and
    # O(log n) for the binary search.
    total = sum(weights)
    cumulative_weights = []
    cumsum = 0
    for weight in weights:
        cumsum += weight / total
        cumulative_weights.append(cumsum)
    return bisect.bisect_left(cumulative_weights, random.random())

