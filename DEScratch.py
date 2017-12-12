import numpy as np
import random as rnd
import math


# - - - - - - - - - - - - - - - I N D I V I D U A L   D E F I N I T I O N - - - - - - - - - - - - - - - - - -
class Population(object):
    def __init__(self, agentnmbr):
        self.agentnmbr = agentnmbr

        # ----------------------------------GENERATE POPULATION--------------------------------------

    def initialise(self):
        """
        input: agentnmbr = number of agents defined by the user (for our problem 20 should be more than sufficient)
        output: either none, or if needed the array of agents. I would suggest however to make the array global.

        creates as many agents as user defines. randomly assigns values to the number of powerplants.
        randomly divides the overall energy created over all the markets
        takes the price of the market (m1,m2,m3) as given as a global variable
        """
        agentnmbr = self.agentnmbr
        # m1 = 0.45
        # m2 = 0.25
        # m3 = 0.20
        kwh1 = 5
        kwh2 = 10
        kwh3 = 20
        self.population = []
        for i in range(0, agentnmbr):
            p1 = rnd.randint(0, 100)
            p2 = rnd.randint(0, 50)
            p3 = rnd.randint(0, 3)
            # randomly choosing how many powerplants we have for each agent
            sum = p1 * kwh1 + p2 * kwh2 + p3 * kwh3
            s1 = rnd.randint(0, sum)
            sum = sum - s1
            s2 = rnd.randint(0, sum)
            sum = sum - s2
            s3 = sum
            # m1 = np.random.uniform(0,1)
            # m2 = np.random.uniform(0,1)
            # m3 = np.random.uniform(0,1)
            # assigning random values for each market, depending on the overall produced energy
            new_agent = (p1, p2, p3, s1, s2, s3, m1, m2, m3)
            self.population.append(new_agent)
        return self.population

    # ---------------------------------------- UPDATE POPULATION-------------------------------------------

    # ADD THIS TRIAL INTO THE POPULATION BY RANDOMLY REMOVING ANY ONE FROM THE POPULATION
    def update_population(self, best_trial):
        # print("52 REPLACE A RANDOM CANDIDATE IN THE POPULATION BY THE BEST TRIAL CANDIDATE")

        self.best_trial = best_trial

        del_idx = np.random.randint(0, len(self.population))
        # print("57 DELETE INDEX", del_idx)

        self.population[del_idx] = best_trial  # Just replace

        # print("61 UPDATED POPULATION", self.population)

        return self.population


# -------------------------------------------- END OF POPULATION CLASS ---------------------------------------


class Individual(Population):
    def __init__(self, genome, revenue):
        super().__init__(populationSize)
        self.genome = genome
        self.revenue = revenue

    def update_revenue(self):
        pass


# - - - - - - - - - - - - - - - D O N O R   S E L E C T I O N - - - - - - - - - - - - - - - - - - - - - - - -

# GENERATE TARGETS AND DONORS FROM THE POPULATION
def donor_selection(population, scaling_factor):
    """
    INPUT: Population, a list of objects containing vectors as a representation for genome projecting into the search-space
    OUTPUT: A list of tuples. Each tuple contains the target at position 1 (0) and the list of donor objects at position 2 (1)
    """
    target_position = 0
    target_and_donors_list = []
    # this is the output list, which contains tuples with the target at position 1 and all donor individuals at 2
    while target_position != len(population):
        target_donors = population.copy()
        target = population[target_position]
        del target_donors[target_position]

        # Randomly select the base for each target
        base_idx = np.random.randint(0, len(target_donors))
        base = target_donors[base_idx]
        del target_donors[base_idx]

        # Select two vectors randomly
        x1_idx = np.random.randint(0, len(target_donors))
        x1 = target_donors[x1_idx]
        del target_donors[x1_idx]

        x2_idx = np.random.randint(0, len(target_donors))
        x2 = target_donors[x2_idx]
        del target_donors[x2_idx]

        # COMPUTE DONOR
        # Subtract two vectors x1 and x2
        sub_dummy = [x - y for x, y in zip(x1, x2)]

        # Scale the resulting vecor
        mul_dummy = np.dot(scaling_factor, sub_dummy)

        # Donor
        donor = [b + x for b, x in (zip(base, mul_dummy))]

        target_and_donors = (target, donor)
        target_and_donors_list.append(target_and_donors)
        target_position += 1

    return target_and_donors_list


