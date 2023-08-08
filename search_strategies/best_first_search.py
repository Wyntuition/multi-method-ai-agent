from data_types.Schedule import Schedule
from priority_queue import PriorityQueue

from parse_files import ParseFiles
from score_schedule import score_schedule


class BestFirstSearch:
    def __init__(self):
        self.best_schedules = []

    def search(self, self_country, initial_state, successor_fn,
               depth_bound, max_frontier_size, max_best_schedules):
        """ 
        - priority queue to store the nodes in frontier
          sorted by their utility value. 
        - successors are added to the frontier 
        - The algorithm terminates when the
          frontier exceeds the maximum size.
        """
        initial_schedule = successor_fn()
        frontier = PriorityQueue()
        frontier.put((0, initial_schedule))
        explored = []
        depth = 0

        resource_weights = ParseFiles.parse_resources_weights()
        resource_proportions = ParseFiles.parse_resources_proportions()

        # Search for optimal schedule
        while len(frontier) > 0:
            # Check max frontier size
            if len(frontier) > max_frontier_size:
                return None

            # Get the next state
            schedule = frontier.pop()

            expected_utility = score_schedule(schedule, self_country,
                                              initial_state, resource_weights, resource_proportions)

            if len(self.best_schedules) < max_best_schedules:
                self.best_schedules.append(
                    Schedule(expected_utility, schedule))
            else:
                for i in range(len(self.best_schedules)):
                    if expected_utility > self.best_schedules[i].score:
                        self.best_schedules[i] = Schedule(
                            expected_utility, schedule)

            # Add current state to explored set
            explored.append(schedule)

            # Generate successors
            if depth < depth_bound:
                successors = successor_fn()
                depth += 1

            # Add successors to frontier
            for successor in successors:
                if successor not in explored:
                    frontier.put(successor)

        return None
