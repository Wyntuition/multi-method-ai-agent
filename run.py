import csv
import os
from DataTypes.Schedule import Schedule
from DataTypes.State import State
from parse_files import ParseFiles
from ExpectedUtility import ExpectedUtility
# from country_scheduler import country_scheduler

directory_path = os.path.dirname(os.path.abspath(__file__)) + "/"


def change_state(country_world_state, schedule):
    # Add/remove the items from the state
    for item in schedule.inputs:
        # print(f"Removing {item[1]} {item[0]} to {country_world_state[item[0]]}")
        country_world_state[item[0]] = float(
            country_world_state[item[0]]) - float(item[1])
    for item in schedule.outputs:
        # print(f"Adding {item[1]} {item[0]} to {country_world_state[item[0]]}")
        country_world_state[item[0]] = float(
            country_world_state[item[0]]) + float(item[1])

# Transfer to another country


def transfer_operation(self_country, other_country, schedule):
    # Add/remove the items from the state
    for item in schedule.inputs:
        self_country[item[0]] = float(
            country_world_state[item[0]]) - float(item[1])
    for item in schedule.outputs:
        other_country[item[0]] = float(
            country_world_state[item[0]]) + float(item[1])


###############################
# PARSE CSV FILES
###############################

# Parse world state
csv_path = directory_path + 'csv/'
world_state = ParseFiles.parse_csv_dict(
    csv_path + 'initial-world-state.csv')

# Parse resource weights
resource_weights = {}
with open(csv_path + "resource-weights.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        resource_weights[row[0]] = float(row[1])
print(resource_weights)

# Parse resource proportions
resource_proportions = {}
with open(csv_path + "resource-proportions.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        resource_proportions[row[0]] = float(row[1])
print(resource_weights)

###############################
# # CALCULATE EXPECTED UTILITY
###############################

# Calculate starting EU for a country
self_country = "Dinotopia"
country_world_state = world_state[self_country]
self_state_quality_start = ExpectedUtility.state_quality_for_country(
    country_world_state, resource_weights, resource_proportions)
print(f"Country's state before transform: {country_world_state}")

# TODO - Transform the world state to recalculate the state quality

# TODO - Check prerequisites that the country has the resources to perform the transformation

# Get all files in the template+path directory
template_path = directory_path + "transformation-templates/"

# for file_name in os.listdir(template_path):
# schedule_path = template_path + file_name

# TODO-1 - randomly generate a schedule from templates/


csv_path = template_path + "alloys.txt"
schedule = Schedule()
# Parse Transformation template
schedule.parse_transformations_by_nested_parens(csv_path)

change_state(country_world_state, schedule)

self_state_quality_end = ExpectedUtility.state_quality_for_country(
    country_world_state, resource_weights, resource_proportions)
print(f"Starting State Quality: {self_state_quality_start}")
print(f"Country's state after transform: {country_world_state}")
print(f"Ending State Quality: {self_state_quality_end}")

# Calculate Discounted Reward

# Test - calculate Discounted Reward - should be -0.03125
q_start = self_state_quality_start
q_end = self_state_quality_end
gamma = 0.5
n = 5  # steps to get into state

discounted_reward = ExpectedUtility.discounted_reward(gamma, n, q_end, q_start)
print(f"Discounted Reward for {self_country}: {discounted_reward}")

# Probability of schedule acceptance
# Equation: we will use the product of the probabilities of the individual P(ci,sj) value
#   - The probability that a country, ci, will agree to a schedule, sj, is computed by the logistic function where x corresponds to DR(ci, sj ) and L = 1, and you can experiment with different values of x0 and k (but use x0 = 0 and k = 1 as starting points)
# TODO: Think about and report on how different parameter settings might reflect biases in the real world (e.g., a reason for shifting x0 might be to reflect opportunity costs — what other benefits might await a patient country?).
# Note that the strategy for estimating the probability that a schedule is accepted (i.e., will be accepted by all parties to the schedule) and succeeds, does not come from statistics accu- mulated over data from the “real world” (to include game play) as we might think is ideal, but our method draws from an information theoretic tradition of estimating probabilities of “events” from the “descriptions” of those events. An assumption in this description- driven methodology is a bias that more “complicated” descriptions represent lower proba- bility events. It is a quantification of Occam’s razor. This is the one way (probably the only way given the time constraints of this class) that the AI agent for your country will take into account the State Qualities of other countries, as well as your own. It has the effect of countering ill-considered greed.

# todo - move rest to classes so easier. Gather participating countries from schedule, or check if SQ changed (Live 8 3:00)
participating_countries = ["Dinotopia", "Atlantis"]
sigmoid_midpoint = 1  # todo is this right?
x0 = discounted_reward - sigmoid_midpoint

# TODO - mess with gamma
k = 1
L = 1


# TODO-1
# Probability of country's acceptance of a schedule
p = ExpectedUtility.logistic_function(x0)

# Multiply them for overall schedule acceptance - TODO - this needs rework for multiple countries that will come with other pieces changing for the same reason
for country in participating_countries:
    p += p * ExpectedUtility.logistic_function(x0)
print(f"Probability of schedule acceptance: {p}")

# Expected Utility calculation
c = 0.1
eu = ExpectedUtility.expected_utility(p, discounted_reward, c)
print(f"Expected Utility: {eu}")


# run country scheduler
your_country_name = "Dinotopia"
resources_filename = "resources.csv"
initial_state_filename = "initial_world_state.csv"
output_filename = "output.csv"
num_output_schedulers = 10
depth_bound = 5
max_frontier_size = 100

# country_scheduler(your_country_name, resources_filename, initial_state_filename,
#                   output_filename, num_output_schedulers, depth_bound, max_frontier_size)