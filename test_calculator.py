import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(2, -2), 0)
        self.assertEqual(self.calc.add(-3, -5), -8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
        self.assertEqual(self.calc.subtract(-2, -2), 0)
        self.assertEqual(self.calc.subtract(-3, -5), 2)
    
    def test_multiple(self):
        self.assertEqual(self.calc.multiply(2, 0), 0)
        self.assertEqual(self.calc.multiply(2, -3), -6)
        self.assertEqual(self.calc.multiply(-5, -3), 15)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 0), "Error can't divide by zero")
        self.assertEqual(self.calc.divide(0, -3), 0)
        self.assertEqual(self.calc.divide(-5, -5), 1)
        self.assertEqual(self.calc.divide(-10, 5), -2)
        self.assertEqual(self.calc.divide(5, 2), 2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(-10, -3), -1)
        self.assertEqual(self.calc.modulo(25, 7), 4)
        self.assertEqual(self.calc.modulo(0, 3), 0)
        self.assertEqual(self.calc.modulo(3, 1), 0)
        self.assertEqual(self.calc.modulo(1, 7), 1)
       


    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()