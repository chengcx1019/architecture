#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: uber_interview.py
@time: 2018/5/21 23:37
"""
"""
same pair of points in a opposite direction
same direction and a pair of points change the position
这题自然要想到有向图，构造一个适合于问题的图节点表示，从而在遍历每一组中条件时不断确认新加入的边是否和已有的规则相冲突，
所谓的冲突就是上面分析的两类,但这又不是传统的图，因为把节点间的传递关系都在每个节点的邻居节点间表现出来了。
"""

N = 0
E = 1
S = 2
W = 3
DIRS = [N, E, S, W]
char_to_direction = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}


def opposite_dir_num(dir):
    return (dir + 2) % 4


class Node(object):
    
    def __init__(self, val):
        self.val = val
        self.edges = []
        for i in range(4):
            self.edges.append(set())


def is_valid(from_node: Node, to_node: Node, new_direction):
    opposite_dir = opposite_dir_num(new_direction)
    if to_node in from_node.edges[opposite_dir]:
        return False
    return True


def add_edgs(from_node: Node, to_node: Node, new_direction):
    opposite_dir = opposite_dir_num(new_direction)
    from_node.edges[new_direction].add(to_node)
    to_node.edges[opposite_dir].add(from_node)

    for dir in DIRS:
        if dir == new_direction:  # 如果位置关系是某一节点同侧则这些节点间的位置关系是模糊的
            continue
        for neighbor in from_node.edges[dir]:
            if neighbor == to_node:
                continue
            neighbor.edges[new_direction].add(to_node)
            to_node.edges[opposite_dir].add(neighbor)
    for dir in DIRS:
        if dir == opposite_dir:
            continue
        for neighbor in to_node.edges[dir]:
            if neighbor == from_node:
                continue
            neighbor.edges[opposite_dir].add(from_node)
            from_node.edges[new_direction].add(neighbor)


def validate(rules):  # a list of string which contain 3 eles seperated by space
    rule_nodes = dict()
    for line in rules:
        rule = line.split(' ')
        print("rule ", rule[0], " ", rule[1], " ", rule[2])
        from_char = rule[2]
        to_char = rule[0]

        if from_char not in rule_nodes.keys():
            rule_nodes[from_char] = Node(from_char)
        if to_char not in rule_nodes.keys():
            rule_nodes[to_char] = Node(to_char)

        from_node = rule_nodes.get(from_char)
        to_node = rule_nodes.get(to_char)

        for direction in rule[1]:
            try:
                dir_num = char_to_direction.get(direction)
            except:
                print("unvalid direction symbol")
                return False
            if not is_valid(from_node, to_node, dir_num):
                return False
            add_edgs(from_node, to_node, dir_num)

    return True


        
    


if __name__ == '__main__':
    pass