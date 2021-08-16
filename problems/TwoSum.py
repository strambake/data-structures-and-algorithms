# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

from typing import List
from unittest import TestCase


class TwoSumSolution():
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store the number need for index
        needs = {}
        result = []

        for index, num in enumerate(nums):
            # Check if this number is needed by any previous number to complete sum
            if num in needs.keys():
                result.append([needs[num], index])
            else:
                need = target-num
                needs[need] = index

        return result



class TestTwoSum(TestCase):
    def testTwoSum(self):
        sol = TwoSumSolution()
        self.assertListEqual([[0,1]], sol.twoSum([2,7,11,15], 9))
        self.assertListEqual([[1,2]], sol.twoSum([3,2,4], 6))
        self.assertListEqual([[0,1]], sol.twoSum([3,3], 6))