import unittest
from exercice_1 import *

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator();

    def test_add(self):
        #Verify additioning values above and below zero 
        self.assertEqual(self.calculator.add(14, 2), 16)
        self.assertEqual(self.calculator.add(-14, -2), -16)
        self.assertEqual(self.calculator.add(999999999999999, 999999999999999), 1999999999999998)

        #Verify Value error context with string values
        self.assertRaises(ValueError, self.calculator.add, 'd', 2)
        self.assertRaises(ValueError, self.calculator.add, '%@', '16')

    def test_subtract(self):
        #Verify substracting values above and below zero 
        self.assertEqual(self.calculator.subtract(14, 2), 12)
        self.assertEqual(self.calculator.subtract(-14, -2), -12)
        self.assertEqual(self.calculator.subtract(999999999999999, 0), 999999999999999)
        self.assertEqual(self.calculator.subtract(-999999999999999, 0), -999999999999999)

        #Verify Value error context with string values
        self.assertRaises(ValueError, self.calculator.subtract, 'd', 2)
        self.assertRaises(ValueError, self.calculator.subtract, '%@', '16')

    def test_multiply(self):
        #Verify multiplying values above and below zero 
        self.assertEqual(self.calculator.multiply(14, 2), 28)
        self.assertEqual(self.calculator.multiply(-14, -2), 28)
        self.assertEqual(self.calculator.multiply(-999999999999999, -999999999999999), 999999999999998000000000000001)
        self.assertEqual(self.calculator.multiply(999999999999999, 999999999999999), 999999999999998000000000000001)

        #Verify Value error context with string values
        self.assertRaises(ValueError, self.calculator.multiply, 'd', 2)
        self.assertRaises(ValueError, self.calculator.multiply, '%@', '16')

    def test_divide(self):
        #Verify dividing values above and below zero 
        self.assertEqual(self.calculator.divide(14, 2), 7)
        self.assertEqual(self.calculator.divide(-14, -2), 7)
        self.assertEqual(self.calculator.divide(999999999999999, 999999999999999), 1)
        self.assertEqual(self.calculator.divide(-999999999999999, -999999999999999), 1)

        #Verify Value error context with string values
        self.assertRaises(ZeroDivisionError, self.calculator.divide, 2, 0)
        self.assertRaises(ValueError, self.calculator.divide, 'd', 2)
        self.assertRaises(ValueError, self.calculator.divide, '%@', '16')

    def test_power(self):
        #Verify power function values above and below zero 
        self.assertEqual(self.calculator.power(14, 2), 196)
        self.assertEqual(self.calculator.power(0, 0), 1)
        self.assertEqual(self.calculator.power(-14, -2), 1)
        self.assertEqual(self.calculator.power(999999999999999, 2), 999999999999998000000000000001)

        #Verify Value error context with string values
        self.assertRaises(ValueError, self.calculator.power, 'd', 2)
        self.assertRaises(ValueError, self.calculator.power, '%@', '16')

    def test_square_root(self):
        #Verify square_root function values above and below zero 
        self.assertEqual(self.calculator.square_root(14), 3.7416573867739458)
        self.assertEqual(self.calculator.square_root(0), 0)
        self.assertEqual(self.calculator.square_root(999999999999999), 31622776.601683777)

        #Verify Value error context with string values
        self.assertRaises(ValueError, self.calculator.square_root, -14)
        self.assertRaises(ValueError, self.calculator.square_root, 'd')

if __name__ == '__main__':
    unittest.main()