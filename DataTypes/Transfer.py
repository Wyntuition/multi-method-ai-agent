class Transfer:
    def __init__(self, country1, country2, item):
        self.country1 = country1
        self.country2 = country2
        self.item = item

    def __str__(self):
        return f"(TRANSFER {self.country1} {self.country2} (({self.item})))"
