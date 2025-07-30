""" String manipulation"""
from collections import Counter, defaultdict
import re


def strStr(haystack: str, needle: str) -> int:
    """ Return the index of first occurrence of needle in haystack, or -1 if not found
        This is the implementation of find() function in Python.
        time O(n*m) memory O(1)
    """
    n_needle = len(needle)
    for i in range(len(haystack) - n_needle + 1):
        match = True
        for j, v in enumerate(needle):
            if haystack[i+j] != v:
                match = False
                break
        if match:
            return i
    return -1


def isValid(s):
    """ For a string, check if remove at most 1 char, all frequences of chars are equal"""
    counts = Counter(s)
    freq_of_freq = Counter(counts.values())
    common_freq = max(freq_of_freq, key=freq_of_freq.get)
    diff = 0
    for v in counts.values():
        diff += abs(common_freq - v)
    if  diff > 1:
            return "NO"
    return "YES"


def substrCount(n, s):
    count = 0
    for i in range(1, n-1):
        # find all same but middle one cases
        if s[i - 1] == s[i + 1] and s[i] != s[i-1]:
            count += 1
            k = 2
            while i - k > 0 and i + k < n and s[i-k] == s[i-1] and s[i+k] == s[i-1]:
                count += 1
                k += 1
    # count all consequent chars
    i = 0
    while i < n:
        count_char = 0
        while i + count_char < n and s[i + count_char] == s[i]:
            count_char += 1
        count += ((count_char+1)*count_char)//2
        i += count_char
    return count

def commonChild(s1, s2):
    """ find longest common child of s1, s2. All chars in this child can
        be found both in s1 and s2 and should be in original order.

        # Todo: get the memory optimised version
    """
    m = len(s1)
    n = len(s2)
    # dp[i][j] store the LCS  from s1[:i+1] s2[:j+1]
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[m][n]


def validWordAbbreviation(word: str, abbr: str) -> bool:
    """
        https://leetcode.com/problems/valid-word-abbreviation
        [Datadog]
        A string can be abbreviated by replacing any number of non-adjacent,
        non-empty substrings with their lengths. The lengths should not have leading zeros.
        
        For example, a string such as "substitution" could be abbreviated as (but not limited to):
        "s10n" ("s ubstitutio n")
        "sub4u4" ("sub stit u tion")
        "12" ("substitution")
        "su3i1u2on" ("su bst i t u ti on")
        "substitution" (no substrings replaced)

        The following are not valid abbreviations:
        "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
        "s010n" (has leading zeros)
        "s0ubstitution" (replaces an empty substring)
        Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.
        A substring is a contiguous non-empty sequence of characters within a string.
        idea:
            Two pointers
            When we see a digit in abbr, we must:
            Ensure it’s not '0' (leading zero is invalid).
            Parse the full number and jump that many characters in word.
            When we see a letter, we must match it exactly with the current letter in word.
    """
    i = j = 0  # i for word, j for abbr

    while i < len(word) and j < len(abbr):
        if abbr[j].isdigit():
            if abbr[j] == '0':
                return False  # no leading zero allowed
            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            i += num
        else:
            if i >= len(word) or word[i] != abbr[j]:
                return False
            i += 1
            j += 1

    return i == len(word) and j == len(abbr)


def most_common_word(paragraph: str, banned: list[str]) -> str:
    """ https://leetcode.com/problems/most-common-word
        Given a string paragraph and a string array of the banned words banned,
        return the most frequent word that is not banned.
        [Datadog]
    """
    # Method 1
    def isAlphabet(c:str) -> bool:
        if ("a"<=c and c <= "z") or ("A"<=c and c <= "Z"):
            return True
        else:
            return False
    tokens = []
    token = ""
    for c in paragraph:
        if isAlphabet(c):
            token += c.lower()
        else:
            if len(token) > 0:
                tokens.append(token)
            token = ""
    if len(token) > 0:
        tokens.append(token)
    banned = set(banned)
    counts = Counter(tokens)
    max_count = 0
    chosed = None
    for word, count in counts.items():
        if word not in banned and count > max_count:
            chosed = word
            max_count = count
    # return chosed
    
    # Method 2 regex
    words = re.findall(r'\w+', paragraph.lower())
    bannet_set = set(banned)
    count = Counter(i for i in words if i not in bannet_set)
    return count.most_common(1)[0][0] # most_common(k) return the top k tuples


def odd_string(words: list[str]) -> str:
    """ odd string difference
        https://leetcode.com/problems/odd-string-difference
        [Datadog]
    """
    n = len(words[0])
    def get_difference(word:str, n:int) -> str:
        diff = ""
        for i in range(n - 1):
            diff += str(ord(word[i+1]) - ord(word[i])) + "-"
        return diff

    # Get patterns for first 3 words to determine which is common
    patterns = [get_difference(words[i], n) for i in range(3)]
    
    # Determine the common pattern
    if patterns[0] == patterns[1]:
        common_pattern = patterns[0]
    elif patterns[0] == patterns[2]:
        common_pattern = patterns[0]
    else:
        common_pattern = patterns[1]

    # Find and return the word with different pattern
    for word in words:
        if get_difference(word, n) != common_pattern:
            return word


def countCharacters(words: list[str], chars: str) -> int:
    """ 1160. Find Words That Can Be Formed by Characters
        https://leetcode.com/problems/find-words-that-can-be-formed-by-characters
        [Datadog]
    """
    char_count = Counter(chars)
    total = 0
    for word in words:
        word_count = Counter(word)
        if len(word_count - char_count) == 0:
            total += len(word)
    return total


def gcdOfStrings(str1: str, str2: str) -> str:
    """ 1071. Greatest Common Divisor of Strings
        https://leetcode.com/problems/greatest-common-divisor-of-strings
    """
    def is_divisor(divident:str, divisor:str) -> bool:
        """check with the divident and divisor relation is correct"""
        l1 = len(divident)
        l2 = len(divisor)
        if l1 % l2 != 0:
            return False
        else:
            multi = l1//l2
            return divident == divisor * multi
    n1 = len(str1)
    n2 = len(str2)
    n = min(n1, n2)
    i = 0
    gc = 0
    while (
        i < n and 
        str1[i] == str2[i]
    ):
        if (
            is_divisor(str1, str1[:i+1]) and
            is_divisor(str2, str2[:i+1])
        ):
            gc = i+1 # only update when there is a valide solution
        i += 1
    return str1[0:gc]




