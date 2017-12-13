# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:08:00 2017

@author: Johannes
"""

import random as rnd
import numpy as np

# - - - - - - - - - - - - - - - - - - - - - - - D E F I N I N G  C L A S S E S - - - - - - - - - - - - - - - - - - - - - - - - - -
class individual():
    def __init__(self,genome):
        self.genome = genome
        self.profit = 0
    def update_profit(self):
        "something"

class problem():
    #by Marieke
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
                
        def plantTypeCost(self,energy_amount):
            cost = self.costPerPlant
            kwhPerPlant = self.kwhPerPlants
            maxPlants =  self.maxPlants
            
            # if s non-positive, return 0
            if(energy_amount <= 0):
                return 0
        
            #if x larger than possible generation, return infinite
            psblgen = kwhPerPlant * maxPlants
            if(energy_amount > psblgen):
                return float('inf')
        
            #otherwise find amount of plants needed to generate s
            plantsNeeded = math.ceil(energy_amount / kwhPerPlant)
        
            #return cost (amount of plants * cost per plant)
            return plantsNeeded * cost
            
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

def init():
    global powerplant1
    global powerplant2
    global powerplant3
    global max_power
    global max_demand
    
    global market1
    global market2
    global market3
    
    powerplant1 = problem.powerplant(1)
    powerplant2 = problem.powerplant(2)
    powerplant3 = problem.powerplant(3)
    
    market1 = problem.market(1)
    market2 = problem.market(1)
    market3 = problem.market(1)
    
    max_power = (
    powerplant1.kwhPerPlants * powerplant1.maxPlants +
    powerplant2.kwhPerPlants * powerplant2.maxPlants +
    powerplant3.kwhPerPlants * powerplant3.maxPlants )
    
    max_demand = (
    market1.maxDemand + market2.maxDemand + market3.maxDemand)
    
    
    
    
    
    
def initalize_population(agentcount):
    
    population = []
    while agentcount != 0:
        
        new_gene = [e1,e2,e3,s1,s2,s3,p1,p2,p3]
        e1 = rnd.randint(0,max_power)
        e2 = rnd.randint(0,max_power)
        e3 = rnd.randint(0,max_power)
        s1 = rnd.randint(0,max_demand)
        s2 = rnd.randint(0,max_demand)
        s3 = rnd.randint(0,max_demand)
        p1 = rnd.uniform(0,market1.maxPrice)
        p2 = rnd.uniform(0,market2.maxPrice)
        p3 = rnd.uniform(0,market3.maxPrice)
        
        new_gene = [e1,e2,e3,s1,s2,s3,p1,p2,p3]
        
        new_individual = individual(new_gene)
        new_individual.update_profit
        
        population.append(new_individual)
        
        
        
def donor_selection(population):
    new_population = []
    for individual in population:
        copy_population = population
        
        base_vector = rnd.choice(copy_population)
        copy_population.remove(base_vector)
        
        donor_vector_1 = rnd.choice(copy_population)
        copy_population.remove(donor_vector_1)
        
        donor_vector_2 = rnd.choice(copy_population)
        
        survivor = differential_mutation(individual, base_vector, donor_vector_1, donor_vector_2, scaling_factor)
        new_population.append(survivor)
    return new_population

def differential_mutation(target, base_vector, donor_vector_1, donor_vector_2, scaling_factor):
    
    distance_vector = np.subtract(donor_vector_1.genome,donor_vector_2.genome)
    distance_vector = distance_vector * scaling_factor
    
    
def selection(parent, child):
    
    parent.update_profit()
    child.update_proft()
    
    if parent.profit >= child.profit:
        return parent
    else:
        return child



    
def user_input():
    #by Yannic(?)
    """
    Output List with control Parameters: [crossoverRate,scalingFactor,populationSize]
    """

    #Our three Control Parameters
    crossoverRate = -1
    scalingFactor = -1
    populationSize = -1
    costprice = -1
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
            #costprice
            output.append(0.6)
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
                scalingFactor = float(input("Please specify Scaling Factor in [0,1]: "))
            else:
                scalingFactor = float(input("Scaling Factor must be must be in [0,1]: "))
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
        #Scaling factor F e (0,1)
        while (costprice <= 0) or (costprice > 1):
            if costprice == -1:
                costprice = float(input("Please specify Cost Price in [0,1[: "))
            else:
                costprice = float(input("Cost Price must be must be in [0,1[: "))
        output.append(costprice)



    return output
  
def __MAIN__():
    init()
    userinput = user_input()
    
    crossoverRate = userinput[0]
    scalingFactor = userinput[1]
    populationSize = userinput[2]
    CostPrice = userinput[3]
    
    pop = initalize_population(agentcount)
    newpop = donor_selection(pop,scalingFactor)
    
__MAIN__()