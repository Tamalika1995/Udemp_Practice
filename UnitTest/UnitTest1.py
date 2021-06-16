import unittest
from TestClass import Example


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Example.add(self, 5, 70), 75)
        self.assertEqual(Example.add(self,5,7),12)
if __name__ == '__main__':
    unittest.main()
