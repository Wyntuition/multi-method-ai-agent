from queue import PriorityQueue


def best_first_search(initial_state, successor_fn,
                      depth_bound, max_frontier_size):
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

    # Search for optimal schedule
    while not frontier.empty():
        # Check max frontier size
        if frontier.qsize() > max_frontier_size:
            return None

        # Get the next state
        current_state = frontier.get()[1]

        # Check if the current state is the goal state
        # if goal_test_fn(current_state):
        #     return current_state

        # Add current state to explored set
        explored.append(current_state)

        # Generate successors
        successors = successor_fn()

        # TODO: expected utility
        # Add successors to frontier
        for successor in successors:
            if successor not in explored:
                # frontier.put((utility_fn(successor), successor))
                frontier.put(successor)

    return None
