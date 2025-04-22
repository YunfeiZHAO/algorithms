""" divide and conquer problems
https://www.youtube.com/watch?v=ib4BHvr5-Ao
https://time.geekbang.org/column/article/73503

map reduce, merge sort, partition sort all use the divide and conquer problem.
1. we seperate problems in sub problems
2. recursively solve sub problems. if a problem is small enough, we can solve it.
3. Merge the sub problems back to the origina problem

When we resolve a problem with divide and conquer, the sub problems have the same pattern
as the orignal problem. They are not related to each other (the main difference to dynamic programming).
There should be a stop dividing condition and the merge complexity should not be high.
"""
