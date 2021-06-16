import unittest
from UnitTest1 import guess_no


class TestGame(unittest.TestCase):
    def test_input(self):
        # please note in the video, I had the parameters flipped it should be the "guess" parameter 1st and "answer" parameter 2nd
        result = guess_no.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = guess_no.run_guess(0, 6)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = guess_no.run_guess(11, 5)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = guess_no.run_guess('11', 5)
        self.assertFalse(result)
if __name__=="__main__":
    unittest.main ###this is not related to the Main file(i.e main.py)
