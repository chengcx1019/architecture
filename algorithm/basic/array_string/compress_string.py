#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: compress_string.py
@time: 2018/5/28 21:00
"""
from collections import OrderedDict


class CompressString(object):

    def __init__(self, ):
        pass

    def compress(self, string):
        if string is None or not string:
            return string
        pre = string[0]
        count = 0
        result = ''
        for char in string:
            if char == pre:
                count += 1
            else:
                # char != pre
                result += self.append_result(pre, count)
                pre = char
                count = 1  # 1 not 0
        result += self.append_result(pre, count)
        return result if len(result) < len(string) else string

    def append_result(self, pre_char, count):
        return pre_char + (str(count) if count > 1 else '')


class Anagram(object):

    def __init__(self, ):
        pass

    def group_anagram(self, items: list):
        if items is None:
            raise TypeError('items cannot be None')
        if not items:
            return items
        order_map = OrderedDict()
        for item in items:
            sorted_item = tuple(sorted(item))
            if sorted_item in order_map:
                order_map[sorted_item].append(item)
            else:
                order_map[sorted_item] = [item]
        result = []
        for item in order_map:
            result.extend(order_map[item])
        return result


if __name__ == '__main__':
    data = ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
    expected = ['ram', 'arm', 'act', 'cat', 'bat', 'tab']
    ana = Anagram()
    print(ana.group_anagram(data))
