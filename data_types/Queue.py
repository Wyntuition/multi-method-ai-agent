'''Defines ScheduleContainer abstract class'''
from abc import ABC, abstractmethod

from schedule import Schedule


class Queue(ABC):
    '''Abstract class '''

    def __init__(self):
        self.queue = []

    @abstractmethod
    def pop(self):
        '''Gets the next Schedule'''

    @abstractmethod
    def put(self, schedule) -> None:
        '''Adds an element to the container'''

    def __len__(self) -> int:
        return len(self.queue)
