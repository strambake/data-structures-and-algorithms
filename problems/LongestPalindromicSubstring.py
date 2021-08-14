# Given a string s, return the longest palindromic substring in s.
# 
# Example 1:
# 
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
# 
# Input: s = "cbbd"
# Output: "bb"
# Example 3:
# 
# Input: s = "a"
# Output: "a"
# Example 4:
# 
# Input: s = "ac"
# Output: "a"
#
# @author: Swapnil Trambake, trambake.swapnil@gmail.com

from utility.LogHelper import logger
from unittest import TestCase


class On2Solution1():
    def longestPalindrome(self, s: str) -> str:
        result = ''
        if s:
            length = len(s)
            for index1 in range(0, length):
                for index2 in range(index1, length):
                    subString = s[index1:index2+1] if index1 != index2 else s[index1]
                    
                    if self.__isPalindrome(subString):
                        if len(subString) > len(result):
                            result = subString

        return result


    def __isPalindrome(self, string: str) -> bool:
        """Worst solution takes o(n^3)

        Args:
            string (str): [description]

        Returns:
            bool: [description]
        """
        logger.debug('Checking substring {} for palindrome...'.format(string))
        palindrome = False
        if string:
            palindrome = True
            midPoint = int(len(string)/2)
            logger.debug('midpoint: {}'.format(midPoint))
            for index in range(midPoint+1):
                respectiveRightIndex = (len(string) - index - 1)
                logger.debug('index: {}, respectiveRightIndex: {}'.format(index, respectiveRightIndex))
                if index < respectiveRightIndex:
                    if respectiveRightIndex < 0:
                        respectiveRightIndex = 0
                    if string[index] != string[respectiveRightIndex]:
                        palindrome = False

        logger.debug('{} is {}'.format(string, 'palindrome' if palindrome else 'not palindrome'))
        return palindrome


class On2Solution2():
    def longestPalindrome(self, s: str) -> str:
        res = ''
        if s:
            start = end = 0            

            for i in range(len(s)):
                length1 = self.__getLongestPalindromeFromMidIndex(s, i, i)
                length2 = self.__getLongestPalindromeFromMidIndex(s, i, i+1)
                length = max(length1, length2)
                if length > (end - start + 1):
                    start = i - int((length-1)/2)
                    end = i + int(length/2)
            res = s[start:(end+1)]

        return res


    def __getLongestPalindromeFromMidIndex(self, s: str, left: int, right: int) -> int:
        if s and left <= right:
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            res = right - left - 1
        else:
            res = 0

        return res



class TestLongestPalindromicSubstring(TestCase):
    def setUp(self) -> None:
        self.testData = {   'babad' :   'bab',
                            'cbbd'  :   'bb',
                            'a'     :   'a',
                            'ac'    :   'a',
                            ''      :   '',
                            'bb'    :   'bb'    }
        return super().setUp()



    def testOn2Solution1(self):
        logger.debug('\nTesting with naive solution having o(n^2)...')
        on2Sol = On2Solution1()

        for testString, result in self.testData.items(): 
            self.assertEqual(result, on2Sol.longestPalindrome(testString), 'Getting longest palindrome of \'{}\''.format(testString))


    def testOn2Solution2(self):
        logger.debug('\nTesting with better solution having o(n^2)...')
        on2Sol = On2Solution2()

        for testString, result in self.testData.items():
            self.assertEqual(result, on2Sol.longestPalindrome(testString), 'Getting longest palindrome of \'{}\''.format(testString))


    def testOn2SolutionLongInput(self):
        on2Sol = On2Solution2()
        input = """civilwartestingwhetherthatnaptionoranynartionsoc
                onceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefieml
                doftzhatwarWehavecometodedicpateaportionofthatfieldasafinal
                restingplaceforthosewhoheregavetheirlivesthatthatnationm
                ightliveItisaltogetherfangandproperthatweshoulddothisBu
                tinalargersensewecannotdedicatewecannotconsecratewecan
                nothallowthisgroundThebravelmenlivinganddeadwhostruggled
                herehaveconsecrateditfaraboveourpoorponwertoaddordetractTghew
                orldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwh
                attheydidhereItisforusthelivingrathertobededicatedheretotheulnfinished
                workwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobehere
                dedicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetake
                increaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthat
                weherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsder
                Godshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeople
                shallnotperishfromtheearth"""
        self.assertEqual('', on2Sol.longestPalindrome(input).strip())
