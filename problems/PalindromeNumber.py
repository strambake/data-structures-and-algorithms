# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
#
# Example 1:
#
# Input: x = 121
# Output: true
# Example 2:
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Example 4:
#
# Input: x = -101
# Output: false

from unittest import TestCase


class Solution():
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if s:
            length = len(s)
            for index in range(int(length/2)):
                if s[index] != s[length - 1 - index]:
                    return False
            return True
        return False


class TestPalindromeNumber(TestCase):
    def setUp(self) -> None:
        self.testData = {   121     :   True,
                            -121    :   False,
                            10      :   False,
                            -101    :   False   }


    def testBruteForceSolution(self):
        sol = Solution()
        for input, result in self.testData.items():
            self.assertEqual(result, sol.isPalindrome(input), msg='Checking palindrome of number {}'.format(input))
