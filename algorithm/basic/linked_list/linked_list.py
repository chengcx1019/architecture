#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: linked_list.py
@time: 2018/5/26 20:02
"""
"""
Implement a linked list with insert, append, find, delete, length, and print methods

"""


class LinkedListNode(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return self.data


class ComplexLinkedListNode(object):
    
    def __init__(self, data, next=None, sibling=None):
        self.data = data
        self.next = next
        self.sibling = sibling


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        counter = 0
        curr = self.head
        while curr:
            counter += 1
            curr = curr.next

        return counter

    def insert(self, data):
        if data is None:
            return
        node = LinkedListNode(data, self.head)
        self.head = node
        return node

    def append(self, data):
        if data is None:
            return
        node = LinkedListNode(data)
        if self.head is None:
            self.head = node
            return node
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node
        return node

    def find(self, data):
        if data is None:
            return
        curr = self.head
        while curr:
            if curr.data == data:
                return curr
            curr = curr.next
        return None

    def delete(self, data):
        if data is None:
            return
        if self.head is None:
            return
        curr = self.head
        if self.head.data == data:
            self.head = self.head.next
        while curr.next:
            if curr.next.data == data:
                curr.next = curr.next.next
                return
            curr = curr.next

    def get_all(self):
        if self.head is None:
            return
        curr = self.head
        datas = []
        while curr is not None:
            datas.append(curr.data)
            curr = curr.next
        return datas


if __name__ == '__main__':
    pass
