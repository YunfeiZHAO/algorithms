""" tool for list """

def replace_recursive(array, target, dest):
    """ Given a list of N dim, replace all elements have the same value as target to dest"""
    for i, l in enumerate(array):
        if l == target or l is target:
            array[i] = dest
        if isinstance(l, list):
            replace_recursive(l, target, dest)

