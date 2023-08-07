from typing import Tuple

from PriorityQueue import PriorityQueue
# from SearchStrategies.GreedyBestFirstSearch import GreedyBestFirstSearch
from DataTypes.State import State
from DataTypes.Action import Action
import csv


def country_scheduler(your_country_name: str, resources_filename: str, initial_state_filename: str,
                      output_filename: str, num_output_schedulers: int, depth_bound: int,
                      max_frontier_size: int) -> None:
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
            if row[0] == your_country_name:
                start_state = State(row[1:], resources)
                break

    # TODO - make generic
    # Define actions
    actions = [

        Action('increase_renewable_energy', 0.1),
        Action('decrease_renewable_energy', -0.1),
        Action('increase_fossil_fuel_use', 0.1),
        Action('decrease_fossil_fuel_use', -0.1),
        Action('do_nothing', 0)
    ]

    # Define utility function
    # TODO
    # def utility_fn(state: State) -> float:
    #     return state.get_utility()

    # Define frontier
    # TODO - use my own
    frontier = PriorityQueue(maxsize=max_frontier_size)
    frontier.put((0, start_state))

    # Define search strategy
    # TODO - use my own, what when where?
    search_strategy = None

    # Search for optimal schedule
    solution = search_strategy.search(
        start_state, actions, depth_bound, max_frontier_size)

    # Write output to file
    with open(output_filename, 'w') as f:
        writer = csv.writer(f)
        for i in range(num_output_schedulers):
            writer.writerow(solution.get_schedule(i))
