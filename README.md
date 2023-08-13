# AI Class Project

A multi-method AI agent that plans and models trading and development (e.g., farming, manufacturing) decisions for a set of virtual countries, with each country possessing virtual resources and incentives for cooperating and competing with other countries. It uses a forward-searching, utility-driven, depth-bounded search, utility-driven scheduler.

It can be tweaked to adjust how much trading is done between each country, and impose things like tariffs and trade embargos. A carbon footprint can also be taken into account. See `expected_utility.py`.

Details: 
- Schedules of assignments are generated for transforms and transfers of resources, and a search strategy was implemented to find the best schedules, maximizing the state quality for a country. 
- I used a best-first search algorithm which uses a priority queue sorted by expected utility to keep track of the best schedules found so far, with a depth-bound limit, to limit the search depth.
- A state quality function is used to evaluate world states, initially and as they are changed by applying the schedules. 
- A successor function is used to generate possible actions the agent can search through, respecting a maximum frontier size, and a maximum number of best schedules to keep. It then performs the search and maintains a list of the best_schedules to be able to return the best one at any given time (anytime search). 
* The expected utility pipeline includes equations and functions to calculate the expected utility of partial resource schedules including:
    * Discounted reward
    * Gamma - discount factor that determines the importance of future rewards relative to immediate rewards.
    * Probability of acceptance
    * x0 
    * Constants K and l are used to adjust impact of resources weights and proportions on state quality 
    * Failure cost - const_c

## Running 

Run `pip3 install && python3 main.py`

The agent terminates when the frontier reaches the set maximum size. 

## Resources, Weights, Initial World State

Resources
- `resource-weights.csv` - defines resource weights 
- `resource-proportions.csv` - is to define the proportion of resource each person gets
- `resource-weights--energy.csv` - defines resource weights with energy resources added

Initial World States
- `initial-world-state.csv` - default world state
- `initial-world-state--energy.csv` - world state where a lot of potential energy is handed out to see how that affects things 

# Additional Experiments

- Working in a type of GDP calculation of a country based on trade, money and labor into a state quality function. Then I was trying to add in tariffs to see what would happen. I could also add in things like a trade embargo. This setup would also allow adding trade balances and deficits between countries, a currency exchange rate, and adding in all kinds of country-based economic metrics.

- Working in a carbon_footprint property into another state quality function. I would like to eventually mess around with giving different countries different state quality functions like these, and see how they do when maximized for economic growth vs environmental sustainability.


# Citations

* The Intergovernmental Panel on Climate Change (IPCC) provides guidelines for calculating greenhouse gas emissions, including carbon dioxide emissions. These guidelines are used by many organizations and governments around the world. (source: https://www.ipcc-nggip.iges.or.jp/public/2006gl/vol4.html)
* The World Resources Institute (WRI) provides a tool called the Greenhouse Gas Protocol that helps organizations calculate their greenhouse gas emissions. The tool includes guidance on how to calculate emissions from different sources, such as electricity use, transportation, and waste. (source: https://ghgprotocol.org/)
* The World Trade Organization (WTO) provides a wealth of information on international trade, including statistics, research, and policy analysis. (source: https://www.wto.org/)
