import unittest
import calculate


class Calculate(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate.add(5, 10), 15)

    def test_subtract(self):
        self.assertEqual(calculate.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(calculate.multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(calculate.divide(10, 5), 2)

        # assertRaises
        self.assertRaises(ValueError, calculate.divide, 10, 0)