# - - - - - - - - - - - - - - - D O N O R   S E L E C T I O N - - - - - - - - - - - - - - - - - - - - - - - -
# def trial_generation(target_and_donors, scaling_factor):

# TRIAL GENERATION FOR SINGLE TARGET,DONOR PAIR

def trial_generation(target_and_donor, CR=0.5):
    target, donor = target_and_donor[0], target_and_donor[1]
    z = []
    for i in range(len(target)):
        r = np.random.uniform(0, 1)
        if r <= CR:
            z.append(donor[i])
        else:
            z.append(target[i])

    return z

#------------------------------------------PROBLEM CONSTANTS---------------------------------

class problem():
    # by Marieke
    class powerplant():
        def __init__(self, planttype):
            if planttype == 1:
                self.kwhPerPlants = 50000
                self.costPerPlant = 10000
                self.maxPlants = 100

            if planttype == 2:
                self.kwhPerPlants = 600000
                self.costPerPlant = 80000
                self.maxPlants = 50

            if planttype == 3:
                self.kwhPerPlants = 4000000
                self.costPerPlant = 400000
                self.maxPlants = 3

    class market():
        def __init__(self, market):
            if market == 1:
                self.maxPrice = 0.45
                self.maxDemand = 2000000

            if market == 2:
                self.maxPrice = 0.25
                self.maxDemand = 30000000

            if market == 3:
                self.maxPrice = 0.2
                self.maxDemand = 20000000


#---------------------------------------- MARKET REVENUE FUNCTION ----------------------------

# Function returns the revenues
# Pass the revenues into selection function below
def calculate_profit(individual):
    genes = individual

    energy_produced = genes[:3]
    market_distribution = genes[2:5]
    price_distribution = genes[5:8]

    plant1 = problem.powerplant(1)
    plant2 = problem.powerplant(2)
    plant3 = problem.powerplant(3)

    market1 = problem.market(1)
    market2 = problem.market(2)
    market3 = problem.market(3)

    total_energy_produced = sum(energy_produced)
    total_energy_distributed = sum(market_distribution)

    purchasing_cost = 0
    if total_energy_produced < total_energy_distributed:
        difference_in_production = total_energy_distributed - total_energy_produced
        purchasing_cost = difference_in_production * 0.6   # CostPrice

    productioncosts = plantTypeCost(energy_produced[0], plant1)
    productioncosts += plantTypeCost(energy_produced[1], plant2)
    productioncosts += plantTypeCost(energy_produced[2], plant3)

    cost = purchasing_cost + productioncosts

    total_revenue = price_distribution[0] * min(market_distribution[0], demand(price_distribution[0], market1))
    total_revenue += price_distribution[1] * min(market_distribution[1], demand(price_distribution[1], market2))
    total_revenue += price_distribution[2] * min(market_distribution[2], demand(price_distribution[2], market3))

    profit = total_revenue - cost

    return profit


def plantTypeCost(s, plant):
    """
    calculates the cost we will have to build n plants of type p

    INPUT
    - s (desired amount of energy)
    - planttype

    """
    kwhPerPlant = plant.kwhPerPlants
    maxPlants = plant.maxPlants
    costPerPlant = plant.costPerPlant
    # if s non-positive, return 0
    if (s <= 0):
        return 0

    # if x larger than possible generation, return infinite
    if (s > kwhPerPlant * maxPlants):
        return float('Inf')

    # otherwise find amount of plants needed to generate s
    plantsNeeded = math.ceil(s / kwhPerPlant)

    # return cost (amount of plants * cost per plant)
    return plantsNeeded * costPerPlant


def demand(sellingPrice, market):
    # by Marieke

    """
    gives us the open demand of a market

    INPUT
    - sellingPrice (the price at which we sell energy)
    - maxPrice (maximum price customers are willing to pay)
    - maxDemand (total demand of a market)

    OUTPUT
    -

    """

    maxPrice = market.maxPrice
    maxDemand = market.maxDemand

    # if the selling price is greater than what customers want to pay, return 0
    if (sellingPrice > maxPrice):
        return 0

    # if nothing is produced for market
    if (sellingPrice <= 0):
        return maxDemand

    # else determine the demand based on the selling price
    demand = maxDemand - sellingPrice ** 2 * maxDemand / maxPrice ** 2

    return demand


