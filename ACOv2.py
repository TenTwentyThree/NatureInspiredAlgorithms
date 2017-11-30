

import numpy as np
import random
from numpy.random import choice
import heapq


class antColony():
    class ant():

        def __init__(self,init_location,possible_locations,pheromone_map,alpha,beta,first_pass):
            """
            Initialite an ant with,

            init_location(int) : initial position of the ant
            possible_locations(List) : List of all possible possible_locations
            path_cost(int) : Cost of the path the ant has traversed
            pheromone_map(List) : List of List, where pheromone_map[i][j] represents row i at column j
            Alpha(float) : determines impact of the pheromone_map in the path selection
            Beta(float ) : determines impact of the distance between node i and i+1 in the path selection
            first_pass(boolean) : determines if we are in the first iteration or not
            """
            self.init_location = init_location
            self.possible_locations = possible_locations
            self.path = []
            self.path_cost = 0
            self.current_location = init_location
            self.pheromone_map = pheromone_map
            self.alpha = alpha
            self.beta = beta
            self.first_pass = True

            self.update_path(init_location)

#---------------------------------------------SOLUTION CONSTRUCTION--------------------------------------#
        def create_path(self):
            """
            Create a path for the ant self
            """
            #as long as the list of Possible locations is not empty, we search for the next node
            while self.possible_locations:
                next = self.pick_path()
                self.traverse(self.current_location,next)

        def pick_path(self):
            """
            Pick a path from self.possible_locations and return it
            """
            #if we are in the first iteration, just take a random path
            if self.first_pass:
                self.first_pass = False
                return random.choice(self.possible_locations)


            #else compute the path by the ACO edge selection Heuristic
            #(pheromoneamount^alpha * (1/distance)^beta)/sum(all alowed moves)
            #attractiveness is the list of numerators computed by the numerator of the formula above
            attractiveness = []
            #denominator has to be computed
            denominator  = 0.0

            #for every location in the possible location, compute th likeliehood
            for possbible_next_location in self.possible_locations:
                #safe the values for the computation
                pheromone_amount = float(self.pheromone_map[self.current_location][possbible_next_location])
                distance = float(tspmap[self.current_location][possbible_next_location])

                #if (self.alpha == 0) and (self.beta == 0):
                attractiveness.append(pheromone_amount*(1/distance))
                #append the numerator list 'attractiveness' with the numerator of the likelyhood
                #attractiveness.append(pow(pheromone_amount, self.alpha)*pow(1/distance, self.beta))
            #Compute the denominator by adding up all possible attractivnesses
            denominator = float(sum(attractiveness))

            #we have to avoid zero devisions, so we compute the smallest number not zero, if the denominator is 0
            if denominator == 0.0:
                def next_up(x):
                    import math
                    import struct
                    # NaNs and positive infinity map to themselves.
                    if math.isnan(x) or (math.isinf(x) and x > 0):
                        return x

                    # 0.0 and -0.0 both map to the smallest +ve float.
                    if x == 0.0:
                        x = 0.0

                        n = struct.unpack('<q', struct.pack('<d', x))[0]

                        if n >= 0:
                            n += 1
                        else:
                            n -= 1
                    return struct.unpack('<d', struct.pack('<q', n))[0]

                for i in attractiveness:
                    attractiveness[i] = next_up(attractiveness[i])
                denominator = next_up(denominator)

            #fill the path Probability list with the computed likeliehoods
            pathProbabilities = []
            for i in range(len(self.possible_locations)):
                if denominator != 0.0:
                    pathProbabilities.append(attractiveness[i]/denominator)
                elif denominator == 0.0:
                    pathProbabilities.append(0)

            #Sample the next path from the probabilities
            toss = random.random()
            cummulative = 0

            for i in range(len(pathProbabilities)):
                if toss <= (pathProbabilities[i] + cummulative):
                    next_city = self.possible_locations[i]
                    return next_city
                cummulative += pathProbabilities[i]


            #next city is the city with the highest probability
            #next_city = self.possible_locations[pathProbabilities.index(max(pathProbabilities))]

            #Initially the Idea was to choose the city by the probability distribution, but somehow it doesn't work \_(o.o)_/
            #draw = choice(self.possible_locations, 1, pathProbabilities)
            #next_city = draw[0]
            #return next_city
