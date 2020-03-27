#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: PyCharm
@file: priority_queue.py
@time: 2018/5/13 23:55
"""
import sys

"""
a priority queue backed by an array_string.
二叉堆
"""


class PriorityQueueNode(object):

    def __init__(self, obj, key):
        self.obj = obj  # node.key
        self.key = key  # dest[node.key]

    def __repr__(self):
        return str(self.obj) + ': ' + str(self.key)


class PriorityQueue(object):

    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def insert(self, node):
        self.array.append(node)
        return self.array[-1]

    def extract_min(self):
        """
        选择最小元素并出队
        """
        if not self.array:
            return None
        minimum = sys.maxsize
        for index, node in enumerate(self.array):
            if node.key < minimum:
                minimum = node.key
                mini_index = index
        return self.array.pop(mini_index)

    def decrease_key(self, obj, new_key):
        """
        更新节点的权重
        """
        for node in self.array:
            if node.obj is obj:
                node.key = new_key
                return node
        return None
    

if __name__ == '__main__':
    pass
