from schedule import Schedule
from queue import Queue


class PriorityQueue(Queue):

    def pop(self):
        return self.queue.pop(0)

    def put(self, schedule: Schedule):
        self.queue.append(schedule)
