# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:15:51 2017

@author: JoJo
"""

import random
import prettytable

class Sackitem:
    def __init__ (self, weight, value):
        self.weight = weight
        self.value = value
        
class individual:
    def __init__(self, genome, ttlweight, ttlvalue, fitness):
        self.genome = genome
        self.mass = ttlweight
        self.value = ttlvalue
        self.fitness = fitness
        


def generatesack(nmbrofitems):
    """This function generates a list of items with random weight/value pairs.
    """
    while nmbrofitems != 0:
        newitem = Sackitem(random.randint(1,10),random.randint(1,20))
        itemlist.append(newitem)
        nmbrofitems -= 1
    return itemlist
      
def geninitialpopulation(counter,itemlist):
    itemlen = len(itemlist)
    population = []
    while counter != 0:
        newgene = []
        for index in range(itemlen):
            gene = random.randint(0,1)
            newgene.append(gene)
        population.append(newgene)
        counter -= 1
    population = populationconstruction(population)
    return population

def evolution(inipop):
    """This function controlls the evolutionary cascade until after 25 consecutive generations, no new better individuals was generated
    in: initial population: list of individuals out: best individual after 25 generations with no change
    """
    popmorph = inipop
    countgenerations = 0
    terminalcount = 0
    bestindiv = inipop[0]
    print("initializing with fitness: ",bestindiv.fitness)
    
    
    while terminalcount != 25:
        

        selection(popmorph)
        
        generationsbest = top_individual(popmorph)
        print("evaluating generation: ",countgenerations)
        countgenerations += 1
        
        
        if generationsbest.fitness > bestindiv.fitness:
            
            bestindiv = generationsbest
            print("Better individual found in generation",countgenerations,"! Top fitness now: ",bestindiv.fitness)
            terminalcount = 0
        else:
            terminalcount += 1

        
        
        popmorph = next_generation(popmorph)
        
        
    return(bestindiv, countgenerations)
        
        
def top_individual(sortedpop):
    """input: sorted and cut list of individuals, output: best individual"""
    topobject = sortedpop[-1]
    return topobject

def selection(population):
    """input: List of individuals, output: sorted and cut list of individuals
    """
    sortedpop = sorted(population, key=lambda individual: individual.fitness)
    toplist = sortedpop[:len(sortedpop)//2]
    return toplist
         
def next_generation(population):
    """input: last generation as list of individual objects, output: a new generation generated from combinging genes from the old one"""
    maxindex = len(population)
    currentgenomes = []
    newgeneration = []
    
    if len(population) %2 == 1:
        del population[0]
    
    for item in population:
        currentgenomes.append(item.genome)
    while maxindex != 0:

        
        getgene1 = random.randint(0,len(currentgenomes)-1)
        parentgene1 = currentgenomes[getgene1]
        del currentgenomes[getgene1]
        
 
        getgene2 = random.randint(0,len(currentgenomes)-1)
        parentgene2 = currentgenomes[getgene2]
        del currentgenomes[getgene2]
        
        cutpoint = random.randint(0,len(parentgene1)-1)
        
        child1 = parentgene1[:cutpoint] + parentgene2[cutpoint:]
        child2 = parentgene2[:cutpoint] + parentgene2[cutpoint:]
        
        
        newgeneration.append(child1)
        newgeneration.append(child2)
        maxindex -= 2
    mutate(newgeneration) 
    final_generation = populationconstruction(newgeneration)
    return final_generation
        
def mutate(population):
    """Input: List of binaries, output: list of binaries with mutated individual"""
    choosemutant = random.randrange(len(population))
    mutant = population[choosemutant]
    del population[choosemutant]
    choosegene2mutate = random.randrange(len(mutant))
    
    if mutant[choosegene2mutate] == 1:
        mutant[choosegene2mutate] = 0
    else:
        mutant[choosegene2mutate] = 1
    population.append(mutant)
    
    return population
        
    
def populationconstruction(listoflist):
    """Input: List of Binary strings, output: new list of individual objects with fitness, weight, value"""
    returnfinishedpopulation = []
    for item in listoflist:
        attributelist = []
        totalweight = 0
        totalvalue = 0
        totalfitness = 0
        iterator = 0
        for index in item:
            if index == 1:
                attributelist.append(itemlist[iterator])
                iterator += 1
            else:
                iterator += 1
        
        for attributeindex in attributelist:
            totalweight = totalweight + attributeindex.weight
            totalvalue = totalvalue + attributeindex.value
        if totalweight > weightlimit:
            totalfitness = -1
        else:
            totalfitness = totalvalue
        newindividual = individual(item,totalweight,totalvalue,totalfitness)
        returnfinishedpopulation.append(newindividual)
    return returnfinishedpopulation
            
  
def initalize():
    """This function requests user input to generate a high-number search space or a low-number search space and handles all console output
    """
    global itemlist
    global limit
    global weightlimit
    global indivcount

    
    itemlist = []
    
    limit = 50000
    print("Initializing with ",limit," Items to choose from")
    sack = generatesack(limit)
    
    weightlimit = 0
    for i in sack:
        weightlimit += i.weight
    weightlimit = weightlimit//2
    print("The napsack weightlimit is: ", weightlimit)
    
    indivcount = 200
    print("Initializing with ",indivcount," Individuals per generation")
    takelist = geninitialpopulation(indivcount, sack)
    final_output = evolution(takelist)
    
    generations = final_output[1]
    final_output = final_output[0]
    
    print("\n")
    print("Best individual:")
    bestindiv = prettytable.PrettyTable()
    bestindiv.field_names = ["weight","total value","fitness"]
    bestindiv.add_row([final_output.mass,final_output.value,final_output.fitness])
    print(bestindiv)
    print("Best solution acheived after ",generations, " generations!")
    print("Distance to weightlimit: ",weightlimit - final_output.mass)

    
    

   
initalize()