#---------------------------------------------SOLUTION CONSTRUCTION Ends--------------------------------------#
        def traverse(self,oldCity,newCity):
            """
            travel from the old node to the new node and update the ant parameters
            oldCity(int) : the current locations
            newCity(int) : the City we choose to visit next
            """
            self.update_path(newCity)
            self.update_pathCost(oldCity,newCity)
            self.current_location = newCity


        def update_path(self,newCity):
            """
            add the new city to the path and remove it from the possible_locations list
            """
            self.path.append(newCity)
            self.possible_locations.remove(newCity)

        def update_pathCost(self,oldCity,newCity):
            """
            add the cost of the path to the new node to the total path_cost
            """
            self.path_cost += tspmap[oldCity][newCity]

    def __init__(self, start, ant_count, alpha, beta,  pheromone_evaporation_coefficient, pheromone_constant, iterations):
        """
        initialize an ant Colony
        start(int) = the starting position of the
        ant_cont(int) = number of the ants in the colony
        Alpha(float) : determines impact of the pheromone_map in the path selection
        Beta(float ) : determines impact of the distance between node i and i+1 in the path selection
        pheromone_evaporation_coefficient(float) : how much pheromone evaporates in one iteration
        pheromone_constant(float) : Parameter to regulate the amount of pheromone that is added to the pheromone_map
        iterations(int) : numebr of iterations we run through
        """

        # Matrix of the pheromone amount over iterations
        self.pheromone_map = self.init_pheromone_map(len(tspmap))
        # Matrix of pheromone amount in iteration
        self.pheromone_map_iteration = self.init_pheromone_map(len(tspmap))

        #start node is set to city 0
        if start is None:
            self.start = 0
        else:
            self.start = start


        #ant_count
        if type(ant_count) is not int:
            raise TypeError("ant_count must be int")
        if ant_count < 1:
            raise ValueError("ant_count must be >= 1")

        self.ant_count = ant_count


        #alpha
        if (type(alpha) is not int) and type(alpha) is not float:
            raise TypeError("alpha must be int or float")

        if alpha < 0:
            raise ValueError("alpha must be >= 0")

        self.alpha = float(alpha)

        #beta
        if (type(beta) is not int) and type(beta) is not float:
            raise TypeError("beta must be int or float")

        if beta < 0:
            raise ValueError("beta must be >= 0")

        self.beta = float(beta)

        #pheromone_evaporation_coefficient
        if (type(pheromone_evaporation_coefficient) is not int) and type(pheromone_evaporation_coefficient) is not float:
            raise TypeError("pheromone_evaporation_coefficient must be int or float")

        self.pheromone_evaporation_coefficient = float(pheromone_evaporation_coefficient)

        #pheromone_constant
        if (type(pheromone_constant) is not int) and type(pheromone_constant) is not float:
            raise TypeError("pheromone_constant must be int or float")

        self.pheromone_constant = float(pheromone_constant)

        #iterations
        if (type(iterations) is not int):
            raise TypeError("iterations must be int")

        if iterations < 0:
            raise ValueError("iterations must be >= 0")

        self.iterations = iterations


        #other initial variables
        self.first_pass = True
        #add ants to the colony
        self.colony = self.init_ants(self.start)
        #sbest cost we have seen so far
        self.shortest_distance = None
        #shortest path we have seen so far
        self.shortest_path_seen = None
        #best ant in the iteration
        self.shortest_ant_in_iteration = None
        self.FirsAnt = True

    def possible_locations(self):
        """
        create a list of all possible locations
        """
        possible_locations = list(range(len(tspmap)))
        return possible_locations

    def init_pheromone_map(self,value = 0.0):
        """
        create the pheromone map,
        has to be the same size of the tspmap
        """
        size = len(tspmap)
        p_map = []
        for row in range(size):
            p_map.append([float(value) for x in range(size)])
        return p_map

    def init_ants(self,start):
        """
        Create ants, if it is first called, else we just 'reset' the ants with the initial values
        """
        if self.first_pass:
            return [self.ant(start, self.possible_locations(), self.pheromone_map,
                    self.alpha, self.beta, first_pass=True) for _ in range(self.ant_count)]

        for ant in self.colony:
            ant.__init__(start,self.possible_locations(),self.pheromone_map,self.alpha,self.beta, self.first_pass)


#---------------------------------- EVAPORATION and INTENSIFICATION--------------------------------#
    def update_pheromone_map(self):
        """
        update the pheromone_map according to the formula
        (1-pheromone_evap_constant)*(pheromoneampunt at position i,j) + sum(pheromoneConstant/length of ant_k  if an ant traveld the edge, 0 otherwise)
        """

        pheromone_factor = 1 - self.pheromone_evaporation_coefficient

        #EVAPORATION update every entry in the pheromone_map
        for i in range(len(self.pheromone_map)):
            for j in range(len(self.pheromone_map)):
                if i != j:
                    self.pheromone_map[i][j] = self.pheromone_map[i][j] * pheromone_factor
                #if i=j we set the value to zero, because we dont want
                else:
                    self.pheromone_map[i][j] = 0
        #Intensification
                #add the new pheromone values from the current iteration to the old pheromone_map
                self.pheromone_map[i][j] += self.pheromone_map_iteration[i][j]

    def update_pheromone_map_iteration(self,ant):
        """
        update the pharomone_map_iteration with the computed pheromone values
        sum(pheromoneConstant/length of ant_k  if an ant traveld the edge, 0 otherwise)
        where ant_k it the ant we passed
        """
        path = ant.path

        #iterate through the path of the ant and update the pheromone_map_iteration at each respective edge the ant has traveled
        for i in range(len(path)-1):
            current_pheromone_value = float(self.pheromone_map_iteration[path[i]][path[i + 1]])

            new_pheromone_amount = self.pheromone_constant/ant.path_cost

            #because the map is symetrical to the diagonal we only need to copy them with respect to the indizes
            self.pheromone_map_iteration[path[i]][path[i + 1]] = current_pheromone_value + new_pheromone_amount
            self.pheromone_map_iteration[path[i + 1]][path[i]] = current_pheromone_value + new_pheromone_amount

