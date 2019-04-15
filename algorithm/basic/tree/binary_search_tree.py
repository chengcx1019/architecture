#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: binary_search_tree.py
@time: 2018/5/16 19:56
"""

"""
bst
"""


class BinaryTreeNode(object):
    
    def __init__(self, data=None):
        self.val = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.val)
        

class BinarySearchTree(object):
    
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if data is None:
            raise TypeError("data can't be none")
        if self.root is None:
            self.root = BinaryTreeNode(data)
            return self.root
        else:
            return self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return BinarySearchTree(data)
        if data < node.val:
            if node.left is None:
                node.left = BinaryTreeNode(data)
                node.left.parent = node
                return node.left
            else:
                return self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = BinaryTreeNode(data)
                node.right.parent = node
                return node.right
            else:
                return self._insert(node.right, data)

#  3(in\pre\post_order) dfs of tree


class Traversal(object):

    def __init__(self):
        pass

    def in_order_traversal(self, node, visit_func):
        """
        left root right
        """
        if node is not None:
            self.in_order_traversal(node.left, visit_func)
            visit_func(node)
            self.in_order_traversal(node.right, visit_func)

    def pre_order_traversal(self, node, visit_func):
        """
        root left right
        """
        if node is not None:
            visit_func(node)
            self.pre_order_traversal(node.left, visit_func)
            self.pre_order_traversal(node.right, visit_func)

    def post_order_traversal(self, node, visit_func):
        """
        left right root
        """
        if node is not None:
            self.post_order_traversal(node.left, visit_func)
            self.post_order_traversal(node.right, visit_func)
            visit_func(node)


if __name__ == '__main__':
    pass
