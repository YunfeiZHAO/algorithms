""" bit related questions """
from typing import List

def generate_super_string(s):
    """Generate all possible super strings."""
    zeros_indices = [i for i, bit in enumerate(s) if bit == '0']
    num_zeros = len(zeros_indices)
    super_strings = []

    for i in range(1 << num_zeros):  # Iterate over all combinations
        temp_bit_list = list(s)
        for j, zero_index in enumerate(zeros_indices):
            if i & (1 << j):  # Check if the j-th bit of i is set
                temp_bit_list[zero_index] = '1'
        super_strings.append("".join(temp_bit_list))
    return super_strings


def super_bitstring(n:int, bit_strings:List):
    """ given a bit string, we can flip zero or more of the 0s in the bit string to 1.
        given a list of bitString and the bit length n. get all possible bit strings that
        we can have.
        Args:
            n: binary size
            bit_strings: list of int of decimal
    """
    super_set = set(bit_strings)
    n_bit_string = len(bit_strings)
    for i in range(n-1):
        for j in range(i+1, n_bit_string):
            u = bit_strings[i]
            v = bit_strings[j]
            intersect = u & v
            if intersect == u:
                super_set.remove(v)
            if intersect == v:
                super_set.remove(u)

    # convert to bin and remove 0b at the begin and extend to n
    bins = [(bin(d)[2:]).zfill(n) for d in super_set]
    super_set = set(bins)
    for s in bins:
        super_strings = generate_super_string(s)
        super_set.update(super_strings)
    return super_set


def get_sum(a: int, b: int) -> int:
    """ https://neetcode.io/problems/sum-of-two-integers
        add two integer without + operation
    """
    # 0x  hexadecimal (base-16) number
    # 32 bits integer max, 01111111 11111111 11111111 11111111
    MAX_INT = 0x7FFFFFFF
    # Mask to get last 32 bits, 11111111 11111111 11111111 11111111
    mask = 0xFFFFFFFF

    while b != 0:
        # Calculate sum without carry using XOR
        sum_ = (a ^ b) & mask
        # Calculate carry using AND, then shift left by 1
        carry = ((a & b) << 1) & mask
        # Prepare for next iteration
        a, b = sum_, carry
    # If a is greater than MAX_INT, it's a negative number in 32-bit
    if a > MAX_INT:
        # Convert to Python's negative integer using two's complement
        return ~(a ^ mask)
    else:
        return a


if __name__ == "__main__":
    # print(super_bitstring(4, [9,2]))
    print(get_sum(1, 9))