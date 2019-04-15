#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_min_bst.py
@time: 2018/5/23 14:15
"""
import unittest

from basic.tree.min_bst import MinBst
from basic.tree.binary_search_tree import BinaryTreeNode
from basic.tree.binary_search_tree import Traversal
from basic.utils.results import Results


class TestMinBst(unittest.TestCase):

    def tearDown(self):
        self.bst = None

    def setUp(self):
        self.bst = MinBst()
        self.traversal = Traversal()
        self.results = Results()

    def test_bst(self):
        node_datas = [1, 2, 3, 5, 6, 7, 8, 9]
        self.assertEqual(self.bst.min_bst(node_datas), 5)


if __name__ == '__main__':
    pass
