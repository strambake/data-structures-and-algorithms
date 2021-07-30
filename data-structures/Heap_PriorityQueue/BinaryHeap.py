#
# A min priority queue implementation using a binary heap.
# @author Swapnil Trambake, trambake.swapnil@gmail.com
#

class BinaryHeap(object):
    def __init__(self) -> None:
        super().__init__()

        self.__heap = []


    def print(self):
        print('The heap is: {}'.format(self.__heap))


    def add(self, item : int):
        print('Adding {}'.format(item))
        self.__heap.append(item)
        self.__swim(len(self.__heap) - 1)


    def poll(self):
        value = self.__heap[0]
        self.__remove(0)
        print('Polled {}'.format(value))
        return value


    def remove(self, value):
        index = self.__find(value)
        if index:
            self.__remove(index)
    

    def __swim(self, index):
        """
        Perform bottom up swim o(log(n)) 
        """
        while True:
            parent = int((index - 1) / 2)
            if parent == index:
                break
            elif self.__heap[parent] >= self.__heap[index]:
                self.__swap(parent, index)
                index = parent
            else:
                break
            

    def __remove(self, index):
        print('Removing {} at index {}'.format(self.__heap[index], index))
        lastIndex = len(self.__heap) - 1
        if index != lastIndex:
            self.__swap(index, lastIndex)
            del self.__heap[lastIndex]

            parentIndex = int((index - 1) / 2)
            if parentIndex <= 0 or self.__heap[parentIndex] < self.__heap[index]:
                self.__sink(index)
            else:
                self.__swim(index)


    def __find(self, value):
        print('Findi
        ng {} in heap'.format(value))
        index = None
        
        for i in range(len(self.__heap)):
            if value == self.__heap[i]:
                index = i
                break

        print ('{} value {} in heap'.format('Found' if index else 'Not found', value))
        return index


    def __sink(self, index):
        """
        Perform top down sink o(log(n))
        """
        while index < len(self.__heap):
            leftChildIndex = 2 * index + 1
            rightChildIndex = 2 * index + 2
            
            if leftChildIndex < len(self.__heap) or rightChildIndex < len(self.__heap):                
                if rightChildIndex < len(self.__heap):
                    if self.__heap[index] > self.__heap[leftChildIndex] and self.__heap[index] > self.__heap[rightChildIndex]:
                        indexToReplace = leftChildIndex if self.__heap[leftChildIndex] <= self.__heap[rightChildIndex] else rightChildIndex
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
