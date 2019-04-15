#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_sort.py
@time: 2018/5/14 19:03
"""
import unittest
from basic.sort.sort import InsertionSort, QucikSort, SelectionSort, MergeSort


class TestSort(unittest.TestCase):
    
    def tearDown(self):
        pass

    def setUp(self):
        pass

    def test_insert_sort(self):
        sort = InsertionSort()
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        self.assertEqual(sort.sort(data), sorted(data))
        self.assertEqual(sort.sort_(data), sorted(data))

    def test_quick_sort(self):
        sort = QucikSort()
        self.assertEqual(sort.sort([]), [])
        self.assertEqual(sort.sort([5]), [5])
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        self.assertEqual(sort.sort(data), sorted(data))
        print('quick sort:\n', data)

    def test_selection_sort(self):
        sort = SelectionSort()
        self.assertEqual(sort.sort([]), [])
        self.assertEqual(sort.sort([5]), [5])
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        self.assertEqual(sort.sort_iterative_alt(data), [-3, -1, 1, 2, 5, 5, 6, 7, 7])
        self.assertEqual(sort.sort(data), [-3, -1, 1, 2, 5, 5, 6, 7, 7])
        self.assertEqual(sort.sort_recursive(data), [-3, -1, 1, 2, 5, 5, 6, 7, 7])

    def test_merge_sort(self):
        sort = MergeSort()
        self.assertRaises(TypeError, sort.sort, None)
        self.assertEqual(sort.sort([5]), [5])
        self.assertEqual(sort.sort([]), [])
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        self.assertEqual(sort.sort(data), sorted(data))



if __name__ == '__main__':
    pass
