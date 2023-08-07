#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import List, Union
from DataTypes.Action import Action
from DataTypes.Heuristic import Heuristic
from DataTypes.Solution import Solution
from DataTypes.State import State


class SearchStrategy(object):

    TREE_BASED_SEARCH: bool

    def __init__(self, tree_based_search: bool) -> None:
        super().__init__()
        self.TREE_BASED_SEARCH = tree_based_search

    def search(self, initial_state: State, actions: List[Action], heuristic: Union[Heuristic, None], goals: List[State]) -> Solution:
        raise NotImplementedError(
            'ERROR: This method must be overridden by a concrete search strategy implementation')
