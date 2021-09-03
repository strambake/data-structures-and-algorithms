#
#   This is implementation of Union-Find data structure, also known as Disjoint Set or Merge-Find set
#   @author Swapnil Trambake, trambake.swapnil@gmail.com
#

import pprint

class UnionFind():
    def __init__(self) -> None:
        super().__init__()

        # key - data, value - parent
        self.__items = {}


    def find(self, item):
        """
        Find the item is present in any set, if present returns the root else None
        """
        root = None
        if item in self.__items.keys():
            root = item

            while self.__items[root] != root:
                root = self.__items[root]

        return root


    def makeSet(self, item):
        """
        Creates a new set with the item
        """
        if not self.find(item):
            # add the item as an independant set and make root as itself
            self.__items[item] = item


    def unify(self, firstItem, secondItem):
        """
        Merges two different set
        """
        root1 = self.find(firstItem)
        root2 = self.find(secondItem)

        if root1 > root2:
            self.__items[root2] = root1
        else:
            self.__items[root1] = root2


    def getSetItemsCount(self):
        """
        Returns list of set item count
        """
        sets = self.__getSets()
        return [len(arr) for arr in sets.values()]


    def printSets(self):
        """
        Prints all sets
        """
        sets = self.__getSets()
        pprint.pprint(sets)


    def __getSets(self):
        """
        Get all sets
        """
        sets = {}
        for item, root in self.__items.items():
            root = self.find(item)

            if root not in sets.keys():
                sets[root] = []
            sets[root].append(item)
        return sets
