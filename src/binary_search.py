""" binary search problem
log(n)
1, optimise a O(n) alogrithm
2, sorted array or rotated sorted array
"""
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


def binary_search_first(nums:list[int], target:int):
    """ get the first occurence position of target (bisect.bisect_left)
        
    """
    if nums is None or len(nums) == 0:
        return -1
    left, right = 0, len(nums) -1
    while left + 1 < right:
        mid = left + (right - left)//2
        if nums[mid] == target:
            right = mid # for ,any position case, you can just return
        elif nums[mid] < target:
            left = mid # (+1, -1 may not work for case when first that is bigger than target... )
        else:
            right = mid
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1


def binary_search_last(nums:list[int], target:int):
    """ get the last occurence position of target (bisect.bisect_right)"""
    n = len(nums)
    if nums is None or n == 0:
        return -1
    left, right = 0, n -1
    while left + 1 < right:
        mid = left + (right - left)//2
        if nums[mid] == target:
            left = mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1

def sqrt(x:int) -> int:
    """ compute and return the square root of x
    idea: **Last** number i that i**2 <= x
    """
    left, right = 1, x
    while left + 1 < right:
        mid = left + (right - left)//2 
        sq_mid = mid ** 2
        if sq_mid == x:
            left = mid
        elif sq_mid < x:
            left = mid
        else:
            right = mid
        
    if right ** 2 <= x:
        return right
    return left


def search_matrix(matrix:list[list[int]], target:int) -> bool:
    """ https://leetcode.com/problems/search-a-2d-matrix
    Each row is sorted in non-decreasing order.
    The first integer of each row is greater
    than the last integer of the previous row.
    """
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left + 1 < right:
        mid = left + (right - left)//2
        row, col = divmod(mid, n)
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid
        else:
            right = mid
    return False


def search_matrix_method2(matrix: list[list[int]], target: int) -> bool:
    """
    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.
    """
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    starts = [row[0] for row in matrix]
    start_pos = bisect.bisect_right(starts, target) - 1
    if start_pos < 0:
        return False
    # Binary search in the identified row
    row = matrix[start_pos]
    col_pos = bisect.bisect_left(row, target)
    return col_pos < n and row[col_pos] == target


def bisect_left_implementation(A:list[int], target:int) -> int:
    n = len(A)
    left, right = 0, n - 1
    while left < right -1:
        mid = left + (right - left)//2
        if (v:=A[mid]) == target:
            right = mid
        elif target > v:
            left = mid
        else:
            right = mid
    if A[left] >= target:
        return left
    if A[right] >= target:
        return right
    return n


def search_in_rotated_sorted_array(nums: list[int], target: int):
    """ https://leetcode.com/problems/search-in-rotated-sorted-array/
        [4,5,6,7,0,1,2] the sorted array is rotated at pivot index k = 3
        [k, k+1,...,n-1]
        All values of nums are unique.
        nums is an ascending array that is possibly rotated.

        For a mid, there can be four cases for target.
        In the first halp of not and bigger or smaller than mid
        So we need to discuss these four cases in the implementation
    """
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid
            else:
                left = mid
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid
            else:
                right = mid
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1




if __name__ == '__main__':
    # arr=[1,2,2,3,5]
    # low=[1,1]
    # high=[2,5]
    # print(count_between(arr, low, high))

    # arr=[1,2,2,2,3,5]
    # print(binary_search_first(arr, 2))

    # arr=[0,2,2,3,5]
    # print(binary_search_last(arr, 2))

    # print(sqrt(81))

    # mat = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    # print(search_matrix(mat, 5))

    # mat = [[1,3]]
    # print(search_matrix_2(mat, 3))

    arr=[0,2,2,3,5]
    print(bisect_left_implementation(arr, 6))


50 minutes