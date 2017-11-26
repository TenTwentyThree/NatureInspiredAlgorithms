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


#----------------------------------Pheromone_update-------------------------------

class PheromonesUpdate(Ant):

    """
    Properties:
    1. Initialize pheromones (Zeros/Random)
    2. Measure the fitness of ants, given pathCost from Parent Class(Ant)
    3. Get the path of the best ant
    4. Evaporation
    5. Intensification
    6. Update pheromones as given in the ACO Schema
    4. Further work: Update pheromones applies to all pheromones with respect to the quality of solutions produced by the ants
    """

    def __init__(self, rho):
        super().__init__(ants, num_cities, paths )
        self.rho = rho

    def init_pheromones(self, num_cities, _random=False):

        """
        :param num_cities:
        :param _random: Type of initialization. Zeros or Random
        :return: array of pheromones
        """

        if _random:
            pheromones = np.random.random((num_cities, num_cities))
            np.fill_diagonal(pheromones, 0)
        else:
            pheromones = np.zeros((num_cities, num_cities))

        return pheromones

    def fitness_measure(self, ants, pathcost):
        """
        :param ants: list of antIDs
        :param pathcost: Path cost of each ant
        :return: fittest_ant, list of their fitness
        """

        fitness_ants = np.subtract(max(pathcost), pathcost)
        fittest_ant = ants[np.argmax(fitness_ants)]

        return fittest_ant, fitness_ants

    def get_path_fittest_ant(self, fittest_ant):

        fittest_ant_path = paths[fittest_ant]

        return fittest_ant_path

    def evaporation(self, pheromones):
        """
        :param pheromones: Array of pheromones
        :return: Array vaporized pheromones
        """

        return np.multiply((1-self.rho), pheromones)

    def intensification(self,pheromones, fitness_ants,fittest_ant):

        """

        :param pheromones: Array of pheromones
        :param fitness_ants: Fitnesses of all ants in the iteration
        :param fittest_ant: Fittest ant index (AntID)
        :return: intensified_pheromones : Of the best ant's path
        """
        path = self.get_path_fittest_ant(fittest_ant)
        intensified_pheromones = pheromones.copy()
        for cities in path:
            i,j = cities
            intensification_factor = np.multiply(self.rho, (fitness_ants[fittest_ant] / np.sum(fitness_ants, axis=0)))
            intensified_pheromones[i][j] = pheromones[i][j] + intensification_factor

        return intensified_pheromones

    def update_pheromones(self, pheromones, ants, fitness_ants, fittest_ant, paths ):

        """
        :param pheromones:  Array of pheromones
        :param ants: list of antIDs
        :param fittest_ant: int (index of the fittest ant in the population)
        :param fitness_ants: list of fitness of each ant
        :param paths : tuple of path of fittest ant
        :return: array updated_pheromones
        """

        updated_pheromones = np.zeros((num_cities, num_cities))
        for tour in range(len(ants)):
            for path in paths[tour]:
                i,j = path
                evaporation_factor = np.multiply((1 - self.rho), pheromones[i][j])
                intensification_factor = np.multiply(self.rho, (fitness_ants[fittest_ant] / np.sum(fitness_ants, axis=0)))
                updated_pheromones[i][j] = evaporation_factor + intensification_factor
                # np.fill_diagonal(tau, 0)  # Hardcoded, just to make sure intensification is not performed between same city

                return updated_pheromones

# ------------------------PheromoneUpdate Class Ends---------------------------

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
