""" greedy alogrithm"""
import collections

def getMinimumCost(k, c):
    """ 
    k people, buy all flows with prices in c. 
    the actual price is c * (times a person visited the magasin).
    find the min total price
    c: [101, 1 ,25, 6]
    idea: buy the most expensive flowers first
    """
    c = sorted(c, reverse=True)
    l = len(c)
    if k >= l:
        return sum(c)
    q = l // k
    r = l % k
    total = 0
    print(c)
    for i in range(1, q + 1):
        current_sum = sum(c[(i - 1) * k: i * k])
        print(c[(i - 1) * k: i * k])
        total += current_sum * i
    if r != 0:
        total += sum(c[-r:]) * (q + 1)
    return total
    

def reverseShuffleMerge(s):
    """ s = merge(reverse(a), shuffle(a))
         find the lexicographically smallest a
    """
    counts = collections.Counter(s) # every element need to reach this counts
    target = {v: c//2 for v,c in counts.items()}
    other = target.copy()
    buff = []
    for i in range(len(s)-1, -1, -1):
        c = s[i]
        while (
            buff and
            (top := buff[-1]) and
            c < top and
            other[top] > 0 and
            target[c] > 0
        ):
            other[top] -= 1
            target[top] += 1
            buff.pop()
        if target[c] > 0:
            buff.append(c)
            target[c] -= 1
        else:
            other[c] -= 1
    return ''.join(buff)


if __name__ == '__main__':
    print(reverseShuffleMerge('eggegg'))