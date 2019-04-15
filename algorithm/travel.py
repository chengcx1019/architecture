#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@software: PyCharm
@file: travel.py
@time: 2018/5/11 19:46
"""
"""
编译器版本: Python 2.7.6
请使用标准输出(sys.stdout)；已禁用图形、文件、网络、系统相关的操作，如Process , httplib , os；缩进可以使用tab、4个空格或2个空格，但是只能任选其中一种，不能多种混用；如果使用sys.stdin.readline，因为默认会带换行符，所以要strip(' ')进行截取；建议使用raw_input()
时间限制: 3S (C/C++以外的语言为: 5 S)   内存限制: 128M (C/C++以外的语言为: 640 M)
输入:
输入描述
输入数据包含M+2行
第一行 整型 node的个数N，范围1-10000
第二行 描述边是M行2列矩阵大小，M  2
第三行-第M+2行表示edge的数据，其中每行代表一条有向边，实际上可以描述成一个N*2的二维数组，行描述边，列表示结点
输出:
输出描述
最大路径的数:一个整型数字
输入范例:
输入范例 例如下面表示总共4个结点和4条边：
4      (总共4个结点，编号0,1,2,3)
4 2
0 1 （从结点0到结点1的一条有向边）
1 2 （从结点1到结点2的一条有向边）
2 3 （从结点2到结点3的一条有向边）
0 2 （从结点0到结点2的一条有向边）
输出范例:
输出范例 例如：
100
"""
from enum import Enum

class Results(object):

    def __init__(self):
        self.results = []

    def add_result(self, result):
        self.results.append(int(str(result)))

    def clear_results(self):
        self.results = []

    def __str__(self):
        return str(self.results)

class State(Enum):

    unvisited = 0
    visiting = 1
    visited = 2

class Node:
    def __init__(self, key):
        self.key = key
        self.visit_state = State.unvisited
        self.incoming_edges = 0
        self.adj_nodes = {}  # Key = key, val = Node
        self.adj_weights = {}  # Key = key, val = weight

    def __repr__(self):
        return str(self.key)

    def __lt__(self, other):
        return self.key < other.key

    def add_neighbor(self, neighbor):
        if neighbor is None :
            raise TypeError('neighbor or weight cannot be None')
        neighbor.incoming_edges += 1
        self.adj_nodes[neighbor.key] = neighbor

    def remove_neighbor(self, neighbor):
        if neighbor is None:
            raise TypeError('neighbor cannot be None')
        if neighbor.key not in self.adj_nodes:
            raise KeyError('neighbor not found')
        neighbor.incoming_edges -= 1
        del self.adj_nodes[neighbor.key]


class Graph:

    def __init__(self):
        self.nodes = {}  # Key = key, val = Node

    def add_node(self, key):
        if key is None:
            raise TypeError('key cannot be None')
        if key not in self.nodes:
            self.nodes[key] = Node(key)
        return self.nodes[key]

    def add_edge(self, source_key, dest_key):
        if source_key is None or dest_key is None:
            raise KeyError('Invalid key')
        if source_key not in self.nodes:
            self.add_node(source_key)
        if dest_key not in self.nodes:
            self.add_node(dest_key)
        self.nodes[source_key].add_neighbor(self.nodes[dest_key])

    def dfs(self, root, visit_func):
        if root is None:
            return
        visit_func(root)
        root.visit_state = State.visited
        for node in root.adj_nodes.values():
            if node.visit_state == State.unvisited:
                self.dfs(node, visit_func)
