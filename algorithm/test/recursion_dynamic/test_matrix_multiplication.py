#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_matrix_multiplication.py
@time: 2018/5/28 15:31
"""
import unittest
from basic.recursion_dynamic.matrix_multiplication import MatrixMultiplication, Metrix


class TestMatrixMultiplication(unittest.TestCase):
    
    def tearDown(self):
        self.mp = None

    def setUp(self):
        self.mp = MatrixMultiplication()

    def test_matrix_multiplication(self):
        metrices_num = [[2, 3], [3, 6], [6, 4], [4, 5]]
        metrices = []
        for num in metrices_num:
            metrices.append(Metrix(num[0], num[1]))
        self.assertEqual(self.mp.find_min_cost(metrices), 124)

    def test_matrix_multiplication2(self):
        metrices_num = [[2, 3], [3, 6], [6, 4]]
        metrices = []
        for num in metrices_num:
            metrices.append(Metrix(num[0], num[1]))
        self.assertEqual(self.mp.find_min_cost(metrices), 84)
        #     0   1   2  offset = 1|2
        # 0   0   36  (24+72)|(36 + 48)
        # 1       0   72
        # 2           0


if __name__ == '__main__':
    pass
