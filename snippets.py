def count_digits(n):
    res = 0
    while n > 0:
        res += 1
        n = n // 10
    return res


def count_matches(n, m):
    """Returns the number of digits that match.
    >>> count_matches(10, 30)
    1
    >>> count_matches(12345, 23456)
    0
    >>> count_matches(212121, 321321)
    2
    >>> count_matches(101, 11) # only one’s place matches
    1
    >>> count_matches(101, 10) # no place matches
    0
    """
    res = 0
    while n > 0 and m > 0:
        if n % 10 == m % 10:
            res += 1
        n = n // 10
        m = m // 10
    return res