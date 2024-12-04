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


