
import unittest
from program import multiplication

class testMult(unittest.TestCase):

    def test_mul1(self):
        result1 = multiplication(5, 10)
        self.assertEqual(result1, 50)

    def test_mul2(self):
        result2 = multiplication(-1, 10)
        self.assertEqual(result2, -10)

    def test_mul3(self):
        result3 = multiplication(-1, -10)
        self.assertEqual(result3, 10)

if __name__ == '__main__':
    unittest.main()
