#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: one_for_all_2_2_10.py
@time: 2018/9/5 09:57
"""
from basic.linked_list.linked_list import LinkedList, LinkedListNode
from basic.stack_queue.stack import Stack
from basic.tree.binary_search_tree import BinaryTreeNode, Traversal
from basic.utils.results import Results
"""
添加问题列表，按文件进行组织

"""

"""
chapter 2
"""


"""
2 单例模式
"""


# 3
class FindTargetInArray(object):
    '''
    3 二维数组中的查找
    '''
    # array 二维列表
    def find(self, target, array):
        # write code here
        height = len(array)
        width = len(array[0])
        curr_row = 0
        curr_col = width - 1
        while curr_row <= height-1 and curr_col >= 0:
            if array[curr_row][curr_col] == target:
                return True
            if array[curr_row][curr_col] > target:
                curr_col -= 1
            else:
                curr_row += 1
        return False


# 4
class ReplaceSpace(object):
    '''
    4 替换空格
    '''
    # s 源字符串
    def replace_space(self, s):
        # write code here
        rep_str = '%20'
        s_len = len(s)
        stack = []
        for i in range(s_len-1, -1, -1):
            if s[i] != ' ':
                stack.append(s[i])
            else:
                stack.append(rep_str)
        return ''.join(stack[::-1])


def test_replace_space():
    rs = ReplaceSpace()
    print(rs.replace_space('We Are Happy'))


'''
5 从尾到头打印单链表
'''


def reverse_linked_list():
    linkedl = LinkedList()
    num_str = '123456'
    for item in num_str:
        linkedl.append(int(item))
    print(linkedl.get_all())

    stack = Stack()
    while linkedl.head:
        stack.push(linkedl.head.data)
        linkedl.head = linkedl.head.next
    while stack.head:
        print(stack.pop())


# 5简化版
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ReverseLinkedList(object):
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def print_listFromTailToHead(self, list_node):
        # write code here
        node = list_node
        stack = []  # 使用[]模拟栈，pop方法模拟出栈
        while node:
            stack.append(node.val)
            node = node.next
        return stack[::-1]


# 6
class ReconstructBinaryTree(object):
    """
    6 重建二叉树
    要求：根据前序遍历和中序遍历重建二叉树
    思路：前序遍历的第一个字符是根节点，中序遍历中根节点的左边是左子树，右边是右子树
    """
    def __init__(self, ):
        pass

    def construct(self, preorder: list, inorder: list):
        if not preorder or not inorder or len(preorder) != len(inorder):
            print('valid input')
            return

        root_index = inorder.index(preorder[0])
        root = BinaryTreeNode(preorder[0])
        root.left = self.construct(preorder[1: root_index+1], inorder[:root_index])
        root.right = self.construct(preorder[root_index+1:], inorder[root_index+1:])

        return root


def test_reconstruct_bt():
    rbt = ReconstructBinaryTree()
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7, 2, 1, 5, 3, 8, 6]
    bt = rbt.construct(preorder, inorder)
    traversal = Traversal()
    results = Results()
    traversal.in_order_traversal(bt, results.add_result)
    print(results.results)


# 7
class QueueByStack(object):
    '''
    7 用两个栈实现队列
    思路：stack1负责存储压入的数据，压入前，需要将stack2的数据都压入stack1中，而stack2负责弹出数据（弹出之前，需要将stack1数据压入stack2中）
    '''
    def __init__(self, ):
        self.stack1 = []
        self.stack2 = []

    def push(self, data):
        if data is None:
            return

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        self.stack1.append(data)

    def pop(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def is_empty(self):
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False


def test_queue_by_stack():
    queue = QueueByStack()
    for item in 'a1b2c3':
        queue.push(item)

    while not queue.is_empty():
        print(queue.pop())


# 8
class RotateArray(object):
    '''
    8 旋转数组的最小数字
    思路1：直接遍历
    思路2：二分查找
    '''
    def min_number_in_rotate_array(self, rotate_array):
        # write code here
        if len(rotate_array) == 0:
            return 0
        for i in range(len(rotate_array)):
            if i < len(rotate_array) - 1:
                if rotate_array[i] > rotate_array[i + 1]:
                    return rotate_array[i + 1]

    # 考虑数组如果是正常排序的数组
    def method2(self, rotate_array):
        if len(rotate_array) == 0:
            return 0
        index1 = 0
        index2 = len(rotate_array) - 1
        mid = index1
        while rotate_array[index1] >= rotate_array[index2]:

            if index2 - index1 == 1:
                mid = index2
                break
            mid = (index1 + index2) // 2
            if rotate_array[index1] <= rotate_array[mid]:
                index1 = mid
            elif rotate_array[index2] >= rotate_array[mid]:
                index2 = mid

        return rotate_array[mid]


# 9
class Fibonacci(object):
    '''
    9 斐波那契数列
    from basic.recursion_dynamic.fibonacci import Fibonacci, 求前n项和
    这里列出一种生成器的方式输出序列
    '''
    # 记忆方式，自顶向下的缓存
    def __init__(self):
        self.cache = {}

    def fibonacci(self, n):
        # write code here
        if n == 0 or n == 1:
            return n
        if n not in self.cache:
            self.cache[n] = self.fibonacci(n - 1) + self.fibonacci(n - 2)
        return self.cache[n]

    # 自底向上的循环模式
    # n指的是序列中第几项，只需叠加n-1次
    def fibonacci_2(self, n):
        # write code here
        if n == 0 or n == 1:
            return n
        a = 0
        b = 1
        for _ in range(n - 1):
            a, b = b, a + b

        return b

    # 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
    # 参数代表的意义略有不同，这里的number实际是指台阶的阶数，而相应对应的斐波那契数列中的 number+1项 也就是从叠加的次数为number
    def jump_loor(self, number):
        # write code here
        if number == 0 or number == 1:
            return number
        a = 0
        b = 1
        for _ in range(number):
            a, b = b, a + b
        return b

    # 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
    # 采用动态规划的思想 最后一步可以跳1阶，2阶，...，n阶，那么
    # F(n) = F(n-1) + F(n-2)... + F(0) ...(1)
    # F(n-1) = F(n-2) + F(n-3)... + F(0) ...(2)
    # (1)式-(2)式得F(n) - F(n-1) = F(n-1) 即 F(n) = 2 * F(n-1)  (n>=2)
    def abnormal_jump(self, number):
        if number <=0:
            return 1
        if number == 1:
            return 1
        return 2*self.abnormal_jump(number-1)


'''
10 二进制中1的个数
测试用例：正数、负数、0
'''


class CountOne(object):

    def __init__(self, ):
        pass

    def count_one(self, n: int):
        count = 0

        while n:
            # print(n)
            count += 1
            n = n & n-1  # 最后一个1会变成0
        return count

    def count_one_2(self, n):
        count = 0
        flag = 1
        while n:
            if n & flag:
                count += 1
            flag = flag << 1
        return count

    def count_one_3(self, n):
        return bin(n).replace("0b", "").count("1") if n >= 0 else bin(2**32+n).replace("0b", "").count("1")


def test_count_one():
    n = -15
    count1 = CountOne()
    result = count1.count_one_2(n)
    print(result)


if __name__ == '__main__':
    # test_reconstruct_bt()
    # test_count_one()
    # reverse_linked_list()
    # test_queue_by_stack()
    # test_fib()
    # test_count_one()
    # test_replace_space(
    test_count_one()