# --------------------------------------- SELECTION--------------------------------------------

# THIS HAS TO BE REPLACED BY THE REVENUE MEASURE FUNCTION WHICH HAS TO RETURN THE INDEX OF TRIALS WITH HIGH PROFIT

def selection(profit):
    # Selection is based on high profit

    # print("146 PROFIT", profit)

    # GET THE MAX PROFIT INDEX

    profit_idx = np.argmax(profit)

    # print("152 Index of trial with max profit", profit_idx)

    # print("153 ---Get that trial vector with high profit out---")

    best_trial = trials[profit_idx]

    # print("158 The best trial is ", best_trial)

    return best_trial


# - - - - - - - - - - - - - - - U S E R   I N P U T - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def user_input():
    """
    Output List with control Parameters: [crossoverRate,scalingFactor,populationSize]
    """

    # Our three Control Parameters
    crossoverRate = -1
    scalingFactor = -1
    populationSize = -1
    # output = [crossoverRate,scalingFactor,populationSize]
    output = []

    default = int(input("Do yo want to use default values? [0]Yes [else]No: "))

    if default == 0:
        # crossoverRate
        output.append(0.5)
        # scalingFactor
        output.append(0.5)
        # populationSize
        output.append(20)
    else:
        print("")
        # Crossover Rate Cr e [0,1]
        while (crossoverRate < 0) or (crossoverRate > 1):
            if crossoverRate == -1:
                crossoverRate = float(input("Please specify Crossover Rate in [0,1]: "))
            else:
                crossoverRate = int(input("Crossover rate must be must be in [0,1]: "))
        output.append(crossoverRate)
        print("")
        # Scaling factor F e (0,1)
        while (scalingFactor <= 0) or (scalingFactor >= 1):
            if scalingFactor == -1:
                scalingFactor = float(input("Please specify Scaling Factor in (0,1): "))
            else:
                scalingFactor = float(input("Scaling Factor must be must be in (0,1): "))
        output.append(scalingFactor)
        print("")
        # population size N > 4
        while populationSize < 5:
            if populationSize == -1:
                print("Recommended Population size: 5-10 times the dimension of the problem.")
                populationSize = int(input("Please specify Population Size: "))
            else:
                populationSize = int(input("Population Size must be bigger than 4: "))
        output.append(populationSize)
    print("")
    print("####---------Initialize Differential Evolution with: ---------###")
    print("")
    print("Crossover Rate: ", crossoverRate)
    print("Scaling Factor: ", scalingFactor)
    print("Population Size: ", populationSize)
    print("")
    print("####----------------------------------------------------------###")
    print("")

    return output


# - - - - - - - - - - - - - - - M A I N - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == '__main__':

    """
    1. Handle user input
    2. Mainloop:
        a initialize population
        b donor selection
            c trial generation
            d Selection
            e update Population
        f Update termination condition value
    3. return best after termination
    """
    # 1. userinput of type List: [crossoverRate,scalingFactor,populationSize]
    userinput = user_input()

    crossoverRate = userinput[0]
    scalingFactor = userinput[1]
    populationSize = userinput[2]

    # 2. Mainloop

    # a initialize population
    pop = Population(populationSize)
    population = pop.initialise()
    # print("254 INITIAL POPULATION", population)

    # search = True
    # while search:
    for i in range(200):
        # b donor selection
        targets_and_donors_list = donor_selection(population, scalingFactor)

        # c trial generation
        trials = []
        for target_and_donor in targets_and_donors_list:
            trials.append(trial_generation(target_and_donor, CR=crossoverRate))

        # GET THE LIST OF REVENUES FROM EACH TRIALS
        list_revenues = []
        for i in range(len(trials)):
            profit = calculate_profit(trials[i])
            list_revenues.append(profit)

        # list_revenues = np.random.randint(0, 15, len(trials))

        # d selection
        print("Maximum revenue acheived so far", max(list_revenues))
        best_trial = selection(list_revenues)

        # e update the population
        population = pop.update_population(best_trial)

        # print("276 Population of iteration %d is %s" % (i, population))
