#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: PyCharm
@file: graph.py
@time: 2018/5/13 15:20
"""

from enum import Enum


class State(Enum):
    unvisited = 0  # white，顶点还未访问
    visiting = 1  # gtey，顶点已被访问，但还存在未访问的邻接顶点
    visited = 2  # black，顶点已被访问，且所有邻接顶点都被访问


class Node(object):

    def __init__(self, key):
        self.key = key
        self.visit_state = State.unvisited
        self.incoming_edges = 0
        self.adj_nodes = {}  # Key = key, val = Node
        self.adj_weights = {}  # Key = key, val = weight

    def add_neighbor(self, neighbor, weight=0):
        if neighbor is None or weight is None:
            raise TypeError('neighbor or weight cannot be None')
        self.incoming_edges += 1
        self.adj_weights[neighbor.key] = weight
        self.adj_nodes[neighbor.key] = neighbor

    def remove_neighbor(self, neighbor):
        if neighbor is None:
            raise TypeError('neighbor cannot be None')
        if neighbor.key not in self.adj_nodes:
            raise KeyError('neighbor not found')
        self.incoming_edges += 1
        del self.adj_nodes[neighbor.key]
        del self.adj_weights[neighbor.key]


class Graph(object):

    def __init__(self, ):
        self.nodes = {}

    def add_node(self, key):
        if key is None:
            raise TypeError('key cannot be None')
        if key not in self.nodes:
            self.nodes[key] = Node(key)
        return self.nodes[key]

    def add_edge(self, source_key, dest_key, weight=0):
        if source_key is None or dest_key is None:
            raise KeyError('Invalid key')
        if source_key not in self.nodes:
            self.add_node(source_key)
        if dest_key not in self.nodes:
            self.add_node(dest_key)
        self.nodes[source_key].add_neighbor(self.nodes[dest_key], weight)

    def add_undirected_edge(self, source_key, dest_key, weight=0):
        if source_key is None or dest_key is None:
            raise KeyError('Invalid key')
        self.add_edge(source_key, dest_key, weight)
        self.add_edge(dest_key, source_key, weight)


"""
图的其他表示方式，邻接表和邻接矩阵
邻接矩阵是对称的
以及判断节点连接方式和节点度的方式也会不一样
"""
class GraphRepresent(object):

    def __init__(self, ):
        pass

    def adjacency_list(self):
        # A Straightforward Adjacency List Representation
        a, b, c, d, e, f, g, h = range(8)
        N = [
            [b, c, d, e, f],  # a
            [c, e],  # b
            [d],  # c
            [e],  # d
            [f],  # e
            [c, g, h],  # f
            [f, h],  # g
            [f, g]  # h
        ]

        b in N[a]  # Neighborhood membership -> True
        len(N[f])  # Degree -> 3

        # A Straightforward Adjacency Set Representation
        a, b, c, d, e, f, g, h = range(8)
        N = [
            {b, c, d, e, f},  # a
            {c, e},  # b
            {d},  # c
            {e},  # d
            {f},  # e
            {c, g, h},  # f
            {f, h},  # g
            {f, g}  # h
        ]

        b in N[a]  # Neighborhood membership -> True
        len(N[f])  # Degree -> 3

        # A Straightforward Adjacency Dict Representation
        a, b, c, d, e, f, g, h = range(8)
        N = [
            {b: 2, c: 1, d: 3, e: 9, f: 4},  # a
            {c: 4, e: 3},  # b
            {d: 8},  # c
            {e: 7},  # d
            {f: 5},  # e
            {c: 2, g: 2, h: 2},  # f
            {f: 1, h: 6},  # g
            {f: 9, g: 8}  # h
        ]

        b in N[a]  # Neighborhood membership -> True
        len(N[f])  # Degree -> 3
        N[a][b]  # Edge weight for (a, b) -> 2

        N = {
            'a': set('bcdef'),
            'b': set('ce'),
            'c': set('d'),
            'd': set('e'),
            'e': set('f'),
            'f': set('cgh'),
            'g': set('fh'),
            'h': set('fg')
        }

    def adjacency__matrix(self):
        # An Adjacency Matrix, Implemented with Nested Lists
        a, b, c, d, e, f, g, h = range(8)
        N = [[0, 1, 1, 1, 1, 1, 0, 0],  # a
             [0, 0, 1, 0, 1, 0, 0, 0],  # b
             [0, 0, 0, 1, 0, 0, 0, 0],  # c
             [0, 0, 0, 0, 1, 0, 0, 0],  # d
             [0, 0, 0, 0, 0, 1, 0, 0],  # e
             [0, 0, 1, 0, 0, 0, 1, 1],  # f
             [0, 0, 0, 0, 0, 1, 0, 1],  # g
             [0, 0, 0, 0, 0, 1, 1, 0]]  # h

        N[a][b]  # Neighborhood membership -> 1
        sum(N[f])  # Degree -> 3

        # 带权值的连接矩阵表示
        a, b, c, d, e, f, g, h = range(8)
        _ = float('inf')

        W = [[0, 2, 1, 3, 9, 4, _, _],  # a
             [_, 0, 4, _, 3, _, _, _],  # b
             [_, _, 0, 8, _, _, _, _],  # c
             [_, _, _, 0, 7, _, _, _],  # d
             [_, _, _, _, 0, 5, _, _],  # e
             [_, _, 2, _, _, 0, 2, 2],  # f
             [_, _, _, _, _, 1, 0, 6],  # g
             [_, _, _, _, _, 9, 8, 0]]  # h

        W[a][b] < _  # Neighborhood membership
        sum(1 for w in W[a] if w < _) - 1  # Degree




if __name__ == '__main__':
    pass
