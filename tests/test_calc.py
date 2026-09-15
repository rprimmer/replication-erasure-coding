"""Independent small-system checks and regressions for the sample errors."""
import itertools
import unittest
from fractions import Fraction

from calc import kc_exact, kc_rl
from sample_code import parity_disks_needed, prob_fail


class CalculationTests(unittest.TestCase):
    def test_exhaustive_failure_outcomes(self):
        # Enumerate disk states, independently of the binomial formula.
        p = Fraction(1, 4)
        for m in range(1, 5):
            for n in range(4):
                expected = Fraction(0)
                for state in itertools.product((False, True), repeat=m+n):
                    if sum(state) > n:
                        weight = Fraction(1)
                        for failed in state:
                            weight *= p if failed else 1-p
                        expected += weight
                self.assertAlmostEqual(prob_fail(float(p), m, n), float(expected))

    def test_paper_example(self):
        self.assertEqual(parity_disks_needed(1e-6, 0.005, 8), 3)
        self.assertLess(prob_fail(0.005, 8, 3), 1e-6)
        self.assertGreaterEqual(prob_fail(0.005, 8, 2), 1e-6)
        self.assertEqual(kc_exact(1e-6, 0.005, 8), 1.375)

    def test_endpoints_and_zero_parity(self):
        self.assertEqual(prob_fail(0, 8, 3), 0)
        self.assertEqual(prob_fail(1, 8, 3), 1)
        self.assertEqual(parity_disks_needed(0.1, 0, 8), 0)
        self.assertEqual(parity_disks_needed(0.1, 0.01, 1), 0)
        # Equality does not satisfy the paper's strict inequality.
        self.assertEqual(parity_disks_needed(0.5, 0.5, 1), 1)

    def test_invalid_inputs(self):
        for args in [(-0.1, 2, 1), (1.1, 2, 1), (0.1, 0, 1),
                     (0.1, 2, -1), (0.1, 1.5, 1), (0.1, 2, 1.5)]:
            with self.assertRaises(ValueError):
                prob_fail(*args)
        for args in [(0, 0.1, 2), (1, 0.1, 2), (0.1, 1, 2)]:
            with self.assertRaises(ValueError):
                parity_disks_needed(*args)
            with self.assertRaises(ValueError):
                kc_rl(*args)

    def test_normal_approximation(self):
        self.assertEqual(kc_rl(0.01, 0, 6), 1)
        # With epsilon=0.5 the normal quantile is exactly zero.
        self.assertAlmostEqual(kc_rl(0.5, 0.2, 6), 1.25)
        self.assertGreater(kc_rl(1e-20, 0.005, 8), 1)


if __name__ == '__main__':
    unittest.main()
