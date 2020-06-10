import unittest
import calculate


class Calculate(unittest.TestCase):
    # TODO
    def test_add(self):
        self.assertEqual(calculate.add(5, 10), 15)
