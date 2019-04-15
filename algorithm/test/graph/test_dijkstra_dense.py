#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_dijkstra_dense.py
@time: 2018/5/14 10:56
"""
import unittest
from basic.graph.dijkstra_dense import DijkstraDense
from basic.graph.graph import Graph


class TestDijkstraDense(unittest.TestCase):

    def tearDown(self):
        self.dijkstra = None
        self.graph = None

    def setUp(self):
        self.graph = Graph()

        self.option = 2
        if self.option == 1:
            edges = [(0, 4, 4), (0, 1, 2),
                     (4, 3, 7),
                     (1, 2, 3),
                     (2, 4, 1), (2, 3, 5),
                     (3, 0, 8)]
        elif self.option == 2:
            edges = [(1, 2, 7), (1, 3, 9), (1, 6, 14),
                     (2, 3, 10), (2, 4, 15),
                     (3, 6, 2), (3, 4, 11),
                     (4, 5, 6),
                     (6, 5, 9)]

        for edge in edges:
            self.graph.add_edge(edge[0], edge[1], weight=edge[2])

        self.dijkstra = DijkstraDense(self.graph)

    def test_dijkstra_dense(self):
        if self.option == 1:
            self.dijkstra.dijkstra(0)
            self.assertEqual(self.dijkstra.dist[3], 10)
            self.assertEqual(self.dijkstra.dist[4], 4)
            self.assertEqual(self.dijkstra.dist[0], 0)
            self.assertEqual(self.dijkstra.dist[1], 2)
            self.assertEqual(self.dijkstra.dist[2], 5)
            self.assertEqual(self.dijkstra.full_path(2), [0, 1, 2])
        elif self.option == 2:
            self.dijkstra.dijkstra_dense(1)
            self.assertEqual(self.dijkstra.dist[1], 0)
            self.assertEqual(self.dijkstra.dist[2], 7)
            self.assertEqual(self.dijkstra.dist[3], 9)
            self.assertEqual(self.dijkstra.dist[4], 20)
            self.assertEqual(self.dijkstra.dist[5], 20)
            self.assertEqual(self.dijkstra.dist[6], 11)
            self.assertEqual(self.dijkstra.full_path(1), [1])
            self.assertEqual(self.dijkstra.full_path(2), [1, 2])
            self.assertEqual(self.dijkstra.full_path(3), [1, 3])
            self.assertEqual(self.dijkstra.full_path(4), [1, 3, 4])
            self.assertEqual(self.dijkstra.full_path(5), [1, 3, 6, 5])
            self.assertEqual(self.dijkstra.full_path(6), [1, 3, 6])

if __name__ == '__main__':
    pass