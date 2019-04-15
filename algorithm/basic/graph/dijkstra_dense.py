#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: dijkstra_dense.py
@time: 2018/5/14 10:10
"""
import sys

from basic.graph.graph import Graph, State

"""
singleSourceShortest
针对稠密图的算法效率更高
Time: O(V^2+E)
while循环进行n（n为顶点数）轮，n的值是多少，最终的结果是每条边都会得到遍历（起始点可达的前提下），因而时间复杂度为E
同时呢对于顶点，需要n轮while循环，同时每层循环内都需要遍历顶点找到当前距离的最小值，时间复杂度是V^2,
综上，得到总体的时间复杂度O(V^2+E)。
"""


class DijkstraDense(object):

    def __init__(self, graph):
        self.graph = graph
        self.pred = {}
        self.dist = {}

        for node in self.graph.nodes.values():
            self.pred[node.key] = -1
            self.dist[node.key] = sys.maxsize

    def dijkstra_dense(self, start_node_key, end_node_key=None):
        if start_node_key is None:
            raise TypeError('Input node keys cannot be None')
        if start_node_key not in self.graph.nodes:
            raise ValueError('Invalid start or end node key')

        self.dist[start_node_key] = 0

        while True:
            #
            u = -1
            sd = sys.maxsize
            # 从未访问顶点找寻找距离小值
            for node in self.graph.nodes.values():
                if node.visit_state == State.unvisited and self.dist[node.key] < sd:
                    sd = self.dist[node.key]
                    u = node.key
            if u == -1:
                break  # start_node是自身是分离的，对其他节点均不可达,算法仅进行一轮，在第2轮即终止
            current_node = self.graph.nodes[u]
            for node in current_node.adj_nodes.values():
                weight = current_node.adj_weights[node.key]
                new_weight = self.dist[current_node.key] + weight
                if new_weight < self.dist[node.key]:
                    self.dist[node.key] = new_weight
                    self.pred[node.key] = u
            self.graph.nodes[u].visit_state = State.visited

        # Walk backwards to determine the shortest path:
        # Start at the end node, walk the previous dict to get to the start node
        if end_node_key:
            return self.full_path(end_node_key)

    def dijkstra_dense_optimization(self, start_node_key, end_node_key=None):
        # in the implementation of c++, leave all data structure of c++ STL(Standard Template Library)
        # to get optimize performance, no optimization in algorithm.
        pass

    def full_path(self, end_node_key):
        reslut = []
        current_node_key = end_node_key
        while current_node_key != -1:
            reslut.append(current_node_key)
            current_node_key = self.pred[current_node_key]
        return reslut[::-1]


if __name__ == '__main__':
    pass