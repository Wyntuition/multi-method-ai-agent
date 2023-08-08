from parse_files import ParseFiles
import os
from random import choice, randint, random
from DataTypes.Transfer import Transfer
from DataTypes.Transform import Transform


class RandomSuccessorFunction:
    def __init__(self, self_country):
        self.self_country = self_country

        self.COUNTRIES = ['Dinotopia', 'Atlantis',
                          'Brodingnang', 'Carpania', 'Erewhon']
        self.RESOURCE_LIST = ParseFiles.parse_resource_list()

    def generate_random_schedule(self, size):
        actions = []
        for i in range(size):
            actions.append(
                self._generate_random_action(self.self_country))
        return actions

    def _generate_random_action(self, country):
        actions = []
        if random() < 0.5:
            # Generate a random transfer
            from_country = choice(self.COUNTRIES)
            to_country = choice(
                [c for c in self.COUNTRIES if c != from_country])
            resource = choice(self.RESOURCE_LIST)
            amount = randint(1, 50)
            transfer = Transfer(from_country, to_country, resource, amount)
            actions.append(transfer)
        else:
            self._load_random_transform_template(country)
            # # Generate a random transform
            # inputs = []
            # outputs = []
            # for j in range(randint(1, 3)):

            #     input_resource = choice(resources)

            #     input_amount = randint(1, 50)
            #     inputs.append((input_resource, input_amount))
            # for j in range(randint(1, 3)):
            #     output_resource = choice(resources)

            #     output_amount = randint(1, 50)
            #     outputs.append((output_resource, output_amount))
            # transfer = Transform(self.country, inputs, outputs)
            # self.actions.append(transfer)

    def _load_random_transform_template(self, country):
        actions = []
        template_dir = "transformation-templates"
        filenames = [f for f in os.listdir(
            template_dir) if os.path.isfile(os.path.join(template_dir, f))]
        if filenames:
            filename = choice(filenames)
            transform = Transform("", [], [])
            transform.parse_transformations_by_nested_parens(filename, country)
            actions.append(transform)
