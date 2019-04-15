# encoding: utf-8

"""
@author: changxin
@mail: PyCharm
@file: test_graph.py
@time: 2018/5/13 16:30
"""
import unittest

from basic.graph.graph import Graph
class TestGraph(unittest.TestCase):

    def tearDown(self):
        self.graph = None

    def setUp(self):
        self.graph = Graph()


    def test_graph(self):
        graph = Graph()
        for key in range(0, 6):
            graph.add_node(key)
        graph.add_edge(0, 1, weight=5)
        graph.add_edge(0, 5, weight=2)
        graph.add_edge(1, 2, weight=3)
        graph.add_edge(2, 3, weight=4)
        graph.add_edge(3, 4, weight=5)
        graph.add_edge(3, 5, weight=6)
        graph.add_edge(4, 0, weight=7)
        graph.add_edge(5, 4, weight=8)
        graph.add_edge(5, 2, weight=9)

        self.assertEqual(graph.nodes[0].adj_weights[graph.nodes[1].key], 5)

if __name__ == '__main__':
    unittest.main()