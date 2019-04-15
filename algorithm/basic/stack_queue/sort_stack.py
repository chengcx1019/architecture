#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: sort_stack.py
@time: 2018/5/29 11:33
"""
from basic.stack_queue.stack import Stack


class SortStack(Stack):
    
    def __init__(self, top=None):
        super(SortStack, self).__init__(top)

    def sort(self):
        buffer = Stack()
        while not self.is_empty():
            temp = self.pop()
            if buffer.is_empty() or temp >= buffer.peek():
                buffer.push(temp)
            else:
                while not buffer.is_empty() and temp <= buffer.peek():
                    self.push(buffer.pop())
                buffer.push(temp)
        return buffer

    def sort_simplify(self):
        buffer = Stack()
        while not self.is_empty():
            temp = self.pop()
            while not buffer.is_empty() and temp < buffer.peek():
                self.push(buffer.pop())
            buffer.push(temp)

        return buffer


if __name__ == '__main__':
    pass
