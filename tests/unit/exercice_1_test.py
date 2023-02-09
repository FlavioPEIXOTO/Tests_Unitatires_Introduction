import unittest
from exercice_1 import *
from math import sqrt

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator();

    def test_add(self):
        self.assertEqual(self.calculator.add(14, 2), 16)
        self.assertEqual(self.calculator.add(-14, -2), -16)

        self.assertRaises(ValueError, self.calculator.add, 'd', 2)
        self.assertRaises(ValueError, self.calculator.add, 'd', '16')

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(14, 2), 12)
        self.assertEqual(self.calculator.subtract(-14, -2), -12)

        self.assertRaises(ValueError, self.calculator.subtract, 'd', 2)
        self.assertRaises(ValueError, self.calculator.subtract, 'd', '16')

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(14, 2), 28)
        self.assertEqual(self.calculator.multiply(-14, -2), 28)

        self.assertRaises(ValueError, self.calculator.multiply, 'd', 2)
        self.assertRaises(ValueError, self.calculator.multiply, 'd', '16')

    def test_divide(self):
        self.assertEqual(self.calculator.divide(14, 2), 7)
        self.assertEqual(self.calculator.divide(-14, -2), 7)
        self.assertRaises(ZeroDivisionError, self.calculator.divide, 2, 0)

        self.assertRaises(ValueError, self.calculator.divide, 'd', 2)
        self.assertRaises(ValueError, self.calculator.divide, 'd', '16')

    def test_power(self):
        self.assertEqual(Calculator.power(14, 2), 196)
        self.assertEqual(Calculator.power(0, 0), 1)
        self.assertEqual(Calculator.power(-14, -2), -1)

        self.assertRaises(ValueError, self.calculator.power, 'd', 2)
        self.assertRaises(ValueError, self.calculator.power, 'd', '16')

    def test_square_root(self):
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(1), 1)
        #self.assertAlmostEqual(square_root(2), sqrt(2), places=7)

        self.assertRaises(ValueError, square_root, 'd')

if __name__ == '__main__':
    unittest.main()