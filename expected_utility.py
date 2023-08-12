import math


class ExpectedUtility:
    '''
    State quality function:
    - substantially dependent on countries resources
    - in our world, we have land, and potential fossil and renewable energy so we can model how impactful these things are in the state function
    - One way: weighted sum of resource factors (wRi * cRi * ARi/AP population)
        - wRi * cRi * ARi/AP population - land, fossil energy, renewable energy
    - Backed up by factors: 
        - https://tradingeconomics.com/indicators

    INPUTS: state, schedule, resource weights

    Psudocode:
    for each country:
        for each resource:
            resource weight = get resource weight from resource-weights.csv
            calculate state quality:
                state quality = wRi * cRi * ARi / A_Population, where
                    - wRi = resource weight
                    - cRi = proportion constant 
                    - ARi = resource amount
                    - A_Population = population of country                
    '''

    @staticmethod
    def apply_schedule(world_state, schedule):
        world_state.apply_action()

    @staticmethod
    def state_quality_function(resource_weight, resource_amount, resource_proportion, population) -> float:
        if (population <= 0):
            return 0
        return resource_weight * resource_proportion * resource_amount / population

    def state_quality_function_energy(resource_weights, resource_amounts, resource_proportions, population, carbon_footprint) -> float:
        if population <= 0:
            return 0

        # Calculate total resource quality
        total_quality = 0
        for resource in resource_weights:
            if resource == "CarbonFootprint":
                continue
            if resource in resource_amounts:
                weight = resource_weights[resource]
                amount = resource_amounts[resource]
                proportion = resource_proportions.get(resource, 1)
                quality = weight * proportion * amount / population
                total_quality += quality

        # Calculate carbon footprint quality
        carbon_weight = resource_weights["CarbonFootprint"]
        carbon_proportion = resource_proportions["CarbonFootprint"]
        carbon_quality = carbon_weight * carbon_proportion * carbon_footprint / population

        # Combine total quality and carbon quality
        state_quality = total_quality - carbon_quality
        return state_quality

    def state_quality_function_gdp(world_state, resource_weights, resource_proportions, trade_rates):
        # Calculate GDP based on the value of goods and services produced
        gdp = 0
        for key, value in world_state.items():
            if key == "Population":
                continue
            if key in resource_weights and key in resource_proportions:
                weight = resource_weights[key]
                proportion = resource_proportions[key]
                value = value * weight * proportion
                gdp += value

        # Calculate GDP based on the value of trade
        for country_name, trade_rates_for_country in trade_rates.items():
            for other_country_name, trade_rate in trade_rates_for_country.items():
                if trade_rate == 0:
                    continue
                if country_name not in world_state or other_country_name not in world_state:
                    continue
                country_gdp = gdp_for_country(
                    world_state, resource_weights, resource_proportions, country_name)
                other_country_gdp = gdp_for_country(
                    world_state, resource_weights, resource_proportions, other_country_name)
                trade_value = trade_rate * min(country_gdp, other_country_gdp)
                gdp += trade_value

        # Return the GDP as the utility value
        return gdp

    def gdp_for_country(world_state, resource_weights, resource_proportions, country_name):
        # Calculate GDP based on the value of goods and services produced by the country
        gdp = 0
        for key, value in world_state.items():
            if key == "Population":
                continue
            if key in resource_weights and key in resource_proportions:
                weight = resource_weights[key]
                proportion = resource_proportions[key]
                value = value * weight * proportion
                if key == "Money" and country_name in value:
                    gdp += value[country_name]
                elif key == "Labor":
                    gdp += value * proportion
        return gdp

    @staticmethod
    def state_quality_for_all(world_state, resource_weights, resource_proportions):
        print("CALCULATING STATE QUALITY...--~~~```")
        for key, value in world_state.items():
            country = key
            population = float(world_state[key]["Population"])
            state_quality = 0

            for resource in resource_weights:
                # When resource is Population, or doesn't exist in the weights table, skip
                if resource != "Population" and resource in world_state[key].keys():
                    resource_weight = resource_weights[resource]
                    resource_amount = float(world_state[key][resource])
                    resource_proportion = resource_proportions[
                        resource] if resource in resource_proportions else 1
                    state_quality = ExpectedUtility.state_quality_function(
                        resource_weight, resource_amount, resource_proportions, population)
                    print(
                        f"\nstate_quality_for_all:Called SQ equation: Country: {country}, Resource: {resource}, Parameters: {resource_weight} * {resource_proportion} * {resource_amount} / {population}. State quality so far: {state_quality}")

            print(f"DONE! State Quality for {country}: {state_quality}")

     # Calculate state quality for a country
    @staticmethod
    def state_quality_for_country(country_state, resource_weights, resource_proportions) -> float:
        country = country_state["Country"]
        population = float(country_state["Population"])
        state_quality = 0

        for resource in resource_weights:
            # When resource is Population, or doesn't exist in the weights table, skip
            if resource != "Population" and resource in country_state.keys():
                resource_weight = resource_weights[resource]
                resource_amount = float(country_state[resource])
                resource_proportion = resource_proportions[resource] if resource in resource_proportions else 1
                state_quality += ExpectedUtility.state_quality_function(
                    resource_weight, resource_amount, resource_proportion, population)
                # print(f"\nstate_quality_for_country:Called SQ equation: Country: {country}, Resource: {resource}, Parameters: {resource_weight} * {resource_proportion} * {resource_amount} / {population}. State quality so far: {state_quality}")

        print(f"DONE! State Quality for {country}: {state_quality}")
        return state_quality

    # Discounted Reward
    # - From final state of schedule
    # - Equation: DR(ci,sj)=gamma^N ∗ (Qend(ci,sj) – Qstart(ci,sj)), where 0 <= gamma <1
    @staticmethod
    def discounted_reward(gamma, n, q_start, q_end) -> float:
        DR = gamma**n * (q_end - q_start)
        return DR

    @staticmethod
    def logistic_function(x):
        return 1 / (1 + math.exp(-x))

    # Expected Utility calculation
    # Equation: EU(ci,sj) = (P(sj) ∗ DR(ci,sj)) + ((1−P(sj)) ∗ C), where ci = self, sj = schedule, C = cost of schedule failure constant
    @staticmethod
    def expected_utility(probability, discounted_reward, c) -> float:
        return probability * discounted_reward + ((1-probability) * c)
