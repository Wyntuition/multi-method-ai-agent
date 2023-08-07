#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import Callable, List
from .State import State


class Action(object):

    steps: List[Callable[[State], State]]
    next_state: State
    action_cost: float
    preconditions: List[Callable[[State], bool]]

    def __init__(self, preconditions: List[Callable[[State], bool]], cost: float, result: State) -> None:
        super().__init__()
        self.next_state = result
        self.action_cost = cost
        self.preconditions = preconditions

    def apply(self, to_state: State) -> State:
        return self.next_state if all([precondition(to_state) for precondition in self.preconditions]) else None


# TODO remove if not needed
