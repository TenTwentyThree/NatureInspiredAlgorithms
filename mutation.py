# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 16:23:12 2017

@author: yj
"""
import random
#list with the probability of choosing the mutation
mutationChoice = [0,0,0]
numberOfMachines = 18

#random fitness function for testing
def fittnes(chromosome):
    return (10 - random.randint(0,20))




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
            # Choose random mutation method or the best one
            randorchoice = random.uniform(0,1)
            '''
            if randorchoice is bigger equal to 0.5 choose the best
            mutation method, else choose one by chance
            '''
            if randorchoice >= 0.5 :
                choice = mutationChoice.index(max(mutationChoice))
            else:
                choice = random.randint(0,2)

            #hold fitness of choromosom to compare later
            fit = fittnes(population[i])

            #mutate with the choosen method
            if choice == 0:
                #mutate
                population[i] = mutateRandomResetting(population[i])
            elif choice == 1:
                #mutate
                population[i] = mutateReverse(population[i])
            elif choice == 2:
                #mutate
                population[i] = mutateScramble(population[i])


            '''
            evaluate new fittnes, if the fittness is better,
            the method gets a better rank and is choosen more often.
            If the fittness is worse, it also gets a worse rank
            '''
            newfit = fittnes(population[i])
            fitdif = newfit-fit
            if fitdif > 0:
                mutationChoice[choice] += fitdif
            else:
                mutationChoice[choice] -= fitdif


    return population


def mutateRandomResetting(chromosome):
    '''
    mutates a specific machine to an other at a random place
    mutates a random allel in a chromosome
    '''
    mutateMachine = random.randint(0,numberOfMachines)
    mutatePlace = random.randint(0,len(chromosome)-1)

#making sure that w do not mutate the one machine to the same machine
    while chromosome[mutatePlace] == mutateMachine:
        mutateMachine = random.randint(0,numberOfMachines)

    chromosome[mutatePlace] = mutateMachine
    return chromosome


def mutateReverse(chromosome):
    chromosomesize = len(chromosome)

    m1 = -1
    m2 = -1
    while m2-m1 <= 2 :
        m1 = random.randint(0,chromosomesize-1)
        m2 = random.randint(0,chromosomesize-1)
    sublist = chromosome[m2:m1:-1]

    for i in range(m1+1,m2):
        chromosome[i] = sublist[i-m1]

    return  chromosome

def mutateScramble(chromosome):
    chromosomesize = len(chromosome)

    m1 = -1
    m2 = -1
    while m2-m1 <= 2 :
        m1 = random.randint(0,chromosomesize-1)
        m2 = random.randint(0,chromosomesize-1)
    sublist = chromosome[m1:m2]

    for i in range(m1,m2):
        sublistLength = len(sublist)-1
        gene = random.randint(0,sublistLength)
        chromosome[i] = sublist[gene]
        sublist.remove(sublist[gene])

    return chromosome


'''
chromosome = [1,2,3,4,5,6,7,8,9]
scramble(chromosome)
print(chromosome)

'''
population = [[1,2,3,"a","b","c"],[4,5,6,"e","f","g"],[7,8,9,"h","i","j"],[10,11,12,"k","l","m"],[13,14,15,"n","o","p"],[16,17,18,"q","r","s"]]
population = mutation(population)
print(mutationChoice)
print(population)
