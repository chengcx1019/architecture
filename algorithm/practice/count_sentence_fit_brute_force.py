#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: count_sentence_fit_brute_force.py
@time: 2018/5/28 19:51
"""


class CountSentenceFit(object):
    
    def __init__(self, ):
        pass

    def compute_sentence_fit_brute_force(self, sentence, rows, cols):
        try:
            iter(sentence)
        except TypeError:
            raise TypeError('sentence must be type str')
        if not isinstance(rows, int) or not isinstance(cols, int):
            raise TypeError('rows and cols must be type int')
        if rows < 0 or cols < 0:
            raise ValueError('rows and cols can\' be negative')
        curr_row = 0
        curr_col = 0
        count = 0
        while curr_row < rows:
            for word in sentence:
                if len(word) > cols - curr_col:
                    curr_col = 0
                    curr_row += 1
                if curr_row >= rows:
                    return count

                if len(word) <= cols - curr_col:
                    curr_col += len(word) + 1
                else:
                    return count  # 因为已经到新行，此时说明单字长度大于列长
            count += 1

        return count

    # todo optimize
    def compute_sentence_fit(self):
        pass


if __name__ == '__main__':
    pass
