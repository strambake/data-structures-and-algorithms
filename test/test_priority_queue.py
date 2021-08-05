import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from data_structures.Heap_PriorityQueue.BinaryHeap import BinaryHeap

def test_binary_heap():
    input = [1, 3, 4, 8, 14, 22]
    heap = BinaryHeap()
    heap.add(1)
    heap.add(8)
    assert  1 == heap.poll()
    heap.add(4)
    heap.add(3)
    assert 3 == heap.poll()
    assert 4 == heap.poll()
    heap.add(14)
    heap.add(22)
    assert 14 == heap.poll()
    assert 22 == heap.poll()