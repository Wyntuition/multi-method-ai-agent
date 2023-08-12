
from world_state import WorldState
from expected_utility import ExpectedUtility
from successors import RandomSuccessorFunction


def score_schedule(schedule, self_country_name, initial_world_state, resource_weights, resource_proportions):

    # Calculate the state quality for each country in the schedule
    # TODO - this needs to use updated state quality function
    state_qualities = {}
    for country_name, resource_amounts in schedule.items():
        if country_name == self_country_name:
            continue
        state_quality = ExpectedUtility.state_quality_for_all(
            resource_amounts, country_name)
        state_qualities[country_name] = state_quality
    participating_countries = list(state_qualities.keys())

    # Calculate initial state quality for my country
    self_state_quality_start = ExpectedUtility.state_quality_for_country(
        initial_world_state[self_country_name], resource_weights, resource_proportions)
    # print(
    #     f"My country's initial state: {initial_world_state[self_country_name]}")

    world_state = WorldState(initial_world_state)
    sch_gen = RandomSuccessorFunction(self_country_name)
    schedule = sch_gen.generate_random_schedule(5)

    updated_world_state = world_state.apply_schedule(schedule)

    self_state_quality_end = ExpectedUtility.state_quality_for_country(
        updated_world_state[self_country_name], resource_weights, resource_proportions)
    print(f"Starting State Quality: {self_state_quality_start}")
    # print(
    #     f"Country's state after transform: {updated_world_state[self_country_name]}")
    print(f"Ending State Quality: {self_state_quality_end}")

    # Probability of schedule acceptance
    # Equation: we will use the product of the probabilities of the individual P(ci,sj) value
    #   - The probability that a country, ci, will agree to a schedule, sj, is computed by the logistic function where x corresponds to DR(ci, sj ) and L = 1, and you can experiment with different values of x0 and k (but use x0 = 0 and k = 1 as starting points)
    # TODO: Think about and report on how different parameter settings might reflect biases in the real world (e.g., a reason for shifting x0 might be to reflect opportunity costs — what other benefits might await a patient country?).
    # Note that the strategy for estimating the probability that a schedule is accepted (i.e., will be accepted by all parties to the schedule) and succeeds, does not come from statistics accu- mulated over data from the “real world” (to include game play) as we might think is ideal, but our method draws from an information theoretic tradition of estimating probabilities of “events” from the “descriptions” of those events. An assumption in this description- driven methodology is a bias that more “complicated” descriptions represent lower proba- bility events. It is a quantification of Occam’s razor. This is the one way (probably the only way given the time constraints of this class) that the AI agent for your country will take into account the State Qualities of other countries, as well as your own. It has the effect of countering ill-considered greed.

    # Calculate Discounted Reward
    q_start = self_state_quality_start
    q_end = self_state_quality_end
    gamma = 0.5
    n = 5  # steps to get into state

    discounted_reward = ExpectedUtility.discounted_reward(
        gamma, n, q_end, q_start)
    print(f"Discounted Reward for {self_country_name}: {discounted_reward}")

    # calculate schedule EU
    # TODO check if SQ changed (Live 8 3:00)
    sigmoid_midpoint = 1
    x0 = discounted_reward - sigmoid_midpoint

    # TODO: tweak
    # Probability of country's acceptance of a schedule (using logistic function)
    const_k = 1  # steepness of the curve
    const_L = 1  # max value of the curve
    p = ExpectedUtility.logistic_function(x0)  # x0 is midpoint of curve

    # Multiply them for overall schedule acceptance -
    for country in participating_countries:
        p += p * ExpectedUtility.logistic_function(x0)
    print(f"Probability of schedule acceptance: {p}")

    # Expected Utility calculation
    const_c = 0.1
    eu = ExpectedUtility.expected_utility(p, discounted_reward, const_c)
    print(f"Expected Utility: {eu}")

    return eu
