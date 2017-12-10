# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:27:24 2017

@author: Johannes
"""

import numpy as np
import random as rnd
import math

# - - - - - - - - - - - - - - - I N D I V I D U A L   D E F I N I T I O N - - - - - - - - - - - - - - - - - - 
class individual():
    def __init__(self, genome, revenue):
        self.genome = np.array(genome)
        self.revenue = revenue
    def update_revenue():
        self.revenue = 0

# - - - - - - - - - - - - - - - P O P U L A T I O N   I N I T I A L I Z A T I O N - - - - - - - - - - - - - - -
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
        #assigning random values for each market, depending on the overall produced energy
        new_agent = individual([p1,p2,p3,s1,s2,s3,m1,m2,m3],0)
        #print(new_agent)
        population.append(new_agent)
    
    print(population)           
    return population
        
    
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
    # 1. userinput of type List: [crossoverRate,scalingFactor,populationSize]
    userinput = user_input()
    
    crossoverRate = userinput[0]
    scalingFactor = userinput[1]
    populationSize = userinput[2]
    
    # 2. Mainloop
    search = True
    while search:
        # a initialize population
        population = initalize_population(populationSize)
        # b donor selection
        target_and_donors_list = donor_selection(population)
    
    
    # 3. Best
    return best_model 
            
        
        
    
    
# - - - - - - - - - - - - - - - D O N O R   S E L E C T I O N - - - - - - - - - - - - - - - - - - - - - - - - 
def donor_selection(population):
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
        print(target_and_donors)
        target_and_donors_list.append(target_and_donors)
        target_position += 1
    return target_and_donors_list

# - - - - - - - - - - - - - - - T R I A L   G E N E R A T I O N - - - - - - - - - - - - - - - - - - - - - - - -
def trial_generation(target_and_donors, scaling_factor):
    """
    
    for each target vector (all vectors in our population are defined as target vectors), we select a base
    the base vector is then removed from the available population pool and two other individuals (except target and base)
    are chosen. These then provide the donor vector for the trial vector / trial individual 
    
    INPUT: 
    - A list of tuples which contain the target and a list of base vectors
    - A constant scaling factor to be applied to the difference between base and target to generate trial objects
    OUTPUT:
    - A list containing tuples
    - tuples contain the original target as well as a trial individual that then can be compared by the fitness function
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
        donor_vector = np.substract(x1.genome,x2.genome) * scaling_factor
        #now create a new individual from the base and update its fitness
        final_donor = np.add(target.genome + donor_vector)
        newindividual = individual(final_donor,0)
        newindividual.update_revenue()
        target_trial_associated_list.append(target, newindividual)
        
    return target_trial_associated_list
        
            
            
            
            
            
            
# - - - - - - - - - - - - - - - HIGH LEVEL PROFIT MODEL - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
"""
    profit = revenue - totalCost
    revenue = soldQuantitiy * sellingPrice
    totalCost = plantTypeCost(all types) + purchasingCost
    productionCost = generatedQuantity * costFactor
    puchasingCost = max(soldQuantity - generatedQuantity, 0) * costPrice

    sellingPrice = price at which we sell the energy to customers
    plantTypeCost = cost we will have to build n plants of type p
    purchasingCost = what we pay if we don't produce enough and have to buy energy from other suppliers
    costPrice = what it costs us to produce the energy
"""
def purchasingCost(e1, e2, e3, s1, s2, s3):
    sumE = e1 + e2 + e3
    sumS = s1 + s2 + s3
    
    purchCost = max((sumS - sumE), 0) * 0.6
    
    return purchCost

def productionCost(e1, e2, e3):
    prodCost = 0
    for i in range(3):
        prodCost = prodCost + plantTypeCost(e)   #how to call plantTypeCost for all types of plants?
    
    return prodCost

def totalCost(e1, e2, e3, s1, s2, s3):
    
    return productionCost(e1, e2, e3) + purchasingCost(e1, e2, e3, s1, s2, s3)


def profitModel(e1, e2, e3, s1, s2, s3, p1, p2, p3):
    
    
    
    purchasingCost = max(soldQuantity - generatedQuantity, 0) * costPrice
    totalCost = plantTypeCost() + purchasingCost
    revenue = soldQuantitiy * sellingPrice
    profit = revenue - totalCost
    

# - - - - - - - - - - - - - - - PLANT COST MODEL - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def plantTypeCost(x, kwhPerPlant, costPerPlant, maxPlants):
    """ 
    calculates the cost we will have to build n plants of type p
    
    INPUT
    - x (desired amount of energy)
    - kwhPerPlant (how much energy one plant provides)
    - maxPlants (maximum amount of plants we can have)

    """
    
    # if x non-positive, return 0
    if(x <= 0):
        return 0
    
    #if x larger than possible generation, return infinite
    if(x > kwhPerPlant * maxPlants):
        return float('Inf')
    
    #otherwise find amount of plants needed to generate x
    plantsNeeded = math.ceil(x / kwhPerPlant)
    
    #return cost (amount of plants * cost per plant)
    return plantsNeeded * costPerPlant


# - - - - - - - - - - - - - - - MARKET MODEL - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
def demand(sellingPrice, maxPrice, maxDemand):
    
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
            output.append(0.5)
            #scalingFactor
            output.append(0.5)
            #populationSize
            output.append(20)
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
    print("Crossover Rate: ",crossoverRate)
    print("Scaling Factor: ",scalingFactor)
    print("Population Size: ",populationSize)
    print("")
    print("####----------------------------------------------------------###")
    print("")


    return output





