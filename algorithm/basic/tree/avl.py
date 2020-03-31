#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: avl.py
@time: 2018/5/16 21:17
"""
"""
1. 本身首先是一棵二叉搜索树
2. 带有平衡条件：每个非叶子节点左右子树的高度之差的绝对值（平衡因子）最多为1.
"""

from collections import deque


class AVLNode(object):

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def compare_to(self, value):
        """
        Returns 0 if equal, negative if smaller and positive if greater.
        Suitable for overriding.
        """
        if self.data == value:
            return 0
        if self.data < value:
            return -1
        return +1

    def rotate_right(self):
        """LL, Perform right rotation around given node."""
        new_root = self.left
        grandson = new_root.right
        self.left = grandson
        new_root.right = self

        self.compute_height()
        return new_root

    def rotate_left(self):
        """Perform left rotation around given node."""
        new_root = self.right
        grandson = new_root.left
        self.right = grandson
        new_root.left = self

        self.compute_height()
        return new_root

    def rotate_left_right(self):
        """Perform left, then right rotation around given node."""
        child = self.left
        new_root = child.right
        grand_left = new_root.left
        grand_right = new_root.right
        # rotate left
        child.right = grand_left
        new_root.left = child
        # rotate right
        self.left = grand_right
        new_root.right = self

        child.compute_height()
        self.compute_height()
        return new_root

    def rotate_right_left(self):
        """Perform right, then left rotation around given node."""
        child = self.right
        new_root = child.left
        grand_left = new_root.left
        grand_right = new_root.right
        # rotate right
        child.left = grand_right
        new_root.right = child

        # rotate left
        self.right = grand_left
        new_root.left = self

        child.compute_height()
        self.compute_height()
        return new_root

    def add_to_subtree(self, parent, data):
        if parent is None:
            return self.new_node(data)
        parent = parent.insert(data)

        return parent

    def insert(self, data):
        if data is None:
            raise TypeError("data is None")

        new_root = self
        if self.compare_to(data) >= 0:
            self.left = self.add_to_subtree(self.left, data)
            if self.height_difference() == 2:
                if self.left.compare_to(data) >= 0:
                    new_root = self.rotate_right()  # LL
                else:
                    new_root = self.rotate_left_right()  # LR
        else:
            self.right = self.add_to_subtree(self.right, data)
            if self.height_difference() == -2:
                if self.right.compare_to(data) < 0:
                    new_root = self.rotate_left()  # RR
                else:
                    new_root = self.rotate_right_left()  # RL

        new_root.compute_height()
        return new_root

    def remove_from_parent(self, parent, data):
        if parent:
            return parent.remove(data)
        return None

    def remove(self, data):
        new_root = self
        rs = self.compare_to(data)
        if rs == 0:
            if self.left is None:  # 若目标节点有左子节点，则左子节点赋值目标节点
                return self.right

            child = self.left
            while child.right:
                child = child.right

            value = child.data
            self.left = self.remove_from_parent(self.left, value)
            self.data = value

            if self.height_difference() == -2:
                if self.right.height_difference() < 0:
                    new_root = self.rotate_left()
                else:
                    new_root = self.rotate_right_left()
        elif rs > 0:
            self.left = self.remove_from_parent(self.left, data)
            if self.height_difference() == -2:
                if self.right.height_difference() < 0:
                    new_root = self.rotate_left()
                else:
                    new_root = self.rotate_right_left()
        else:
            self.right = self.remove_from_parent(self.right, data)
            if self.height_difference() == 2:
                if self.left.height_difference >= 0:
                    new_root = self.rotate_right()
                else:
                    new_root = self.rotate_left_right()

        new_root.compute_height()
        return new_root

    def new_node(self, data):
        """Return new Binary Node, amenable to subclassing."""
        return AVLNode(data)

    def compute_height(self):
        height = -1
        if self.left:
            height = max(height, self.left.height)
        if self.right:
            height = max(height, self.right.height)

        self.height = height + 1

    def dynamic_height(self):
        height = -1
        if self.left:
            height = max(height, self.left.dynamic_height())
        if self.right:
            height = max(height, self.right.dynamic_height())

        return height + 1

    def height_difference(self):
        left_target = 0
        right_target = 0
        if self.left:
            left_target = 1 + self.left.height
        if self.right:
            right_target = 1 + self.right.height

        return left_target - right_target

    def dynamic_height_difference(self):
        left_height = 0
        right_height = 0
        if self.left:
            left_height = 1 + self.left.dynamic_height()
        if self.right:
            right_height = 1 + self.right.dynamic_height()

        return left_height - right_height

    def assert_avl_property(self):
        """Validate AVL property for BST node."""
        if abs(self.dynamic_height_difference()) > 1:
            return False
        if self.left:
            if not self.left.assert_avl_property():
                return False
        if self.right:
            if not self.right.assert_avl_property():
                return False

        return True

    def in_order(self):
        """In order traversal generator of tree rooted at given node."""
        if self.left:
            for n in self.left.in_order():
                yield n

        yield self.data

        if self.right:
            for n in self.right.in_order():
                yield n

    def pre_order(self):
        yield self.data

        if self.left:
            for n in self.left.pre_order():
                yield n

        if self.right:
            for n in self.right.pre_order():
                yield n

    def post_order(self):

        if self.left:
            for n in self.left.post_order():
                yield n

        if self.right:
            for n in self.right.post_order():
                yield n

        yield self.data

    def bfs(self):
        queue = deque()
        queue.append(self)

        while queue:
            node = queue.popleft()
            yield node.data
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def __repr__(self):
        """Useful debugging function to produce linear tree representation."""
        leftS = ''
        rightS = ''
        if self.left:
            leftS = str(self.left)
        if self.right:
            rightS = str(self.right)
        return "(L:" + leftS + " " + str(self.value) + " R:" + rightS + ")"


class AVLTree(object):

    def __init__(self):
        self.root = None

    def __repr__(self):
        if self.root is None:
            return "avl:()"
        return "avl:" + str(self.root)

    def insert(self, data):
        if data is None:
            raise TypeError(data is None)
        if self.root is None:
            self.root = AVLNode(data)
        else:
            self.root = self.root.insert(data)

    def remove(self, data):
        if self.root:
            self.root = self.root.remove(data)

    def assert_avl_property(self):
        if self.root:
            return self.root.assert_avl_property()
        else:
            return True

    def __contains__(self, target):
        if target is None:
            raise TypeError("target is None")
        node = self.root
        while node:
            rs = node.compare_to(target)
            if rs > 0:
                node = node.left
            elif rs < 0:
                node = node.right
            else:
                return True

        return False


if __name__ == '__main__':
    avl = AVLTree()
    node_datas = [5, 2, 8, 1, 3, 4]
    for node_data in node_datas:
        avl.insert(node_data)
    avl.remove(3)