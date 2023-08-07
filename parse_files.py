
# read a file and return the result as a list
import csv
import os

from DataTypes.State import State

directory_path = os.path.dirname(os.path.abspath(__file__)) + "/"
template_path = directory_path + "transformation-templates/"
csv_path = directory_path + "csv/"


class ParseFiles():

    @staticmethod
    def parse_world_state():
        # Parse world state
        csv_path = directory_path + 'csv/'
        return ParseFiles.parse_csv_dict(
            csv_path + 'initial-world-state.csv')

    @staticmethod
    def parse_resources_weights():
        resource_weights = {}
        with open(csv_path + "resource-weights.csv", "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                resource_weights[row[0]] = float(row[1])
        print(resource_weights)
        return resource_weights

    @staticmethod
    def parse_resources_proportions():
        resource_proportions = {}
        with open(csv_path + "resource-proportions.csv", "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                resource_proportions[row[0]] = float(row[1])
        print(resource_proportions)
        return resource_proportions

    # Parse world state csv files
    @staticmethod
    def parse_csv(file_path) -> list[State]:
        world_state = []
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                state = State(*row)
                world_state.append(state)
        return world_state

    @staticmethod
    def parse_csv_dict(file_path):
        world_state = {}
        with open(file_path, "r") as file:
            csv_reader = csv.DictReader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                key = row['Country']
                world_state[key] = row
        return world_state
