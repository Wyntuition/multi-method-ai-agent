import os
from typing import Tuple

from PriorityQueue import PriorityQueue
from DataTypes.Schedule import Schedule
from DataTypes.Transform import Transform
from parse_files import ParseFiles
from DataTypes.State import State
from DataTypes.Action import Action
import csv


def country_scheduler(self_country_name: str, resources_filename: str, initial_state_filename: str,
                      output_filename: str, num_output_schedulers: int, depth_bound: int,
                      max_frontier_size: int) -> None:

    self_country = self_country_name

    ######################################
    # Get start state
    ######################################
    # TODO1
    start_state = ParseFiles.parse_world_state()

    ######################################
    # Generate a schedule
    ######################################
    # TODO - how do I get the AI to start choosing actions based on EU results?
    schedule = Schedule(self_country)
    schedule = schedule.generate_random_schedule(10, resources_filename)

    # Gather transforms to run
    # transform = Transform(self_country)
    # transform.parse_transformations_by_nested_parens(
    #     'transformation-templates/')

    ######################################
    # Search through priority queue for optimal schedules, checking bounds
    ######################################

    # calculate schedule EU

    # # generate successor by adding new random schedule

    # Define utility function
    # TODO
    # def utility_fn(state: State) -> float:
    #     return state.get_utility()

    # Define frontier and put initial schedule in
    # TODO - use my own
    frontier = PriorityQueue(maxsize=max_frontier_size)
    frontier.put((0, schedule))

    # Define search strategy
    # TODO - use my own, what when where?
    search_strategy = None

    # Search for optimal schedule
    solution = search_strategy.search(
        start_state, schedule.ac, depth_bound, max_frontier_size)

    ######################################
    # write schedule to file
    ######################################
    with open(output_filename, 'w') as f:
        writer = csv.writer(f)
        for i in range(num_output_schedulers):
            writer.writerow(solution.get_schedule(i))
    # for filename in os.listdir('transformation-templates', 'r'):
    #     template_path = os.path.join(templates_path, filename)
    #     with open(template_path, 'r') as file:
    #         contents = file.read().strip()
    #         transform = Transform(template_path, self.logger)
    #         actions.append(transform_action)

    # Load resources from file
    resources = {}
    with open(resources_filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            resources[row[0]] = float(row[1])

    # Load initial state from file
    start_state = None
    with open(initial_state_filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == self_country_name:
                start_state = State(row[1:], resources)
                break


# schedule final output should be in this format, with EU of each state, and EU of the whole schedule
# [ (TRANSFORM self ...) EU: S_1
#   (TRANSFER self C2 ((Housing 3))) EU: S_2
#   ...
#   (TRANSFORM self ...) EU: S_N
# ]
