from __future__ import annotations
from typing import List, Union
from ..DataTypes import Action, Heuristic, Node, PriorityQueue, Solution, State
from .SearchStrategy import SearchStrategy


class HeuristicDepthFirstSearch(SearchStrategy):

    def __init__(self, tree_based_search: bool) -> None:
        super().__init__(tree_based_search)

    def _expand(self, actions: List[Action], heuristic: Heuristic, node: Node) -> List[Node]:
        nodes = PriorityQueue(lambda node: heuristic.apply(node.STATE), False)
        for action in actions:
            next_state = action.apply(node.STATE)
            if next_state is not None:
                nodes.add(Node(next_state, node, action,
                          node.PATH_COST + action.ACTION_COST))
        return nodes.as_list()

    def search_with_reached(self, initial_state: State, actions: List[Action], heuristic: Heuristic, goals: List[State]) -> Solution:
        visited = []
        node = Node(initial_state, None, None, 0.0)
        frontier = [node]
        reached = [node.STATE]
        while len(frontier):
            node = frontier.pop()
            visited.append(node.STATE)
            if node.STATE in goals:
                return Solution(node, visited)
            for child in self._expand(actions, heuristic, node):
                if child.STATE not in reached:
                    reached.append(child.STATE)
                    frontier.append(child)
        return Solution(None)

    def search_without_reached(self, initial_state: State, actions: List[Action], heuristic: Heuristic, goals: List[State]) -> Solution:
        visited = []
        frontier = [Node(initial_state, None, None, 0.0)]
        while len(frontier):
            node = frontier.pop()
            visited.append(node.STATE)
            if node.STATE in goals:
                return Solution(node, visited)
            for child in self._expand(actions, heuristic, node):
                frontier.append(child)
        return Solution(None)

    def search(self, initial_state: State, actions: List[Action], heuristic: Heuristic, goals: List[State]) -> Solution:
        search_function = self.search_without_reached if self.TREE_BASED_SEARCH else self.search_with_reached
        return search_function(initial_state, actions, heuristic, goals)
