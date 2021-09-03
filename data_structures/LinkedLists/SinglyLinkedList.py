from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self) -> None:
        self.__root = None


    def insert(self, val: int):
        if self.__root:
            p = self.__root
            while p.next:
                p = p.next
            p.next = ListNode(val)
        else:
            self.__root = ListNode(val)


    def getRootNode(self) -> Optional[ListNode]:
        return self.__root
