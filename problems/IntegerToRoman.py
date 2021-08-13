# Author: Swapnil Trambake, trambake.swapnil@gmail.com
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.
# Example 1:
#
# Input: num = 3
# Output: "III"
# Example 2:
#
# Input: num = 4
# Output: "IV"
# Example 3:
#
# Input: num = 9
# Output: "IX"
# Example 4:
#
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# Example 5:
#
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

from unittest import TestCase


class Solution(object):
    def __init__(self) -> None:
        super().__init__()
        self.__romans = {
            1       :   'I',
            2       :   'II',
            3       :   'III',
            4       :   'IV',
            5       :   'V',
            9       :   'IX',
            10      :   'X',
            40      :   'XL',
            50      :   'L',
            90      :   'XC',
            100     :   'C',
            400     :   'CD',
            500     :   'D',
            900     :   'CM',
            1000    :   'M'}

        


    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        output = ""

        # Iterate over all keys in descending order
        for key in sorted(self.__romans.keys(), reverse=True):
            # If num is zero or None, return output
            if not num:
                return output

            # Check if num is greater than the current key
            if num >= key:
                digit = int(num / key)
                for _unused_index in range(0, digit):
                    output += self.__romans[key]
                num %= key 

        return output


class TestIntegerToRoman(TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        return True

    def testIntToRoman3(self):
        self.assertEqual('III', self.sol.intToRoman(3))


    def testIntToRoman4(self):
        self.assertEqual('IV', self.sol.intToRoman(4))


    def testIntToRoman9(self):
        self.assertEqual('IX', self.sol.intToRoman(9))


    def testIntToRoman58(self):
        self.assertEqual('LVIII', self.sol.intToRoman(58))
    

    def testIntToRoman1994(self):
        self.assertEqual('MCMXCIV', self.sol.intToRoman(1994))


    def testIntToRoman40(self):
        self.assertEqual('XL', self.sol.intToRoman(40))

    def testIntToRoman400(self):
        self.assertEqual('CD', self.sol.intToRoman(400))
