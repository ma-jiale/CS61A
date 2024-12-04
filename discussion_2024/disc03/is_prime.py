# def is_prime(n):
#     assert n > 1
#     i = 2
#     while i < n:
#         if n % i == 0:
#             return False
#         i = i + 1
#     return True

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    assert n > 1

    return helper(n, 2)

def helper(n, i):
    """检查i到n之间的整数能否整除n"""
    if i == n:
        return True
    elif n % i == 0:
        return False
    return helper(n, i + 1)