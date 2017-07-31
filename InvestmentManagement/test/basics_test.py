import unittest

import InvestmentManagement.basics as basics

class BasicsTests(unittest.TestCase):

    def test_return(self):
        expected = 0.09
        self.assertAlmostEqual(expected, basics.calc_return(100, 110), places=2)

if __name__ == '__main__':
    unittest.main()   # pragma: no cover
