#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import List
from .Node import Node
from .State import State

class Solution(object):

   PATH: List[Node]
   VISITED: List[State]

   def __init__(self, goal_node: Node, visited_nodes: List[State]) -> None:
      super().__init__()
      self.PATH = []
      current_node = goal_node
      while current_node is not None:
         self.PATH.append(current_node)
         current_node = current_node.PARENT
      self.PATH.reverse()
      self.VISITED = visited_nodes

   def print_solution(self):
      print('Solution: ', end='')
      for node in self.PATH[:-1]:
         print('{} -> '.format(node.STATE), end='')
      print('{}'.format(self.PATH[-1].STATE))

   def print_visited_order(self):
      print('Visited Nodes: ', end='')
      for node in self.VISITED[:-1]:
         print('{} -> '.format(node), end='')
      print('{}'.format(self.VISITED[-1]))
