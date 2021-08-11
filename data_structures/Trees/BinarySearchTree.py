"""
Binary search tree implemention
Author: Swapnil Trambake, trambake.swapnil@gmail.com
"""

class BinarySearchTree():
    def __init__(self) -> None:
        super().__init__()
        self.__maxNodes = 32
        self.__rootIndex = 0
        self.__nodes = []
        for _unused_i in range(self.__maxNodes):
            self.__nodes.append(None)


    def add(self, value : int):
        if self.__isEmpty():
            self.__nodes[self.__rootIndex] = value
        else:
            index = self.__rootIndex

            while self.__hasNodeValue(index):
                if value <= self.__getNodeValue(index):
                    index = self.__leftChildIndex(index)
                else:
                    index = self.__rightChildIndex(index)
            self.__nodes[index] = value


    def inorder(self):
        output = []
        self.__inorder(self.__rootIndex, output)
        return output


    def preorder(self):
        output = []
        self.__preorder(self.__rootIndex, output)
        return output


    def postorder(self):
        output = []
        self.__postorder(self.__rootIndex, output)
        return output


    def __isEmpty(self) -> bool:
        return bool(self.__nodes[0])


    def __getNodeValue(self, index):
        return self.__nodes[index] if index < len(self.__nodes) else None


    def __hasNodeValue(self, index) -> bool:
        return self.__getNodeValue(index) is not None


    @staticmethod
    def __leftChildIndex(index) -> int:
        return 2*index + 1


    @staticmethod
    def __rightChildIndex(index) -> int:
        return 2*index + 2


    def __inorder(self, index, output):
        if self.__hasNodeValue(index):
            self.__inorder(self.__leftChildIndex(index), output)
            output.append(self.__getNodeValue(index))
            self.__inorder(self.__rightChildIndex(index), output)


    def __preorder(self, index, output):
        if self.__hasNodeValue(index):
            output.append(self.__getNodeValue(index))
            self.__preorder(self.__leftChildIndex(index), output)
            self.__preorder(self.__rightChildIndex(index), output)


    def __postorder(self, index, output):
        if self.__hasNodeValue(index):
            self.__postorder(self.__leftChildIndex(index), output)
            self.__postorder(self.__rightChildIndex(index), output)
            output.append(self.__getNodeValue(index))
