def memory(n):
    """ 返回一个使用传入的函数修改n的函数
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x- 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def f(g):
        nonlocal n
        n = g(n)
        return n
    return f




