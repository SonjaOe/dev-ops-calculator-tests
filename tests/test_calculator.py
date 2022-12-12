import calculator.calculator as calculator
import unittest

class test_calculator(unittest.TestCase):
    def test_plus(self):
        num1 = 1.8
        num2 = 2.4
        expected_result = 4.2
        result = calculator.plus(num1, num2)
        self.assertEqual(expected_result, result)
    
    def test_minus(self):
        num1 = 1.8
        num2 = 2.4
        expected_result = -0.6
        result = calculator.minus(num1, num2)
        self.assertAlmostEqual(expected_result, result)

    def test_multiply(self):
        num1 = 1.8
        num2 = 2.4
        expected_result = 4.32
        result = calculator.multiply(num1, num2)
        self.assertAlmostEqual(expected_result, result)

    def test_divide(self):
        num1 = 1.8
        num2 = 2.4
        expected_result = 0.75
        result = calculator.divide(num1, num2)
        self.assertAlmostEqual(expected_result, result)

    def test_divide_by_zero(self):
        num1 = 1.8
        num2 = 0
        expected_result = "Cannot divide by zero"
        result = calculator.divide(num1, num2)
        self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()