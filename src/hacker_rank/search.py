""" Search related questions """
from collections import deque
import sys

def binary_search(arr, l, r, value):
    """ binary search
        arr: no decreasing arr
        l: left index
        r: right index
        value: the value to find
    """
    while l <= r:
        median = (l + r) // 2
        m_value = arr[median]
        if value == m_value:
            return median
        elif value > m_value:
            l = median + 1
        else:
            r = median - 1
    return -1


def whatFlavors(cost, money):
    """ Cost is not ordered cost array of items, money is the total money.
        get 1-indexed items index of two flavors that used up all money.
        we assume that there always a unique solution.

        nlog(n)
    """
    # Write your code here
    size = len(cost)

    indexed_list = list(enumerate(cost))
    sorted_list = sorted(indexed_list, key=lambda x: x[1])
    cost = [x[1] for x in sorted_list]
    original_indices = [x[0] for x in sorted_list]

    cost = sorted(cost)
    for i in range(size - 1):
        v = cost[i]
        j = binary_search(cost, i+1, size-1, money-v)
        if j != -1:
            p1 = original_indices[i]+1
            p2 = original_indices[j]+1
            print(f'{min(p1,p2)} {max(p1,p2)}')


def triplets(a, b, c):
    """ a, b, c three list. find number of tuple (i, j , k) b[j] >= a[i] and b[j] >= c[i]"""
    total = 0
    p_a = 0
    l_a = len(a)
    prev_a = None
    count_a = 0

    prev_b = None

    p_c = 0
    l_c = len(c)
    prev_c = None
    count_c = 0


    for e in b:
        if e == prev_b:
            continue
        else:
            prev_b = e
        while p_a < l_a and a[p_a] <= e:
            if a[p_a] != prev_a:
                count_a += 1
            prev_a = a[p_a]
            p_a += 1

        while p_c < l_c and c[p_c] <= e:
            if c[p_c] != prev_c:
                count_c += 1
            prev_c = c[p_c]
            p_c += 1

        total += count_a * count_c
    return total

a = [1,3,5,7]
b = [5,7,9]
c = [7,9,11,13]

# a = [1,4,5]
# b = [2,3,3]
# c = [1,2,3]

print(triplets(a,b,c))

