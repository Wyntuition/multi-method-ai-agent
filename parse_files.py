
# read a file and return the result as a list
import csv
import os

from country_state import CountryState

directory_path = os.path.dirname(os.path.abspath(__file__)) + "/"
template_path = directory_path + "transformation-templates/"
csv_path = directory_path + "csv/"


class ParseFiles():

    def parse_transform_file(file_path):
        with open(os.path.join(template_path, file_path), "r") as file:
            return file.read()

    def parse_resource_list():
        resource_list = []
        with open(csv_path + 'resource-weights.csv', "r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                resource_list.append(row[0])
        return resource_list

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
    def parse_csv(file_path) -> list[CountryState]:
        world_state = []
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                state = CountryState(*row)
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
