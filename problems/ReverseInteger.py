# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# Example 1:
#
# Input: x = 123
# Output: 321
# Example 2:
#
# Input: x = -123
# Output: -321
# Example 3:
#
# Input: x = 120
# Output: 21
# Example 4:
#
# Input: x = 0
# Output: 0

from utility.LogHelper import logger
from unittest import TestCase


class BruteForceSolution():
    def reverse(self, x: int) -> int:
        digits = []
        signed = x < 0 

        if signed:
            x = x*-1

        while x > 0:
            digits.append(x%10)
            x = int(x/10)

        output = 0
        for index in range(len(digits)):
            decimal = 1
            for _unused_index in range(len(digits) - index - 1):
                decimal *= 10

            output += (digits[index]*decimal)


        return output*-1 if signed else 0 if output >= 0xFFFFFFF else output


class OptimizedSolution():
    def reverse(self, x: int) -> int:
        signed = x < 0 

        if signed:
            x = x*-1

        output = 0
        index = 0
        while x > 0:
            digit = x%10
            output = int(output*10 + digit) 
            index += 1
            x = int(x/10)

        return 0 if output > 0x7FFFFFFF else output*-1 if signed else output
        


class TestReverseInteger(TestCase):
    def setUp(self) -> None:
        self.testData = {   123         :   321,
                            -123        :   -321,
                            120         :   21,
                            0           :   0 }


    def testBruteForceSolution(self):
        sol = BruteForceSolution()
        for input, result in self.testData.items():
            self.assertEqual(result, sol.reverse(input))


    def testOptimizedSolution(self):
        self.testData[1534236469] = 0
        self.testData[-2147483412] = -2143847412
        self.testData[-2147483648] = 0
        sol = OptimizedSolution()
        for input, result in self.testData.items():
            self.assertEqual(result, sol.reverse(input), 'Reverse of {}'.format(input))
