"""
A min priority queue implementation using a binary heap.
@author Swapnil Trambake, trambake.swapnil@gmail.com
"""

class BinaryHeap():
    """
    Class implements binary heap using array
    """
    def __init__(self) -> None:
        super().__init__()

        self.__heap = []


    def print(self):
        """
        Prints heap on console
        """
        print('The heap is: {}'.format(self.__heap))


    def add(self, item : int):
        """
        Add element into binary heap
        """
        print('Adding {}'.format(item))
        self.__heap.append(item)
        self.__swim(len(self.__heap) - 1)


    def poll(self):
        """
        Poll the heap, which gets high priority element
        """
        value = self.__heap[0]
        self.__remove(0)
        print('Polled {}'.format(value))
        return value


    def remove(self, value):
        """
        Removes specific element from heap
        """
        index = self.__find(value)
        if index:
            self.__remove(index)


    def __remove(self, index):
        print('Removing {} at index {}'.format(self.__heap[index], index))
        last_index = len(self.__heap) - 1
        if index != last_index:
            self.__swap(index, last_index)
            del self.__heap[last_index]

            parent_index = int((index - 1) / 2)
            if parent_index <= 0 or self.__heap[parent_index] < self.__heap[index]:
                self.__sink(index)
            else:
                self.__swim(index)


    def __find(self, value):
        print('Finding {} in heap'.format(value))
        index = None

        for i, val in enumerate(self.__heap):
            if value == val:
                index = i
                break

        print ('{} value {} in heap'.format('Found' if index else 'Not found', value))
        return index


    def __swim(self, index):
        """
        Perform bottom up swim o(log(n))
        """
        while True:
            parent = int((index - 1) / 2)
            if parent != index and \
                self.__heap[parent] >= self.__heap[index]:
                self.__swap(parent, index)
                index = parent
            else:
                break



    def __sink(self, index):
        """
        Perform top down sink o(log(n))
        """
        while index < len(self.__heap):
            leftChildIndex = 2 * index + 1
            rightChildIndex = 2 * index + 2

            if leftChildIndex < len(self.__heap) or rightChildIndex < len(self.__heap):
                if rightChildIndex < len(self.__heap):
                    if self.__heap[index] > self.__heap[leftChildIndex] and \
                        self.__heap[index] > self.__heap[rightChildIndex]:
                        indexToReplace = leftChildIndex \
                            if self.__heap[leftChildIndex] <= self.__heap[rightChildIndex] \
                            else rightChildIndex
                    elif self.__heap[index] > self.__heap[leftChildIndex]:
                        indexToReplace = leftChildIndex
                    else:
                        break
                else:
                    if self.__heap[index] > self.__heap[leftChildIndex]:
                        indexToReplace = leftChildIndex
                    else:
                        break
            else:
                break

            self.__swap(index, indexToReplace)
            index = indexToReplace



    def __swap(self, index1, index2):
        temp = self.__heap[index2]
        self.__heap[index2] = self.__heap[index1]
        self.__heap[index1] = temp
