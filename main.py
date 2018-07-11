"""
Project Euler # 150 - 'Counting Digits'
"""

from math import log10

def naive_f(n, d, a=0):
    """
    >>> naive_f(0, 1)
    0
    >>> naive_f(1, 1)
    1
    >>> naive_f(2, 1)
    1
    >>> naive_f(12, 1)
    5
    >>> naive_f(199980, 1)
    199979
    >>> naive_f(199981, 1)
    199981
    >>> naive_f(10, 7)
    1
    >>> naive_f(100, 0)
    12
    >>> naive_f(100, 7)
    20
    >>> naive_f(1000, 0)
    193
    >>> naive_f(1000, 7)
    300
    >>> naive_f(100, 5, 70)
    3
    >>> naive_f(100, 8, 70)
    13
    """
    count = 0
    for i in range(a, n + 1):
        count += str(i).count(str(d))
    return count


def f(n, d, start=0):
    """
    >>> f(0, 1)
    0
    >>> f(1, 1)
    1
    >>> f(2, 1)
    1
    >>> f(12, 1)
    5
    >>> f(199980, 1)
    199979
    >>> f(199981, 1)
    199981
    >>> f(10, 7)
    1
    >>> f(100, 0)  # doctest: +SKIP
    12
    >>> f(100, 7)
    20
    >>> f(1000, 0)  # doctest: +SKIP
    193
    >>> f(1000, 7)
    300
    >>> f(100, 5, 70)  # doctest: +SKIP
    3
    >>> naive_f(100, 8, 70)  # doctest: +SKIP
    13
    """
    if n < 10:
        return 1 if n >= d else 0
    limit = int(log10(n))
    return limit * 10**(limit - 1) + sum(str(i).count(str(d)) for i in range(10**limit, n + 1))


if __name__ == '__main__':
    import doctest; doctest.testmod()
