import unittest
from io import StringIO
import sys

# Assuming your function is in a file named `greet.py`
from a import greetCandidates

class TestGreetCandidates(unittest.TestCase):
    def test_greetCandidates(self):
        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function
        greetCandidates()

        # Reset redirect
        sys.stdout = sys.__stdout__

        # Check if the output is as expected
        self.assertEqual(captured_output.getvalue().strip(), "Thanks for joining Git class")

if __name__ == '__main__':
    unittest.main()
