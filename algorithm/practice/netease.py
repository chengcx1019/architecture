#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: netease.py
@time: 2018/9/9 18:11
"""

"""
最大不重复子串：用hash map维护一个滑动窗口
"""


def max_substring(s):
    table = dict()
    max_len = -1
    cur_left = 0

    for i, char in enumerate(s):
        if char in table and table[char] >= cur_left:  # 有的字符因为其他字符的影响已不在最大连续不重复子串中
            cur_left = table[char] + 1
        else:
            max_len = max(max_len, i - cur_left + 1)
        table[char] = i

    return max_len


if __name__ == '__main__':
    pass
