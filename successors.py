from parse_files import ParseFiles
import os
from random import choice, randint, random
from data_types.Transfer import Transfer
from data_types.Transform import Transform


class RandomSuccessorFunction:
    def __init__(self, self_country):
        self.self_country = self_country
        self.actions = []

        self.COUNTRIES = ['Dinotopia', 'Atlantis',
                          'Brodingnang', 'Carpania', 'Erewhon']
        self.RESOURCE_LIST = ParseFiles.parse_resource_list()

    def generate_random_schedule(self, size):
        for i in range(size):
            self._generate_random_action(self.self_country)
        return self.actions

    def _generate_random_action(self, country):
        if random() < 0.5:
            self._generate_transfer()
        else:
            self._load_random_transform_template(country)

    def _generate_transfer(self):
        # Generate a random transfer
        from_country = choice(self.COUNTRIES)
        to_country = choice(
            [c for c in self.COUNTRIES if c != from_country])
        resource = choice(self.RESOURCE_LIST)
        amount = randint(1, 20)
        transfer = Transfer(from_country, to_country, resource, amount)
        self.actions.append(transfer)

    def _load_random_transform_template(self, country):
        template_dir = "transformation-templates"
        filenames = [f for f in os.listdir(
            template_dir) if os.path.isfile(os.path.join(template_dir, f))]
        if filenames:
            filename = choice(filenames)
            transform = Transform("", [], [])
            transform.parse_transformations_by_nested_parens(
                filename, country)
            self.actions.append(transform)
