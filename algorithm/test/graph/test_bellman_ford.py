#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_bellman_ford.py
@time: 2018/5/14 09:10
"""
import unittest
from basic.graph.bellman_ford import BellmanFord
from basic.graph.graph import Graph

class TestBellmanFord(unittest.TestCase):
    
    def tearDown(self):
        self.graph = None

        self.bellman_ford = None

    def setUp(self):
        self.graph = Graph()
        self.option = 2

        if self.option == 1:
            edges = [(0, 4, 2),
                     (1, 3, -2),
                     (2, 1, -3),
                     (3, 2, 6),
                     (4, 3, 4), (4, 1, 5)]
        elif self.option == 2:
            edges = [(0, 1, 2),
                     (1, 3, 4), (1, 4, 5),
                     (2, 4, -3),
                     (3, 2, 6), # test negative cycle (3, 2, 4)
                     (4, 3, -2), ]

        for edge in edges:
            self.graph.add_edge(edge[0], edge[1], weight=edge[2])

        self.bellman_ford = BellmanFord(self.graph)

    def test_bellman_ford(self):
        self.bellman_ford.bellman_ford(0)
        if self.option == 1:
            self.assertEqual(self.bellman_ford.dist[0], 0)
            self.assertEqual(self.bellman_ford.dist[1], 7)
            self.assertEqual(self.bellman_ford.dist[2], 11)
            self.assertEqual(self.bellman_ford.dist[3], 5)
            self.assertEqual(self.bellman_ford.dist[4], 2)
            self.assertEqual(self.bellman_ford.full_path(0), [0])
            self.assertEqual(self.bellman_ford.full_path(1), [0, 4 ,1])
            self.assertEqual(self.bellman_ford.full_path(2), [0, 4, 1, 3, 2])
            self.assertEqual(self.bellman_ford.full_path(3), [0, 4, 1, 3])
            self.assertEqual(self.bellman_ford.full_path(4), [0, 4])
        if self.option == 2:
            self.assertEqual(self.bellman_ford.dist[0], 0)
            self.assertEqual(self.bellman_ford.dist[1], 2)
            self.assertEqual(self.bellman_ford.dist[2], 11)
            self.assertEqual(self.bellman_ford.dist[3], 5)
            self.assertEqual(self.bellman_ford.dist[4], 7)
            self.assertEqual(self.bellman_ford.full_path(0), [0])
            self.assertEqual(self.bellman_ford.full_path(1), [0, 1])
            self.assertEqual(self.bellman_ford.full_path(2), [0, 1, 4, 3, 2])
            self.assertEqual(self.bellman_ford.full_path(3), [0, 1, 4, 3])
            self.assertEqual(self.bellman_ford.full_path(4), [0, 1, 4])
        
    

if __name__ == '__main__':
    pass