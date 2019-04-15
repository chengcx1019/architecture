#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: lca_tree.py
@time: 2018/5/20 00:17
"""

"""Find the lowest common ancestor of two nodes in a binary tree"""


class Node(object):
    
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.key)


class BinaryTree(object):
    
    def lca(self, root, node1, node2):
        if None in (root, node1, node2):
            return None
        if (not self._node_in_tree(root, node1) or not self._node_in_tree(root, node2)):
            return None
        return self._lca(root, node1, node2)

    def _node_in_tree(self, root, node):
        if root is None:
            return None
        if root is node:
            return True
        left = self._node_in_tree(root.left, node)
        right = self._node_in_tree(root.right, node)
        return left or right

    def _lca(self, root, node1, node2):
        if root is None:
            return None
        if root is node1 or root is node2:
            return root
        left_node = self._lca(root.left, node1, node2)
        right_node = self._lca(root.right, node1, node2)
        if left_node is not None and right_node is not None:
            return root
        return left_node if left_node is not None else right_node
        

if __name__ == '__main__':
    node10 = Node(10)
    node5 = Node(5)
    node12 = Node(12)
    node3 = Node(3)
    node1 = Node(1)
    node8 = Node(8)
    node9 = Node(9)
    node18 = Node(18)
    node20 = Node(20)
    node40 = Node(40)
    node3.left = node1
    node3.right = node8
    node5.left = node12
    node5.right = node3
    node20.left = node40
    node9.left = node18
    node9.right = node20
    node10.left = node5
    node10.right = node9
    root = node10
    node0 = Node(0)
    binary_tree = BinaryTree()
    binary_tree.lca(root, node1, node8)
