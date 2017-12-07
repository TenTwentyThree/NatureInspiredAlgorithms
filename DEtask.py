# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:27:24 2017

@author: Johannes
"""

# - - - - - - - - - - - - - - - I N D I V I D U A L   D E F I N I T I O N - - - - - - - - - - - - - - - - - - 
class individual():
    def __init__(self,genome,revenue):
        self.genome = genome
        self.revenue = revenue
    def update_revenue():
        return None


#- - - - - - - - - - - - - - - M A I N - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
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
#- - - - - - - - - - - - - - - D O N O R  - - - - - - - - - - - - - - - - - - - - - - - - 
def donor_selection(population):
    """
    INPUT: Population, a list of objects containing vectors as a representation for genome projecting into the search-space
    OUTPUT: A list of tuples. Each tuple contains the target at position 1 (0) and the list of donor objects at position 2 (1)
    """
    target_position = 0
    target_and_donors_list = []
    #this is the output list, which contains tuples with the target at postion 1 and all donor individuals at 2
    while target_position != len(population):
        target_donors = population
        target = population[target_position]
        del target_donors[target_position]
        target_and_donors = (target, target_donors)
        target_and_donors_list.append(target_and_donors)
        target_position += 1
    return target_and_donors_list
        
        
        
        
#- - - - - - - - - - - - - - - U S E R   I N P U T - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def user_input():
    return None