# Merge two sorted linked lists and return it as a sorted list. 
# The list should be made by splicing together the nodes of the first two lists.
# 
# Example 1:
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# 
# Example 2:
# Input: l1 = [], l2 = []
# Output: []
# 
# Example 3:
# Input: l1 = [], l2 = [0]
# Output: [0]

from data_structures.LinkedLists.SinglyLinkedList import SinglyLinkedList, ListNode
from typing import List, Optional
from unittest import TestCase


class Solution:
    def __init__(self) -> None:
        self.__outputList = None
        self.__lastNode = None

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    self.__insert(l1.val)
                    l1 = l1.next
                else:
                    self.__insert(l2.val)
                    l2 = l2.next
            elif l1:
                self.__insert(l1.val)
                l1 = l1.next
            elif l2:
                self.__insert(l2.val)
                l2 = l2.next
        
        return self.__outputList


    def __insert(self, val: int):
        if not self.__outputList:
            self.__outputList = ListNode(val)
            self.__lastNode = self.__outputList
        else:
            self.__lastNode.next = ListNode(val)
            self.__lastNode = self.__lastNode.next


class TestMergingTwoSortedList(TestCase):
    def test(self):
        self.__test([], [[], []])
        self.__test([0], [[], [0]])
        self.__test([1,1,2,3,4,4], [[1,2,4],[1,3,4]])
    
    
    def __test(self, result, input):
        firstList = SinglyLinkedList()
        for val in input[0]:
            firstList.insert(val)

        secondList = SinglyLinkedList()
        for val in input[1]:
            secondList.insert(val)

        sol = Solution()
        outputListNode = sol.mergeTwoLists(firstList.getRootNode(), secondList.getRootNode())

        outputArr = []
        while outputListNode:
            outputArr.append(outputListNode.val)
            outputListNode = outputListNode.next

        self.assertListEqual(result, outputArr)
