#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations
from typing import Callable
from .State import State

class Heuristic(object):

   EVALUATION: Callable[[State], float]

   def __init__(self, evaluation_function: Callable[[State], float]) -> None:
      super().__init__()
      self.EVALUATION = evaluation_function

   def apply(self, to_state: State) -> float:
      return self.EVALUATION(to_state)
