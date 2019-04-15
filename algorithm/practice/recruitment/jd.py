#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: jd.py
@time: 2018/9/10 21:52
"""
from basic.graph.graph import Graph


def similar(s, t):
    table = {}
    for i in range(len(t)):
        if (s[i] not in table and t[i] in table.values()) or (s[i] in table and t[i] != table[s[i]]) :
            return False
        elif s[i] not in table:
            table[s[i]] = t[i]
    print(s)
    return True


def solve(S, T):
    t_len = len(T)
    s_len = len(S)

    count = 0
    for i in range(s_len):
        if i + t_len <= s_len:
            current = S[i:i + t_len]

            if similar(current, T):
                count += 1
    return count


def test():
    s = 'ababcb'
    t = 'xyx'
    # s = 'abccdeefzzazff'
    # t = 'xyaa'
    print(solve(s, t))


"""
给定一张包含N个点、M条边的无向图，每条边连接两个不同的点，且任意两点间最多只有一条边。
对于这样的简单无向图，如果能将所有点划分成若干个集合，使得任意两个同一集合内的点之间没有边相连，
任意两个不同集合内的点之间有边相连，则称该图为完全多部图。现在你需要判断给定的图是否为完全多部图。


解题思路，核心的思路为不相关的顶点间必须有相同的邻接顶点，任意从某一节点开始，找到其邻接顶点，并判断剩下的节点是否有相同邻接顶点
"""


def is_edge_in_graph(edge, edges):
    for item in edges:
        if set(edge) == set(item):
            return True


def delete_edges(nodes: set, edges):
    new_edges = []
    for edge in edges:
        tag = True
        for node in nodes:
            if node in edge:
                tag = False
        if tag:
            new_edges.append(edge)
    return new_edges


def is_complete_graph(nodes: set, edges):
    if len(nodes) <= 1:
        return True
    curr = nodes.pop()
    curr_relate = set()
    for edge in edges:
        if curr in edge:
            edge_nodes = set(edge)
            edge_nodes.remove(curr)
            curr_relate.add(edge_nodes.pop())
    curr_unrelate = nodes - curr_relate
    for i in curr_unrelate:
        for j in curr_relate:
            if not is_edge_in_graph([i, j], edges):
                return False

    curr_unrelate.add(curr)
    new_edges = delete_edges(curr_unrelate, edges)
    return is_complete_graph(curr_relate, new_edges)


def main():
    """
    从控制台获取测试用例，示例见下方
    :return:
    """
    num = int(input())
    count = 0
    while count < num:
        n, m = tuple(map(int, input().split(' ')))
        nodes = set()
        edges = []
        for _ in range(m):
            edge = list(map(int, input().split(' ')))
            nodes.add(edge[0])
            nodes.add(edge[1])
            edges.append(edge)
        print(is_complete_graph(nodes, edges))
        count += 1
"""
控制台输入示例：第一行表示用例数，其后第一行是节点数和边数，之后是一组边，然后是新的节点数和边数及相应的一组边，依次类推
2
5 7
1 3
1 5
2 3
2 5
3 4
4 5
3 5（True）
4 3
1 2
2 3
3 4（False）
"""


def test_is_complete_graph():
    case = [[1, 3], [1, 5], [2, 3], [2, 5],
     [3, 4], [4, 5], [3, 5],
     [3, 6], [5, 6]]
    case = [[1, 2], [2, 3], [3, 4]]
    nodes = set()
    edges = []
    for edge in case:
        nodes.add(edge[0])
        nodes.add(edge[1])
        edges.append(edge)
    print(nodes)
    print(edges)
    print(is_complete_graph(nodes, edges))


def is_graph(nodes):
    if len(nodes) <= 1:
        return True
    source_temp = []
    temp = []
    curr = None
    for i in nodes:
        curr = i
        for key in nodes[i].adj_nodes:
            temp.append(key)
        break

    for node in nodes.values():
        if node.key == curr:
            continue
        if node.key not in temp:
            source_temp.append(node.key)
    if len(nodes) - 1 != len(source_temp) + len(temp):
        return False
    if len(temp) > 0:
        for key in source_temp:
            for item in temp:
                if item not in nodes[key].adj_nodes and key not in nodes[item].adj_nodes:
                    return False
    extra = {}

    for i in temp:
        delete_node = []
        for item in nodes[i].adj_nodes:
            if item not in temp:
                delete_node.append(item)
        for item in delete_node:
            del nodes[i].adj_nodes[item]
        extra[i] = nodes[i]

    return is_graph(extra)


def complete_multi_graph():

    count_num = int(input())
    count = 0
    while count < count_num:
        g = Graph()
        node_num, adjs_num = map(int, input().split(' '))
        for i in range(adjs_num):
            adj = list(map(int, input().split(' ')))
            g.add_edge(adj[0], adj[1])

    return is_graph(g)


if __name__ == '__main__':
    # test_cases = [[(1, 2), (2, 3), (3, 4)],
    #               [[1, 3], [1, 5], [2, 3], [2, 5],
    #               [3, 4], [4, 5], [3, 5],
    #                [3, 6], [5, 6]]]
    #
    # for case in test_cases:
    #     g = Graph()
    #     for edge in case:
    #         g.add_edge(edge[0], edge[1])
    #
    #     print(is_graph(g.nodes))
    # complete_multi_graph
    main()
