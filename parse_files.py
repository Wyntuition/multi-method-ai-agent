
# read a file and return the result as a list
import csv

from DataTypes.State import State


class ParseFiles:

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


def read_file(filename) -> list:
    with open(filename, 'r') as file:
        return file.read().splitlines()
