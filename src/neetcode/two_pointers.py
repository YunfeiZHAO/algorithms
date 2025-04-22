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

if __name__ == "__main__":
    s="Was it a car or a cat I saw?"
    print(isPalindrome(s))