import  unittest
import calc
class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(3, 5)
        self.assertEqual(result, 8)