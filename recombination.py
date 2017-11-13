# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 08:39:05 2017

@author: yj
"""

import random


def onepoint(p1,p2):
    '''
    Generate a crossover point and then copy
    sublist 1 of p1 in c1 and of p2 in c2 and then copy
    sublist 2 of p1 in c2 and of p2 in c1
    '''
    parentlength = (len(p1)-1)
    #create children 1 and 2
    c1 = []
    c2 = []
    #generate random cuttpoint
    cutpoint = random.randint(1,parentlength)
    #Copy Sublist into respective parents
    c1, c2 = ([p1[:cutpoint] + p2[cutpoint:]], [p2[:cutpoint] + p1[cutpoint:]])
    return c1,c2

def uniformCrossover(p1,p2):
    #save parentlenth for quick exces
    parentlength = (len(p1))
    #define a treshold to choose from which parent you take the genom
    threshold = 0.5
    c1=[]
    c2=[]

    #create a random template of length parentlength with values (0,1)
    template = []
    for i in range(parentlength):
        template.append(random.uniform(0,1))
    print(template)

    '''
    iterate though the parents, if value of template is bigger than threshold
    copy gene from p1 in c1 else p2 (and respectively for c2)
    '''
    for i in range(parentlength):
        if template[i] > threshold:
            c1.append(p1[i])
            c2.append(p2[i])
        else:
            c1.append(p2[i])
            c2.append(p1[i])
    #return the new children
    return c1,c2

def recombine(matingpool):
    '''
    Get's the selected matingpool and returns a sub-population with the recombined
    childs
    '''
    children = []
    #which reombination method we want to use, untill now just 1
    recomMethod = 1

    #recombine 2 parents from the matingpool untill the mating pool ist empty
    while len(matingpool) > 0:
        #in every iteration compute the matingpool size again, because its shrinking
        sizeMatingPool = len(matingpool)-1
        choice1 = -1
        choice2 = -1

        #select two random differnet parents from the mating pool
        while choice1 == choice2:
            choice1 = random.randint(0,sizeMatingPool)
            choice2 = random.randint(0,sizeMatingPool)

        #save the two parents
        parent1 = matingpool[choice1]
        parent2 = matingpool[choice2]

        #execute the recombination method of your choice and save the new children in c1 and c2
        if recomMethod == 1:
            c1,c2 = onepoint(parent1,parent2)
        elif recomMethod == 2:
            c1,c2 = uniformCrossover(parent1,parent2)

        #add new children to the set of all children
        children.append(c1)
        children.append(c2)
        #remove the parents from the matingpool
        matingpool.remove(parent1)
        matingpool.remove(parent2)





    return children




