#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: in_order_successor_bst.py
@time: 2018/5/22 23:27
"""
from basic.tree.binary_search_tree import BinarySearchTree, BinaryTreeNode

class InOrderSuccessorBst(BinarySearchTree):

    def __init__(self):
        super(InOrderSuccessorBst, self).__init__()

    def in_order_successor(self, node: BinaryTreeNode):
        if node is None:
            raise TypeError("node can't be None")
        if node.right is not None:
            return self._left_most(node.right)
        else:
            return self._next_ancestor(node)

    def _left_most(self, node: BinaryTreeNode):
        if node.left is not None:
            return self._left_most(node.left)
        else:
            return node.val

    def _next_ancestor(self, node: BinaryTreeNode):
        if node.parent is not None:
            if node.parent.val > node.val:
                return node.parent.val
            else:
                return self._next_ancestor(node.parent)

        return None


if __name__ == '__main__':
    pass
