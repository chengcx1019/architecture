#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_invert_bst.py
@time: 2018/5/18 08:14
"""
import unittest

from basic.tree.invert_bst import InvertBst
from basic.utils.results import Results

class TestBinarySearchTreeBfs(unittest.TestCase):

    def tearDown(self):
        self.bst = None
        self.results = None


    def setUp(self):
        self.bst = InvertBst()
        self.results = Results()

    def test_bst(self):
        node_datas = [5, 2, 8, 1, 3, 9, 7, 6]
        for node_data in node_datas:
            self.bst.insert(node_data)
        self.assertEqual(self.bst.root.val, 5)
        self.bst.bfs(self.results.add_result)
        self.assertEqual(self.results.results, [5, 2, 8, 1, 3, 7, 9, 6])
        self.results.clean_results()
        # invert tree
        self.bst.invert_tree()
        self.bst.bfs(self.results.add_result)
        self.assertEqual(self.results.results, [5, 8, 2, 9, 7, 3, 1, 6])
        self.results.clean_results()

if __name__ == '__main__':
    pass