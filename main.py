"""
Project Euler # 156 - 'Counting Digits'
"""

from math import log10

def naive_f(n, d):
    """
    >>> naive_f(0, 0)
    1

    >>> naive_f(0, 1)
    0

    >>> naive_f(1, 1)
    1

    >>> naive_f(2, 1)
    1

    >>> naive_f(12, 1)
    5

    >>> naive_f(10, 7)
    1

    >>> naive_f(100, 0)
    12

    >>> naive_f(100, 5)
    20

    >>> naive_f(100, 7)
    20

    >>> naive_f(100, 8)
    20
    
    >>> naive_f(1000, 0)
    193

    >>> naive_f(1000, 7)
    300

    >>> naive_f(199980, 1)
    199979

    >>> naive_f(199981, 1)
    199981
    """
    count = 0
    for i in range(n + 1):
        count += str(i).count(str(d))
    return count


def f(n, d):
    """
    >>> f(0, 0)
    1

    >>> f(0, 1)
    0

    >>> f(1, 1)
    1

    >>> f(2, 1)
    1

    >>> f(12, 1)
    5

    >>> f(10, 7)
    1

    >>> f(100, 0)
    12

    >>> f(100, 5)
    20

    >>> f(100, 7)
    20

    >>> f(100, 8)
    20

    >>> f(1000, 0)
    193

    >>> f(1000, 7)
    300

    >>> f(3539, 5)
    1044

    >>> f(7478, 6)
    3198

    >>> f(199980, 1)
    199979

    >>> f(199981, 1)
    199981
    """
    if n == 0:
        return 1 if d == 0 else 0
    s = 0
    for i in range(int(log10(n)) + 1):
        s1 = 1 + (n - 10**i * d) % 10**(i + 1)
        s2 = (n + 10**i * (-d % 10)) // 10**(i + 1)
        s += max(min(s1, 10**i) * (s2 > 0) + 10**i * (s2 - 1), 0)
    return s + (1 if d == 0 else 0)


if __name__ == '__main__':
    import doctest; doctest.testmod()
