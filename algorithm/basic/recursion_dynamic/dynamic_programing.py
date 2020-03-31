#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: dynamic_programing.py
@time: 2018/9/9 14:41
"""
import sys

# transfer from a to b
class LevenshteinDistance(object):
    
    def __init__(self, ):
        pass

    def min_levenshtein_distance(self, a, b):
        width = len(a) + 1  # column
        height = len(b) + 1  # row
        # 实例化python的矩阵确实麻烦
        lev_matrix = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(0)
            lev_matrix.append(row)

        for i in range(0, width):
            lev_matrix[0][i] = i
        for j in range(1, height):
            lev_matrix[j][0] = j

        for j in range(1, height):
            for i in range(1, width):
                indicator = 0 if a[i-1] == b[j-1] else 1
                lev_matrix[j][i] = min(lev_matrix[j][i-1] + 1,  # deletion
                                       lev_matrix[j-1][i] + 1,  # insertion
                                       lev_matrix[j-1][i-1] + indicator)  # substitution

        return lev_matrix[height-1][width-1]


def test_min_levenshtein_distance():
    solution = LevenshteinDistance()
    print(solution.min_levenshtein_distance('ME', 'MY'))
    print(solution.min_levenshtein_distance('Saturday', 'Sunday'))
    

# 币值最大化问题：一排硬币，原始位置互不相邻，总金额最大
class MaxCash(object):
    
    def __init__(self, ):
        pass

    def max_cash_top(self, coins: list, n):
        if n == 0:
            return 0
        if n == 1:
            return coins[n-1]
        return max(self.max_cash_top(coins, n-1), self.max_cash_top(coins, n-2) + coins[n-1])

    def max_cash_top_cache(self, coins: list, n, cache):
        if n == 0:
            return 0
        if n == 1:
            return coins[n-1]
        if n in cache:
            return cache[n]
        cache[n] = max(self.max_cash_top_cache(coins, n-1, cache), self.max_cash_top_cache(coins, n-2, cache) + coins[n-1])
        return cache[n]

    def max_cash_botom_top(self, coins: list, n):
        precount = 0
        count = coins[0]
        for i in range(1, n):
            new_count = max(count, precount + coins[i])
            precount = count
            count = new_count
        return count


def test_max_cash_botom_top():
    solution = MaxCash()
    coins = [5, 1, 2, 10, 6, 2]
    print(solution.max_cash_botom_top(coins, 6))
    cache = {}
    print(solution.max_cash_top_cache(coins, 6, cache))


# 'change' problem 找零问题，找零金额为n，最小需要多少枚不同面值的硬币
class ChangeMaking(object):
    
    def __init__(self, ):
        pass

    def change_making(self, coins, n):
        if n == 0:
            return 0
        coins_len = len(coins)

        for i in range(1, n+1):
            temp = sys.maxsize
            j = 0
            while j < coins_len and i >= coins[j]:
                temp = min(self.change_making(coins, i - coins[j]), temp)
                j += 1
            temp = temp + 1
        return temp

    def change_making_cache(self, coins, n, cache):
        if n == 0:
            return 0
        coins_len = len(coins)
        for i in range(1, n+1):
            temp = sys.maxsize
            j = 0
            while j < coins_len and i >= coins[j]:
                if i-coins[j] not in cache:
                    cache[i-coins[j]] = self.change_making_cache(coins, i - coins[j], cache)
                temp = min(cache[i - coins[j]], temp)
                j += 1
            cache[i] = temp + 1
        return cache[n]


def test_change_making():
    solution = ChangeMaking()
    print(solution.change_making([1, 3, 4], 6))
    cache = {}
    print(solution.change_making_cache([1, 3, 4], 6, cache))



class RobotCoinCollect(object):
    """
    在nxm格木板中放有一些硬币，每格的硬币数目最多为一个。在木板左上方的一个机器人需要收集尽可能多的硬币并把
    它们带到右下角的单元格。每一步机器人可以选择向右或向下走一步。
    设计一个算法找出机器人能够找到的最大硬币数目并给出相应的路径。
    """
    
    def __init__(self, ):
        pass

    def _matrix(self, n, m):
        matrix = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(0)
            matrix.append(row)
        return matrix

    def robot_coin_collect(self, n, m, coins: list, path):
        """coins = [(1, 1), (0, 4), (1, 3),
        (2, 3), (2, 5), (3, 2), (3, 5),
        (4, 0), (4, 4)]"""

        coin_matrix = self._matrix(n, m)

        for coin in coins:
            coin_matrix[coin[0]][coin[1]] = 1

        count_coin = self._matrix(n, m)
        count_coin[0][0] = coin_matrix[0][0]
        for j in range(m):
            if j > 0:
                count_coin[0][j] = count_coin[0][j-1] + coin_matrix[0][j]
        for i in range(1, n):
            count_coin[i][0] = count_coin[i-1][0] + coin_matrix[i][0]

            for j in range(1, m):
                # indicator = 1 if (i, j) in coins else 0
                count_coin[i][j] = max(count_coin[i-1][j], count_coin[i][j-1]) + coin_matrix[i][j]
        path.append([n-1, m-1])
        self.find_path(count_coin, path, n-1, m-1)
        return count_coin[n-1][m-1]

    def find_path(self, count_coin, path:list, n, m):
        if m == 0 and n == 0:
            return
        if m >= 1 and n >= 1:
            if count_coin[n][m-1] >= count_coin[n-1][m]:
                path.append([n, m-1])
                self.find_path(count_coin, path, n, m-1)
            else:
                path.append([n-1, m])
                self.find_path(count_coin, path, n-1, m)
        elif m > 0:  # 到达第一行
            while m > 0:
                path.append([0, m-1])
                m -= 1
        elif n > 0:  # 到达第一列
            while n > 0:
                path.append([n-1, 0])
                n -= 1


def test_robot_collect_coins():
    coins = [(1, 1), (0, 4), (1, 3), (2, 3), (2, 5), (3, 2), (3, 5), (4, 0), (4, 4)]
    solution = RobotCoinCollect()
    path = []
    print(solution.robot_coin_collect(5, 6, coins, path))
    print(path)


class MFKnapsack(object):
    
    def __init__(self, weights: list, values: list):
        self.weights = weights
        self.values = values
        self.cache = {}

    def mfk_napsack(self, i, j):
        key = tuple([i, j])
        if i == 0 and j >= 0 or i >=0 and j == 0:
            self.cache[key] = 0
            return 0

        if key in self.cache:
            return self.cache[key]
        if self.weights[i-1] > j:
            self.cache[key] = self.mfk_napsack(i-1, j)

        else:
            self.cache[key] = max(self.mfk_napsack(i-1, j),
                                     self.mfk_napsack(i-1, j - self.weights[i-1]) + self.values[i-1])
        return self.cache[key]



def test_mfk_napsack():
    weights = [2, 1, 3, 2]
    values = [12, 10, 20, 15]
    solution = MFKnapsack(weights, values)
    solution.mfk_napsack(4, 5)
    print(len(solution.cache), solution.cache)

if __name__ == '__main__':
    # test_min_levenshtein_distance()
    # test_max_cash_botom_top()
    # test_change_making()
    # test_robot_collect_coins()
    test_mfk_napsack()
