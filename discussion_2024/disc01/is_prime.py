def is_prime(n):
    """
    判断一个自然数是否为质数

    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    i = 2
    if n == 1:
        return False
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True