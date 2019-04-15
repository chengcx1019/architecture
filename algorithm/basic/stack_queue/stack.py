#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: stack.py
@time: 2018/5/26 20:53
"""
from basic.linked_list.linked_list import LinkedList, LinkedListNode


class Stack(LinkedList):
    """
    Implement a stack with push, pop, peek, and is_empty methods using a linked list.
    """
    def __init__(self, top=None):
        super(Stack, self).__init__(top)

    def push(self, data):
        super(Stack, self).insert(data)
        return self.head

    def pop(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def peek(self):
        return self.head.data if self.head is not None else None

    def is_empty(self):
        return self.peek() is None

        
if __name__ == '__main__':
    pass
