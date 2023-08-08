# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

# from __future__ import annotations
# from typing import List, Union
# from DataTypes import Action, Heuristic, Node, Solution, State
# from SearchStrategies import SearchStrategy
# from PriorityQueue import PriorityQueue


# class GreedyBestFirstSearch(SearchStrategy):

#     def __init__(self, tree_based_search: bool) -> None:
#         super().__init__(tree_based_search)

#     def _expand(self, actions: List[Action], node: Node) -> List[Node]:
#         nodes: List[Node] = []
#         for action in actions:
#             next_state = action.apply(node.STATE)
#             if next_state is not None:
#                 nodes.append(Node(next_state, node, action,
#                              node.PATH_COST + action.ACTION_COST))
#         return nodes

#     def search_with_reached(self, initial_state: State, actions: List[Action], heuristic: Union[Heuristic, None], goals: List[State]) -> Solution:
#         visited = []
#         node = Node(initial_state, None, None, 0.0)
#         frontier = PriorityQueue(
#             lambda node: heuristic.apply(node.STATE), True).add(node)
#         reached = {node.STATE: node}
#         while not frontier.is_empty():
#             node = frontier.pop()
#             visited.append(node.STATE)
#             if node.STATE in goals:
#                 return Solution(node, visited)
#             for child in self._expand(actions, node):
#                 if child.STATE not in reached or child.PATH_COST < reached[child.STATE].PATH_COST:
#                     reached[child.STATE] = child
#                     frontier.add(child)
#         return Solution(None)

#     def search_without_reached(self, initial_state: State, actions: List[Action], heuristic: Union[Heuristic, None], goals: List[State]) -> Solution:
#         visited = []
#         node = Node(initial_state, None, None, 0.0)
#         frontier = PriorityQueue(
#             lambda node: heuristic.apply(node.STATE), True).add(node)
#         while not frontier.is_empty():
#             node = frontier.pop()
#             visited.append(node.STATE)
#             if node.STATE in goals:
#                 return Solution(node, visited)
#             for child in self._expand(actions, node):
#                 frontier.add(child)
#         return Solution(None)

#     def search(self, initial_state: State, actions: List[Action], heuristic: Union[Heuristic, None], goals: List[State]) -> Solution:
#         search_function = self.search_without_reached if self.TREE_BASED_SEARCH else self.search_with_reached
#         return search_function(initial_state, actions, heuristic, goals)
