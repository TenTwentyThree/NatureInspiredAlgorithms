# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:32:15 2017

@author: Till
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:27:24 2017

@authors:
    Johannes
    Marieke
    Saran
    Till
    Yannic
"""

import numpy as np
import random as rnd
import math

# - - - - - - - - - - - - - - - I N D I V I D U A L   D E F I N I T I O N - - - - - - - - - - - - - - - - - - 
class individual():
    def __init__(self, genome):
        self.genome = np.array(genome)
        self.revenue = self.genome[3]*self.genome[6] + self.genome[4]*self.genome[7] + self.genome[5]*self.genome[8]
        
    def update_revenue(self):
        profit = 0
        costs = self.costs()
        
        if self.genome[3] > 2000000:
            self.revenue = 0
        if self.genome[4] > 30000000:
            self.revenue = 0
        if self.genome[5] > 20000000:
            self.revenue = 0
        #print(self.revenue)
        
        profit = self.revenue-costs
        return profit
    
    def costs(self):
        
        c = 0
        #production costs
        cost1 = self.building_cost(self.genome[0],kwh1,10000,100)
        cost2 = self.building_cost(self.genome[1],kwh2,80000,50)
        cost3 = self.building_cost(self.genome[2],kwh3,400000,3)        
        
        #purchasing costs
        produced = self.genome[0]+self.genome[1]+self.genome[2]
        sold = self.genome[3]+self.genome[4]+self.genome[5]
        
        if sold > produced:
            c =+ (sold - produced)*0.6
            
        if self.genome[0] > 100* kwh1:
            c =+ 1000000000
        
        if self.genome[1] > 50* kwh2:
            c =+ 1000000000
        
        if self.genome[2] > 3* kwh3:
            c =+ 1000000000
        
        c =+ cost1 +cost2 +cost3
        #print("COSTS ARE THIS HIGH!!: ",costs)
        
        return c
    
    def building_cost(self,x, kwhPerPlant, costPerPlant, maxPlants):
        """
        Nicos functions of costs
        """
        if x <= 0:
            return 0
        
        if x > kwhPerPlant * maxPlants:
            return 100000000
        
        plantsNeeded = math.ceil(x / kwhPerPlant)
        
        return plantsNeeded * costPerPlant

# - - - - - - - - - - - - - - - P O P U L A T I O N   I N I T I A L I Z A T I O N - - - - - - - - - - - - - - -
def initialise(agentnmbr):
    #by Yannic(?), Till(?), Saran(?), Marieke(?)
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
    global kwh1 
    global kwh2
    global kwh3
    population = []
    kwh1 = 50000
    kwh2 = 600000
    kwh3 = 4000000
    for i in range(0,agentnmbr):
        p1 = rnd.randint(0,100)
        p2 = rnd.randint(0,50)
        p3 = rnd.randint(0,3)
        #randomly choosing how many powerplants we have for each agent
        
        ttlsum = p1*kwh1 + p2*kwh2 + p3*kwh3
        #print(sum)
        s1 = rnd.randint(0,ttlsum)
        ttlsum = ttlsum - s1
        #print(sum)
        s2 = rnd.randint(0,ttlsum)
        ttlsum = ttlsum - s2
        #print(sum)
        s3 = ttlsum
        
        e1 = p1 * kwh1
        e2 = p2 * kwh2
        e3 = p3 * kwh3
        #assigning random values for each market, depending on the overall produced energy
        new_agent = individual([e1,e2,e3,s1,s2,s3,m1,m2,m3])
        #print(new_agent)
        population.append(new_agent)
    
    #print(population)           
    return population
        
    
# - - - - - - - - - - - - - - - M A I N - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def __MAIN__():
   #by Johannes, Yannik, Till, Saran, Marieke
   
    # 1. userinput of type List: [crossoverRate,scalingFactor,populationSize]
    userinput = user_input()
    
    crossoverRate = userinput[0]
    scalingFactor = userinput[1]
    populationSize = userinput[2]
    
    counter = 0
    
    popcounter = 0
    
    # 2. Mainloop
    population = initialise(populationSize)
    
    current_best = rnd.choice(population)
    
    while counter < 20:
        
        target_and_donors_list = donor_selection(population)
        
        trial = trial_generation(target_and_donors_list, scalingFactor, crossoverRate)
        
        population = selection(trial)
        
        generations_best = find_best(population)
        
        #print("Currently expected maximal Profit: ",generations_best.update_revenue())
        #print("Currently best Genome: ", generations_best.genome)
        
        if current_best.revenue >= generations_best.revenue:
            counter += 1
        else:
            current_best = generations_best
        popcounter += 1
        
        
        
        
        
        
    
    print("Convergence termination reached after",popcounter,"generations.")
    print("Best Profit found!: ",generations_best.update_revenue())
    # 3. Best
    return current_best 
            
        
        
    
    
# - - - - - - - - - - - - - - - D O N O R   S E L E C T I O N - - - - - - - - - - - - - - - - - - - - - - - - 
def donor_selection(population):
    #by Johannes
    """
    
    This function basically generates a number of permutations of the population where one element is chosen as the target vector and the others as donors or bases
    
    
    INPUT: Population, a list of objects containing vectors as a representation for genome projecting into the search-space
    OUTPUT: A list of tuples. Each tuple contains the target at position 1 (0) and the list of donor objects at position 2 (1)
    """
    target_position = 0
    target_and_donors_list = []
    #this is the output list, which contains tuples with the target at postion 1 and all donor individuals at 2
    while target_position != len(population):
        target_donors = list(population)
        target = population[target_position]
        del target_donors[target_position]
        target_and_donors = (target, target_donors)
        target_and_donors_list.append(target_and_donors)
        target_position += 1
    return target_and_donors_list

# - - - - - - - - - - - - - - - T R I A L   G E N E R A T I O N - - - - - - - - - - - - - - - - - - - - - - - -
def trial_generation(target_and_donors, scaling_factor, crossover):
    #by Johannes
    """
    
    for each target vector (all vectors in our population are defined as target vectors), we select a base
    the base vector is then removed from the available population pool and two other individuals (except target and base)
    are chosen. These then provide the donor vector for the trial vector / trial individual.
    The trial vector is then generated and its coordinates (genes) are recombined with the genes of the target to form a child
    The program then returns a list with tuples containing the target vector and the generated offspring to be evaluted by a selection function
    
    INPUT: 
    - A list of tuples which contain the target and a list of base vectors
    - A constant scaling factor to be applied to the difference between base and target to generate trial objects
    OUTPUT:
    - A list containing tuples
    - tuples contain the original target as well as a trial individual that then can be compared by the revenue function
    """
    

    target_trial_associated_list = []
    for target_donor_tuple in target_and_donors:
        #because the input for this function is a touple of an object and a list of object, we split the tuple for easy handling
        target = target_donor_tuple[0]
        all_other_vectors = target_donor_tuple[1]
        #Select a base randomly from the list of potential bases (all other vectors than the target vector)
        base = rnd.choice(all_other_vectors)
        all_other_vectors.remove(base)
        #Choose donor vector 1
        x1 = rnd.choice(all_other_vectors)
        #and remove it from the list of potential vectors to choose as donor vectors
        all_other_vectors.remove(x1)
        #choose donor vector 2
        x2 = rnd.choice(all_other_vectors)
        #calculate the distance between the two vectors and scale it by the scaling factor
        donor_vector = np.subtract(x1.genome,x2.genome) * scaling_factor
        #now create a new individual from the base and update its revenue.
        final_donor = np.add(target.genome, donor_vector)
        
        
        
        # R E C O M B I N A T I O N   S T A R T S   H E R E
        
        target_genome = target.genome
        gene_pos = 0
        new_genome = []
        while gene_pos != len(target_genome):
            crossover = rnd.uniform(0,1)
            if crossover < 0.5:
                new_genome.append(final_donor[gene_pos])
            else:
                new_genome.append(target_genome[gene_pos])
            gene_pos += 1
        child = individual(new_genome)
        child.update_revenue()
        newtuple = (target, child)
        target_trial_associated_list.append(newtuple)
        
    return target_trial_associated_list
        
              
# - - - - - - - - - - - - - - - S E L E C T I O N - - - - - - - - - - - - - - - - - - - - - - - -
def selection(overpopulation):
    #by Johannes
    """
    This function selects between the original target vector and a child generated by trial_generation.
    
    INPUT:
    - A list of tuples, each containing a pair of original target vector and a child
    
    OUTPUT:
    - new population that contains the fittest individuals
    """
    new_population = []
    for pair in overpopulation:
        target = pair[0]
        child = pair[1]
        
        target.update_revenue()
        child.update_revenue()
        
        if target.revenue > child.revenue:
            new_population.append(target)
        else:
            new_population.append(child)
    return new_population
        
        
# - - - - - - - - - - - - - - - F I N D  B E S T  I N D I V I D U A L - - - - - - - - - - - - - - - - - - - - - -

def find_best(population):
    #by Johannes
    """
    This function simply iterates through a population and returns the fittest individual
    INPUT:
    - A list of individuals, the population
    OUTPUT:
    - An object of the type "individual" that has the highest revenue value
    """
    
    best = rnd.choice(population)
    best.update_revenue()
    
    for individual in population:
        individual.update_revenue()
        
        if individual.revenue > best.revenue:
            best = individual
            
    return best
            

# - - - - - - - - - - - - - - - MARKET MODEL - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
def demand(sellingPrice, maxPrice, maxDemand):
    #by Marieke
    
    """
    gives us the open demand of a market
    
    INPUT
    - sellingPrice (the price at which we sell energy)
    - maxPrice (maximum price customers are willing to pay)
    - maxDemand (total demand of a market)
    
    OUTPUT
    - 
    
    """
    
    #if the selling price is greater than what customers want to pay, return 0
    if (sellingPrice > maxPrice):
        return 0
    
    #if nothing is produced for market
    if (sellingPrice <= 0):
        return maxDemand
    
    #else determine the demand based on the selling price
    demand = maxDemand - sellingPrice**2 * maxDemand / maxPrice**2
    
    return demand
        
        
        
        
        
# - - - - - - - - - - - - - - - U S E R   I N P U T - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def user_input():
    #by Yannic(?)
    """
    Output List with control Parameters: [crossoverRate,scalingFactor,populationSize]
    """

    #Our three Control Parameters
    crossoverRate = -1
    scalingFactor = -1
    populationSize = -1
    #output = [crossoverRate,scalingFactor,populationSize]
    output = []


    default = int(input("Do yo want to use default values? [0]Yes [else]No: "))

    if default == 0:
            #crossoverRate
            output.append(0.1)
            #scalingFactor
            output.append(0.1)
            #populationSize
            output.append(10)
    else:
        print("")
        #Crossover Rate Cr e [0,1]
        while (crossoverRate < 0) or (crossoverRate > 1):
            if crossoverRate == -1:
                crossoverRate = float(input("Please specify Crossover Rate in [0,1]: "))
            else:
                crossoverRate = int(input("Crossover rate must be must be in [0,1]: "))
        output.append(crossoverRate)
        print("")
        #Scaling factor F e (0,1)
        while (scalingFactor <= 0) or (scalingFactor >= 1):
            if scalingFactor == -1:
                scalingFactor = float(input("Please specify Scaling Factor in (0,1): "))
            else:
                scalingFactor = float(input("Scaling Factor must be must be in (0,1): "))
        output.append(scalingFactor)
        print("")
        #population size N > 4
        while (populationSize < 5):
            if populationSize == -1:
                print("Recommended Population size: 5-10 times the dimension of the problem.")
                populationSize = int(input("Please specify Population Size: "))
            else:
                populationSize = int(input("Population Size must be bigger than 4: "))
        output.append(populationSize)
    print("")
    print("####---------Initialize Differential Evolution with: ---------###")
    print("")
    print("Crossover Rate: ",output[0])
    print("Scaling Factor: ",output[1])
    print("Population Size: ",output[2])
    print("")
    print("####----------------------------------------------------------###")
    print("")


    return output


__MAIN__()


