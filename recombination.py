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
    #copy sublists of p1 and p2 into the childs
    for i in range(cutpoint):
        c1.append(p1[i])
        c2.append(p2[i])
    #copy second sublists of p1 and p2 into the childs
    for j in range(cutpoint,parentlength+1):
        c1.append(p2[j])
        c2.append(p1[j])
    return c1,c2

def method2():
    '''
    TODO
    '''
    return true

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
            c1,c2 = method2(parent1,parent2)

        #add new children to the set of all children
        children.append(c1)
        children.append(c2)
        #remove the parents from the matingpool
        matingpool.remove(parent1)
        matingpool.remove(parent2)




    #return the new subset of children 
    return children

