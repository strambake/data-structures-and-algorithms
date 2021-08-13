# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, 
# which, together with the x-axis forms a container, such that the container contains the most water.
#
# Notice that you may not slant the container.
#
# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
#
# Example 2:
# Input: height = [1,1]
# Output: 1
#
# Example 3:
# Input: height = [4,3,2,1,4]
# Output: 16
#
# Example 4:
# Input: height = [1,2,1]
# Output: 2

from unittest import TestCase


from typing import List


class On2Solution():
    """ Brute force solution takes o(n^2) time complexity
    """
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        for i in range(0, len(heights)):
            for j in range(i+1, len(heights)):
                water = min(heights[i], heights[j]) * (j-i)
                if water > maxWater:
                    maxWater = water

        return maxWater


class OnSolution():
    """Better solution with o(n) complexity
    """
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        i = 0
        j = len(heights) - 1
        while i != j:
            water = min(heights[i], heights[j]) * (j-i)
            if water > maxWater:
                    maxWater = water

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return maxWater



class TestContainerWithMostWater(TestCase):
    def setUp(self) -> None:
        self.testData = {   1   :   [1,1],
                            16  :   [4, 3, 2, 1, 4],
                            49  :   [1,8,6,2,5,4,8,3,7],
                            2   :   [1,2,1] }


    def testNaiveSolution(self):
        sol = On2Solution()
        for result, input in self.testData.items():
            self.assertEqual(result, sol.maxArea(input), 'Checking container with most water in {}'.format(input))


    def testOnSolution(self):
        sol = OnSolution()
        for result, input in self.testData.items():
            self.assertEqual(result, sol.maxArea(input), 'Checking container with most water in {}'.format(input))
