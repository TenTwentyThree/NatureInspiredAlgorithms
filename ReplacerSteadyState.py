# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 14:27:32 2017

@author: Till
"""

# Selects n random individuals and replaces them with the n children
import random


def steadystate(population, children):
    childrensize = len(children)
    populationsize = len(population) - 1

    # select random parents from the population and remove them
    for i in range(0, childrensize):
        kill = random.randint(0, populationsize)
        population.remove(population[kill])
        populationsize = populationsize - 1

    # Children take place in new population
    for i in range(0, childrensize):
        population.append(children[i])

    print(population)
    return population

def steady_state(population, children):
    number_of_selected = random.randint(1,len(population))
    while number_of_selected > 0:
        
