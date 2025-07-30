""" sliding window related questions """
from collections import defaultdict
import bisect
import heapq
from heapq import heappop, heappush




def lengthOfLongestSubstring(s: str) -> int:
    """ https://leetcode.com/problems/longest-substring-without-repeating-characters/
        find the longuest substring of s with no repeted letter.
    """
    l = 0
    max_len = 0
    buff = set()
    for r, v in enumerate(s):
        while v in buff:
            buff.remove(s[l])
            l += 1
        buff.add(v)
        max_len = max(max_len, r-l+1)
    return max_len


def median_sliding_window_basic(nums:list[int], k:int) -> list[int]:
    """ get the sliding window median with bisearch
        https://leetcode.com/problems/sliding-window-median
        [Datadog]
    """

    # 1. brute force, klogk*(n-k+1)

    # def get_median(sub:list[int]):
    #     """ get the median for list l """
    #     sub = sorted(sub)
    #     n_s = len(sub)
    #     if n_s % 2 == 1:
    #         l = r = n_s // 2
    #     else:
    #         l = n_s // 2 - 1
    #         r = n_s // 2
    #     return (sub[l] + sub[r])/2

    # n = len(nums)
    # meds = []
    # for i in range(n-k+1):
    #     win = nums[i:i+k]
    #     meds.append(get_median(win))
    # return meds

    # 2. two bisect O(n * k) as removing and add the element in 
    # sub list is O(k) if it is not at the begin or the end

    medians = []

    window = sorted(nums[:k])  # Initial window, sorted
    for i in range(k, len(nums) + 1):
        # Calculate and store the median
        if k % 2 == 1:
            median = window[k // 2]
        else:
            median = (window[k // 2 - 1] + window[k // 2]) / 2
        medians.append(median)

        if i == len(nums):
            break

        # Remove the element going out of the window
        out_elem = nums[i - k]
        pos = bisect.bisect_left(window, out_elem)
        window.pop(pos)

        # Insert the new element
        in_elem = nums[i]
        bisect.insort_left(window, in_elem)

    return medians

# 3. sliding median with max min and min max heaps
class DualHeap:
    def __init__(self, k):
        self.small = []  # max-heap (invert values for Python)
        self.large = []  # min-heap
        self.delayed = defaultdict(int)  # count of elements to remove
        self.k = k
        self.small_size = 0  # size of valid elements in small
        self.large_size = 0  # size of valid elements in large

    def prune(self, heap):
        # Remove elements marked as delayed from the top of the heap
        while heap and self.delayed[heap[0][1]] > 0:
            num = heap[0][1]
            self.delayed[num] -= 1
            if self.delayed[num] == 0:
                del self.delayed[num]
            heapq.heappop(heap)

    def balance(self):
        # Balance the heaps so that their sizes differ at most 1
        if self.small_size > self.large_size + 1:
            val, num = heapq.heappop(self.small)
            heapq.heappush(self.large, (-val, -num))
            self.small_size -= 1
            self.large_size += 1
            self.prune(self.small)
        elif self.small_size < self.large_size:
            val, num = heapq.heappop(self.large)
            heapq.heappush(self.small, (-val, -num))
            self.large_size -= 1
            self.small_size += 1
            self.prune(self.large)

    def add(self, num):
        # Add new number to one of the heaps
        if not self.small or num <= -self.small[0][0]:
            heapq.heappush(self.small, (-num, -num))
            self.small_size += 1
        else:
            heapq.heappush(self.large, (num, num))
            self.large_size += 1
        self.balance()

    def remove(self, num):
        # Mark number for delayed removal
        self.delayed[num] += 1
        if self.small and num <= -self.small[0][0]:
            self.small_size -= 1
            if self.small[0][1] == -num:
                self.prune(self.small)
        else:
            self.large_size -= 1
            if self.large and self.large[0][1] == num:
                self.prune(self.large)
        self.balance()

    def get_median(self):
        if self.k % 2 == 1:
            return float(-self.small[0][0])
        else:
            return (-self.small[0][0] + self.large[0][0]) / 2.0


class SlidingMedian:
    """ util class for two heaps method"""
    def __init__(self, k: int):
        self.k = k
        self.lo = []  # max-heap via negatives
        self.hi = []  # min-heap
        self.to_remove = defaultdict(int)
        self.lo_size = 0  # valid elements count (excluding lazily deleted)
        self.hi_size = 0

    def add(self, x: int) -> None:
        if not self.lo or x <= -self.lo[0]:
            heappush(self.lo, -x)
            self.lo_size += 1
        else:
            heappush(self.hi, x)
            self.hi_size += 1
        self._rebalance()

    def remove(self, x: int) -> None:
        self.to_remove[x] += 1
        if x <= -self.lo[0]:
            self.lo_size -= 1
            if x == -self.lo[0]:
                self._prune(self.lo, sign=-1)
        else:
            self.hi_size -= 1
            if self.hi and x == self.hi[0]:
                self._prune(self.hi, sign=1)
        self._rebalance()

    def median(self) -> float:
        if self.k % 2:
            return float(-self.lo[0])
        else:
            return (-self.lo[0] + self.hi[0]) / 2.0

    def _rebalance(self) -> None:
        # Ensure size(lo) >= size(hi) and differs by at most 1
        if self.lo_size > self.hi_size + 1:
            val = -heappop(self.lo)
            self.lo_size -= 1
            heappush(self.hi, val)
            self.hi_size += 1
            self._prune(self.lo, sign=-1)
        elif self.lo_size < self.hi_size:
            val = heappop(self.hi)
            self.hi_size -= 1
            heappush(self.lo, -val)
            self.lo_size += 1
            self._prune(self.hi, sign=1)

        self._prune(self.lo, sign=-1)
        self._prune(self.hi, sign=1)

    def _prune(self, heap, sign):
        # Pop elements that are marked for deletion
        while heap:
            val = -heap[0] if sign == -1 else heap[0]
            if self.to_remove[val] > 0:
                heappop(heap)
                self.to_remove[val] -= 1
            else:
                break

def median_sliding_window_basic(nums:list[int], k:int) -> list[int]:
    """ get the sliding window median with min and max heaps
        https://leetcode.com/problems/sliding-window-median
        [Datadog]
    """
    # 3. optimized method for the sliding window median problem 
    # using two heaps (a max-heap and a min-heap).
    # This approach maintains two heaps to keep track of the lower half and
    # the upper half of the current sliding window elements efficiently:

    # Adding and removing elements to/from heaps happens in O(log k) time, 
    # where k is the window size.

    # a "lazy deletion" technique with a hash map keeps track of elements 
    # to remove without immediately deleting them from heaps, cleaning up only when necessary.
    # Two heaps: small (max-heap), large (min-heap)
    # Python heapq is a min heap, so to simulate max heap, we push negative values.
    
    if k == 0:
        return []
    sm = SlidingMedian(k)
    res = []

    # first window
    for i in range(k):
        sm.add(nums[i])
    res.append(sm.median())

    # slide
    for i in range(k, len(nums)):
        sm.add(nums[i])
        sm.remove(nums[i - k])
        res.append(sm.median())

    return res
