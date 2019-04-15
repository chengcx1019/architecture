#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: n_steps.py
@time: 2018/5/28 23:56
"""


class NSteps(object):
    
    def __init__(self, ):
        pass

    def n_steps(self, num_steps):
        if num_steps is None:
            raise TypeError('num_steps con\'t be None')
        cache = {}
        return self._n_steps(num_steps, cache)

    def _n_steps(self, num_steps, cache):
        if num_steps < 0:
            return 0
        if num_steps == 0:
            return 1
        cache[num_steps] = (self._n_steps(num_steps-1, cache) +
                            self._n_steps(num_steps-2, cache) +
                            self._n_steps(num_steps-3, cache))
        return cache[num_steps]


if __name__ == '__main__':
    pass
