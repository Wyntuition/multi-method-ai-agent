from data_types.Transfer import Transfer
from data_types.Transform import Transform


class WorldState:
    def __init__(self, countries):
        self.world_state = countries

    def apply_schedule(self, schedule):
        for action in schedule:
            self.apply_action(action)
        return self.world_state

    def apply_action(self, action):
        if isinstance(action, Transfer):
            self.apply_transfer(action)
        elif isinstance(action, Transform):
            self.apply_transform(action)

    def apply_transfer(self, transfer):
        if transfer.from_country in self.world_state and transfer.to_country in self.world_state:
            from_country = self.world_state[transfer.from_country]
            to_country = self.world_state[transfer.to_country]

            if (transfer.resource in from_country) and (transfer.resource in to_country) and (int(from_country[transfer.resource]) > transfer.amount):
                amount = int(from_country[transfer.resource])
                amount -= transfer.amount
                from_country[transfer.resource] == amount
                self.world_state[transfer.from_country][transfer.resource] = amount

                amount = int(to_country[transfer.resource])
                amount += transfer.amount
                to_country[transfer.resource] == amount
                self.world_state[transfer.to_country][transfer.resource] = amount

    def apply_transform(self, transform):
        for input_resource, input_amount in transform.inputs:
            amount = int(self.world_state[transform.country][input_resource])
            if amount < int(input_amount):
                return
            else:
                amount -= int(input_amount)
                self.world_state[transform.country][input_resource] = amount
        for output_resource, output_amount in transform.outputs:
            amount = int(self.world_state[transform.country][output_resource])
            amount += int(output_amount)
            self.world_state[transform.country][output_resource] = amount
