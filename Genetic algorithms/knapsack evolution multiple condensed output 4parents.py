# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:15:51 2017

@author: JoJo
"""

import random
import prettytable
import xlsxwriter

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
    
    
    while terminalcount != 25:
        

        selection(popmorph)
        
        generationsbest = top_individual(popmorph)

        countgenerations += 1
        
        
        if generationsbest.fitness > bestindiv.fitness:
            
            bestindiv = generationsbest

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
    
    if len(population) %4 == 1:
        del population[0]
        
    if len(population) %4 == 2:
        del population[0]
        del population[1]
        
    if len(population) %4 == 3:
        del population[0]
        del population[1]
        del population[2]
    maxindex = len(population)
    
    for item in population:
        currentgenomes.append(item.genome)
    while maxindex != 0:

        sublist = []
        getgene1 = random.randint(0,len(currentgenomes)-1)
        parentgene1 = currentgenomes[getgene1]
        del currentgenomes[getgene1]
        
 
        getgene2 = random.randint(0,len(currentgenomes)-1)
        parentgene2 = currentgenomes[getgene2]
        del currentgenomes[getgene2]
        
        getgene3 = random.randint(0,len(currentgenomes)-1)
        parentgene3 = currentgenomes[getgene3]
        del currentgenomes[getgene3]
        
 
        getgene4 = random.randint(0,len(currentgenomes)-1)
        parentgene4 = currentgenomes[getgene4]
        del currentgenomes[getgene4]
        
        cutpoint = random.randint(0,len(parentgene1)-1)
        cutpoint2 = random.randint(0,len(parentgene1)-1)
        cutpoint3 = random.randint(0,len(parentgene1)-1)
        cutpoint4 = random.randint(0,len(parentgene1)-1)
        
        child1 = parentgene1[:cutpoint] + parentgene2[cutpoint:]
        child2 = parentgene2[:cutpoint2] + parentgene2[cutpoint2:]
        child3 = parentgene3[:cutpoint3] + parentgene2[cutpoint3:]
        child4 = parentgene4[:cutpoint4] + parentgene2[cutpoint4:]
        
        sublist.append(child1)
        sublist.append(child2)
        sublist.append(child3)
        sublist.append(child4)
        
        fingene1 = random.randint(0,len(sublist)-1)
        pargene1 = sublist[fingene1]
        del sublist[fingene1]
        
 
        fingene2 = random.randint(0,len(sublist)-1)
        pargene2 = sublist[fingene2]
        del sublist[fingene2]
        
        fingene3 = random.randint(0,len(sublist)-1)
        pargene3 = sublist[fingene3]
        del sublist[fingene3]
        
 
        fingene4 = random.randint(0,len(sublist)-1)
        pargene4 = sublist[fingene4]
        del sublist[fingene4]
        
        
        sncutpoint = random.randint(0,len(parentgene1)-1)
        sncutpoint2 = random.randint(0,len(parentgene1)-1)
        sncutpoint3 = random.randint(0,len(parentgene1)-1)
        sncutpoint4 = random.randint(0,len(parentgene1)-1)
        
        finchild1 = pargene1[:sncutpoint] + parentgene2[sncutpoint:]
        finchild2 = pargene2[:sncutpoint2] + parentgene2[sncutpoint2:]
        finchild3 = pargene3[:sncutpoint3] + parentgene2[sncutpoint3:]
        finchild4 = pargene4[:sncutpoint4] + parentgene2[sncutpoint4:]
        
        
        
        
        
        
        newgeneration.append(finchild1)
        newgeneration.append(finchild2)
        newgeneration.append(finchild3)
        newgeneration.append(finchild4)
        
        maxindex -= 4
        
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
    weightlimit = 0
    limit = 0
    indivcount = 0
    
    
    limit = 10000
    sack = generatesack(limit)
    
    
    for i in sack:
        weightlimit += i.weight
    weightlimit = weightlimit//2

    
    indivcount = 10
    takelist = geninitialpopulation(indivcount, sack)
    final_output = evolution(takelist)
    
    final_output = final_output[0]
    

    return (weightlimit, final_output.mass)

def run_and_create():
    worksheetweight = []
    worksheetvalue = []
    workbook = xlsxwriter.Workbook('Numericoutput4parents10000 10 50.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    row2 = 0
    col = 0
    nmb = 0
    
    
    times = 50
    while times != 0:
        chartdump = initalize()
        worksheetweight.append(chartdump[0])
        worksheetvalue.append(chartdump[1])
        nmb += 1
        print("Processing iteration #",nmb)
        times -= 1
        
    for item in worksheetweight:
        worksheet.write(row, col,     item)
        row += 1
        
    for val in worksheetvalue:
        worksheet.write(row2, col + 1,  val)
        row2 += 1
        
    workbook.close()

run_and_create()

        
    
    
    
    
    
    
    
    
    