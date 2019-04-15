#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: sort_analogy.py
@time: 2018/9/6 22:55
"""


class MergeTwoArrays(object):

    def __init__(self, ):
        pass

    def nerge_two_arrays(self, array_a: list, array_b: list, source_len, dest_len):
        if array_a is None and array_b is None:
            return
        if source_len < 0 or dest_len < 0:
            raise TypeError('index can\'t be None')
        if array_a is None:
            return array_b
        if array_b is None:
            return array_a
        source_curr = source_len - 1
        dest_curr = dest_len - 1
        insert_index = source_len + dest_len - 1
        while dest_curr >= 0:
            if array_a[source_curr] > array_b[dest_curr]:
                array_a[insert_index] = array_a[source_curr]
                source_curr = source_curr - 1
            else:
                array_a[insert_index] = array_b[dest_curr]
                dest_curr = dest_curr - 1
            insert_index -= 1
        return array_a


if __name__ == '__main__':
    a = [1, 4, 6, 8, 9, None, None, None]
    b = [3, 5, 7]
    mta = MergeTwoArrays()
    print(mta.nerge_two_arrays(a, b, 5, 3))