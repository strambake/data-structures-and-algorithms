# Given a string containing digits from 2-9 inclusive, 
# return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# 
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = ""
# Output: []

# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]

from typing import List
from utility.LogHelper import logger
from unittest import TestCase

class Solution():
    def __init__(self) -> None:
        self.__letterMap = {    '0' :   [],
                                '1' :   [],
                                '2' :   ['a', 'b', 'c'],
                                '3' :   ['d', 'e', 'f'],
                                '4' :   ['g', 'h', 'i'],
                                '5' :   ['j', 'k', 'l'],
                                '6' :   ['m', 'n', 'o'],
                                '7' :   ['p', 'q', 'r', 's'],
                                '8' :   ['t', 'u', 'v'],
                                '9' :   ['w', 'x', 'y', 'z']    }
    
    
    def letterCombinations(self, phoneNumber: str) -> List[str]:
        combinations = []
        self.__letterCombinations(phoneNumber, '', combinations)
        return combinations


    def __letterCombinations(self, phoneNumber: str, combination: str, combinations: List[str]):
        if phoneNumber:
            for c in self.__letterMap[phoneNumber[0]]:
                combination += c
                self.__letterCombinations(phoneNumber[1:], combination, combinations)
                combination = combination[:-1] # remove added character for next pass
        elif combination:
                combinations.append(combination)


class TestLetterCombinationsOfPhoneNumber(TestCase):
    def setUp(self) -> None:
        self.testData = {   '23'    :   ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'],
                            ''      :   [],
                            '2'     :   ['a', 'b', 'c'],
                            '5'     :   ['j', 'k', 'l'] }
        
    def test(self):
        sol = Solution()
        for input, result in self.testData.items():
            self.assertListEqual(result, sol.letterCombinations(input), 'Letter combinations of {}'.format(input))
