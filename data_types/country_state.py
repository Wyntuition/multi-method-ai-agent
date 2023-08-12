class CountryState:

    def __init__(self, country, resources):
        self.country = country
        self.resources = resources

    def __str__(self):
        return f"Country: {self.country}\nResources: {self.resources}"

    def get_resource_amount(self, resource):
        return self.resources[resource]

    def increment_resource_amount(self, resource, amount):
        self.resources[resource] += amount

    def decrement_resource_amount(self, resource, amount):
        self.resources[resource] -= amount
