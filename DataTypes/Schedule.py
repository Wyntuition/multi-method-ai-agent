import os
from random import choice, randint, random
from DataTypes.Transfer import Transfer
from DataTypes.Transform import Transform
from pyparsing import nestedExpr


class Schedule:
    def __init__(self, self_country):
        self.country = self_country
        self.actions = []
        self.score = 0.0


#######
# TODO: clean when definitely not going to use

# def read_schedule_from_file(file_path):
#     schedule_inputs = {}
#     schedule_outputs = {}

#     with open(file_path, "r") as file:
#         section = ""
#         for line in file:
#             line = line.strip()
#             if line == "":
#                 continue
#             if line.startswith("(TRANSFORM"):
#                 country = line.split()[11]
#             if line.startswith("(INPUTS"):
#                 section = "inputs"
#             elif line.startswith("(OUTPUTS"):
#                 section = "outputs"
#             else:
#                 key, value = line[1:-1].split()
#                 if section == "inputs":


#                     schedule_inputs[key] = int(value)
#                 elif section == "outputs":
#                     schedule_outputs[key] = int(value)

#     return Schedule(schedule_inputs, schedule_outputs)
