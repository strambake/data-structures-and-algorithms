# Fenwick tree data structure implementation
# @author: Swapnil Trambake, trambake.swapnil@gmail.com
#
# Fenwick tree (also called as Binary Index Tree aka BIT) is a data structure which
#   - calculates the value of function 'f' in a given range [l, r] in o(logn) time
#   - updates the value of list in o(logn) time
#   - requires o(n) extra space
#
# Application of the Fenwick tree is calculating the sum of a range
#

import copy
from typing import List


class FenwickTree():
    def __init__(self, nums : List[int]) -> None:
        self.__nums = [0]
        if nums:
            self.__nums.extend(nums)
            self.__tree = []
            self.__buildTree()


    def rangeSum(self, left: int, right: int) -> int:
        # For fenwick tree the range is always prefix of right minus
        if self.__nums and 0 <= left <= right <= len(self.__nums):
            sum = self.__prefixSum(right) - self.__prefixSum(left-1)
        else:
            sum = 0
        return sum


    def __buildTree(self):
        # https://youtu.be/BHPez138yX8

        length = len(self.__nums)

        # Copy the array into tree as is
        self.__tree = copy.deepcopy(self.__nums)

        # Iterate the tree and build tree
        for index in range(1, length):
            # At any index update the sum at next responsible index if index is less than N
            nextResponsibleIndex = index + self.__lsb(index)
            if nextResponsibleIndex < length:
                self.__tree[nextResponsibleIndex] += self.__tree[index]



    def __prefixSum(self, index: int) -> int:
        sum = 0
        while index > 0:
            sum += self.__tree[index]
            index -= self.__lsb(index)
        return sum


    @staticmethod
    def __lsb(index: int) -> int:
        return index & (index * -1)
