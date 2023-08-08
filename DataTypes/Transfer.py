class Transfer:
    def __init__(self, country1, country2, resource, amount):
        self.country1 = country1
        self.country2 = country2
        self.resource = resource
        self.amount = amount

    def __str__(self):
        return f"(TRANSFER {self.country1} {self.country2} (({self.resource} {self.amount})))"
