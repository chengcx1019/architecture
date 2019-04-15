#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: PyCharm
@file: test_graph_dfs.py
@time: 2018/5/13 17:34
"""
import unittest
from basic.graph.graph_dfs import GraphDfs


class TestGraphDfs(unittest.TestCase):

    def setUp(self):
        self.graph = GraphDfs()

    def tearDown(self):
        self.graph = None

    def test_graph_dfs(self):
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

        self.assertEqual(len(self.graph.nodes), 16)
        self.assertEqual(len(self.graph.nodes[0].adj_nodes), 3)
        self.graph.dfs(0, self.graph.dfs_visit)
        self.assertEqual(self.graph.pred[2], 1)
        # self.assertEqual(self.graph.finished[2], 8)
        keys = self.graph.discovered.values()

        all_keys = list(keys)

        index = []
        for j in range(len(all_keys)):
            min = all_keys[j]
            min_index = j
            for i in range(j+1, len(all_keys)):
                if all_keys[i] < min:
                    min = all_keys[i]
                    min_index = i
            all_keys[j], all_keys[min_index] = all_keys[min_index], all_keys[j]
            index.append(min_index)

        sorted_index = []
        for sorted_value in all_keys:
            for key in self.graph.discovered:
                if self.graph.discovered[key] == sorted_value:
                    sorted_index.append(key)

        for key in sorted_index:
            print(key, " ", self.graph.pred[key], self.graph.discovered[key], self.graph.finished[key])


if __name__ == '__main__':
    pass
