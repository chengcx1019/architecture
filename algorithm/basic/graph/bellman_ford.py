#!/usr/bin/env python
# encoding: utf-8

# Time: O(V*E)
"""
@author: changxin
@mail: PyCharm
@file: bellman_ford.py
@time: 2018/5/14 08:17
"""
import sys

from basic.graph.graph import Graph
"""
singleSourceShortest
适用于包含负权重的图，但不能存在负环
抛出几个别人基于基准测试后的结论：
BellmanFord在稠密图上性能退化剧烈
使用优先队列的Dijkstra算法在稀疏图上具有优异表现
"""


class BellmanFord(object):
    
    def __init__(self, graph):
        self.graph = graph
        self.pred = {}
        self.dist = {}

        for node_key in graph.nodes:
            self.pred[node_key] = -1
            self.dist[node_key] = sys.maxsize

    def bellman_ford(self, start_node_key, end_node_key=None):
        self.dist[start_node_key] = 0
        n = len(self.graph.nodes)
        for i in range(n):
            fail_on_update = (i == n-1)
            leave_early = True
            # 对于每个顶点，检查能不能找到它到start_node的最短路径，即便是最坏的情况，在第n-1轮，包括start_node在内的n-1个顶点
            # 已经更新了距离
            for current_node in self.graph.nodes.values():
                for node in current_node.adj_nodes.values():
                    weight = current_node.adj_weights[node.key]
                    new_weight = weight + self.dist[current_node.key]
                    if new_weight < self.dist[node.key]:
                        if fail_on_update:
                            raise ValueError('Graph has negative cycle')
                        self.dist[node.key] = new_weight
                        self.pred[node.key] = current_node.key
                        leave_early = False
            # 如果某一次对所有边的遍历没有更新权重，则说明各距离已经达到最优，算法终止
            if leave_early:
                break

        if end_node_key:
            return self.full_path(end_node_key)

    def full_path(self, end_node_key):
        reslut = []
        current_node_key = end_node_key
        while current_node_key != -1:
            reslut.append(current_node_key)
            current_node_key = self.pred[current_node_key]
        return reslut[::-1]

    

if __name__ == '__main__':
    pass