#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_binary_search_tree.py
@time: 2018/5/16 20:18
"""
import unittest

from basic.tree.binary_search_tree import BinarySearchTree, Traversal
from basic.utils.results import Results

class TestBinarySearchTree(unittest.TestCase):

    def tearDown(self):
        self.bst = None
        self.results = None


    def setUp(self):
        self.bst = BinarySearchTree()
        self.results = Results()
        self.traversal = Traversal()

    def test_bst(self):
        node_datas = [5, 2, 8, 1, 3]
        for node_data in node_datas:
            self.bst.insert(node_data)
        self.assertEqual(self.bst.root.val, 5)
        self.traversal.in_order_traversal(self.bst.root, self.results.add_result)
        self.assertEqual(self.results.results, [1, 2, 3, 5, 8])
        self.results.clean_results()
        self.traversal.pre_order_traversal(self.bst.root, self.results.add_result)
        self.assertEqual(self.results.results, [5, 2, 1, 3, 8])
        self.results.clean_results()
        self.traversal.post_order_traversal(self.bst.root, self.results.add_result)
        self.assertEqual(self.results.results, [1, 3, 2, 8, 5])
        self.results.clean_results()


    

if __name__ == '__main__':
    pass