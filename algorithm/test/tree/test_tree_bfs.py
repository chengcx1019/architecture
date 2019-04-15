#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_tree_bfs.py
@time: 2018/5/16 21:02
"""
import unittest

from basic.tree.bst_bfs import BinarySearchTreeBfs
from basic.utils.results import Results

class TestBinarySearchTreeBfs(unittest.TestCase):

    def tearDown(self):
        self.bst = None
        self.results = None


    def setUp(self):
        self.bst = BinarySearchTreeBfs()
        self.results = Results()

    def test_bst(self):
        node_datas = [5, 2, 8, 1, 3, 9, 7, 6]
        for node_data in node_datas:
            self.bst.insert(node_data)
        self.assertEqual(self.bst.root.val, 5)
        self.bst.bfs(self.results.add_result)
        self.assertEqual(self.results.results, [5, 2, 8, 1, 3, 7, 9, 6])
        self.results.clean_results()



if __name__ == '__main__':
    pass