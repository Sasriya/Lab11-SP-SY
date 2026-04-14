import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 3), 4)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(2,1), 1)
        self.assertEqual(subtract(3, 1), 2)
        self.assertEqual(subtract(4, 1), 3)

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(0, 5), 0)
        self.assertEqual(mul(-2, 6), -12)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(5, 20), 4)
        self.assertEqual(div(-2, 10), -5)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertRaises(ZeroDivisionError):
            (div(0, 5))


    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 1), 0)
        self.assertEqual(logarithm(4, 2), 2)
        self.assertEqual(logarithm(25, 5), 2)

    def test_log_invalid_base(self): # 1 assertion
        self.assertRaises(ValueError):
            (logarithm(0))
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, -5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)

    def test_sqrt(self):  # 3 assertions
        self.assertAlmostEqual(square_root(25), 5.0)
        self.assertAlmostEqual(square_root(9), 3.0)
        with self.assertRaises(ValueError):
            square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()