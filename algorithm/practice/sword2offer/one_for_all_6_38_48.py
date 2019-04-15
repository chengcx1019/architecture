#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: one_for_all_6_38_48.py
@time: 2018/9/6 15:53
"""
from basic.tree.lca_tree import Node
"""
chapter 6
"""


"""
38 数字在排序数组中出现的次数
总是把数据的容量想象到非常大，使用二分查找
"""


class HowManyTimes(object):

    def __init__(self, ):
        pass

    def how_many_times(self, nums: list, objection):
        if nums is None or objection is None:
            return
        if not nums:
            return 0
        first_k = self._get_first_k(nums, len(nums), 0, len(nums)-1, objection)
        last_k = self._get_last_k(nums, len(nums), 0, len(nums)-1, objection)
        if first_k < 0 and last_k < 0:
            return 0
        if first_k < 0 or last_k < 0:
            return 1
        return last_k - first_k + 1

    def _get_first_k(self, nums, length, start, end, k):
        if start == end and nums[start] != k:
            return -1
        mid = (start + end) // 2

        if nums[mid] == k:
            if mid > 0 and nums[mid - 1] != k or mid == 0:
                return mid
            end = mid - 1
        elif nums[mid] < k:
            if mid < length - 1 and nums[mid + 1] == k:
                return mid+1
            end = mid - 1
        else:
            start = mid + 1

        return self._get_first_k(nums, length, start, end, k)

    def _get_last_k(self, nums, length, start, end, k):
        if start == end and nums[start] != k:
            return -1
        mid = (start + end) // 2

        if nums[mid] == k:
            if mid < length - 1 and nums[mid+1] != k or mid == length - 1:
                return mid
            start = mid + 1

        elif nums[mid] < k:
            start = mid + 1
        else:
            if mid > 0 and nums[mid-1] == k:
                return mid - 1
            end = mid - 1

        return self._get_last_k(nums, length, start, end, k)


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data or not k:
            return 0

        start = 0
        end = len(data)
        count = 0
        tag = False
        while start < end:
            mid = (start + end) // 2
            if mid == start or mid == end:
                if data[mid] == k:
                    count += 1
                    tag = True
                break
            if data[mid] == k:
                count += 1
                tag = True
                break
            elif data[mid] > k:
                end = mid
            else:
                start = mid
        if tag:
            loop = mid
            while loop < len(data)-1:
                loop += 1
                if data[loop] != k:
                    break
                count += 1
            loop = mid
            while loop > 0:
                loop -= 1
                if data[loop] != k:
                    break
                count += 1
            return count
        else:
            return 0

def test_GetNumberOfK():
    # 精彩的测试用例
    data = [([1, 2, 3, 3, 3, 3], 3),
            ([3], 3),
            ([1, 3, 3, 3, 3, 4, 5], 2)]
    # solution = Solution()
    solution = HowManyTimes()
    for item in data:
        print(solution.how_many_times(item[0], item[1]))


"""
39 二叉树的深度
"""


class TreeDepth(object):
    
    def __init__(self, ):
        pass

    def tree_depth(self, root):
        if root is None:
            return
        return self._tree_depth(root)

    def _tree_depth(self, root):
        if root is None:
            return 0
        left = self._tree_depth(root.left)
        right = self._tree_depth(root.right)

        return left + 1 if left > right else right + 1

    def is_balance(self, root):
        if root is None:
            return True

        left = self._tree_depth(root.left)
        right = self._tree_depth(root.right)
        if abs(left - right) > 1:
            return False

        return self.is_balance(root.left) and self.is_balance(root.right)

    # 诚然后序遍历是一个很契合要求的思路，同样是递归的思路，却做到了自底向上的不重复计算
    def is_balance_2(self, root):
        depth = [-1]
        return self._is_balance_2(root, depth)

    def _is_balance_2(self, root, depth):
        if root is None:
            depth[0] = 0
            return True
        left = [-1]
        right = [-1]
        if self._is_balance_2(root.left, left) and self._is_balance_2(root.right, right):
            if abs(left[0] - right[0]) <= 1:
                depth[0] = left[0] + 1 if left[0] > right[0] else right[0] + 1
                return True
        return False


def test_tree_depth():
    node10 = Node(10)
    node5 = Node(5)
    node12 = Node(12)
    node3 = Node(3)
    node1 = Node(1)
    node8 = Node(8)
    node9 = Node(9)
    node18 = Node(18)
    node20 = Node(20)
    node40 = Node(40)

    node3.left = node1
    node3.right = node8
    node5.left = node12
    node5.right = node3
    node20.left = node40
    node9.left = node18
    node9.right = node20
    node10.left = node5
    node10.right = node9
    root = node10
    td = TreeDepth()
    print(td.tree_depth(root))
    node60 = Node(60)
    node80 = Node(80)
    node12.left = node60
    node18.right = node80
    print(td.is_balance(root), td.is_balance_2(root))
    print(td.tree_depth(root))


"""
40 数组中只出现一次的数字
（一个数组中除了两个数字外，其他的数字都出现了两次，找出这两个只出现一次的数）
如果数组中只有一个数字是单独的，其他都成对出现，那么对数组中的元素进行连续的异或运算，即可得到这个唯一值
把这两个单独的数字分成两组
"""


class TwoUniqueNum(object):

    def __init__(self, ):
        pass

    def two_unique_num(self, nums: list):
        if nums is None or not nums:
            return
        xor_result = self._xor(nums)
        binary_xor_result = bin(xor_result)
        length = len(binary_xor_result)
        first_one = binary_xor_result.find('1')
        tag = 2**(length - first_one - 1)
        left = []
        right = []
        for item in nums:
            if item & tag == tag:
                left.append(item)
            else:
                right.append(item)
        return [self._xor(left), self._xor(right)]

    def _xor(self, nums):  # 一个数组间数字连续进行异或运算
        result = nums[0]
        for item in nums[1:]:
            result ^= item
        return result


def test_two_unique_num():
    tun = TwoUniqueNum()
    test_cases = [[2, 4, 3, 6, 3, 2, 5, 5]]
    print(tun._xor(test_cases[0]))

    print(tun.two_unique_num(test_cases[0]))


"""
41 和为s的两个数字 VS 和为s的连续正数序列
1. 从已排好序的序列中找到给定和的序列
2. 输出和为s的连续正数序列
"""


class FindNumsWithSum(object):
    
    def __init__(self, ):
        pass

    def find_nums_with_sum(self, sorted_nums: list, sum: int):
        result = [-1, -1]
        found = False
        if sorted_nums is None or not sorted_nums:
            return found

        ahead = 0  # 数组头指针
        behind = len(sorted_nums) - 1  # 数组尾指针
        while ahead < behind:
            curr_sum = sorted_nums[ahead] + sorted_nums[behind]
            if curr_sum == sum:
                result[0] = sorted_nums[ahead]
                result[1] = sorted_nums[behind]
                found = True
                break
            elif curr_sum < sum:
                ahead += 1
            else:
                behind -= 1

        return found, result

    def find_seq_with_sum(self, sum: int):
        if sum is None or sum < 3:
            return
        start = 1
        end = 2
        result = []  # 每一项是一个tuple，包含起点和终点
        mid = (sum + 1) / 2  # 想到这个条件才是重点
        curr = start + end
        while start < mid:
            if curr == sum:
                result.append((start, end))  # 还可能存在其他解，end需要继续往后走
            elif curr > sum:
                curr -= start
                start += 1
                continue

            end += 1
            curr += end
        return result

    def print_result(self, rt):
        for s_e in rt:
            print(''.join([str(i) for i in range(s_e[0], s_e[1]+1)]))


def test_find_nums_with_sum():
    solution = FindNumsWithSum()
    test_caases = [([1, 2, 4, 7, 11, 15], 15)]
    for case in test_caases:
        result = solution.find_nums_with_sum(case[0], case[1])
        if result[0]:
            print(result[1])
        else:
            print('no result!')
    solution.print_result(solution.find_seq_with_sum(15))


"""
42 翻转单词顺序与左旋转字符串
"""


"""
43 n个骰子的点数

