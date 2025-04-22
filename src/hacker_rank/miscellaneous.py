""" diverse questions"""

def flippingBits(n):
    """ n is unsigned int32. flip all bit 1 -> 0 0 -> 1 and retunr the new int32"""
    # Flip all bits and mask to ensure it's a 32-bit unsigned integer
    return ~n & 0xFFFFFFFF

