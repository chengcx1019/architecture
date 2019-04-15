#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: math.py
@time: 2018/5/29 00:24
"""
import math


class Math(object):
    
    def __init__(self, ):
        pass

    def check_prime(self, number):
        if number is None or not isinstance(number, int):
            raise TypeError('number must be int')
        if number < 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    def check_prime_optimized(self, number):
        if number is None or not isinstance(number, int):
            raise TypeError('number must be int')
        if number < 2:
            return False
        for i in range(2, int(math.sqrt(number)+1)):
            if number % i == 0:
                return False
        return True
        

if __name__ == '__main__':
    pass
