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

def crossover2():
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
    recomMethod = 1
    while not matingpool:
        sizeMatingPool = len(matingpool)-1
        choice1 = -1
        choice2 = -1

        while choice1 == choice2:
            choice1 = random.randint(0,sizeMatingPool)
            choice2 = random.randint(0,sizeMatingPool)

        if recomMethod == 1:
            c1,c2 = onepoint(matingpool[choice1],matingpool[choice2])
            children.append(c1)
            children.append(c2)
            matingpool.remove(matingpool[choice1])
            matingpool.remove(matingpool[choice2])
        '''
        elif recomMethod == 2:
            c1,c2 = crossover2(matingpool[choice1],matingpool[choice2])
            children.append(c1)
            children.append(c2)
        '''

    return children



