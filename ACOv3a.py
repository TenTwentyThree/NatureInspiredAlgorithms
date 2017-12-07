# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:31:29 2017

@author: Johannes
"""

import numpy as np
import random

class ant():
    def __init__(self, alpha,beta,path,cost):
        self.alpha = alpha
        self.beta = beta
        self.path = path
        self.cost = cost
        
    def update_cost(self):
        totalcost = 0
        for item in self.path:
            totalcost = totalcost + item
        self.cost = totalcost
    

        
class colony():
    def __init__(self, numberofants, totalvalue, bestpath, evapconstant, pherofact):
        self.colony = []
        self.numberofants = numberofants
        self.totalvalue = totalvalue
        self.bestpath = []
        self.evapconstant = evapconstant
        self.pherofact = pherofact
        
    def initialize_ants(self,numberofants):
        newcolony = []
        while numberofants !=0:
            newant = ant(alpha, beta, [], 0)
            choose_initial_path(newant)
            newcolony.append(newant)
            numberofants -= 1
        self.colony = newcolony
    
    def return_best_ant(self):
        for ant in colony:
            ant.update_cost()
        best = sorted(colony, key=lambda individual: ant.cost)
        topant = best[-1]
        self.bestpath = topant.path
        self.totalvalue = topant.cost
        
def create_pheromone_matrix():
    w = 150
    h = 150
    p_matrix = [[0 for x in range(w)] for y in range(h)]
    return p_matrix
        
def update_pheromone_matrix(pheromone_matrix):
    
    updated_matrix = pheromone_matrix
    for xcoordinates in updated_matrix:
        for ycoordinates in xcoordinates
            ycoordinates = ycoordinates * p_factor
    return updated_matrix

def choose_initial_path(someant):
    
    ycoordinates = list(range(1,150))
    startingpoint = 0
    endpoint = 0
        #we start at city 0 and choose a random city
        #we technically don't need the endpoint variable but I kept it here to make the code more readable
        
    newpath = []
    while len(ycoordinates) != 0:
        chosencity = random.choice(ycoordinates)
        newpath.append(city_matrix[startingpoint][chosencity])
        pheromone_matrix[startingpoint][chosencity] += len(ycoordinates) / 100
        startingpoint = chosencity
        ycoordinates.remove(chosencity)
    newpath.append(city_matrix[startingpoint][endpoint])
    someant.path = newpath
    
        
            
        
        
             

    
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
    
def user_input():
    global antnmbr
    global p_evap_co
    global p_factor
    global alpha
    global beta
    global iterations
    global default
    global city_matrix
    


    benchmark = -1
    antnmbr = -1
    p_evap_co = -1
    p_factor = -1
    alpha = -1
    beta = -1
    iterations = -1
    default = -1


    print("#----- USERINTERFACE - Input 0 for a default Value -----#")

    #Default
    while (default != 0) or (default != 1):
        default = int(input("Do yo want to use default values? [0]Yes  [1]No: "))
        if default == 0:
            benchmark = 2
            antnmbr = 50
            p_evap_co = 0.4
            p_factor = 0.4
            alpha = 1
            beta = 1
            iterations = 20
            city_matrix = read_file(benchmark)
            return None
        if default == 1:


            #Benchmark Input
            while (benchmark != 0) and (benchmark != 1) and (benchmark != 2) and (benchmark != 3):
                if benchmark == -1:
                    benchmark = int(input("Please specify TSP benchmark to use [1],[2],[3]: "))
                else:
                    benchmark = int(input("Benachmark must be [1],[2],[3]: "))
                if benchmark == 0:
                    benchmark = 1
            #AntNumber Input
            while antnmbr < 0:
                if antnmbr == -1:
                    antnmbr = int(input("Please specify number of ants to be used: "))
                else:
                    antnmbr = int(input("Please specify number of ants (must be 0 for default or higher): "))
                if antnmbr == 0:
                    antnmbr = 20
            #Evaporation constant
            while p_evap_co < 0:
                if p_evap_co == -1:
                    p_evap_co = float(input("Please specify Evaporation Constant: "))
                else:
                    p_evap_co = float(input("Please specify Evaporation Constant bigger than 0 or zero for default: "))
                if p_evap_co == 0:
                    p_evap_co = 0.4
            #Pheromone Factor
            while p_factor < 0:
                if p_factor == -1:
                    p_factor = float(input("Please specify Intensification Constant: "))
                else:
                    p_factor = float(input("Please specify Intensification Constant:  bigger than 0 or zero for default: "))
                if p_factor == 0:
                    p_factor = 0.4
            #Alpha
            while alpha < 0:
                if alpha == -1:
                    alpha = float(input("Please specify Alpha Value(no default): "))
                else:
                    alpha = float(input("Please specify Alpha Value bigger or equal to zero: "))
            #beta
            while beta < 0:
                if beta == -1:
                    beta = float(input("Please specify Beta Value: "))
                else:
                    beta = float(input("Please specify Beta Value bigger or equal to zero: "))
            while iterations < 1:
                if iterations == -1:
                    iterations = int(input("Please specify the number of iterations before termination: "))
                else:
                    iterations = int(input("Please specify the number of iterations before termination that is bigger than 0 or 0 for default: "))
                if iterations == 0:
                    iterations = 20
            print("")
            print("Initialize ACO with:")
            print("")
            print("Benchamrk: ",benchmark)
            print("Number of ants: ",antnmbr)
            print("Evaporation Coefficient: ",p_evap_co)
            print("Pheromone Constant: ",p_factor)
            print("Alpha Value: ",alpha)
            print("Beta Value: ",beta)
            print("Terminate after  ",iterations," Iterations.")
            print("")
            city_matrix = read_file(benchmark)
            return None



    
    
def __MAIN__():
    user_input()
    global pheromone_matrix
    pheromone_matrix = create_pheromone_matrix()
    newcolony = colony(antnmbr, 0, [], p_evap_co, p_factor)
    while iterations != 0:
        return None
        
    
    
__MAIN__()