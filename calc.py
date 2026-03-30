import unittest
import Calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = Calc.add(3, 5)
        self.assertEqual(result, 8)

    def test_sub(self):
        result = Calc.sub(3, 5)
        self.assertEqual(result, 2)

     
