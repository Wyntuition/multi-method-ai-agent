from DataTypes.Schedule import Schedule
from DataTypes.Queue import Queue


class PriorityQueue(Queue):
    '''A simple priority - elements sorted by score'''

    def pop(self) -> Schedule:
        '''Returns the element with the highest score'''
        return self.queue.pop(0)

    def put(self, schedule: Schedule) -> None:
        '''Adds an element to the queue and sorts it'''
        self.queue.append(schedule)
        # self.queue.sort(key=lambda x: x.score) TODO
