"""Binomial-tail calculations for small erasure-code groups."""
from math import comb, fsum


def prob_fail(p, m, n):
    """Probability of more than n failures among m+n disks."""
    if not 0 <= p <= 1:
        raise ValueError("p must be between 0 and 1")
    if not isinstance(m, int) or m < 1:
        raise ValueError("m must be a positive integer")
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    return fsum(comb(m+n, i) * p**i * (1-p)**(m+n-i)
                for i in range(n+1, m+n+1))


def parity_disks_needed(epsilon, p, m):
    """Smallest n with loss probability strictly below epsilon."""
    if not 0 < epsilon < 1:
        raise ValueError("epsilon must be between 0 and 1, exclusive")
    if not 0 <= p < 1:
        raise ValueError("p must be between 0 and 1, excluding 1")
    n = 0
    while prob_fail(p, m, n) >= epsilon:
        n += 1
    return n
