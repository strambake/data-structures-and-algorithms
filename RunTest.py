"""
Test Runner class

@Author Swapni Trambake, trambake.swapnil@gmail.com
"""

import os
import sys
from unittest import TextTestRunner, TestLoader
from unittest.suite import TestSuite

sys.path.append(os.path.dirname(__file__))

from problems.IntegerToRoman import TestIntegerToRoman

class RunTests():
    def __init__(self) -> None:
        self.suit = TestSuite()
        self.suit.addTests(TestLoader().loadTestsFromTestCase(TestIntegerToRoman))


if __name__ == "__main__":
    testRunner = TextTestRunner()
    testRunner.run(RunTests().suit)
