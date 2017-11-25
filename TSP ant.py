# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:33:10 2017
@author: JoJo
"""

import numpy as np

class ant:
    def __init__(self,possible_locations, path, pathCost):
        """
        initialize an ant, to traverse the map
        possible_locations -> a list of possible locations the ant can travel to
        path -> a list of integers, where each integer represents a city, and the path[i] to the path[i+1] entrence is an edge the ant has traveled 
        pathCost -> cost, in this case the sum of the edgecosts the ant has traveled
        """
        
        self.possible_locations = [range(0,149)]
        self.path = []
        self.pathCost = 0

        
    def path_length(self):
        """
        This function updates the length of the path the ant has traveled 
        """
        for i in range(len(self.path)-1):
            self.pathCost += pathMat[self.path[i]][self.path[i+1]]
            
    
    def update_path(self, edge):
        """
        Adds a new node to self.path and
        removes the pass from self.possible_locations so we can't visit nods twice 
        """
        self.path.append(edge)
        self.possible_locations.remove(edge)
        
    def walk(self):
        """
        selects the next City to go to and updates the chosen path
        """
    
        while self.possible_locations:
            nextCity = choseCity()
            update_path(nextCity)
            
    def choseCity(self,citiesToVisit):
         """choses the next city based on the pheromone level
            calculate the attractiveness of each possible transition from the current location
            then randomly choose a next path, based on its attractiveness
        
        to be done
        """
    
    def findSolution(self):
        """
        As long as the 
        """
        while self.possible_locations:
            next_city = self.walk()
            self.update_path()
        
        
    
    def get_pathCost(self):
        if 
            
def BestWay(ants):    
    """
    Evaluates the best way in this iteration, concidering all path_lengths of all ants
    input: list of all ants
    output: bestWay: Integer value for the shortest way found
    """
    bestWay = ants[0].path_length()
    for ant in ants:
        if ants[ant].path_length() < bestWay:
            bestWay = ants[ant].path_length()
                
    return bestWay



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

def mainloop():
    """
    ACO scheme:
 
    repeat
        for ant k ∈ {1,...,m}
             construct a solution
        endfor
        forall pheromone values do
            decrease the value by a certain percentage {evaporation}
        endfor
        forall pheromone values corresponding to good solutions
        do
            increase the value {intensification}
        endfor
    until stopping criterion is met
    """
    
    for ant in AntColony:
        ant.findSolution()
     
            



def initalize(benchmark, antnmbr):
    global tspmat
    tspmat = read_file(benchmark)
    createAnts(antnmbr)
    

def createAntColony(antnmbr):
    """
    creates an array 'ant' with as many ant-objects in it as user input wanted
    """
    AntColony = []
    for i in range(0,antnmbr):
        AntColony.append(ant)
        
    
def user_input():
    benchmark = int(input("Please specify TSP benchmark to use [1],[2],[3]: "))
    antnmbr = int(input("Please specify number of ants to be used: "))
    
    initalize(benchmark, antnmbr)
    
    
user_input()
