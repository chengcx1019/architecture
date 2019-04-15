#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_mst_prim.py
@time: 2018/5/14 16:38
"""
import unittest
from basic.graph.mst_prim import MSTPrim
from basic.graph.graph import Graph


class TestMSTPrim(unittest.TestCase):

    def tearDown(self):
        self.mst_prim = None
        self.graph = None

    def setUp(self):
        self.graph = Graph()

        self.option = 1
        if self.option == 1:
            edges = [(0, 1, 2), (0, 4, 4),
                     (1, 2, 3),
                     (2, 4, 1), (2, 3, 5),
                     (3, 0, 8),
                     (4, 3, 7)]
        elif self.option == 2:
            edges = []

        for edge in edges:
            self.graph.add_edge(edge[0], edge[1], weight=edge[2])

        self.mst_prim = MSTPrim(self.graph)

    def test_mst_prim(self):
        if self.option == 1:
            self.mst_prim.mst_prim(0)
            self.assertEqual(self.mst_prim.pred[0], -1)
            self.assertEqual(self.mst_prim.pred[1], 0)
            self.assertEqual(self.mst_prim.pred[2], 1)
            self.assertEqual(self.mst_prim.pred[3], 2)
            self.assertEqual(self.mst_prim.pred[4], 2)

        elif self.option == 2:
            pass
if __name__ == '__main__':
    pass