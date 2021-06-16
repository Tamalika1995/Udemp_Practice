import unittest
from UnitTest1 import main


class TestMain(unittest.TestCase):

    def setUp(self) :
        print("about a run a test")
    def tearDown(self)  :
        print("cleanUP")
    def test_main(self):
        name='tamalika'
        age=26
        result= main.print_hi(name, age)
        self.assertEqual(result,'Hi, tamalika --you are 26 years old')

    def test_main1(self):
        name = 'tamalika'
        age = 26
        result = main.print_hi(name, age)
        self.assertNotEqual(result, 'Hi, tamalika --you are 67 years old')

    def test_main2(self):
         testparam='jgfghf'
         result = main.sum1(testparam)
         self.assertTrue(isinstance(result, ValueError))
    def test_main3(self):
         testparam=10
         result = main.sum1(testparam)
         self.assertEqual(result, 15)
    def test_main4(self):
         testparam='jgfghf'
         result = main.sum1(testparam)
         self.assertIsInstance(result, ValueError)
    def test_main4(self):
         testparam=None
         result = main.sum1(testparam)
         self.assertEqual(result, "enter a no")
    def test_main5(self):
         testparam=""
         result = main.sum1(testparam)
         self.assertEqual(result, "enter a no")

if __name__=="__main__":
    unittest.main ###this is not related to the Main file(i.e main.py)
