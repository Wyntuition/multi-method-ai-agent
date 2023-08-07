import csv


class State:
    # def __init__(self, country, population, available_land, metallic_elements, timber, metallic_alloys, potential_fossil_energy, potential_renewable_energy, electronics, housing):
    #     self.country = country
    #     self.population = int(population)
    #     self.available_land = int(available_land)
    #     self.metallic_elements = int(metallic_elements)
    #     self.timber = int(timber)
    #     self.metallic_alloys = int(metallic_alloys)
    #     self.potential_fossil_energy = int(potential_fossil_energy)
    #     self.potential_renewable_energy = int(potential_renewable_energy)
    #     self.electronics = int(electronics)
    #     self.housing = int(housing)

    # def __str__(self):
    #     return f"Country: {self.country}\nPopulation: {self.population}\nAvailable Land: {self.available_land}\nMetallic Elements: {self.metallic_elements}\nTimber: {self.timber}\nMetallic Alloys: {self.metallic_alloys}\nPotential Fossil Energy: {self.potential_fossil_energy}\nPotential Renewable Energy: {self.potential_renewable_energy}\nElectronics: {self.electronics}\nHousing: {self.housing}"

    def __init__(self, country, resources):
        self.country = country
        self.resources = resources

    def __str__(self):
        return f"Country: {self.country}\nResources: {self.resources}"
