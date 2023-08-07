#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import Callable, List
from .State import State

class Action(object):

   NEXT_STATE: State
   ACTION_COST: float
   PRECONDITIONS: List[Callable[[State], bool]]

   def __init__(self, preconditions: List[Callable[[State], bool]], cost: float, result: State) -> None:
      super().__init__()
      self.NEXT_STATE = result
      self.ACTION_COST = cost
      self.PRECONDITIONS = preconditions

   def apply(self, to_state: State) -> State:
      return self.NEXT_STATE if all([precondition(to_state) for precondition in self.PRECONDITIONS]) else None
