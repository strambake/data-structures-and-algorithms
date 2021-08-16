# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

from typing import List
from unittest import TestCase


class Solution():
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''

        if strs:
            for index, char in enumerate(strs[0]):
                match = True
                for s in strs[1:]:
                    if index >= len(s) or s[index] != char:
                        match = False
                        break

                if match:
                    prefix += strs[0][index]
                else:
                    break

        return prefix


class TestLongestCommonPrefix(TestCase):
    def setUp(self) -> None:
        self.__testData = { 'fl'    :   ['flower', 'flow', 'flight'],
                            ''      :   ['dog', 'racecar', 'car'],
                            'a'     :   ['ab', 'a']}


    def test(self):
        sol = Solution()
        for result, input in self.__testData.items():
            self.assertEquals(result, sol.longestCommonPrefix(input), 'Getting longest common prefix of {}'.format(input))