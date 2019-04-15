#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: set_of_stack.py
@time: 2018/5/26 21:17
"""
from basic.stack_queue.stack import Stack

"""
Implement SetOfStacks that wraps a list of stacks, where each stack is bound by a capacity
"""


class StackWithCapacity(Stack):
    
    def __init__(self, top=None, capacity=10):
        super(StackWithCapacity, self).__init__(top)
        self.capacity = capacity
        self.num_items = 0

    def is_empty(self):
        return self.num_items == 0

    def is_full(self):
        return self.num_items == self.capacity

    def pop(self):
        self.num_items -= 1
        return super(StackWithCapacity, self).pop()

    def push(self, data):
        if self.is_full():
            raise Exception("Stack is full")
        super(StackWithCapacity, self).push(data)
        self.num_items += 1


class SetOfStack(object):
    
    def __init__(self, stack_capacity):
        self.stack_capacity = stack_capacity
        self.stacks = []
        self.last_stack = None

    def push(self, data):
        if self.last_stack is None or self.last_stack.is_full():
            self.last_stack = StackWithCapacity(None, self.stack_capacity)
            self.stacks.append(self.last_stack)

        self.last_stack.push(data)

    def pop(self):
        if self.last_stack is None:
            return None
        data = self.last_stack.pop()
        if self.last_stack.is_empty():
            self.stacks.pop()
            self.last_stack = self.stacks[-1] if self.stacks else None
        return data
    

if __name__ == '__main__':
    stack = SetOfStack(stack_capacity=2)
    stack.push(5)
    stack.push(3)
    stack.push('a')
    stack.push('b')
    a = stack.pop()
    b = stack.pop()
    c = stack.pop()
    d = stack.pop()
    print(a, b, c, d)