"""


"""
44 扑克牌的顺子
统计0的数目，以及排序后的间隔数，最后比对二者是否相等
"""

class IsContinuous(object):
    
    def __init__(self, ):
        pass

    def is_continuous(self, s):
        # write code here
        if not s:
            return False
        nums = []
        zero = 0
        for item in s:
            if item == 0:
                zero += 1
                continue
            nums.append(item)
        nums = sorted(nums)
        margin_all = 0
        start = 0
        while start < len(nums) - 1:
            margin = nums[start + 1] - nums[start]
            if margin == 0:
                return False
            if margin > 1:
                margin_all += margin - 1  # 填补间隔需要的数字
            start += 1
        return zero >= margin_all


def test_is_continuous():
    test_cases = [[1, 0, 0, 1, 0],
                  [],
                  [1, 3, 2, 5, 4]]
    solution = IsContinuous()
    for case in test_cases:
        print(solution.is_continuous(case))

        
    


"""
45 圆圈中最后剩下的数字
0,...,n-1这n个数字排成一个圆圈，从数字0开始每次删除第m个数字，求出圈中剩余的最后一个数字
"""


class LastRemaining(object):

    def __init__(self, ):
        pass

    def last_remaining(self, n, m):
        if n < 0 or m < 0:
            return

        if n == 1:
            return 0

        last = 0
        for i in range(2, n+1):
            last = (last + m) % i
        return last

    def last_remaining_recursion(self, n, m):
        if n == 1:
            return 0
        return (self.last_remaining_recursion(n-1, m) + m) % n


def test_last_remaining():
    n = 5
    m = 3
    solution = LastRemaining()
    print(solution.last_remaining(n, m) == solution.last_remaining_recursion(n, m), solution.last_remaining(n, m))


"""
46 求1+2...+n
"""


"""
47 不用加减乘除做加法
同为1则产生进位，&运算后左移一位即进位，异或的结果是两树相加不考虑进位
"""


class AddWithoutOperation(object):
    
    def __init__(self, ):
        pass

    def add(self, num1, num2):
        carry = 1
        while carry:
            sum = num1 ^ num2
            carry = 0xFFFFFFFF & ((num1 & num2) << 1)
            carry = -(~(carry - 1) & 0xFFFFFFFF) if carry > 0x7FFFFFFF else carry

            num1 = sum
            num2 = carry

        return num1


def test_add():
    solution = AddWithoutOperation()
    print(solution.add(444, 555))
test_add()


"""
48 不能被继承的类
pass
"""

if __name__ == '__main__':
    # test_two_unique_num()
    # test_find_nums_with_sum()
    # test_last_remaining()
    # test_add()
    # test_GetNumberOfK()
    pass