""" position related problems"""
from typing import List


def merge(intervals: list[list[int]]) -> list[list[int]]:
    """ merge overlapping intervals
        [[1,3],[2,4],[5,7],[6,8]] -> [[1,4],[5,8]]
        [[1,4],[2,3]] -> [[1,4]]
        nlog(n) time complexity
        link: https://leetcode.com/problems/merge-intervals/
        first sort the intervals by start time, then iterate through them,
        if the current interval overlaps with the last merged interval, merge them,
    """
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    it = iter(intervals)
    merged = [next(it)]
    for current in it:
        last = merged[-1]
        if last[1] >= current[0]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged


def left_rotation(l:list, d:int):
    """ left rotate n position of a iterable, inplace method"""
    def reverse(l, start, end):
        """reverse the elements in l from start to end"""
        while start < end:
            l[start], l[end] = l[end], l[start]
            start += 1
            end -= 1

    length = len(l)
    d %= length
    if d == 0:
        return l
    reverse(l, 0, d - 1)
    reverse(l, d, length - 1)
    reverse(l, 0, length - 1)
    return l


def minimum_bribes(q):
    """ a queue [1,3,2,4,5], each number is the original place (increase order), 
        3 asked 2 for a bride, each element can ask for maximum 2 times of brides.
    """
    total_brides = 0
    for i, p in enumerate(q):
        adv = p - (i+1)
        if adv > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2), i):
            # check only if the origin place before current place and 
            # only the element before original place can be reached by an element after it.
            # as all elements can have maximum two brides
            if q[j] > q[i]:
                total_brides += 1
    print(total_brides)

def minimum_swaps(arr):
    """ get mini sweap time for a un ordered array from an order consequetive array
        [7, 1, 3, 2, 4, 5, 6]: 5 times 
        find all circles and switch = circle size - 1
    """
    def circle_size(i, v):
        """ get circle size"""
        n = 0
        start = i
        while True:
            arr[i] = -1
            i = v - 1
            v = arr[i]
            n += 1
            if i == start:
                break
        return n

    total = 0
    for i, v in enumerate(arr):
        if v != -1 and v != i+1:
            # n_switch = circle size - 1
            total += circle_size(i, v) - 1
    return total


def array_manipulation(n, queries):
    """
    Starting with a 1-indexed array of zeros and a list of operations,
    for each operation add a value to each array element between two given indices, inclusive.
    Once all operations have been performed, return the maximum value in the array.
    link:
    https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

    Instead of calculate each update, we for a update value [a, b, k]
    we update the diff at position a with k and b+1 with -k.
    So the realy value is the cusum of diff.
    for example
    [0,1,0,0,-2,0,0] -> [0,1,1,1,-1,-1,-1]
    """
    # create a diff array to avoir caculation each time
    diff = [0] * (n+1)
    for a, b, k in queries:
        diff[a] += k
        if b < n:
            diff[b+1] -= k
    m = 0
    value = 0
    for v in diff:
        value += v
        if value > m:
            m = value
    return m


def longestMountain(arr: List[int]) -> int:
    """ Find the length of the longest mountain in an array.
        https://leetcode.com/problems/longest-mountain-in-array/

        get the tops of the mountain, then get the length of each mountain
        This is O(n) time complexity and O(1) space complexity. 
        But it need two passes through the array.
    """
    def get_length(arr, i):
        """Get the length of the mountain with the peak at index i."""
        l, r, n = i, i, len(arr)
        if not (i > 0 and i < n - 1 and arr[i] > arr[i - 1] and arr[i] > arr[i + 1]):
            return 0
        while l > 0 and arr[l - 1] < arr[l]:
            l -= 1
        while r < n - 1 and arr[r + 1] < arr[r]:
            r += 1
        length = r - l + 1
        return length

    max_length = 0
    tops = []
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            tops.append(i)
    for t in tops:
        length = get_length(arr, t)
        if length > max_length:
            max_length = length
    return max_length


def longestMountain_one_pass(arr: List[int]) -> int:
    l, r, n = 0, 1, len(arr)
    passed = False
    max_length = 0
    while r < len(arr):
        if passed:
            if r + 1 >= n or arr[r] <= arr[r + 1]:
                length = r - l + 1
                max_length = max(max_length, length)
                l = r
                passed = False
        else:
            if r + 1 < n and arr[r] > arr[r + 1]:
                passed = True
        r += 1
    return max_length


if __name__ == '__main__':
    arr = [7, 1, 3, 2, 4, 5, 6]
    print(minimum_swaps(arr))
