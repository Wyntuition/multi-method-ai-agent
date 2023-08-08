import csv


class CountryState:
    # def __str__(self):
    #     return f"Country: {self.country}\nPopulation: {self.population}\nAvailable Land: {self.available_land}\nMetallic Elements: {self.metallic_elements}\nTimber: {self.timber}\nMetallic Alloys: {self.metallic_alloys}\nPotential Fossil Energy: {self.potential_fossil_energy}\nPotential Renewable Energy: {self.potential_renewable_energy}\nElectronics: {self.electronics}\nHousing: {self.housing}"

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
