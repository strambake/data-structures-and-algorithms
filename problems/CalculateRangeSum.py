#
#

from typing import List
from unittest import TestCase


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
