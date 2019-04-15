#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: floyd_warshall.py
@time: 2018/5/14 11:25
"""
import sys

from basic.graph.graph import Graph
"""
allPairsShortest
Time: O(V^3)
构建路径的时间为O(E)，而主要的时间消耗在最小化路径上，即优化距离矩阵上
边的权值必须为正值
"""


class FloydWarshall(object):
    
    def __init__(self, graph: Graph):
        self.graph = graph
        self.node_num = len(self.graph.nodes)
        self.pred = []
        self.dist = []
        for i in range(self.node_num):
            self.pred.append([-1] * self.node_num)
            self.dist.append([sys.maxsize] * self.node_num)
        # TODO 节点key值被限制为数组索引，必须存在对应关系
        for current_node in self.graph.nodes.values():
            self.dist[current_node.key][current_node.key] = 0
            for node in current_node.adj_nodes.values():
                self.dist[current_node.key][node.key] = current_node.adj_weights[node.key]
                self.pred[current_node.key][node.key] = current_node.key

    def floyd_warshall(self):
        option = 2
        if option == 1:
            """本想做无效节点的判断，结果出错了，因为在更新过程中，u-t及t-v还存在跨节点的可达关系
                像下面的判断就忽略了这部分的可达关系，因而部分节点没有被更新
            """
            for transfer_node in self.graph.nodes.values():
                for current_node in self.graph.nodes.values():
                    if current_node.key == transfer_node.key:
                        continue
                    if transfer_node.key not in current_node.adj_nodes: # u对t可达
                        continue
                    for node in self.graph.nodes.values():
                        if node.key in transfer_node.adj_nodes: # t对v可达
                            new_weight = self.dist[current_node.key][transfer_node.key] + \
                                         self.dist[transfer_node.key][node.key]
                            if new_weight < self.dist[current_node.key][node.key]:
                                self.dist[current_node.key][node.key] = new_weight
                                self.pred[current_node.key][node.key] = self.pred[transfer_node.key][node.key]
        elif option == 2:
            for transfer_node in self.graph.nodes.values():
                for current_node in self.graph.nodes.values():
                    for node in self.graph.nodes.values():
                        new_weight = self.dist[current_node.key][transfer_node.key] +\
                                     self.dist[transfer_node.key][node.key]
                        if new_weight < self.dist[current_node.key][node.key]:
                            self.dist[current_node.key][node.key] = new_weight
                            self.pred[current_node.key][node.key] = self.pred[transfer_node.key][node.key]

    def construct_shortest_path(self, start_node_key, end_node_key):
        # 以初始节点开始，从终点节点倒推1
        path = [end_node_key]
        current_pred = self.pred[start_node_key][end_node_key]
        while current_pred != -1:
            path.append(current_pred)
            if current_pred == start_node_key:
                break
            current_pred = self.pred[start_node_key][current_pred]  # pred存储两顶点最优路径的倒数第二个顶点

        return path[::-1]


if __name__ == '__main__':
    # pass
    graph = Graph()

    floyd_warshall = FloydWarshall(graph)
    floyd_warshall.pred = [[-1, 0, 1, 2, 0],
                           [3, -1, 1, 2, 2],
                           [3, 0, -1, 2, 2],
                           [3, 0, 1, -1, 0],
                           [3, 0, 1, 4, -1]]
    path = floyd_warshall.construct_shortest_path(1, 4)
    # 10，210， 3210，40
    # 0321，21，321，421
    # 032，1032，32，42
    # 03，103，2103，403
    # 034，1034，21034,34
    for i in range(5):
        for j in range(5):
            if i != j:
                print(floyd_warshall.construct_shortest_path(i, j))
    print(path)
    # print(floyd_warshall.pred)
    # print(floyd_warshall.dist)

