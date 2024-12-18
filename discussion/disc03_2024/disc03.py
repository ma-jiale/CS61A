def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        "*** YOUR CODE HERE ***"
        all_but_last, last = n // 10, n % 10
        print(last)
        swipe(all_but_last)
        print(last)


def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 1: # 确保了当n递减到1或0时，递归能够正确停止，并返回正确的结果。
        return 1
    else:
        return n * skip_factorial(n - 2)
    

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


def hailstone(n):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n):
    return hailstone(n // 2) + 1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
def odd(n):
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    return hailstone(n * 3 + 1) + 1


def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def turn(i, who, direction):

        print("Player"+str(who)+"says"+str(i))
        if i == n:
            return who
        "*** YOUR CODE HERE ***"
        if has_seven(i) or i % 7 == 0:
            direction = -direction
            if direction == 1: 
                print("Switch back to clockwise")
            else:
                print("Switch back to counterclockwise")
        who + direction
        if who < 1:
            who = k
        if who > k:
            who = 1
        return turn(i + 1, who, direction)
    return turn(1, 1, 1)

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)
    
#  Implement a main() function that will leave Karel stopped halfway in the middle of the bottom row.    
# from karel.stanfordkarel import *

# def main():
#    # your code here...
#    if front_is_clear():
#       move()
#    if front_is_clear():
#       move()
#       main()
#       move()
#    else:
#       turn_left()
#       turn_left()