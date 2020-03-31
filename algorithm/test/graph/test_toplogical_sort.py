#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin.cheng
@mail: chengcx1019@gmail.com
@time: 2020-03-31 09:31
"""
from unittest import TestCase

from basic.graph.topplogical_sort import DAGTopSort

if __name__ == '__main__':
    pass


class TestDAGTopSort(TestCase):

    def setUp(self):
        self.graph = DAGTopSort()

    def tearDown(self):
        self.graph = None

    def test_make_top_sort(self):
        edges = [(0, 1), (0, 2),
                 (1, 3),
                 (2, 3), (2, 4),
                 (3, 4)]
        for edge in edges:
            self.graph.add_edge(edge[0], edge[1])

        self.graph.dfs(0, self.graph.make_top_sort)
        self.assertEqual(self.graph.top_sort,[4, 3, 1, 2, 0])
