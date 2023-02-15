import unittest
from string_calculator import StringCalculator

""" 
test cases 

scenario    input, output
empty string:    "" ,0
no number:   ",", 0
one number: "1", 1
one number: ",1", 1
one number: "1,", 1
two numbers: "2,3", 5
two number negative: "-2,3", 1
Exception: invalid iput, no number: "a,bc"
Exception: invalid iput, too many number: "1,34,7"
Exception: invalid iput, mix: "4,bc"

"""


class TestStringCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.stringCalculator = StringCalculator()
        return super().setUp()

    def test_return_0(self) -> None:
        self.assertEqual(0, self.stringCalculator.add(""))

    def test_no_number_return_0(self) -> None:
        self.assertEqual(0, self.stringCalculator.add(","))

    def test_return_1(self) -> None:
        self.assertEqual(1, self.stringCalculator.add("1"))


if __name__ == "__main__":
    unittest.main()
