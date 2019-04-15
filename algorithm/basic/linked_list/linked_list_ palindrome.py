#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: linked_list_ palindrome.py
@time: 2018/5/26 19:43
"""
from basic.linked_list.linked_list import LinkedList


class LnkedListPalindrome(LinkedList):
    """Determine if a linked list is a palindrome"""
    def __init__(self):
        super(LnkedListPalindrome, self).__init__()

    def is_palindrome(self):
        if self.head is None:
            return False
        reversed_list = LinkedList()
        length = 0
        curr = self.head
        while curr:
            reversed_list.insert(curr)
            length += 1
            curr = curr.next

        iteration_length = length // 2
        curr = self.head
        curr_re = reversed_list.head
        for _ in range(iteration_length):
            if curr.data != curr_re.data:
                return False
            curr = curr.next
            curr_re = curr_re.next
        return True


if __name__ == '__main__':
    pass
