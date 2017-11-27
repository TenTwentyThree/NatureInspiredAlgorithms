# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:33:10 2017
@author: JoJo, yj, tn
"""

import numpy as np
import random
from numpy.random import choice


class ant:
    def __init__(self):
        """
        initialize an ant, to traverse the map
        possible_locations -> a list of possible locations the ant can travel to
        path -> [1,2,5,3,4,6,1] a list of integers, where each integer represents a city, and the path[i] to the path[i+1] entrance is an edge the ant has traveled
        pathCost -> cost, in this case the sum of the edgecosts the ant has traveled
        """

        self.possible_locations = list(range(len(tspmat)))
        self.path = [0]
        self.pathCost = 0

#----------------------------------Solution Construction-------------------------------


    def findSolution(self):
        """
        As long as the List of possible next location self.possible_locations is not empty
        we chosse the next City and update the path
        """
        while self.possible_locations:
            # first chose the next city
            next_city = self.choseCity()
            # update the path with the new city
            self.update_path(next_city)
            # updte the path cost of the ant
            self.update_pathCost()


    def choseCity(self):
        """choses the next city based on the pheromone level
            calculate the attractiveness of each possible transition from the current location
            then randomly choose a next path, based on its attractiveness
        """
        current_location = self.get_location()
        possible_locations = self.possible_locations

        # probabilitys to visit the node, mapped over the possible_locations list
        pathProbabilities = []
        #List with all numerator values for each possible next_location
        numeratorList= []
        #Total sum of te denumerator, still has to be computed
        total_sum = 0
        # Compute the numerator for every possible node and save in the numeratorList
        for i in range(len(self.possible_locations)):
            #get the pheromone_amount for the possible nect location and the distance between those cities
            pheromone_amount = pheromone_map[current_location][possible_locations[i]]
            distance = float(1/tspmat[current_location][possible_locations[i]])

            #fill the numerator list
            numeratorList.append(pow(pheromone_amount, alpha)*pow(1/distance, beta))
        #compute the denominator
        denominator = sum(numeratorList)

        #compute the path probabilities by deviding the numerator with the deonominator
        for i in range(len(self.possible_locations)):
            pathProbabilities.append(numeratorList[i]/denominator)



        draw = choice(possible_locations, 1, p=pathProbabilities)
        next_node = draw[0]
        return next_node
        #randomly choose the next path
        #Not quit shure about this
        toss = random.random()

        cummulative = 0
        for possible_next_location in pathProbabilities:
            weight = possible_next_location
            if toss <= weight + cummulative:
                return self.possible_locations[pathProbabilities.index(possible_next_location)]
            cummulative += weight

#----------------------------------Solution Construction Ends-------------------------------



    def update_pathCost(self):
        """
        This function updates the Cost (length) of the path the ant has traveled
        """
        self.pathCost = 0
        for i in range(len(self.path)-1):
            self.pathCost += tspmat[self.path[i]][self.path[i+1]]


    def update_path(self, city):
        """
        Adds a new node to self.path and
        removes the pass from self.possible_locations so we can't visit nods twice
        """
        self.path.append(city)
        self.possible_locations.remove(city)

    def get_pathCost(self):
        """
        get the past cost
        """
        if len(self.possible_locations) != 0:
            return self.pathCost
        return None

    def get_path(self):
        """
        get the path, if it's created completely
        """
        #if len(self.possible_locations) != 0:
        path = self.path
        return path
        #return None

    def get_location(self):
        """
        return the current location of the ant
        """
        path = self.path
        return path[-1]



# ------------------------PheromoneUpdate Class 2.0----------------------------
def evaporation():
    p_map = pheromone_map
    pheromone_factor = 1 - pheromone_evap_constant
    for i in range(len(p_map)):
        for j in range(len(p_map)):
            p_map[i][j] = p_map[i][j] * pheromone_factor
    return p_map

def intensification(antColony):
    p_map = pheromone_map

    for ant in antColony:
        path = ant.path
        for node in range(len(path)-2):
            pheromone_map[path[node]][path[node+1]] = pheromone_map[path[node]][path[node+1]] + pheromoneConstant/ant.pathCost
            pheromone_map[path[node]][path[node+1]] = pheromone_map[path[node]][path[node+1]] + pheromoneConstant/ant.pathCost


    return p_map



def update_pheromone_map(antColony):

    #evaporate and intensify the phromone map
    pheromone_map = evaporation()
    pheromone_map = intensification(antColony)

    #return the updated pheromone map
    return pheromone_map



# ------------------------PheromoneUpdate Class 2.0 Ends-----------------------
def bestAnt(antColony):
    """
    Evaluates the best way in this iteration, concidering all path_lengths of all ants
    input: list of all ants
    output: bestWay: Integer value for the shortest way found
    """
    bestAnt = antColony[0].pathCost
    for ant in antColony:
        if ant.pathCost < bestAnt:
            bestWay = ant.pathCost

    return bestAnt



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

#----------------------------------Main loop-------------------------------

def mainloop():
    """
    ACO scheme:

    repeat
        for ant k ∈ {1,...,m}
             construct a solution {solution finding}
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

    best_path = []

    while "Terminationcondition":

        antColony = createAntColony(antnmbr)

        #create pathes for every ant in the ANt AntColony
        for ant in antColony:
            ant.findSolution()

        #update pheromone mappe
        pheromone_map = update_pheromone_map(antColony)

        bestAntLength = bestAnt(antColony)
        print("Best Length: ", bestAntLength)

    return best_path

#----------------------------------Main loop Ends-------------------------------


def initalize(benchmark, antNumber,p_Constant, evapConst):
    global tspmat
    global pheromone_map
    global pheromone_evap_constant
    global pheromoneConstant
    global antnmbr
    global alpha
    global beta
    tspmat = read_file(benchmark)
    antnmbr = antNumber
    pheromone_map = create_pheromone_map()
    pheromone_evap_constant = evapConst
    pheromoneConstant = p_Constant
    alpha = 1
    beta = 0


    #create a pheromone map similar to the size of the tsp_mat


    best_path = mainloop()



def create_pheromone_map():
    pheromone_map = [[] for _ in range(len(tspmat))]
    for sublist in pheromone_map:
        for i in range(len(tspmat)):
            sublist.append(1)
    return pheromone_map



def createAntColony(antnmbr):
    """
    creates an array 'ant' with as many ant-objects in it as user input wanted
    """
    AntColony = []
    for i in range(0,antnmbr):
        AntColony.append(ant())

    return AntColony


def user_input():
    benchmark = 1# int(input("Please specify TSP benchmark to use [1],[2],[3]: "))
    antnmbr = 20# int(input("Please specify number of ants to be used: "))
    evapConst = 0.5#float(input("Please specify Evaporation Constant: "))
    p_Constant =8# float(input("Please specify Intensification Constant: "))

    initalize(benchmark, antnmbr, p_Constant, evapConst)


user_input()
