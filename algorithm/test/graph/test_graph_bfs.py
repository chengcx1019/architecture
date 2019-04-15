#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: PyCharm
@file: test_graph_bfs.py
@time: 2018/5/13 21:16
"""
import unittest
from basic.graph.graph_bfs import GraphBfs

class TestGraphBfs(unittest.TestCase):

    def setUp(self):
        self.graph = GraphBfs()

    def tearDown(self):
        self.graph = None

    def test_graph_bfs(self):
        # 0 for s, 15 for t

        # for i in range(16):
        #     self.graph.nodes[i] = Node(i)

        edges = [(0, 1), (0, 6), (0, 8),
                 (1, 2), (1, 3),
                 (2, 10), (2, 11),
                 (3, 4), (3, 12),
                 (4, 5), (4, 13),
                 (5, 6), (5, 9),
                 (6, 7),
                 (7, 8), (7, 9),
                 (8, 14),
                 (9, 15)]
        for edge in edges:
            self.graph.add_undirected_edge(edge[0], edge[1])

        self.graph.bfs(0, self.graph.bfs_visit)

        for key in self.graph.pred:
            print(key, " ", self.graph.pred[key],  self.graph.dist[key])



if __name__ == '__main__':
    pass