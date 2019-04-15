#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_floyd_warshall.py
@time: 2018/5/14 13:38
"""

import unittest
from basic.graph.floyd_warshall import FloydWarshall
from basic.graph.graph import Graph


class TestFloydWarshall(unittest.TestCase):

    def tearDown(self):
        self.floyd_warshall = None
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

        self.floyd_warshall = FloydWarshall(self.graph)

    def test_dijkstra_dense(self):
        if self.option == 1:
            self.floyd_warshall.floyd_warshall()
            print(self.floyd_warshall.dist)
            print(self.floyd_warshall.pred)
            self.assertEqual(self.floyd_warshall.dist[0][1], 2)
            self.assertEqual(self.floyd_warshall.dist[0][2], 5)
            self.assertEqual(self.floyd_warshall.dist[0][3], 10)
            self.assertEqual(self.floyd_warshall.dist[0][4], 4)
            self.assertEqual(self.floyd_warshall.dist[4][1], 17)
            self.assertEqual(self.floyd_warshall.construct_shortest_path(0, 1), [0, 1])
            self.assertEqual(self.floyd_warshall.construct_shortest_path(0, 2), [0, 1, 2])
            self.assertEqual(self.floyd_warshall.construct_shortest_path(0, 3), [0, 1, 2, 3])
            self.assertEqual(self.floyd_warshall.construct_shortest_path(0, 4), [0, 4])
            self.assertEqual(self.floyd_warshall.construct_shortest_path(1, 2), [1, 2])
            self.assertEqual(self.floyd_warshall.construct_shortest_path(1, 3), [1, 2, 3])
            self.assertEqual(self.floyd_warshall.construct_shortest_path(4, 1), [4, 3, 0, 1])

        elif self.option == 2:
            pass


if __name__ == '__main__':
    pass