# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 16:23:12 2017

@author: Till
"""
import random
#randomly mutates one int to another. So gives a job to another machine.
#the mutation probability is set to 0.06
#needs a global variable numberOfMachines
def mutationRandomResetting(population):
    probability = 0.06
    populationsize = len(population)

#if the mutationprobability is matched we mutate the chromosome
    for i in range(populationsize):
        mutation = random.uniform(0,1)
        if mutation <= probability:
            mutate(population[i])
            
    print(population)
    
#mutates a specific machine to an other at a random place
#mutates a random allel in a chromosome
def mutate(chromosome):
    mutateMachine = random.randint(0,numberOfMachines)
    mutatePlace = random.randint(0,len(chromosome)-1)
    
#making sure that w do not mutate the one machine to the same machine
    while chromosome[mutatePlace] == mutateMachine:
        mutateMachine = random.randint(0,numberOfMachines)
        
    chromosome[mutatePlace] = mutateMachine
