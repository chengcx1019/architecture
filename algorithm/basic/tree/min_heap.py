#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: min_heap.py
@time: 2018/5/16 21:15
"""
from basic.tree.bst_bfs import BinarySearchTreeBfs

"""
abstract data type-- priority queue
binary heap is one of implementations;
min heap (the key of parent node is smaller than any child node) max heap on the contrary;

not all trees are binary search tree
a array_string can represent a tree, wierd, 2*index+1 for left child, 2*index+2 for right child, to get parent take:(index-1)/2;
"""


class MinHeap(object):
    
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def insert(self, key):
        if key is None:
            raise TypeError("key can't be None")
        self.array.append(key)
        self._bubble_up(index=len(self.array)-1)

    def peek_min(self):
        return self.array[0] if self.array else None

    def extra_min(self):
        """move the last element to the root"""
        if not self.array:
            return None
        if len(self.array) == 1:
            return self.array.pop(0)
        minimum = self.array[0]
        self.array[0] = self.array.pop(-1)
        self._bubble_down(index=0)
        return minimum

    def _bubble_down(self, index):
        min_child_index = self._find_smaller_child(index)
        if min_child_index == -1:
            return
        if self.array[index] > self.array[min_child_index]:
            self.array[index], self.array[min_child_index] = self.array[min_child_index], self.array[index]
            self._bubble_down(min_child_index)

    def _bubble_up(self, index):
        if index == 0:
            return
        parent = (index - 1) // 2
        if self.array[parent] < self.array[index]:
            return
        else:
            self.array[parent], self.array[index] = self.array[index], self.array[parent]
            self._bubble_up(parent)

    def _find_smaller_child(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        if right_child_index >= len(self.array):
            if left_child_index >= len(self.array):
                return -1
            else:
                return left_child_index
        else:
            if self.array[left_child_index] < self.array[right_child_index]:
                return left_child_index
            else:
                return right_child_index


if __name__ == '__main__':
    pass
