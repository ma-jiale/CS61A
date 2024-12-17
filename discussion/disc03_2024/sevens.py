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