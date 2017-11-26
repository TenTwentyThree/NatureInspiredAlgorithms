import numpy as np


#Dummy class
class Ant:

    def __init__(self, num_cities, ants):
        self.num_cities = num_cities
        self.ants = ants


    def path_cost(self):

        pathcost = np.random.randint(1, 5, 5)
        return pathcost


class PheromonesUpdate(Ant):

    def __init__(self, rho):
        super().__init__(ants, num_cities)
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

        return fittest_ant,fitness_ants


    def update_pheromones(self, tau, fittest_ant, fitness_ants):
        """
        :param tau:  pheromones
        :param rho: evaporation constant
        :param fittest_ant: int (index of the fittest ant in the population)
        :param fitness_ants: list of fitness of each ant
        :return: updated_pheromones

        """

        evaporation_factor = np.multiply((1 - self.rho), tau)
        intensification_factor = np.multiply(self.rho, (fitness_ants[fittest_ant] / np.sum(fitness_ants, axis=0)))
        updated_tau = evaporation_factor + intensification_factor
        np.fill_diagonal(updated_tau, 0)  # Hardcoded, just to make sure intensification is not performed bet
        return updated_tau


# Test variables
ants = [0, 1, 2, 3, 4]  # Ant IDs
num_cities = 5
fitness_ants = np.random.rand(1, 5)
rho = 0.5

ant = Ant(ants, num_cities)
pathcost = ant.path_cost()
pheromones_update = PheromonesUpdate(rho)
pheromones = pheromones_update.init_pheromones(num_cities=5, _random=True)
_fittest_ant, _fitness_ants = pheromones_update.fitness_measure(ants, pathcost)
updated_tau = pheromones_update.update_pheromones(tau=pheromones, fittest_ant=_fittest_ant, fitness_ants=_fitness_ants )


print("Path Cost",pathcost)
print("Fitness of ants", fitness_ants)
print("Fittest Ant", np.argmin(fitness_ants))
print("Pheromones Initialized \n ", pheromones)
print("Fitnesses of ants are %s and the fittest ant is %s  "%(_fitness_ants, _fittest_ant))
print("Updated pheromone", updated_tau)
