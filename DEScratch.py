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
        m1 = 0.45
        m2 = 0.25
        m3 = 0.20
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

        print("61 UPDATED POPULATION", self.population)

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

#---------------------------------------- MARKET REVENUE FUNCTION ----------------------------

# Function returns the revenues
# Pass the revenues into selection function below

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
    print("254 INITIAL POPULATION", population)

    # search = True
    # while search:
    for i in range(10):
        # b donor selection
        targets_and_donors_list = donor_selection(population, scalingFactor)

        # c trial generation
        trials = []
        for target_and_donor in targets_and_donors_list:
            trials.append(trial_generation(target_and_donor, CR=crossoverRate))

        # GET THE LIST OF REVENUES FROM EACH TRIALS
        # SHOULD BE FROM MARKET REVENUE MEASURE
        # but for time being i just took some random revenue values for each trials
        # and pass them inside the selection function
        list_revenues = np.random.randint(0, 15, len(trials))

        # d selection
        best_trial = selection(list_revenues)

        # e update the population
        population = pop.update_population(best_trial)

        print("276 Population of iteration %d is %s" % (i, population))
