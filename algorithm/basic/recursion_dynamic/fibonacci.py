#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: fibonacci.py
@time: 2018/5/28 13:50
"""


class Fibonacci(object):
    
    def __init__(self):
        pass

    def fibo_iterative(self, n):
        a = 0
        b = 1
        for _ in range(n):
            a, b = b, a+b
        return a

    def fibo_recursive(self, n):
        if n == 0 or n == 1:
            return n
        else:
            return self.fibo_recursive(n - 1) + self.fibo_recursive(n - 2)

    def fibo_dynamic(self, n):
        cache = {}
        return self._fibo_dynamic(n, cache)

    def _fibo_dynamic(self, n, cache):
        if n == 0 or n == 1:
            return n
        if n in cache:
            return cache[n]
        cache[n] = self._fibo_dynamic(n - 1, cache) + self._fibo_dynamic(n - 2, cache)
        return cache[n]

 
if __name__ == '__main__':
    pass