#---------------------------------- EVAPORATION and INTENSIFICATION ENDS--------------------------------#
    def mainloop(self):
        """
        mainloop which loops through the differnet steps:
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
        """
        terminate = 0
        while terminate <= self.iterations:
            terminate += 1
            #SOLUTION FINDING
            for ant in self.colony:
                ant.create_path()

            #COMPUTE INTENSIFICATION VALUES
            for ant in self.colony:
                self.update_pheromone_map_iteration(ant)

                #set best path to an initial value
                if self.FirsAnt:
                    self.shortest_ant_in_iteration = ant.path_cost
                    self.FirsIteraton = False

                if not self.shortest_distance:
                    self.shortest_distance = ant.path_cost
                if not self.shortest_path_seen:
                    self.shortest_path_seen = ant.path_cost

                #find the best path in all the ants in the iteration
                if ant.path_cost < self.shortest_ant_in_iteration:
                    self.shortest_ant_in_iteration = ant.path_cost
                #find overall best path
                if ant.path_cost < self.shortest_distance:

                    terminate = 0

                    self.shortest_distance = ant.path_cost
                    self.shortest_path_seen = ant.path
                    print("#-------------------# Shortest Path : ", self.shortest_distance,"   #------#")

            print("Shortest Path: ", self.shortest_ant_in_iteration)
            #restet FirstAnt for next iteration
            self.FirsAnt = True
            #EVAPORATION and INTENSIFCATION
            self.update_pheromone_map()

            if self.first_pass:
                self.first_pass = False

            #Reset seth ants in the colony
            self.init_ants(self.start)

            #reset the pheromone_map_iteration matrix
            self.pheromone_map_iteration = self.init_pheromone_map()

        #return the shortest distance and the path of the SHortest distance
        return self.shortest_distance, self.shortest_path_seen
#---------------------------------------- CLASSES END --------------------------------------#

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

    if filename == 4:
        tspmat = np.loadtxt("4.tsp")

    valuematrix = tspmat.astype(int)
    return valuematrix

def initalize(benchmark):
    global tspmap
    tspmap = read_file(benchmark)

    Colony = antColony(None, antnmbr, al, be,  p_evap_co, p_factor, iterations)
    shortest_distance, shortest_path = Colony.mainloop()

    print("The shortest path has cost: ",shortest_distance)
    print("The path is: ",shortest_path)


def user_input():
    global antnmbr
    global p_evap_co
    global p_factor
    global al
    global be
    global iterations
    global default

    benchmark = -1
    antnmbr = -1
    p_evap_co = -1
    p_factor = -1
    al = -1
    be = -1
    iterations = -1
    default = -1


    print("#----- USERINTERFACE - Input 0 for a default Value -----#")

    #Default
    while (default != 0) or (default != 1):
        default = int(input("Do yo want to use default values? [0]Yes  [1]No: "))
        if default == 0:
            benchmark = 1
            antnmbr = 50
            p_evap_co = 0.4
            p_factor = 0.4
            al = 1
            be = 1
            iterations = 100
            print("")
            print("Initialize ACO with:")
            print("")
            print("Benchamrk: ",benchmark)
            print("Number of ants: ",antnmbr)
            print("Evaporation Coefficient: ",p_evap_co)
            print("Pheromone Constant: ",p_factor)
            print("Alpha Value: ",al)
            print("Beta Value: ",be)
            print("Terminate after  ",iterations," Iterations without improvement.")
            print("")
            initalize(benchmark)
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
            while al < 0:
                if al == -1:
                    al = float(input("Please specify Alpha Value(no default): "))
                else:
                    al = float(input("Please specify Alpha Value bigger or equal to zero: "))
            #beta
            while be < 0:
                if be == -1:
                    be = float(input("Please specify Beta Value: "))
                else:
                    be = float(input("Please specify Beta Value bigger or equal to zero: "))
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
            print("Alpha Value: ",al)
            print("Beta Value: ",be)
            print("Terminate after  ",iterations," Iterations.")
            print("")
            initalize(benchmark)
            return None


user_input()
