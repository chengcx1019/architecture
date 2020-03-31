#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin.cheng
@mail: chengcx1019@gmail.com
@time: 2020-03-31 09:23
"""
from basic.graph.graph import State
from basic.graph.graph_dfs import GraphDfs

"""
暂未进行有向无环图的校验
"""
class DAGTopSort(GraphDfs):

	def __init__(self):
		super(DAGTopSort, self).__init__()
		self.top_sort = []

	def make_top_sort(self, current_node):
		current_node.visit_state = State.visiting
		self.count += 1  # 开始访问顶点及顶点访问结束均需要累加计数器
		self.discovered[current_node.key] = self.count
		for node in current_node.adj_nodes.values():
			if node.visit_state == State.unvisited:  # 如果顶点是不是white，那么当前顶点就会知道该邻接顶点已被或正在被访问
				self.pred[node.key] = current_node.key
				self.make_top_sort(node)
		current_node.visit_state = State.visited
		self.top_sort.append(current_node.key)
		self.count += 1  # 开始访问顶点及顶点访问结束均需要累加计数器
		self.finished[current_node.key] = self.count


if __name__ == '__main__':
    pass
