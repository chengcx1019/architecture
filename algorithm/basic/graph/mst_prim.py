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
定义顶点集合V，边集合E
最小生成树算法
无向连通图中寻找一个边的子集ST，即寻找边的权值总和最小的连通子图
为每个节点选择权重最小的前继节点

算法概述：选定顶点集合S和边集T，初始随机选择s进入S，之后从所有边中选择权值最小的边(u,v)[满足u in S且 v in V-S] 放入 ST 中，
同时将v放入S中，直到取出所有顶点至S停止。
"""


class MSTPrim(object):
    
    def __init__(self, graph: Graph):
        self.graph = graph
        self.pred = {}
        self.keys = {}
        self.in_queue = {}  # tag for node set V, True for V-S, False for S
        self.priority_queue = PriorityQueue()
        self.result = []

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
            mini_node_key = self.priority_queue.extract_min().obj  # 选出边<u,v>，这一轮出现的是上一个进入S的节点权重最小的邻接节点，即v
            self.in_queue[mini_node_key] = False
            curren_node = self.graph.nodes[mini_node_key]
            # 清除u剩余的邻接节点权重
            self.clear_pre_node_weight(curren_node)

            for node in curren_node.adj_nodes.values():
                if self.in_queue[node.key]:
                    weight = curren_node.adj_weights[node.key]  # A->B的权重存储在A的邻接权重中 A.adj_weights: {B.key:weight}
                    if weight < self.keys[node.key]:
                        self.keys[node.key] = weight
                        self.pred[node.key] = mini_node_key
                        self.priority_queue.decrease_key(node.key, weight)
            self.result.append(curren_node.key)
        print(self.result)

    def clear_pre_node_weight(self, curren_node):
        pre_key = self.pred[curren_node.key]
        if pre_key > -1:
            pre_node = self.graph.nodes[pre_key]
            for node in pre_node.adj_nodes.values():
                key = node.key
                if self.in_queue[key]:
                    self.keys[key] = sys.maxsize
                    self.pred[key] = -1
                    self.priority_queue.decrease_key(key, self.keys[key])


if __name__ == '__main__':
    pass
