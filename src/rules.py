""" Some questions defined some rules and we need to get the key points in these rules"""

def can_transform(start: str, result: str) -> bool:
    """ https://leetcode.com/problems/swap-adjacent-in-lr-string 
        Check whether we can ge results from start.

        Rules translation:
        L and R are like people in lines, X are the spaces.
        L can only move to left and R can only move to right

        Rules transform:
        1. If we remove all X, the start and result should be the same string (relative position)
        2. The for each L, we need to make sure that it do not need to go right to achieve the result string.
        3. For each R, we check the same thing.
    # """
    # 1. A basic implementation
    # s_x = start.replace('X', '')
    # r_x = result.replace('X', '')
    # if s_x != r_x:
    #     return False
    # pos = {
    #     "s_l": [],
    #     "s_r": [],
    #     "r_l": [],
    #     "r_r": []
    # }
    # for i, (s, r) in enumerate(zip(start, result)):
    #     match s:
    #         case "L":
    #             pos["s_l"].append(i)
    #         case "R":
    #             pos["s_r"].append(i)
    #     match r:
    #         case "L":
    #             pos["r_l"].append(i)
    #         case "R":
    #             pos["r_r"].append(i)
    # # As we check ther relative order in the first pass,
    # # they have the same length
    # n_l = len(pos["s_l"])
    # for i in range(n_l):
    #     if pos["s_l"][i] < pos["r_l"][i]:
    #         return False
    # n_r = len(pos["s_r"])
    # for i in range(n_r):
    #     if pos["s_r"][i] > pos["r_r"][i]:
    #         return False
    # return True


    #2. implementation with two pointers
    if len(start) != len(result):
        return False
    n = len(start)
    i = j = 0
    while i < n or j < n:
        while i < n and start[i] == "X":
            i += 1
        while j < n and result[j] == "X":
            j += 1
        if i == n and j == n:
            return True
        if i == n or j == n:
            return False
        if start[i] != result[j]:
            return False
        if start[i] == "L" and i < j:
            return False
        if start[i] == "R" and i > j:
            return False
        i += 1
        j += 1
    return True





