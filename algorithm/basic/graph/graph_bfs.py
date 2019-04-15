#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: PyCharm
@file: graph_bfs.py
@time: 2018/5/13 20:18
"""
from collections import deque
import sys

from basic.graph.graph import Graph, Node, State


class GraphBfs(Graph):

    def __init__(self, ):
        super(GraphBfs, self).__init__()
        self.pred = {}  # 记录每个顶点的前驱顶点
        self.dist = {}  # 记录起始顶点到当前顶点的最短路径
        self.queue = deque()

    def bfs(self, root, visit_fun):
        for node in self.nodes.values():
            self.pred[node.key] = -1
            self.dist[node.key] = sys.maxsize
        self.nodes[root].visit_state = State.visiting
        self.dist[root] = 0
        self.queue.append(self.nodes[root])

        while self.queue:
            node = self.queue.popleft()
            visit_fun(node)

    def bfs_visit(self, current_node):

        for node in current_node.adj_nodes.values():
            if node.visit_state == State.unvisited:
                self.pred[node.key] = current_node.key
                node.visit_state = State.visiting  # 迭代的是字典的视图，修改会反映到字典实体上
                self.dist[node.key] = self.dist[current_node.key] + 1
                self.queue.append(node)
        current_node.visit_state = State.visited


if __name__ == '__main__':
    graph = GraphBfs()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.bfs(0, graph.bfs_visit)
    print(graph.pred)
    print(graph.dist)
