import os
from random import random
from DataTypes.Transfer import Transfer
from pyparsing import nestedExpr


class Schedule:
    def __init__(self, self_country):
        self.country = self_country
        self.actions = []

        # TODO: pull from initial state file
        self.COUNTRIES = ['Dinotopia', 'Atlantis',
                          'Brodingnang', 'Carpania', 'Erewhon']
        self.RESOURCE_LIST = []

    def generate_random_schedule(self, size, resources_filename):
        # Get list of resources
        with open('resource-weights.csv', newline='') as csv:
            reader = csv.DictReader(csv)
            for row in reader:
                self.RESOURCE_LIST = row['Resource']

        for i in range(size):
            self.actions.append(self._generate_random_transfer())
            self.actions.append(
                self._load_random_transform_template(self.country))

    def _generate_random_transfer(self, resources: dict):

        # todo: generate successor?

        if random.random() < 0.5:
            # Generate a random transfer
            from_country = random.choice(self.COUNTRIES)
            to_country = random.choice(
                [c for c in self.COUNTRIES if c != from_country])
            resource = random.choice(resources)
            amount = random.randint(1, 50)
            transfer = Transfer(from_country, to_country, resource, amount)
            self.actions.append(transfer)
        else:
            # Generate a random transform
            inputs = []
            outputs = []
            for j in range(random.randint(1, 3)):

                input_resource = random.choice(resources)

                input_amount = random.randint(1, 50)
                inputs.append((input_resource, input_amount))
            for j in range(random.randint(1, 3)):
                output_resource = random.choice(resources)

                output_amount = random.randint(1, 50)
                outputs.append((output_resource, output_amount))
            transform = Transform(self.country, inputs, outputs)
            self.actions.append(transform)

    def _load_random_transform_template(self, country):
        template_dir = "transformation-templates"
        filenames = os.listdir(template_dir)
        if filenames:
            filename = random.choice(filenames)
            with open(os.path.join(template_dir, filename), "r") as file:
                template_str = file.read()
                template = nestedExpr().parseString(template_str).asList()[0]
                transform_name = template[0]
                inputs = [(item[0], int(item[1])) for item in template[1]]
                outputs = [(item[0], int(item[1])) for item in template[2]]
                self.transform_templates[transform_name] = (inputs, outputs)


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
