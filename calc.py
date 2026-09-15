"""Python 3 version of the paper's historical calculator.

The normal approximation is retained for comparison, not as a substitute
for the binomial-tail calculation. Intended for small disk groups.
"""
from math import sqrt
from statistics import NormalDist

from sample_code import parity_disks_needed, prob_fail


def kc_rl(epsilon, p, m):
    """Redundancy factor from the Rodrigues-Liskov approximation."""
    if not 0 < epsilon < 1:
        raise ValueError("epsilon must be between 0 and 1, exclusive")
    if not 0 <= p < 1:
        raise ValueError("p must be between 0 and 1, excluding 1")
    if not isinstance(m, int) or m < 1:
        raise ValueError("m must be a positive integer")
    # Symmetry avoids rounding 1-epsilon to 1 for small epsilon.
    se = -NormalDist().inv_cdf(epsilon)
    a = 1.0 - p
    return ((se * sqrt(a*p/m) + sqrt(4*a + se**2*a*p/m)) / (2*a))**2


def kc_exact(epsilon, p, m):
    """Redundancy factor using the smallest sufficient parity count."""
    n = parity_disks_needed(epsilon, p, m)
    return (m+n) / m


if __name__ == "__main__":
    print("Approximate redundancy (m=6, p=0.001):", kc_rl(1e-6, 0.001, 6))
    print("Binomial redundancy (m=6, p=0.001):", kc_exact(1e-6, 0.001, 6))
    print("Binomial redundancy (m=8, p=0.005):", kc_exact(1e-6, 0.005, 8))
    print("8+3 loss probability (p=0.005):", prob_fail(0.005, 8, 3))
