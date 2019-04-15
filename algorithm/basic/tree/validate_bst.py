#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: validate_bst.py
@time: 2018/5/23 14:26
"""
import sys
from basic.tree.binary_search_tree import BinarySearchTree
"""
Determine if a tree is a valid binary search tree
"""


class ValidateBst(BinarySearchTree):

    def validate_bst(self):
        if self.root is None:
            raise TypeError("root can't be None")
        return self._validate(self.root)

    def _validate(self, node, minimum=-sys.maxsize, maximum=sys.maxsize):
        if node is None:
            return True
        if node.val < minimum or node.val >= maximum:  # 需要和binary search tree的判断逻辑一致，相等的数去右子树
            return False
        if not self._validate(node.left, minimum, node.val):
            return False
        if not self._validate(node.right, node.val, maximum):
            return False
        return True


if __name__ == '__main__':
    pass
