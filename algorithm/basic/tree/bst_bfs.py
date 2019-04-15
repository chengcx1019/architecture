#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: bst_bfs.py
@time: 2018/5/16 20:55
"""

from collections import deque

from basic.tree.binary_search_tree import BinarySearchTree


class BinarySearchTreeBfs(BinarySearchTree):
    
    def __init__(self):
        super(BinarySearchTreeBfs, self).__init__()
        
    def bfs(self, visit_func):
        if self.root is None:
            raise TypeError("root is None")
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            visit_func(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


if __name__ == '__main__':
    pass