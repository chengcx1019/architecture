#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: min_bst.py
@time: 2018/5/23 14:02
"""
from basic.tree.binary_search_tree import BinaryTreeNode


class MinBst(object):
    """
    create a binary search tree with minist heigth from a sorted array_string
    """
    def __init__(self, root=None):
        self.root = root

    def min_bst(self, sorted_array):
        if sorted_array is None:
            return None
        self.root = self._min_bst(sorted_array, 0, len(sorted_array) - 1)
        return self.root.val

    def _min_bst(self, array, start, end):
        if start > end:
            return
        mid = (end + start) // 2
        node = BinaryTreeNode(array[mid])
        node.left = self._min_bst(array, start, mid - 1)
        node.right = self._min_bst(array, mid + 1, end)
        return node


if __name__ == '__main__':
    pass
