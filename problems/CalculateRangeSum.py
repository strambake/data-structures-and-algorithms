#
#

import os
import sys
from typing import List
from unittest import TestCase
from unittest.signals import removeResult

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from data_structures.Trees.FenwickTree import FenwickTree


class RangeSumNaiveSolution():
    def __init__(self, nums: List[int] = None) -> None:
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        """
        Calculates sum with linear time o(n)
        """
        sum = 0
        if self.nums and left >= 0 and left <= right and right <= len(self.nums):
            for num in self.nums[left:(right+1)]:
                sum += num

        return sum


class TestRangeSumNaiveSolution(TestCase):
    def setUp(self) -> None:
        self.input = [-2, 0, 3, -5, 2, -1]

    def testRangeSumValidIndexes(self):
        input = [-2, 0, 3, -5, 2, -1]
        self.assertEqual(1, RangeSumNaiveSolution(input).sumRange(0, 2))
        self.assertEqual(-1, RangeSumNaiveSolution(input).sumRange(2, 5))
        self.assertEqual(-3, RangeSumNaiveSolution(input).sumRange(0, 5))
        

    def testRangeSumInvalidIndexes(self):
        input = [-2, 0, 3, -5, 2, -1]
        self.assertEqual(0, RangeSumNaiveSolution(input).sumRange(0, 7))
        self.assertEqual(0, RangeSumNaiveSolution(input).sumRange(5, 0))

    
    def testRangeSumEmptyList(self):
        self.assertEqual(0, RangeSumNaiveSolution().sumRange(0, 3))


    def testRangeSumSameIndex(self):
        input = [-1]
        self.assertEqual(-1, RangeSumNaiveSolution(input).sumRange(0, 0))


class RangeSumUsingPrefixSum():
    """
    Calculates sum with linear time o(1)
    Need extra space of o(n)
    Solution is to prepare a new array of n+1 having prefix sums
    Disadvantage: Updates to array cause regeneration of prefix sum array
    """
    def __init__(self, nums: List[int] = None) -> None:
        self.nums = nums
        if self.nums:
            self.prefixSums = [0] * (len(self.nums) + 1)
            # Generate prefix sum
            for index, num in enumerate(self.nums):
                self.prefixSums[index+1] = self.nums[index] + self.prefixSums[index]
        


    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        if self.nums and left >= 0 and left <= right and right <= len(self.nums):
            sum = self.prefixSums[right+1] - self.prefixSums[left] 
        return sum


class TestRangeSumUsingPrefixSum(TestCase):
    def setUp(self) -> None:
        self.input = [-2, 0, 3, -5, 2, -1]

    def testRangeSumValidIndexes(self):
        input = [-2, 0, 3, -5, 2, -1]
        self.assertEqual(1, RangeSumUsingPrefixSum(input).sumRange(0, 2))
        self.assertEqual(-1, RangeSumUsingPrefixSum(input).sumRange(2, 5))
        self.assertEqual(-3, RangeSumUsingPrefixSum(input).sumRange(0, 5))
        

    def testRangeSumInvalidIndexes(self):
        input = [-2, 0, 3, -5, 2, -1]
        self.assertEqual(0, RangeSumUsingPrefixSum(input).sumRange(0, 7))
        self.assertEqual(0, RangeSumUsingPrefixSum(input).sumRange(5, 0))

    
    def testRangeSumEmptyList(self):
        self.assertEqual(0, RangeSumUsingPrefixSum().sumRange(0, 3))


    def testRangeSumSameIndex(self):
        input = [-1]
        self.assertEqual(-1, RangeSumUsingPrefixSum(input).sumRange(0, 0))


class RangeSumUsingFenwickTree():
    """
    Calculates sum with linear time o(1)
    Need extra space of o(n)
    Solution is to prepare a new array of n+1 having prefix sums
    Disadvantage: Updates to array cause regeneration of prefix sum array
    """
    def __init__(self, nums: List[int] = None) -> None:
        self.fenwickTree = FenwickTree(nums)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.fenwickTree.rangeSum(left, right)


class TestRangeSumUsingFenwickTree(TestCase):
    def setUp(self) -> None:
        self.input = [-2, 0, 3, -5, 2, -1]

    def testRangeSumValidIndexes(self):
        input = [-2, 0, 3, -5, 2, -1]
        # Fenwick tree is one based index
        self.assertEqual(1, RangeSumUsingFenwickTree(input).sumRange(1, 3))
        self.assertEqual(-1, RangeSumUsingFenwickTree(input).sumRange(3, 6))
        self.assertEqual(-3, RangeSumUsingFenwickTree(input).sumRange(1, 6))
        

    def testRangeSumInvalidIndexes(self):
        input = [-2, 0, 3, -5, 2, -1]
        self.assertEqual(0, RangeSumUsingFenwickTree(input).sumRange(1, 8))
        self.assertEqual(0, RangeSumUsingFenwickTree(input).sumRange(6, 1))

    
    def testRangeSumEmptyList(self):
        self.assertEqual(0, RangeSumUsingFenwickTree().sumRange(1, 4))


    def testRangeSumSameIndex(self):
        input = [-1]
        self.assertEqual(-1, RangeSumUsingFenwickTree(input).sumRange(1, 1))
