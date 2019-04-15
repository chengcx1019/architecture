#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: mst_prim.py
@time: 2018/5/14 15:26
"""
import sys

from basic.graph.graph import Graph
from basic.array_string.priority_queue import PriorityQueue, PriorityQueueNode
"""
最小生成树算法
无向连通图中寻找一个边的子集ST，即寻找边的权值总和最小的连通子图
为每个节点选择权重最小的前继节点

算法概述：选定顶点集合S和边集T，初始随机旋转s进入S，之后从所有变种选择权值最小的边(u,v)[满足u in S且v in V-S]放入T中，
同时将v放入S中，直到取出所有顶点至S停止。
"""


class MSTPrim(object):
    
    def __init__(self, graph: Graph):
        self.graph = graph
        self.pred = {}
        self.keys = {}
        self.in_queue = {}  # tag for node set V, True for V-S, False for S
        self.priority_queue = PriorityQueue()

        for node in self.graph.nodes.values():
            self.pred[node.key] = -1
            self.keys[node.key] = sys.maxsize
            self.in_queue[node.key] = True
            self.priority_queue.insert(PriorityQueueNode(node.key, self.keys[node.key]))

    # 随机选择一个顶点开始
    def mst_prim(self, start_node_key):
        """
        :param start_node_key:random choose a node to start
        """
        if start_node_key is None:
            raise TypeError('Input node keys cannot be None')
        if start_node_key not in self.graph.nodes:
            raise ValueError('Invalid start or end node key')

        self.keys[start_node_key] = 0  # 优先级，按照目标，越小优先级越高
        self.priority_queue.decrease_key(start_node_key, self.keys[start_node_key])
        while self.priority_queue:
            mini_node_key = self.priority_queue.extract_min().obj
            self.in_queue[mini_node_key] = False
            curren_node = self.graph.nodes[mini_node_key]

            for node in curren_node.adj_nodes.values():
                if self.in_queue[node.key]:
                    weight = curren_node.adj_weights[node.key]
                    if weight < self.keys[node.key]:
                        self.keys[node.key] = weight
                        self.pred[node.key] = mini_node_key
                        self.priority_queue.decrease_key(node.key, weight)


if __name__ == '__main__':
    pass
