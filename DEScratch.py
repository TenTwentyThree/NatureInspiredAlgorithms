import numpy as np
import random as rnd


def initialise(agentnmbr):
    """
    input: agentnmbr = number of agents defined by the user (for our problem 20 should be more than sufficient)
    output: either none, or if needed the array of agents. I would suggest however to make the array global.

    creates as many agents as user defines. randomly assigns values to the number of powerplants.
    randomly divides the overall energy created over all the markets
    takes the price of the market (m1,m2,m3) as given as a global variable
    """
    m1 = 0.45
    m2 = 0.25
    m3 = 0.20
    kwh1 = 5
    kwh2 = 10
    kwh3 = 20
    population = []
    for i in range(0, agentnmbr):
        p1 = rnd.randint(0, 100)
        p2 = rnd.randint(0, 50)
        p3 = rnd.randint(0, 3)
        # randomly choosing how many powerplants we have for each agent

        sum = p1 * kwh1 + p2 * kwh2 + p3 * kwh3
        # print(sum)
        s1 = rnd.randint(0, sum)
        sum = sum - s1
        # print(sum)
        s2 = rnd.randint(0, sum)
        sum = sum - s2
        # print(sum)
        s3 = sum
        # assigning random values for each market, depending on the overall produced energy
        new_agent = (p1, p2, p3, s1, s2, s3, m1, m2, m3)
        # print(new_agent)
        population.append(new_agent)


    return population


def generate_newgenome():
    """
    Create energy list within max range
    Planned amount of energy sold
    Price for market of type 1

    newgenome = []

    # Energy produced with plants of type i
    newgenome.append(np.random.randint(1, 50000))  # e1
    newgenome.append(np.random.randint(1, 6000000))  # e2
    newgenome.append(np.random.randint(1, 4000000))  # e3


    # Energy planned to be sold to market
    newgenome.append(np.random.randint(1, 50000))  # s1
    newgenome.append(np.random.randint(1, 6000000))  # s2
    newgenome.append(np.random.randint(1, 4000000))  # s3

    # Price for market of type
    newgenome.append(np.random.uniform(0, 0.5))  # p1
    newgenome.append(np.random.uniform(0, 0.3))  # p2
    newgenome.append(np.random.uniform(0, 25))  # p3


    # newgenome = np.random.randint(0,5,5).tolist()
    # newgenome = [float(gene) for gene in newgenome]

    return newgenome

# print(generate_newgenome())

def generate_new_pop(num_pop):

    pop = []
    for _ in range(num_pop):
        pop.append(generate_newgenome())

    return pop

# pop = generate_new_pop(8)
"""
pop = initialise(5)

print("POPULATION",len(pop))
# -----------------------------
# - - - - - - - - - - - - - - - M A I N - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def __MAIN__():
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
    #this is the output list, which contains tuples with the target at position 1 and all donor individuals at 2
    while target_position != len(population):
        target_donors = population.copy()
        target = population[target_position]
        del target_donors[target_position]

        # Randomly select the base for each target
        base_idx = np.random.randint(0,len(target_donors))
        base = target_donors[base_idx]
        del target_donors[base_idx]

        #Select two vectors randomly
        x1_idx = np.random.randint(0,len(target_donors))
        x1 = target_donors[x1_idx]
        del target_donors[x1_idx]

        x2_idx = np.random.randint(0,len(target_donors))
        x2  = target_donors[x2_idx]
        del target_donors[x2_idx]

        # COMPUTE DIFFERENCE DONOR
        # Subtract two vectors x1 and x2
        sub_dummy = [x - y for x,y in zip(x1,x2)]
        mul_dummy = np.dot(scaling_factor,sub_dummy)
        donor = [b + x for b, x in (zip(base, mul_dummy))]

        target_and_donors = (target, donor)
        target_and_donors_list.append(target_and_donors)
        target_position += 1
    return target_and_donors_list

targets_and_donors = donor_selection(pop,0.5)
print("TARGETS AND DONORS ",len(targets_and_donors))


# - - - - - - - - - - - - - - - D O N O R   S E L E C T I O N - - - - - - - - - - - - - - - - - - - - - - - -
# def trial_generation(target_and_donors, scaling_factor):

# TRIAL GENERATION FOR SINGLE TARGET,DONOR PAIR

def trial_generation(target_and_donor,CR = 0.5):

    target,donor = target_and_donor[0],target_and_donor[1]
    z = []
    for i in range(len(target)):
        r = np.random.uniform(0,1)
        if r<= CR:
            z.append(donor[i])
        else:
            z.append(target[i])

    return z

# GENERATE TRIALS FOR ENTIRE TARGET-DONOR PAIRS
trials = []
for target_and_donor in targets_and_donors:
    trials.append(trial_generation(target_and_donor))

print("TRIALS",len(trials))


# SELECTION
# Selection is based on high profit

profit = np.random.randint(0,15,len(trials))

print("PROFIT",profit)

# GET THE MAX PROFIT INDEX

profit_idx = np.argmax(profit)

print("Index of trial with max profit",profit_idx)

print("---Get that trial vector with high profit out---")

best_trial = trials[profit_idx]

print("The best trial is ", best_trial)

# ADD THIS TRIAL INTO THE POPULATION BY RANDOMLY REMOVING ANY ONE FROM THE POPULATION
# def update_population(best_trial)
print("REPLACE A RANDOM CANDIDATE IN THE POPULATION BY THE BEST TRIAL CANDIDATE")

del_idx = np.random.randint(0,len(pop))

print("DELETE INDEX",del_idx)
pop[del_idx] = best_trial   # Just replace the best way

# del pop[del_idx]

# pop.append(best_trial)

print("UPDATED POPULATION", pop)