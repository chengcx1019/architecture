#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_avl.py
@time: 2018/5/17 11:13
"""
import unittest

from basic.tree.avl import AVLTree
from basic.tree.avl import AVLTree
from basic.utils.results import Results

class TestBinarySearchTree(unittest.TestCase):

    def tearDown(self):
        self.avl = None
        self.results = None


    def setUp(self):
        self.option = 1
        if self.option == 1:
            self.avl = AVLTree()
        elif self.option ==2:
            self.avl = AVLTree()
        self.results = Results()

    def test_avl(self):

        if self.option ==1:
            node_datas = [5, 2, 8, 1, 3, 4]
            for node_data in node_datas:
                self.avl.insert(node_data)
                self.assertEqual(self.avl.assert_avl_property(), True)
            self.assertEqual(self.avl.root.data, 3)
            self.assertEqual(list(self.avl.root.in_order()),[1, 2, 3, 4, 5, 8])
            self.assertEqual(list(self.avl.root.pre_order()), [3, 2, 1, 5, 4, 8])
            self.assertEqual(list(self.avl.root.post_order()), [1, 2, 4, 8, 5, 3])
            self.assertEqual(list(self.avl.root.bfs()), [3, 2, 5, 1, 4, 8])
            self.assertEqual(self.avl.root.right.left.data, 4)
            self.avl.remove(3)
            self.assertEqual(self.avl.root.data, 2)
            self.assertEqual(list(self.avl.root.in_order()), [1, 2, 4, 5, 8])
            self.assertEqual(list(self.avl.root.pre_order()), [2, 1, 5, 4, 8])
            self.assertEqual(list(self.avl.root.post_order()), [1, 4, 8, 5, 2])
            self.assertEqual(list(self.avl.root.bfs()), [2, 1, 5, 4, 8])
            self.avl.insert(9)
            self.assertEqual(self.avl.root.data, 5)
            self.assertEqual(self.avl.root.left.right.data, 4)
            self.assertEqual(list(self.avl.root.in_order()), [1, 2, 4, 5, 8, 9])
            self.avl.remove(1)
            self.avl.remove(4)
            self.avl.insert(6)
            self.avl.insert(7)
            self.assertEqual(self.avl.root.data, 6)
            self.assertEqual(list(self.avl.root.in_order()), [2, 5, 6, 7, 8, 9])
            self.assertEqual(list(self.avl.root.pre_order()), [6, 5, 2, 8, 7, 9])
            self.assertEqual(list(self.avl.root.post_order()), [2, 5, 7, 9, 8, 6])
            self.assertEqual(list(self.avl.root.bfs()), [6, 5, 8, 2, 7, 9])
            self.assertEqual(self.avl.root.height_difference(), 0)
        elif self.option == 2:
            node_datas = [5, 2, 8, 1, 3, 4]
            for node_data in node_datas:
                self.avl.add(node_data)
            print(self.avl.assert_avl_property())
            print(list(self.avl.root.inorder()))
            self.assertEqual(self.avl.root.value, 3)
            self.avl.remove(3)
            print(list(self.avl.root.inorder()))
            self.assertEqual(self.avl.root.value, 2)
            self.avl.add(9)
            print(list(self.avl.root.inorder()))
            self.assertEqual(self.avl.root.value, 5)


if __name__ == '__main__':
    pass
