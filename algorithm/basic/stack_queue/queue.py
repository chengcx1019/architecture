#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: queue.py
@time: 2018/5/28 23:09
"""
from basic.linked_list.linked_list import LinkedListNode
"""queue implement using a linked list"""


class Queue(object):

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        if data is None:
            raise TypeError('data can\'t be None')
        node = LinkedListNode(data)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.head is None and self.tail is None:
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return data
# TODO: 优先队列的各种实现方式 （数组，堆（斐波那契堆） changxin.cheng@nio.com

if __name__ == '__main__':
    pass
