""" string manipulation """
from collections import Counter

def divide_simply(s1, s2):
    """ s1/s2 simply the common variables, result in no common chars """
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

if __name__ == '__main__':
    s1 = 'abbd'
    s2 = 'be'
    print(divide_simply(s1,s2))