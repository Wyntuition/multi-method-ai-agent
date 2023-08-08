class Transfer:
    def __init__(self, from_country, to_country, resource, amount):
        self.from_country = from_country
        self.to_country = to_country
        self.resource = resource
        self.amount = amount

    def __str__(self):
        return f"(TRANSFER {self.from_country} {self.to_country} (({self.resource} {self.amount})))"

    def __lt__(self, other):
        """
        Defines the < operator for the Transfer class.
        """
        # TODO
        if not isinstance(other, Transfer):
            return
        return self.amount < other.amount
