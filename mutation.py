# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 16:23:12 2017

@author: Till
"""
import random
#randomly mutates one int to another. So gives a job to another machine.
#the mutation probability is set to 0.06
#needs a global variable numberOfMachines
def mutation(population):
    probability = 0.06
    populationsize = len(population)

#if the mutationprobability is matched we mutate the chromosome
    for i in range(populationsize):
        mutation = random.uniform(0,1)
        if mutation <= probability:
            if mutation1:
                mutateRandomResetting(population[i])
            elif mutation2:
                mutateReverse(population[i])
    print(population)

#mutates a specific machine to an other at a random place
#mutates a random allel in a chromosome
def mutateRandomResetting(chromosome):
    mutateMachine = random.randint(0,numberOfMachines)
    mutatePlace = random.randint(0,len(chromosome)-1)

#making sure that w do not mutate the one machine to the same machine
    while chromosome[mutatePlace] == mutateMachine:
        mutateMachine = random.randint(0,numberOfMachines)

    chromosome[mutatePlace] = mutateMachine

def mutateReverse(chromosome):
    '''
    choose two rendom points and flip array in between 
    '''
    #save length for quick access
    chromosomesize = len(chromosome)

    m1 = -1
    m2 = -1
    #as long as m2 is smaller than m1 and make sure that they are at least 2 numbers appart 
    while m2-m1 <= 2 :
        #create points randomly
        m1 = random.randint(0,chromosomesize-1)
        m2 = random.randint(0,chromosomesize-1)
    print(m1)
    print(m2)
    #flip the sublist 
    sublist = chromosome[m2:m1:-1]
    
    #put sublist in chromosome at the respective position 
    for i in range(m1+1,m2):
        chromosome[i] = sublist[i-m1]

    return  chromosome
