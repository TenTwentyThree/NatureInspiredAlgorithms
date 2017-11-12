#selects the random individuals and replaces them with the children
import random

def SteadyState(population,children)
childrensize = len(children) - 1
populationsize = len(population) - 1

#select random parents from the population and remove them
for i in range(0,childrensize):
  kill = random.randint(0:populationsize)
  population.remove(kill)

#Children take place in new population
population.appennd(children)

return population
