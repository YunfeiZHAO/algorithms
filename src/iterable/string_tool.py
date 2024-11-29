""" string manipulation """
import string
from collections import Counter


def divide_simply(s1, s2):
    """ s1/s2 simplify the common variables, result in no common chars """
    s1 = Counter(s1)
    s2 = Counter(s2)
    for c, n1 in s1.items():
        if c in s2:
            n2 = s2[c]
            if n1 >= n2:
                s1[c] = n1 - n2
                del s2[c]
            else:
                s2[c] = n2 - n1
                del s1[c]
    s1 = ''.join([char * freq for char, freq in s1.items()])
    s2 = ''.join([char * freq for char, freq in s2.items()])
    return (s1, s2)


def generate_one_char_diff_strings(s: str, str_set:set=None):
    """ generate same length string, with only one character difference """
    return [
        g_s
        for i in range(len(s))
        for char in string.ascii_lowercase
        if char != s[i] and (g_s := s[:i] + char + s[i + 1:]) in str_set
    ]


def compare_same_len_diff_n(str1: str, str2: str) -> bool:
    """ count the different char numbers for the first n common elements, 
        n is the length of the shortest string.
    """
    if len(str1) != len(str2):
        return False
    diff_count = sum(char1 != char2 for char1, char2 in zip(str1, str2))
    return diff_count

if __name__ == '__main__':
    s1 = 'abbd'
    s2 = 'be'
    print(divide_simply(s1,s2))

