# Nary tree implemention
# Author: Swapnil Trambake, trambake.swapnil@gmail.com


# Node structure to hold node value and it's corresponding left and right child link
class Node():
    def __init__(self, value: int) -> None:
        super().__init__()
        self.val = value
        self.children : int = []


# Class implements N-ary undirected tree
class NaryTree():
    def __init__(self, rootValue) -> None:
        super().__init__()
        self.__root = Node(rootValue)


    def insertNode(self, nodeValue : int, parent : int):
        parentNode = self.__find(parent)
        if parentNode:
            newNode = Node(nodeValue)
            parentNode.children.append(newNode)


    def inorder(self) -> []:
        output = []
        self.__inorder(self.__root, output)
        return output


    def preorder(self) -> []:
        output = []
        self.__preorder(self.__root, output)
        return output


    def postorder(self) -> []:
        output = []
        self.__postorder(self.__root, output)
        return output


    def levelorder(self) -> []:
        output = []
        queue = []
        queue.append(self.__root)

        while queue.count():
            node = queue.pop(0)
            output.append(node.val)
            for child in node.children:
                queue.append(child)

        return output

    def __find(self, nodeValue: int) -> Node:
        return self.__findNode(self.__root, nodeValue)


    def __findNode(self, node : Node, nodeValue : int) -> Node:
        foundNode = None
        if node.val == nodeValue:
            foundNode = node
        else:
            for child in node.children:
                n = self.__findNode(child, nodeValue)
                if n:
                    foundNode = n
        return foundNode


    def __inorder(self, node : Node, output) -> None:
        if node:
            numChilds = len(node.children)
            if numChilds > 1:
                for index in range(numChilds - 1):
                    self.__inorder(node.children[index], output)
            output.append(node.val)

            if (numChilds - 1) > 0:
                self.__inorder(node.children[numChilds - 1], output)


    def __preorder(self, node: Node, output : []) -> None:
        if node:
            output.append(node.val)
            for child in node.children:
                self.__preorder(child, output)


    def __postorder(self, node: Node, output : []) -> None:
        if node:
            for child in node.children:
                self.__postorder(child, output)
            output.append(node.val)
