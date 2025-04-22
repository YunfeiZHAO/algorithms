""" binary search problem"""
import bisect

def count_between(arr, low, high):
    """ count the number of elements in each interval, the intervals are closed.
    Args:
        arr: arr of elements
        low: list of lower bound of an intervals
        high: list of higher bound of intervals
    bisect is to find the insert index.
    if an element already exist:
    bisect_left: show index of element inserted in left 
    bisect_right: show index of element inserted in right
    """
    arr = sorted(arr)
    result = [0] * len(low)
    for i, (l, h) in enumerate(zip(low, high)):
        left = bisect.bisect_left(arr, l)
        right = bisect.bisect_right(arr, h)
        result[i] = right - left
    return result

if __name__ == '__main__':
    arr=[1,2,2,3,5]
    low=[1,1]
    high=[2,5]
    print(count_between(arr, low, high))
