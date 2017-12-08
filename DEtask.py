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
        self.genome = genome
        self.revenue = revenue
    def update_revenue():
        return None
"""# - - - - - - - - - - - - - - - P R O B L E M  &  P A R A M E T E R   D E S C R I P T I O N - - - - - - - - - -
class problem():
    class powerplant():
        def __init__(self, planttype):
            if planttype == 1:
                self.power = 50000
                self.cost = 10000
                self.amount = 100
                
            if planttype == 2:
                self.power = 600000
                self.cost = 80000
                self.amount = 50
                
            if planttype == 3:
                self.power = 4000000
                self.cost = 400000
                self.amount = 3
        None
    def market_model():
        None
    def plant_cost_model():
        None
    def 
"""
# - - - - - - - - - - - - - - - P O P U L A T I O N   I N I T I A L I Z A T I O N - - - - - - - - - - - - - - -
def initalize_population(individualcount):
    population = []
    while individualcount != 0:
        newgenome = "somethingsomething in numpy"
        newindividual = individual(newgenome,0)
        newindividual.update_revenue()
        population.append(newindividual)
        individualcount -= 1
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
# - - - - - - - - - - - - - - - D O N O R   S E L E C T I O N - - - - - - - - - - - - - - - - - - - - - - - - 
def donor_selection(population):
    """
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

# - - - - - - - - - - - - - - - D O N O R   S E L E C T I O N - - - - - - - - - - - - - - - - - - - - - - - -
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
    - tuples contain the original target as well as a list of donors
    """
    
    
    
    """
    MISTAKE THAT NEEDS TO BE FIXED:
        
    At the moment, I select EVERY individual in the list of bases to be a base, one is ought to select only one randomly!!!!!!"""
    for target_donor_tuple in target_and_donors:
        #because the input for this function is a touple of an object and a list of object, we split the tuple for easy handling
        target = target_donor_tuple[0]
        all_donors = target_donor_tuple[1]
        
        target_donors_associated_list = []
        for one_donor in all_donors:
            aux_donors = list(all_donors)
            
            aux_donors.pop(one_donor)
            #After we removed the individual we want to compare our target to from the list, we choose two other vectors from the remaining list
            x1 = rnd.choice(aux_donors)
            aux_donors.remove(x1)
            x2 = rnd.choice(aux_donors)
            
            #donor vector is selected by computing the difference between the genome of the randomly chosen individuals and scaling it with the scaling factor
            donor_vector = np.substract(x1.genome,x2.genome) * scaling_factor
            
            final_donor = np.add(target.genome + donor_vector)
            newindividual = individual(final_donor,0)
            newindividual.update_revenue()
            target_donors_associated_list.append(newindividual)
            
            
            
            
            
            
# - - - - - - - - - - - - - - - HIGH LEVEL PROFIT MODEL - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
"""
    profit = revenue - totalCost
    revenue = soldQuantitiy * sellingPrice
    totalCost = plantTypeCost + purchasingCost
    puchasingCost = max(soldQuantity - generatedQuantity, 0) * costPrice

"""


# - - - - - - - - - - - - - - - PLANT COST MODEL - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def plantTypeCost(x, kwhPerPlant, costPerPlant, maxPlants):
y    """ 
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
    if(x > kwhPerPlants * maxPlants):
        return float('Inf')
    
    #otherwise find amount of plants needed to generate x
    plantsNeeded = math.ceil(x / kwhPerPlant)
    
    #return cost (amount of plants * cost per plant)
    return plantsNeeded * costPerPlant


# - - - - - - - - - - - - - - - MARKET MODEL - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
def demand(sellingPrice, maxPrice, maxDemand):
    
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
    return None
