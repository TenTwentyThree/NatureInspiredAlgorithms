# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:08:00 2017

@author: Johannes
"""

import random as rnd
import numpy as np
import math

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
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
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
    market1.maxDemand + market2.maxDemand + market3.maxDemand )
    
    
    
    
    
    
def initalize_population(agentcount):
    
    population = []
    while agentcount != 0:
        
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
    return population
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
donor_selection -> differential_mutation -> genetic_crossover - > gene_edit - > selection
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        
def donor_selection(population, scaling_factor):
    new_population = []
    for individual in population:
        copy_population = population
        
        base_vector = rnd.choice(copy_population)
        copy_population.remove(base_vector)
        
        x1 = rnd.choice(copy_population)
        copy_population.remove(x1)
        
        x2 = rnd.choice(copy_population)
        
        survivor = differential_mutation(individual, base_vector, x1, x2, scaling_factor)
        new_population.append(survivor)
    return new_population

def differential_mutation(target, base_vector, x1_vector, x2_vector, scaling_factor):
    
    target_genes = target.genome
    
    distance_vector = np.subtract(x1_vector.genome, x2_vector.genome)
    distance_vector = distance_vector * scaling_factor
    
    donor_genome = np.add(base_vector.genome,distance_vector)
    
    gene_edit(target)
    
    child = genetic_crossover(target_genes, donor_genome)
    
    gene_edit(child)
    
    fighting_pit = selection(target,child)
    return fighting_pit
    
    
    
def genetic_crossover(target_genes, donor_genes):
    pointer = 0
    new_genome = []
    
    while pointer != len(target_genes) - 1:
        
        cross = rnd.uniform(0,1)
        
        if cross > crossoverRate:
            new_genome.append(target_genes[pointer])
        else:
            new_genome.append(donor_genes[pointer])
        pointer += 1
    child = individual(new_genome)
    child.update_profit()
    return child
            
            
def gene_edit(individual):
    """
    This function searchs for genes that project outside of the boundaries of the search space and returns them into the boundaries
    """
    edited_genes = []
    
    production = individual.genome[:3]
    distribution = individual.genome[2:5]
    
    price1 = individual.genome[6]
    price2 = individual.genome[7]
    price3 = individual.genome[8]
    
    for product in production:
        if production > max_power or production < 0:
            edited_genes.append(max_power)
        else:
            edited_genes.append(product)
            
    for distributer in distribution:
        if distributer > max_demand or distributer < 0:
            edited_genes.append(max_demand)
        else:
            edited_genes.append(distributer)
    
    if price1 > market1.maxPrice or price1 < 0:
        edited_genes.append(market1.maxPrice)
    else:
        edited_genes.append(price1)
        
    if price1 > market2.maxPrice or price2 < 0:
        edited_genes.append(market2.maxPrice)
    else:
        edited_genes.append(price2)
        
    if price3 > market3.maxPrice or price3 < 0:
        edited_genes.append(market3.maxPrice)
    else:
        edited_genes.append(price3)
    
    individual.genome = edited_genes
    individual.update_profit()
    return individual

    

    
def selection(parent, child):
    
    parent.update_profit()
    child.update_proft()
    
    if parent.profit >= child.profit:
        return parent
    else:
        return child

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
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
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def evaluate_self(individual):
    
    production_genome = individual.genome[:3]
    distribution_genome = individual.genome[3:6]
    price_genome = individual.genome[6:9]
    
    
    production_cost = evaluate_production_costs(production_genome)
    
    market_demand_1 = demand(price_genome[0], market1)
    market_demand_2 = demand(price_genome[1], market2)
    market_demand_3 = demand(price_genome[2], market3)
    

def evaluate_production_costs(plant_genome):
    cost_plant_1 = plantTypeCost(plant_genome[0],powerplant1)
    cost_plant_2 = plantTypeCost(plant_genome[1],powerplant2)
    cost_plant_3 = plantTypeCost(plant_genome[2],powerplant3)
    
    total_production_costs = cost_plant_1 + cost_plant_2 + cost_plant_3
    return total_production_costs

def plantTypeCost(s, plant):
    """ 
    calculates the cost we will have to build n plants of type p
    
    INPUT
    - s (desired amount of energy)
    - planttype
    
    """
    kwhPerPlant = plant.kwhPerPlants
    maxPlants =  plant.maxPlants
    costPerPlant = plant.costPerPlant
    # if s non-positive, return 0
    if(s <= 0):
        return 0
    
    #if x larger than possible generation, return infinite
    psblgen = kwhPerPlant * maxPlants
    if(s > psblgen):
        return float('inf')
    
    #otherwise find amount of plants needed to generate s
    plantsNeeded = math.ceil(s / kwhPerPlant)
    
    #return cost (amount of plants * cost per plant)
    return plantsNeeded * costPerPlant

    

def demand(sellingPrice, market):
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
    
    maxPrice = market.maxPrice
    maxDemand = market.maxDemand
    
    #if the selling price is greater than what customers want to pay, return 0
    if (sellingPrice > maxPrice):
        return 0
    
    if sellingPrice < 0:
        return 0
    
    #if nothing is produced for market
    if (sellingPrice <= 0):
        return maxDemand
    
    #else determine the demand based on the selling price
    demand = maxDemand - sellingPrice**2 * maxDemand / maxPrice**2
    
    return demand
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  

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
    global crossoverRate
    
    crossoverRate = userinput[0]
    scalingFactor = userinput[1]
    populationSize = userinput[2]
    CostPrice = userinput[3]
    
    pop = initalize_population(agentcount)
    newpop = donor_selection(pop,scalingFactor)
    
__MAIN__()