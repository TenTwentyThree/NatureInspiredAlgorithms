# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 14:27:32 2017

@author: Till
"""

# Selects n random individuals and replaces them with the n children
import random


def steady_state(population, children):
    picklistparent = []
    number_of_selected = random.randint(1,len(population))
    print(number_of_selected)

    while number_of_selected > 0:
        
        selectreplaceparent = random.randint(0,len(population) - 1)
        selectreplacechild = random.randint(0,len(children) - 1)
        
        while selectreplaceparent in picklistparent:
            selectreplaceparent = random.randint(0,len(population) - 1)

            
        population[selectreplaceparent] = children[selectreplacechild]
        picklistparent.append(selectreplaceparent)
        
        del children[selectreplacechild]
        number_of_selected -= 1

    return population
