# Binary tree implemention
# Author: Swapnil Trambake, trambake.swapnil@gmail.com

from enum import Enum

# Enumeration for node position
class NodePosition_E(Enum):
    Left    = 0
    Right   = 1


# Node structure to hold node value and it's corresponding left and right child link
class Node():
    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value
        self.left : Node = None
        self.right : Node = None


# Class implements binary tree data structure
class BinaryTree():
    def __init__(self, rootValue) -> None:
        super().__init__()
        self.__root = Node(rootValue)


    def insertNode(self, value : int, parent : int, nodePosition : NodePosition_E):
        self.__insertNode(self.__root, value, parent, nodePosition)


    def inorder(self):
        output = []
        self.__inorder(self.__root, output)
        return output


    def preorder(self):
        output = []
        self.__preorder(self.__root, output)
        return output


    def postorder(self):
        output = []
        self.__postorder(self.__root, output)
        return output


    def __insertNode(self, node : Node, value : int, parent : int, nodePosition : NodePosition_E):
        if not node:
            return

        if node.value == parent:
            newNode = Node(value)

            if nodePosition == NodePosition_E.Left:
                node.left = newNode
            elif nodePosition == NodePosition_E.Right:
                node.right = newNode
        else:
            self.__insertNode(node.left, value, parent, nodePosition)
            self.__insertNode(node.right, value, parent, nodePosition)


    def __inorder(self, node : Node, output):
        if node:
            self.__inorder(node.left, output)
            output.append(node.value)
            self.__inorder(node.right, output)


    def __preorder(self, node : Node, output):
        if node:
            output.append(node.value)
            self.__preorder(node.left, output)
            self.__preorder(node.right, output)


    def __postorder(self, node : Node, output):
        if node:
            self.__postorder(node.left, output)
            self.__postorder(node.right, output)
            output.append(node.value)
