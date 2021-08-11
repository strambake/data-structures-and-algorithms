#
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
#
# @author: Swapnil Trambake, trambake.swapnil@gmail.com
#
#   Example 1:
#
#   Input: nums = [100,4,200,1,3,2]
#   Output: 4
#   Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#   Example 2:
#
#   Input: nums = [0,3,7,2,5,8,4,6,0,1]
#   Output: 9
# 
#
#   Constraints:
#
#   0 <= nums.length <= 105
#   -109 <= nums[i] <= 109

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from unittest import TestCase
from typing import List

from data_structures.UnionFind.UnionFind import UnionFind


class UsingUnionFind(object):
    def __init__(self, input : List[int]) -> None:
        super().__init__()
        self.__list = input

        self.__unionFind = UnionFind()

    def calculateLongestConsecutiveSubsequence(self):
        for item in self.__list:
            # Check if item is present in any set
            root = self.__unionFind.find(item)
            
            if not root:
                # Item doesn't exists in any set
                self.__unionFind.makeSet(item)
            
            # Let's find next or previous consecutive number exists in set
            nextRoot = self.__unionFind.find(item + 1)
            prevRoot = self.__unionFind.find(item - 1)
            if nextRoot:
                self.__unionFind.unify(item, item+1)
            if prevRoot:
                self.__unionFind.unify(item, item-1) 

        counts = self.__unionFind.getSetItemsCount()
        max = 0
        for count in counts:
            if max < count:
                max = count

        return max
                


class TestLongestConsecutiveSubsequence(TestCase):
    def testLongestConsecutiveSubsequence(self):
        input = [100,4,200,1,3,2] 
        sol = UsingUnionFind(input)
        self.assertEqual(4, sol.calculateLongestConsecutiveSubsequence())
