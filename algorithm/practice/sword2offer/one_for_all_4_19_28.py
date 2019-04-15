#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: one_for_all_4_19_28.py
@time: 2018/9/6 15:53
"""
from basic.linked_list.linked_list import ComplexLinkedListNode
from basic.tree.binary_search_tree import BinarySearchTree, BinaryTreeNode
"""
chapter 4 
"""


# 19
class Solution:
    """
    19 二叉树的镜像
    """
    # 返回镜像树的根节点
    def mirror(self, root):
        # write code here
        if root is None:
            return
        left = root.left
        right = root.right
        root.left = self.mirror(right)
        root.right = self.mirror(left)
        return root


"""
20 顺时针打印矩阵
关键是推导得到循环打印的开始和停止条件，以及每个循环中每一边的开始条件，比如1X1，只有一条边需要打印，
2X2最后一条边无需打印
"""


class PrintMatrix(object):

    def __init__(self, ):
        self.result = []

    def print_matrix(self, matrix):
        if not matrix:
            return
        # loop time relate with rows and columns, We notice that the start coordinates are (0, 0), (1, 1)...
        rows = len(matrix)
        columns = len(matrix[0])
        start = 0
        while rows > 2 * start and columns > 2 * start:
            self.print_circle(matrix, start, rows, columns, self.result)
            start += 1

    def print_circle(self, matrix, start, rows, cols, result):
        """
        确定每一层循环的
        """
        row = rows - 2 * start
        col = cols - 2 * start
        end_h = row + start - 1  # vertical
        end_w = col + start - 1  # horizon

        # left -> right
        for w in range(start, end_w + 1):
            result.append(matrix[start][w])
        # top -> bottom
        if start < end_h:
            for h in range(start + 1, end_h + 1):
                result.append(matrix[h][end_w])
        # right -> left
        if start < end_w and start < end_h:
            for w in range(start, end_w)[::-1]:
                result.append(matrix[end_h][w])
        # bottom -> top
        if start < end_w and start < end_h - 1:
            for h in range(start + 1, end_h)[::-1]:
                result.append(matrix[h][start])


class Solution:
    def __init__(self):
        self.result = []

    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        rows = len(matrix)
        columns = len(matrix[0])
        start = 0
        while rows > 2 * start and columns > 2 * start:
            self.print_circle(matrix, start, rows, columns)
            start += 1
        return self.result

    def print_circle(self, matrix, start, rows, columns):
        width = columns - 2 * start
        height = rows - 2 * start
        end_w = start + width - 1  # 索引总是比实际长度-1
        end_h = start + height - 1

        # left -> right
        for w in range(start, end_w + 1):
            self.result.append(matrix[start][w])
        # top -> bottom
        if end_h > start:
            for h in range(start + 1, end_h + 1):
                self.result.append(matrix[h][end_w])
        # right -> left
        if end_w > start and end_h > start:
            for w in range(start, end_w)[::-1]:
                self.result.append(matrix[end_h][w])
        # bottom -> top
        if end_h - 1 > start and end_w > start:
            for h in range(start + 1, end_h)[::-1]:
                self.result.append(matrix[h][start])

def test_print_matrix():
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    matrix = [[1]]

    pm = PrintMatrix()
    pm.print_matrix(matrix)
    solution = Solution()
    solution.printMatrix(matrix)
    print(pm.result)


"""
21 包含min函数的栈
"""


class MinStack(object):
    # stack backed by list
    def __init__(self, ):
        self.stack = []
        self.mini = []

    def push(self, val):
        if not val:
            return
        if not self.stack:
            self.stack.append(val)
            self.mini.append(val)
        else:
            if self.mini and val < self.mini[-1]:
                self.mini.append(val)
            else:
                self.mini.append(self.mini[-1])

    def pop(self):
        if self.stack:
            self.mini.pop()
            return self.stack.pop()

    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]

    def min(self):
        return self.mini[-1] if self.mini else None


def test_mini_stack():
    mini_stack = MinStack()
    print(mini_stack.push(3), mini_stack.min())


"""
22 栈的压入弹出序列
依次弹出出栈序列首字符，开始循环
push_seq, pop_seq,如果栈当前非空，比较栈顶字符与当前出栈字符，不匹配则比较压栈序列和出栈序列，与出栈序列第一个字符不同字符依次进栈，两个序列弹出相同字符；
比较栈顶字符与当前出栈字符，相同则弹出字符，同时判断压栈序列是否为空，若为空，则依次比较栈的出栈元素和出栈序列是否相等
循环结束
"""
class IsPopOrder:
    def is_pop_order(self, pushV, popV):
        # write code here
        if not pushV or not popV:
            return False
        stack = []
        while popV:  # 以弹出序列作为循环条件
            pop_val = popV[0]
            if stack and stack[-1] == pop_val:
                stack.pop()
                popV.pop(0)
            else:
                while pushV:
                    if pushV[0] != pop_val:
                        stack.append(pushV.pop(0))
                    else:
                        pushV.pop(0)
                        popV.pop(0)
                        break
            if not pushV:
                while stack:
                    if stack.pop() != popV.pop(0):
                        return False
        return True


def test_is_pop_order():
    solution = IsPopOrder()
    ret = solution.is_pop_order([1,2,3,4,5],[4,5,3,2,1])
    print(ret)


"""
23 从上往下打印二叉树
即广度优先遍历二叉树
"""
from collections import deque
class BFS(object):

    def __init__(self, ):
        self.result = []

    def bfs(self, root: BinaryTreeNode):
        if root is None:
            return []

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            self.result.append(node.val)


"""
24 二叉树的后序遍历序列
判断一个序列是不是给定二叉搜索树的后续遍历，关注后序遍历的特性
每个序列的最后一个元素是根节点，左子比根节点都要小，右子比根节点都大
"""


def is_post_order(order: list):
    # 事实上除了最初序列为空，递归过程中不会出现空序列进入调用的情况，在单元素就会返回了，而且一定会返回TRUE
    if order is None or len(order) == 0:
        return False
    root = order[-1]
    left = 0
    # 如果只有一个元素的话，不会进入循环，因而不会出现数组越界，并且 left=0，right=left，返回true
    while order[left] < root:
        left += 1

    right = left
    while right < len(order) - 1:
        if order[right] < root:
            return False
        right += 1
    is_left = True if left == 0 else is_post_order(order[:left])  # 左子序列为空, 因而left = 0，左子满足
    is_right = True if left == right else is_post_order(order[left: right])  # 右子树为空，因而left==right，右子满足
    return is_left and is_right


class IsPostOrder(object):

    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence and len(sequence) == 0:
            return False
        root = sequence[-1]
        left = 0
        while sequence[left] < root:
            left += 1
        right = left
        while right < len(sequence) - 1:
            if sequence[right] < root:
                return False
            right += 1
        is_left = True if left == 0 else self.VerifySquenceOfBST(sequence[:left])
        is_right = True if left == right else self.VerifySquenceOfBST(sequence[left: right])
        return is_left and is_right


"""
25 二叉树中和为某一值的路径
二叉树中路径的和为某一固定值的所有路径
"""


class FindPathSum(object):

    def __init__(self, ):
        pass

    def find_path(self, bst_root, expected_sum):
        if bst_root is None:
            return
        path = []
        current_num = 0
        self._find_path(bst_root, expected_sum, path, current_num)

    def _find_path(self, bst_root, expected_sum, path, current_sum):
        is_leaf = bst_root.left is None and bst_root.right is None
        current_sum += bst_root.data
        path.append(bst_root.data)
        if current_sum == expected_sum and is_leaf:
            print(path[:])  # 注意path的引用问题

        if bst_root.left is not None:
            self._find_path(bst_root.left, expected_sum, path, current_sum)
        if bst_root.right is not None:
            self._find_path(bst_root.right, expected_sum, path, current_sum)

        # cut current node from path and current value before returning to parent
        current_sum -= bst_root.data
        path.pop()


class FindSumPath(object):
    def __init__(self):
        self.ret = []

    # 返回二维列表，内部每个列表表示找到的路径
    def find_path(self, root, expect_number):
        if root is None:
            return self.ret
        path = []
        curr_sum = 0

        def _find_path(root, expected_sum, path, current_num):
            is_leaf = root.left is None and root.right is None
            current_num += root.val
            path.append(root.val)
            if current_num == expected_sum and is_leaf:
                self.ret.append(path[:])
            if root.left:
                _find_path(root.left, expected_sum, path, current_num)
            if root.right:
                _find_path(root.right, expected_sum, path, current_num)
            current_num -= root.val  # 回溯
            path.pop()
        _find_path(root, expect_number, path, curr_sum)


def test_find_path():
    from basic.tree.binary_search_tree import BinaryTreeNode
    root = BinaryTreeNode(10)
    node2 = BinaryTreeNode(5)
    node3 = BinaryTreeNode(12)
    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(7)
    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5

    fps = FindPathSum()
    fps.find_path(root, 22)


# 26
class CloneComplexLinkedList(object):
    """
    26 复杂链表的复制
    由于每个节点的额外指向不能确定是在前面还是后面，因而如果不采用额外的空间或者经历一次遍历之后，指向的节点可能还没有被复制
    """
    def __init__(self, ):
        pass

    def clone_complex_linkedlist(self, head: ComplexLinkedListNode):
        if head is None:
            return
        self._clone_linkedlist(head)
        self._construct_sibling(head)
        return self._split_linkedlist(head)

    def _clone_linkedlist(self, head: ComplexLinkedListNode):
        loop_node = head
        while loop_node:
            clone_node = ComplexLinkedListNode('a')
            clone_node.data = loop_node.data
            clone_node.next = loop_node.next
            clone_node.sibling = None  # can be removed( it is default)

            loop_node.next = clone_node
            loop_node = clone_node.next

    def _construct_sibling(self, head: ComplexLinkedListNode):
        loop_node = head
        while loop_node:
            if loop_node.sibling is not None:
                loop_node.next.sibling = loop_node.sibling.next
            loop_node = loop_node.next.next

    def _split_linkedlist(self, head: ComplexLinkedListNode):
        if head is None:
            return
        loop_node = head

        clone_head = clone_loop_node = loop_node.next
        loop_node.next = clone_loop_node.next
        loop_node = loop_node.next

        while loop_node:
            clone_loop_node.next = loop_node.next
            clone_loop_node = clone_loop_node.next
            loop_node.next = clone_loop_node.next
            loop_node = loop_node.next

        return clone_head
# test refer test_cloen_complex_linkedlist


# 27
class TransferBstToDoubleLinkedList(object):
    """
    27 二叉搜索树与双向链表
    将二叉搜索树转换成一个排序的双向链表
    中序遍历可将搜索二叉树从小到大遍历
    """
    def __init__(self, ):
        pass

    # 输入为树的根节点
    def transfer(self, root):
        if root is None:
            return
        last_node = None  # 当前构建的链表最后一个节点
        last_node = self._construct(root, last_node)

        while last_node is not None and last_node.left is not None:  # 将链表指针指向最左边的节点
            last_node = last_node.left

        return last_node

    def _construct(self, root, last):
        curr = root
        if curr.left is not None:
            last = self._construct(curr.left, last)

        if last is not None:
            last.right = curr
        curr.left = last
        last = curr
        if curr.right is not None:
            last = self._construct(curr.right, last)
        return last




import itertools
class Permutation(object):
    """
    28 字符串的排列
    1 permutation只能处理不含重复字符的情况，
    2 而_Permutation可以处理更一般的情况
    3 repeat_char是一种突然就实现了的方法
    """
    def __init__(self, ):
        self.str_perm = []
        self.result = []
        self.ret = []

    def permutation(self, chars: str):
        for item in chars:
            chars_tmp = chars.replace(item, '')
            self.str_perm.append(item)
            if len(chars_tmp) > 0:
                self.permutation(chars_tmp)
            else:
                self.result.append(''.join(self.str_perm))
            self.str_perm.pop()

    def sub(self, string, index, new_char):
        new = []
        for s in string:
            new.append(s)
        new[index] = new_char
        return ''.join(new)


    def _Permutation(self, ss):
        for i, item in enumerate(ss):
            s = self.sub(ss, i, '')
            self.str_perm.append(item)
            if len(s) > 0:
                self._Permutation(s)
            else:
                self.result.append(self.str_perm[:])  # 注意深浅复制问题
            self.str_perm.pop()

    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        self._Permutation(ss)
        for i in self.result:
            if "".join(i) not in self.ret:
                self.ret.append("".join(i))
        return self.ret

    def repeat_char(self, ss):
        result = []
        if not ss:
            return []
        else:
            res = itertools.permutations(ss)
            for i in res:
                if "".join(i) not in result:
                    result.append("".join(i))
        return result


def test_permutation():
    chars = 'abc'
    p = Permutation()
    p.Permutation(chars)
    print(p.result)
    

if __name__ == '__main__':
    # test_find_path()
    # test_permutation()
    # test_print_matrix()
    # test_mini_stack()
    # test_is_pop_order()
    test_permutation()