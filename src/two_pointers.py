""" Two pointers """
import re

def isPalindrome(s: str) -> bool:
    """Valid Palindrome"""
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    s = s.lower()
    l, r = 0, len(s)-1
    while l <= r:
        if s[l] != s[r]:
            return False
        else:
            l += 1
            r -= 1
    return True


def maxArea(height: list[int]) -> int:
    """ https://leetcode.com/problems/container-with-most-water/
        Given n non-negative integers a1, a2, ..., an where each represents a point at coordinate (i, ai).
        n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
        Find two lines which together with x-axis forms a container, such that the container contains the most water.
        Return the maximum amount of water a container can store.

        we put two pointers at the beginning and end of the array.
        We calculate the area between the two pointers and move the pointer with the smaller height towards the other pointer.
        This is because the area is limited by the shorter line, so moving the taller line won't increase the area.
        We repeat this until the two pointers meet.
    """
    l, r = 0, len(height) - 1
    max_surface = 0
    while r > l:
        h_l = height[l]
        h_r = height[r]
        surface = (r - l) * min(h_l, h_r)
        max_surface = max(max_surface, surface)
        if h_l < h_r:
            l += 1
        else:
            r -= 1
    return max_surface


def minAvailableDuration(
        slots1: list[list[int]],
        slots2: list[list[int]],
        duration: int) -> list[int]:
    """ get the min common time slot with at least duriaton given.
        https://leetcode.com/problems/meeting-scheduler 
        [Datadog]
    """
    p1 = p2 = 0
    n1, n2 = len(slots1), len(slots2)
    slots1.sort()
    slots2.sort()
    while p1 < n1 and p2 < n2:
        s1, e1 = slots1[p1]
        s2, e2 = slots2[p2]

        start = max(s1, s2)
        end   = min(e1, e2)

        if end - start >= duration:
            return [start, start + duration]

        # advance the one that ends earlier
        if e1 <= e2:
            p1 += 1
        else:
            p2 += 1

    return []




        










if __name__ == "__main__":
    s="Was it a car or a cat I saw?"
    print(isPalindrome(s))