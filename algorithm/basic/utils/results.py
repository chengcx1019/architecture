#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: results.py
@time: 2018/5/16 20:27
"""
class Results(object):

    def __init__(self):
        self.results = []

    def add_result(self, result):
        self.results.append(int(str(result)))

    def clean_results(self):
        self.results = []

    def __str__(self):
        return str(self.results)






if __name__ == '__main__':
    pass