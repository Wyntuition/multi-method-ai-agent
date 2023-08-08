import os
from country_scheduler import country_scheduler
from parse_files import ParseFiles

directory_path = os.path.dirname(os.path.abspath(__file__)) + "/"

csv_path = directory_path + 'csv/'
world_state = ParseFiles.parse_csv_dict(
    csv_path + 'initial-world-state.csv')


# run country scheduler
your_country_name = "Dinotopia"
resources_filename = "resources.csv"
initial_state_filename = "initial_world_state.csv"
output_filename = "output.csv"
num_output_schedulers = 10
depth_bound = 5
max_frontier_size = 100

country_scheduler(your_country_name, world_state, output_filename,
                  num_output_schedulers, depth_bound, max_frontier_size)
