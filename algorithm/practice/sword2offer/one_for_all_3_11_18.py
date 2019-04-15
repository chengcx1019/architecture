#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: one_for_all_3_11_18.py
@time: 2018/9/6 15:53
"""
from basic.linked_list.linked_list import LinkedList, LinkedListNode
from basic.tree.binary_search_tree import BinaryTreeNode
"""
chapter 3
"""

"""
11 数值的整数次方
"""


class Power(object):

    def __init__(self, ):
        pass

    def _equal_zero(self, num):
        if abs(num) < 1e-7:
            return True
        return False

    def power(self, base, exponent):
        if self._equal_zero(base) and self._equal_zero(exponent):
            raise ValueError('can\'t both be zero')

        if self._equal_zero(base) and exponent < 0:
            raise ZeroDivisionError('zero division')

        is_negative = False
        if exponent < 0:
            is_negative = True
        result = self._power_value(base, abs(exponent))

        if is_negative:
            result = 1 / result

        return result

    def _power_value(self, base, exponent):
        if exponent == 1:
            return base
        elif self._equal_zero(exponent):
            return 1
        result = self._power_value(base, exponent >> 1)
        result *= result
        if exponent & 1 == 1:
            result *= base

        return result


def test_power():
    power = Power()
    test_cases = [(0, 0), (10, 2), (10, 3), (10, -3), (0, -3)]
    for testcase in test_cases:
        base, expoent = testcase
        try:
            print(power.power(base, expoent))
        except Exception as e:
            print('exception:', e)


"""
12 打印1到最大的n位数
"""

"""
13 O(1)时间删除链表结点
"""

"""
14 调整数组顺序使奇数位于偶数前面
"""


class OddBeroreEven(object):

    def __init__(self, ):
        pass

    def odd_before_even(self, num_list):
        if not num_list:
            return
        pre = 0
        post = len(num_list) - 1
        while pre < post:

            if num_list[pre] % 2 == 0 and num_list[post] % 2 != 0:
                num_list[pre], num_list[post] = num_list[post], num_list[pre]

            if num_list[pre] % 2 != 0:
                pre += 1
            if num_list[post] % 2 == 0:
                post -= 1
        return num_list

    def _merge(self, left, right):
        l = 0
        r = 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] % 2 != 0:
                result.append(left[l])
                l += 1
            elif left[l] % 2 == 0 and right[r] % 2 != 0:
                result.append(right[r])
                r += 1
            elif left[l] % 2 == 0 and right[r] % 2 == 0:
                result.append(left[l])
                l += 1
        while l < len(left):
            result.append(left[l])
            l += 1
        while r < len(right):
            result.append(right[r])
            r += 1
        return result

    # 如果对本题进行修改，输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
    # 所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
    # 定义一个新的排序规则奇数小于任意偶数，并应用一种稳定的排序方式，另外，如果原始数组是无序的，则判断条件还需要相应改变
    def re_order_array(self, array):
        # write code here
        if len(array) < 2:
            return array
        mid = len(array) // 2
        left = self.re_order_array(array[:mid])
        right = self.re_order_array(array[mid:])
        return self._merge(left, right)


def test_odd_before_even():
    test_cases = [[1, 2, 3, 4, 5], [9, 3, 1, 0, 1, 9], [1, 2, 1, 2, 9, 3]]
    cls = OddBeroreEven()
    for case in test_cases:
        print(cls.odd_before_even(case))


"""
15 链表中倒数第k个结点
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LastK(object):
    def find_kth_to_tail(self, head, k):
        # write code here

        node = head
        node2 = head
        count = 0
        result = []
        while node2:
            if count < k:

                count += 1
            else:
                node = node.next
            node2 = node2.next
        if count < k:
            return

        return node


"""
16  反转链表
测试用例:空链表，只有一个节点的链表
"""


class ReverseLinkedList(object):

    def __init__(self, ):
        pass

    def reverse_linkedlist(self, phead):
        """
        pnode是当前链表中操作的节点，
        pre记录反转链表目前的首节点
        pnext存储当前链表的下一节点
        """
        if not phead:
            return
        if not phead.next:
            return phead
        pre = None
        reverse = LinkedList()
        pnode = phead
        while pnode:
            pnext = pnode.next
            if not pnext:
                reverse.head = pnode
            pnode.next = pre
            pre = pnode
            pnode = pnext
        return reverse


