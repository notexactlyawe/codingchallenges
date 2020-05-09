import os
import unittest
import subprocess
from read_results import parse_results

class ReadResultsTest(unittest.TestCase):
    TESTFILE = "test.csv"

    def tearDown(self):
        os.remove(self.TESTFILE)

    def test_simple_case(self):
        with open("simple_results", "r") as f:
            subprocess.run(["python3", "read_results.py", self.TESTFILE], stdin=f, timeout=1)

        with open(self.TESTFILE, 'r') as test:
            t = test.readlines()

        with open("expected_results.csv", "r") as expected:
            exp = expected.readlines()

        self.assertEqual(exp, t)

if __name__ == "__main__":
    unittest.main()
