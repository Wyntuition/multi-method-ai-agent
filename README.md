# Project - Part 1 

Workflow for running transformations and transfers, calculating Expected Utility, which is the foundation for the rest of the agent work. 

## Running 

Run `pip3 install && python3 run.py`

## Workflow 

Start with `run.py` as it is the entrypoint to the agent running. You can see it parsing the resource CSV files, world states, calling classes to process transformation templates and making the calculations for the Expected Utility. 

## Calculations: State Quality, Discounted Rewards, Success Probabilities

Calculations are implemented in the class `ExpectedUtility`, and called in the right sequence to determine the Expected Utility, in the `run.py` file.

## Classes to represent State, Action Templates, Actions 

- See `Schedule.py`, `State.py` and run.py is the current agent parsing templates and CSV files, and running them concretely

## Resources, Weights, Initial World State

Resources
- `resource-weights.csv` - defines resource weights 
- `resource-proportional.csv` - is to define the proportion of resource each person gets

Initial World States
- `initial-world-state.csv` - default world state
- `initial-world-state--same-resources.csv` - default world state
- `initial-world-state--energy.csv` - world state where a lot of potential energy is handed out to see how that affects things 

