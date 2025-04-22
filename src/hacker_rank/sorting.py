""" Sorting problems"""
from collections import defaultdict
from functools import cmp_to_key


class Player:
    """ compare player 
        first in decreasing order score
        second in increasing order name
    """
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return f"{self.name}: {self.score}"

    @staticmethod
    def comparator(a, b):
        """ compare operation"""
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        else:
            if a.name <= b.name:
                return -1
            else:
                return 1


def test_player():
    """ run the Player comparator"""
    data = [["amy", 100],
            ["david", 100],
            ["heraldo", 50],
            ["aakansha", 75],
            ["aleksa ", 150]]
    players = []
    for name, score in data:
        player = Player(name, score)
        players.append(player)
    players = sorted(players, key=cmp_to_key(Player.comparator))
    for p in players:
        print(p)


def find_med(bucket, d):
    """ find median value from bucket of value counts"""
    pair = d%2 == 0
    med_count =  [d//2 + 1, d//2] if pair else [d//2+1]
    cur_count = 0
    med = 0
    for i, c in enumerate(bucket):
        cur_count += c
        while med_count and med_count[-1] <= cur_count:
            med += i
            med_count.pop()
        if len(med_count) == 0:
            break
    return med/2 if pair else med


def activityNotifications(expenditure, d):
    """ if the d+1's value is bigger than the previous d expenditure's median
        then there will be a notice. get the total notice.
        Args:
            expenditure: number of values
            d: days
        1 <= n <= 2*10^5
        1 <= d <=n
        0 <= expenditure[i] <= 200
        we can use bucket sort idea as the expenditure is limited
    """
    n = len(expenditure)
    max_expenditure = 200
    bucket = [0] * (max_expenditure + 1)
    alert = 0
    for i in range(d):
        bucket[expenditure[i]] += 1
    for i in range(d,n):
        cur_e = expenditure[i]
        if cur_e >= find_med(bucket, d) * 2:
            alert += 1
        bucket[expenditure[i - d]] -= 1
        bucket[expenditure[i]] += 1
    return alert


def check_just_complete(machines, goal, n):
    """ check with time n which machines can just achieve the goal.
        we check whether n achieve the goal and n-1 can not.
    """
    s_p = sum([(n-1)//m for m in machines])
    s = sum([n//m for m in machines])
    if s >= goal:
        if s_p < goal:
            return 0
        else:
            return 1
    else:
        return -1


def minTime(machines, goal):
    """ get min time to have the goal number of products.
        Args: 
            machines: list of time needed to produce a product for each machine.
            goal: total products needed
    """
    most_efficient = min(machines)
    # get upper bound
    r = most_efficient * goal
    l = 0
    mid = (l + r)//2
    while (c := check_just_complete(machines, goal, mid)) != 0:
        if c == -1:
            l = mid + 1
        else:
            r = mid - 1
        mid = (l + r)//2
    return mid


def count_inversions(arr):
    """ count the inversion number of an arr
        for i,j, if i < j and arr[i] > arr[j] then there is an inversion.
    """
    def merge_sort(arr):
        """ we use merge sort to do the count here"""
        n = len(arr)
        if n == 1:
            return arr, 0
        mid = n // 2
        l, inv_l = merge_sort(arr[:mid])
        r, inv_r = merge_sort(arr[mid:])
        merged, inv_split = merge(l, r)
        total_inv = inv_l + inv_r +  inv_split
        return merged, total_inv

    def merge(left, right):
        """ merge of part left and right"""
        i = j = inv = 0
        l_n, r_n = len(left), len(right)
        merge = []
        while i < l_n and j < r_n:
            if left[i] <= right[j]:
                merge.append(left[i])
                i += 1
            else:
                merge.append(right[j])
                inv += l_n - i
                j += 1
        merge += left[i:]
        merge += right[j:]
        return merge, inv

    _, total = merge_sort(arr)
    return total


if __name__ == "__main__":
    # machines = [4,5,6]
    # goal = 12
    # print(minTime(machines, goal))

    arr = [2,1,3,1,2]
    print(count_inversions(arr))
