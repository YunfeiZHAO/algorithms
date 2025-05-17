""" sliding window related questions """

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