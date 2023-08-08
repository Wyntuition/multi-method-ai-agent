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

    PROCESSING: State quality for each country: For each resource, run through state value function and aggregate the values

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
        state_quality = resource_weight * resource_proportion * resource_amount / population
        return state_quality

    # Calculate state quality for all countries
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
