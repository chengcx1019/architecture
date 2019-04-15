#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: traversal_tree_bottom_up.py
@time: 2018/6/5 11:02
"""
"""
从底层到顶层，反向逐层输出树
"""


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bottom_up_traversal(root):
    if root is None:
        raise TypeError("root can't be None")
    from collections import deque
    queue = deque()
    queue.append(root)
    result = []
    while queue:
        queue_size = queue.__len__()
        current_level = []
        for i in range(queue_size):
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            current_level.append(node.val)
        result.append(current_level)
    for i in range(len(result)-1, -1, -1):
        print(result[i])


if __name__ == '__main__':
    node3 = TreeNode(3)
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node3.left = node9
    node3.right = node20
    node20.left = node15
    node20.right = node7
    bottom_up_traversal(node3)
