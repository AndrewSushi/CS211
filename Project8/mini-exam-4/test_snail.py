"""Test cases for snail graphics"""

import unittest
from snail import *


def trim_all(s: str) -> str:
    """Trim all lines in a multi-line string, to
    compare while ignoring indentation.
    """
    parts = s.strip().split("\n")
    trimmed_parts = [s.strip() for s in parts]
    return "\n".join(trimmed_parts)


class TestExample(unittest.TestCase):
    def test_example_ox(self):
        """The O-X combination encoded in hexadecimal"""
        expected = trim_all("""
        #  #  #  #  #  #  #  # 
        #  #  -  -  -  -  #  # 
        #  -  #  -  -  #  -  # 
        #  -  -  #  #  -  -  # 
        #  -  -  #  #  -  -  # 
        #  -  #  -  -  #  -  # 
        #  #  -  -  -  -  #  # 
        #  #  #  #  #  #  #  # 
        """)
        commands = ['BB', 'BD', 'BF', 'B9', 'BC', 'BF', 'BA', '81']
        snail = Snail()
        snail.interpret(commands)
        produced = trim_all(str(snail.slate))
        self.assertEqual(expected, produced)

    def test_example_s(self):
        expected = trim_all("""
        #  #  #  #  #  #  #  # 
        #  -  -  -  -  -  -  - 
        #  -  -  -  -  -  -  - 
        #  #  #  #  #  #  #  # 
        -  -  -  -  -  -  -  # 
        -  -  -  -  -  -  -  # 
        -  -  -  -  -  -  -  # 
        #  #  #  #  #  #  #  # 
        """)
        commands = ['3B', 'BF', '9D', 'BB', 'A5', 'C7']
        snail = Snail()
        snail.interpret(commands)
        produced = trim_all(str(snail.slate))
        self.assertEqual(expected, produced)

    def test_example_z(self):
        expected = trim_all("""
        #  #  #  #  #  #  #  # 
        -  -  -  -  -  -  #  - 
        -  -  -  -  -  #  -  - 
        -  -  -  -  #  -  -  - 
        -  -  -  #  -  -  -  - 
        -  -  #  -  -  -  -  - 
        -  #  -  -  -  -  -  - 
        #  #  #  #  #  #  #  # 
        """)
        commands = ['BB', 'BE', 'C3']
        snail = Snail()
        snail.interpret(commands)
        produced = trim_all(str(snail.slate))
        self.assertEqual(expected, produced)

    def test_example_o_o(self):
        expected = trim_all("""
        #  #  #  #  #  #  #  # 
        #  -  -  -  -  -  -  # 
        #  -  #  #  #  #  #  # 
        #  -  #  -  -  -  #  # 
        #  -  #  -  -  -  #  # 
        #  -  #  -  -  -  #  # 
        #  -  #  #  #  #  #  # 
        #  #  #  #  #  #  #  # 
        """)
        commands = ['BB', 'BD', 'BF', 'B9', '14', 'A3', 'A5', 'A7', 'A1']
        snail = Snail()
        snail.interpret(commands)
        produced = trim_all(str(snail.slate))
        self.assertEqual(expected, produced)


if __name__ == "__main__":
    unittest.main()
