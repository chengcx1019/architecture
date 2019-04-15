#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: matrix_multiplication.py
@time: 2018/5/21 23:28
"""
import sys
"""
Given a list of 2x2 matrices, minimize the cost of matrix multiplication.
"""


class Metrix(object):

    def __init__(self, first, second):
        self.first = first
        self.second = second


class MatrixMultiplication(object):
    
    def __init__(self, ):
        pass

    def find_min_cost(self, metrices):
        if metrices is None:
            raise TypeError('metrices can\'t be None')
        if not metrices:
            return 0
        size = len(metrices)
        T = [[0]*size for _ in range(size)]
        for offset in range(1, size):
            for i in range(size - offset):
                j = i + offset
                min_cost = sys.maxsize
                for k in range(i, j):
                    # metrixs[k].second is same as metrixs[k+1].first
                    cost = T[i][k] + T[k+1][j] + metrices[i].first * metrices[k].second * metrices[j].second
                    if cost < min_cost:
                        min_cost = cost
                T[i][j] = min_cost
        return T[0][size-1]


if __name__ == '__main__':
    pass
