#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: sort.py
@time: 2018/5/14 18:51
"""


class InsertionSort(object):
    """
    Time:O(n), O(n^2), O(n^2)
    Time: O(n^2) avarage, worst. O(1) best if input is already sorted.
    Space: O(1)

    In-place
    Stable
    small dataset
    每一个值r与左边所有的值比较，确定插入位置l，后面的[l:r]数据向后移一位
    """
    def __init__(self):
        pass

    def sort(self, data):
        if data is None:
            raise TypeError("data can't be None")
        if len(data) < 2:
            return data
        for r in range(1, len(data)):
            for l in range(r):
                if data[r] < data[l]:
                    # 确定插入点l,缓存r位置值
                    temp = data[r]
                    data[l+1: r+1] = data[l: r]
                    data[l] = temp
        return data

    def sort_(self, data):
        if data is None:
            raise TypeError("data can't be None")
        for r in range(1, len(data)):
            self._insert(data, r, data[r])
        return data

    def _insert(self, data, pos, value):
        i = pos - 1
        while(i >= 0 and data[i] > value):
            data[i + 1] = data[i]
            i = i - 1
        data[i + 1] = value


class MedianSort(object):
    """
    Time：
    """
    def __init__(self, ):
        pass

    def sort(self):
        """
        """
        pass
        
"""
归并排序和快速排序的对比：在归并排序中，数据的划分是很快的，算法的主要运行时间在于合并子问题的解，
而在快速排序中，算法的主要工作在划分阶段，而不需要再去合并子问题的解了
"""
class MergeSort(object):
    """
    Complexity:
        Time: O(n log(n))
        Space: O(n)

    """
    def __init__(self, ):
        pass

    def sort(self, data):
        if data is None:
            raise TypeError('data can\'t be None')
        return self._sort(data)

    def _sort(self, data):
        if len(data) < 2:
            return data

        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        left = self._sort(left)
        right = self._sort(right)
        return self._merge(left, right)

    def _merge(self, left, right):
        l = 0
        r = 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        while l < len(left):
            result.append(left[l])
            l += 1
        while r < len(right):
            result.append(right[r])
            r += 1
        return result



class QucikSort(object):
    """Misc:
    * More sophisticated implementations are in-place, although they still take up recursion depth space
    * Most implementations are not stable

    See Quicksort on wikipedia:

    Typically, quicksort is significantly faster in practice than other Θ(nlogn) algorithms,
    because its inner loop can be efficiently implemented on most architectures[presumably because it has good cache locality],
    and in most real-world data, it is possible to make design choices which minimize the probability of requiring quadratic time.
    See: Quicksort vs merge sort: http://stackoverflow.com/a/90477"""
    def __init__(self, ):
        pass

    def sort(self, data):
        if data is None:
            raise TypeError('data can\'t be None')
        return self._sort(data)

    def _sort(self, data):
        if len(data) < 2:
            return data
        pivot_index = len(data) // 2
        pivot = data[pivot_index]
        equal = []
        left = []
        right = []
        for item in data:
            if item == pivot:
                equal.append(item)
            elif item < pivot:
                left.append(item)
            else:
                right.append(item)
        left_ = self._sort(left)
        right_ = self._sort(right)

        return left_ + equal + right_


class RadixSort(object):  # 基排序

    def __init__(self, ):
        pass


class SelectionSort(object):
    
    def __init__(self, ):
        pass

    # method 1
    def sort(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data

        for i in range(len(data) - 1):
            min_index = i
            for j in range(i+1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]
        return data

    # method 2
    def sort_iterative_alt(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data
        for i in range(len(data) - 1):
            self._swap(data, i, self._find_min_index(data, i))
        return data

    def _find_min_index(self, data, start):
        min_index = start
        for i in range(start + 1, len(data)):
            if data[i] < data[min_index]:
                min_index = i
        return min_index

    def _swap(self, data, i, j):
        if i != j:
            data[i], data[j] = data[j], data[i]
        return data

    # method 3
    def sort_recursive(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data
        return self._sort_recursive(data, start=0)

    def _sort_recursive(self, data, start):
        if data is None:
            return
        if start < len(data) - 1:
            self._swap(data, start, self._find_min_index(data, start))
            self._sort_recursive(data, start + 1)
        return data






class HeapSort(object):
    """in-place
        not stable
    """

    def __init__(self, ):
        pass


if __name__ == '__main__':
    sort = MergeSort()
    data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
    print(sort.sort(data))
