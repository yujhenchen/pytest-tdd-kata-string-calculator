import sys


class StringCalculator:

    """
    The method can take up to two numbers,
    separated by commas, and will return their sum as a result.
    So the inputs can be: “”, “1”, “1,2”. For an empty string, it will return 0
    """

    def add(self, string: str) -> int:
        if string.isnumeric():
            return int(string)
        return 0
