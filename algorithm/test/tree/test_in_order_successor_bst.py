#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_in_order_successor_bst.py
@time: 2018/5/23 12:48
"""
import unittest

from basic.tree.in_order_successor_bst import InOrderSuccessorBst
from basic.tree.binary_search_tree import Traversal
from basic.utils.results import Results


class TestBinarySearchTreeBfs(unittest.TestCase):

    def tearDown(self):
        self.bst = None

    def setUp(self):
        self.bst = InOrderSuccessorBst()
        self.traversal = Traversal()
        self.results = Results()
        

    def test_bst(self):
        node_datas = [5, 2, 8, 1, 3, 9, 7, 6]
        for node_data in node_datas:
            self.bst.insert(node_data)
        self.traversal.in_order_traversal(self.bst.root, self.results.add_result)
        print(self.results.results)
        test_node = self.bst.root.left.right
        print(test_node.parent.parent)
        self.assertEqual(self.bst.in_order_successor(test_node), 5)
if __name__ == '__main__':
    pass