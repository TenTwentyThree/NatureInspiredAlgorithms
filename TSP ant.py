# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:33:10 2017
@author: JoJo, yj, tn
"""

import numpy as np

class ant:
    def __init__(self,possible_locations, path, pathCost):
        """
        initialize an ant, to traverse the map
        possible_locations -> a list of possible locations the ant can travel to
        path -> [1,2,5,3,4,6,1] a list of integers, where each integer represents a city, and the path[i] to the path[i+1] entrence is an edge the ant has traveled
        pathCost -> cost, in this case the sum of the edgecosts the ant has traveled
        """

        self.possible_locations = list(range(150))
        self.path = []
        self.pathCost = 0




    def findSolution(self):
        """
        As long as the List of possibl enext location self.possible_locations is not empty
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
        current_location = self.get_location
        # probabilitys to visit the node, mapped over the possible_locations list
        pathProbabilities = []
        #List with all numerator values for each possible next_location
        numeratorList= []
        #Total sum of te denumerator, still has to be computed
        total_sum = 0
        # Compute the numerator for every possible node and save in the numeratorList
        for i in range(len(self.possible_locations)):
            #get the pheromone_amount for the possible nect location and the distance between those cities
            pheromone_amount = float(pheromone_map[self.get_location()][self.possible_locations[i]])
            distance = float(1/tspmat[current_location][self.possible_locations[i]])

            #fill the numerator list
            numeratorList.append(pow(pheromone_amount, alpha)*pow(1/distance, beta))
        #compute the denominator
        denominator = sum(numeratorList)

        #compute the path probabilities by deviding the numerator with the deonominator
        for i in range(len(self.possible_locations)):
            pathProbabilities.append(numeratorList[i]/denominator)

        #randomly choose the next path
        #Not quit shure about this 
		toss = random.random()
					
		cummulative = 0
		for possible_next_location in pathProbabilities:
			weight = possible_next_location
			if toss <= weight + cummulative:
				return self.possible_locations[pathProbabilities.index(possible_next_location)]
			cummulative += weight


    def update_pathCcost(self):
        """
        This function updates the Cost (length) of the path the ant has traveled
        """
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
        if len(self.possible_locations) = 0:
            return self.pathCost
        return None

    def get_path(self):
        """
        get the path, if it's created completely
        """
        if len(self.possible_locations) = 0:
            return self.path
        return None

    def get_location(self):
        """
        return the current location of the ant
        """
        return self.path[-1]

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
    while "Terminationcondition":
        #create pathes for every ant in the ANt AntColony
        for ant in AntColony:
            ant.findSolution()


        #since the matrix is symatrical acording to the diagonal we only need to comute the upper right triangal, and copy it to the lower left triangal
        for i in range(len(pheromone_map)):
            for j in range(i,len(pheromone_map)):

                if i != j :
                pheromone = #updated pheromone map after evaporation
                else:
                     pheromone = 0
                #update the respective entry in the pheromone map
                pheromone_map[i][j] = pheromone
                pheromone_map[j][i] = pheromone

        #since the matrix is symatrical acording to the diagonal we only need to comute the upper right triangal, and copy it to the lower left triangal
        for i in range(len(pheromone_map)):
            for j in range(i,len(pheromone_map)):

                if i != j :
                pheromone = #updated pheromone map after internsification
                else:
                     pheromone = 0
                #update the respective entry in the pheromone map
                pheromone_map[i][j] = pheromone
                pheromone_map[j][i] = pheromone





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
