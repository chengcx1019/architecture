#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: duplicate_linked_list.py
@time: 2018/5/28 16:09
"""
from basic.linked_list.linked_list import LinkedList, LinkedListNode


class DuplicateLinkedList(LinkedList):

    def __init__(self, head=None):  # todo test init
        super(DuplicateLinkedList, self).__init__(head)

    def remove_dupes(self):
        if self.head is None:
            return
        cache = set()
        node = self.head
        while node is not None:
            if node.data not in cache:
                cache.add(node.data)
                pre = node
                node = node.next
            else:
                pre.next = node.next
                node = node.next

    def remove_dupes_single_pointer(self):
        if self.head is None:
            return
        node = self.head
        cache = set({node.data})
        while node.next is not None:
            if node.next.data not in cache:
                cache.add(node.next.data)
                node = node.next
            else:
                node.next = node.next.next

    def remove_dupes_in_place(self):
        if self.head is None:
            return
        node = self.head
        while node is not None:
            runner = node
            while runner.next is not None:
                if runner.next.data == node.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            node = node.next


if __name__ == '__main__':
    pass