def test_reverse_linkedlist():
    normal = LinkedList()
    test_data = [9, 3, 1, 0, 1, 9]
    test_data = [9]
    for item in test_data:
        normal.append(item)
    print(normal.get_all())
    reverse_l = ReverseLinkedList()
    reverse = reverse_l.reverse_linkedlist(normal.head)
    print('reverse', reverse.get_all())


"""
17 合并两个排序的链表
合并链表merge，两者有一方不空时进入循环：

"""


class MergeLinkedList(object):

    def __init__(self, ):
        pass

    def merge(self, head1, head2):
        if not head1 and not head2:
            return
        elif not head1:
            return head2
        elif not head2:
            return head1

        l1 = head1
        l2 = head2
        merge = LinkedList()

        while l1 and l2:
            if l1.data < l2.data:
                merge.append(l1.data)
                l1 = l1.next
            else:
                merge.append(l2.data)
                l2 = l2.next
        while l2:
            merge.append(l2.data)
            l2 = l2.next
        while l1:
            merge.append(l1.data)
            l1 = l1.next
        return merge

    def merge_2(self, p_head1, p_head2):
        # write code here
        if not p_head1 and not p_head2:
            return
        if not p_head1:
            return p_head2
        if not p_head2:
            return p_head1
        p1 = p_head1
        p2 = p_head2

        if p1.val <= p2.val:
            merge = ListNode(p1.val)
            p1 = p1.next
        else:
            merge = ListNode(p2.val)
            p2 = p2.next
        merge_head = merge
        while p1 and p2:
            if p1.val <= p2.val:
                merge.next = ListNode(p1.val)
                p1 = p1.next
            else:
                merge.next = ListNode(p2.val)
                p2 = p2.next
            merge = merge.next
        while p1:
            merge.next = ListNode(p1.val)
            merge = merge.next
            p1 = p1.next
        while p2:
            merge.next = ListNode(p2.val)
            merge = merge.next
            p2 = p2.next
        return merge_head

    def merge_recurssion(self, head1, head2):
        if not head1 and not head2:
            return
        elif not head1:
            return head2
        elif not head2:
            return head1

        l1 = head1
        l2 = head2
        merge = LinkedListNode(0)

        if l1.data < l2.data:
            merge.data = l1.data
            merge.next = self.merge_recurssion(l1.next, l2)
        else:
            merge.data = l2.data
            merge.next = self.merge_recurssion(l1, l2.next)

        return merge


def test_merge_linkedlist():
    l1 = LinkedList()
    l2 = LinkedList()
    test_data1 = [1, 3, 5]
    test_data2 = [2, 6, 7, 8]
    for item in test_data1:
        l1.append(item)
    for item in test_data2:
        l2.append(item)
    merge_l = MergeLinkedList()
    merge = merge_l.merge(l1.head, l2.head)
    merge2 = LinkedList()
    merge2.head = merge_l.merge_recurssion(l1.head, l2.head)
    print('merge', merge2.get_all())


"""
18 树的子结构
约定空树不是任意一个树的子结构
递归停止条件：为描述方便，判断右树是不是左树的子树，左树的当前节点的左子或右子为空，而右树当前节点的左子或右子不为空；其他均为空或左树不为空，均返回真值；均不为空，继续递归
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SubTree(object):

    def __init__(self, ):
        pass

    def has_subtree(self, tree1: BinaryTreeNode, tree2: BinaryTreeNode):
        if not tree2:
            return False  # 空树不是任何树的子树
        if not tree1:
            return False
        result = False
        if tree1.val == tree2.val:
            result = self.does_tree1_has_tree2(tree1, tree2)
        if not result:
            return self.has_subtree(tree1.left, tree2) or self.has_subtree(tree1.right, tree2)
        else:
            return True

    def does_tree1_has_tree2(self, tree1, tree2):
        if not tree1 and tree2:
            return False
        if tree1 and tree2:
            if tree1.val != tree2.val:
                return False
            else:
                return self.does_tree1_has_tree2(tree1.left, tree2.left) and self.does_tree1_has_tree2(tree1.right, tree2.right)
        return True




if __name__ == '__main__':
    pass
