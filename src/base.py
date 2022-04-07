"""Changing bases."""

digits = {}

for i in range(0, 10):
    digits[i] = str(i)

digits[10] = 'A'
digits[11] = 'B'
digits[12] = 'C'
digits[13] = 'D'
digits[14] = 'E'
digits[15] = 'F'


def change_to_base(n: int, b: int) -> str:
    """
    Return `n` in base `b`.

    The base `b` must be in the range 2 to 16.

    >>> change_to_base(1, 2)
    '1'
    >>> change_to_base(31, 2)
    '11111'
    >>> change_to_base(31, 8)
    '37'
    >>> change_to_base(31, 16)
    '1F'
    """
    assert 2 <= b <= 16

    # zero is a special case
    if n == 0:
        return '0'

    # dealing with sign (this isn't safe outside of Python!)
    sign, n = ('', n) if n > 0 else ('-', -n)

    res = []
    while n:
        res.append(digits[n % b])
        # Integer division is always "floor division" in Python. That means
        # that we cannot get 0 for negative numbers (we will get -1). Other
        # languages do "truncate division" and there a number in the range
        # (-1,0] maps to zero. Yet other languages don't specify it (and then
        # we have to get creative!). Here, we ensure that n and b are
        # positive; then floor and truncate division is the same, and
        # when n < b we get zero.
        n //= b
    return sign + "".join(res[::-1])
