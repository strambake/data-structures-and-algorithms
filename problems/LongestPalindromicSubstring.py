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


class NaiveSolution():
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        result = ''
        for index1 in range(0, length):
            for index2 in range(index1, length):
                subString = s[index1:(index2+1)] if index1 != index2 else s[index1]
                
                if self.__isPalindrome(subString):
                    if len(subString) > len(result):
                        result = subString
                    break

        return result


    def __isPalindrome(self, string: str) -> bool:
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


class TestNaiveSolution(TestCase):
    def testLongestPalindromicSubstring(self):
        logger.debug('Hey hey ...')
        naiveSolution = NaiveSolution()
        self.assertEqual('bab', naiveSolution.longestPalindrome('babad'))
        self.assertEqual('bb', naiveSolution.longestPalindrome('cbbd'))
        self.assertEqual('a', naiveSolution.longestPalindrome('a'))
        self.assertEqual('a', naiveSolution.longestPalindrome('ac'))
        self.assertEqual('', naiveSolution.longestPalindrome(''))
        self.assertEqual('bb', naiveSolution.longestPalindrome('bb'))
        # self.assertEqual('', naiveSolution.longestPalindrome('civilwartestingwhetherthatnaptionoranynartionsoc'\
        #     'onceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefieml'\
        #         'doftzhatwarWehavecometodedicpateaportionofthatfieldasafinal'\
        #             'restingplaceforthosewhoheregavetheirlivesthatthatnationm'\
        #                 'ightliveItisaltogetherfangandproperthatweshoulddothisBu'\
        #                     'tinalargersensewecannotdedicatewecannotconsecratewecan'\
        #                         'nothallowthisgroundThebravelmenlivinganddeadwhostruggled'\
        #                             'herehaveconsecrateditfaraboveourpoorponwertoaddordetractTghew'\
        #                                 'orldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwh'\
        #                                     'attheydidhereItisforusthelivingrathertobededicatedheretotheulnfinished'\
        #                                         'workwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobehere'\
        #                                             'dedicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetake'\
        #                                                 'increaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthat'\
        #                                                     'weherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsder'\
        #                                                         'Godshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeople'\
        #                                                             'shallnotperishfromtheearth'))
