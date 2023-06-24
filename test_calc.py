# Author: Mitch Allen

# To run:
#   python test_calc.py
#   python -m unittest test_calc.py
#   python -m unittest 

import io
import unittest
from unittest.mock import patch
from calc import Calc

class CalcTest(unittest.TestCase):

    def verify_output(self,user_input,expected_output):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with patch('builtins.input', side_effect=user_input):
                c = Calc()
                c.run()

            self.assertIn(expected_output, fake_stdout.getvalue())

    def test_quit(self):
        user_input = ['quit']
        expected_output = f"Bye!"
        self.verify_output(user_input,expected_output)

    def test_add(self):
        user_input = ['add 5', 'quit']
        expected_output = f"total: 5.0"
        self.verify_output(user_input,expected_output)

    def test_sub(self):
        user_input = ['sub 5', 'quit']
        expected_output = f"total: -5.00"
        self.verify_output(user_input,expected_output)

if __name__ == '__main__':
    unittest.main()

