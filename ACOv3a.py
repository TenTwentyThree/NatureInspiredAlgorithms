# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:31:29 2017

@author: Johannes
"""

import numpy as np
import random

class ant():
    def __init__(self, alpha,beta,path):
        self.alpha = alpha
        self.beta = beta
        self.path = path
        
    def return_path_length(self):
        totalcost = 0
        for item in self.path:
            totalcost = totalcost + item
        return totalcost
    
    def choose_initial_path(self):
        ycoordinates = list(range(1,150))
        startingpoint = 0
        endpoint = 0
        #we start at city 0 and choose a random city
        #we technically don't need the endpoint variable but I kept it here to make the code more readable
        
        newpath = []
        
        while len(ycoordinates) != 1:
            chosencity = random.choice(ycoordinates)
            newpath.append(city_matrix[startingpoint][chosencity])
            startingpoint = chosencity
            ycoordinates.remove(chosencity)
        newpath.append(city_matrix[startingpoint][endpoint])
        
        self.path = newpath
    
    def choose_beta_path(self)
    
def initialize_ants(numberofants):
    colony = []
    while numberofants !=0:
        newant = ant(glob_alpha, glob_beta, [])
        newant.choose_initial_path()
        colony.append(newant)
        numberofants -= 1
    return colony


    
    
    
    
    
    
        
    
def read_file(filename):
    """
    This function reads in the tsp files and converts them into int matrices. The matrix can be accessed globably with the variable name tspmat
    """
    if filename == 1:
        tspmat = np.loadtxt("1.tsp")

    if filename == 2:
        tspmat = np.loadtxt("2.tsp")

    if filename == 3:
        tspmat = np.loadtxt("3.tsp")


    valuematrix = tspmat.astype(int)
    
    return valuematrix

def initalize():
    global glob_alpha
    global glob_beta
    global city_matrix
    
    benchmark = int(input("Please specify benchmark file number: "))
    glob_alpha = 1
    glob_beta = 1
    city_matrix = read_file(benchmark)

initalize()