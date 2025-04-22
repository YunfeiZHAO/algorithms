""" bits operation related question"""

def count_bits(n):
    """ n is a int32, get the number of 1s in its binary format"""
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n >>= 1
    return count

if __name__ == '__main__':
    print(count_bits(23))