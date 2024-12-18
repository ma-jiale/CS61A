def fizzbuzz(n):
    """
    The fizzbuzz function takes a positive integer n and prints out a single line for each integer from 1 to n. For each i:
    If i is divisible by both 3 and 5, print fizzbuzz.
    If i is divisible by 3 (but not 5), print fizz.
    If i is divisible by 5 (but not 3), print buzz.
    Otherwise, print the number i.

    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    k = 1
    while k <= n:
        if k % 3 == 0 and k % 5 == 0:
            print("fizzbuzz")
        elif k % 3 == 0 and k % 5 != 0:
            print("fizz")
        elif k % 5 == 0 and k % 3 != 0:
            print("buzz")
        else:
            print(k)
        k += 1

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

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    uniques = 0 
    k = 0 
    while k < 10:
        if has_digit(n, k):
            uniques += 1
        k += 1
    return uniques

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    while n != 0:
        if n % 10 == k:
            return True
        n = n // 10
    return False