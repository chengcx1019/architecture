#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: invert_bst.py
@time: 2018/5/18 08:08
"""
from basic.tree.binary_search_tree import BinarySearchTree
from basic.tree.bst_bfs import BinarySearchTreeBfs

class InvertBst(BinarySearchTreeBfs):

    def __init__(self):
        super(InvertBst, self).__init__()

    def invert_tree(self):
        if self.root is None:
            raise TypeError("root can't be None")
        return self._invert_tree(self.root)

    def _invert_tree(self, root):
        if root is None:
            return
        self._invert_tree(root.left)
        self._invert_tree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root


if __name__ == '__main__':
    pass