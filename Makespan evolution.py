# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 08:39:05 2017

@author: JoJo
"""

import random


# ---------------------------------------------------------------P R E D E F I N I T I O N   O F   E X P E R I M E N T   A N D   O B J E C T S --------------------

class Individual:
    """an indivdual is a python object that has the values "genome" and "fitness"
    The genome is a list of integer between 1 and 20, encoding job distribution. Its length is determined by the number of jobs
    fitness is the eucledian distance between all total machine runtimes. If the distance is low, the fitness is high."""

    def __init__(self, genome, fitness):
        self.genome = genome
        self.fitness = fitness
        """the fitness of an individual is updated with simply calling individual.update_fitness()"""
<<<<<<< HEAD
=======
        
    def update_fitness(self):
        totaldistance = 0
        iterator = 0
        machine =  [0]*numberofmachines
        for index in self.genome:
            machine[index - 1] += joblist[iterator]
            iterator += 1
        for totaltime in machine:
            for compare in machine:
                totaldistance += abs(totaltime - compare)
        self.fitness = 0 - totaldistance
            
            

>>>>>>> 775debe136ff050e558f9dba71e41d067b66ecdf

    def update_fitness(self):
        pass


def gen_rand_standard(nmbofitems):
    """This generator generates jobs for experiment 1&2"""
    standardlist = []
    while nmbofitems != 0:
<<<<<<< HEAD
        newjob = random.randint(10, 1000)
        yield newjob


=======
        newjob = random.randint(10,1000)
        standardlist.append(newjob)
        nmbofitems -= 1
    return standardlist
        
        
>>>>>>> 775debe136ff050e558f9dba71e41d067b66ecdf
def gen_rand_one(nmbofitems):
    """This generator generates jobs for the FIRST experiment involing runtimes between 100 and 300"""
    onelist = []
    while nmbofitems != 0:
<<<<<<< HEAD
        newjob = random.randint(100, 300)
        yield newjob


=======
        newjob = random.randint(100,300)
        onelist.append(newjob)
        nmbofitems -= 1
    return onelist
        
>>>>>>> 775debe136ff050e558f9dba71e41d067b66ecdf
def gen_rand_two(nmbofitems):
    """This generator generates jobs for the SECOND experiment involing runtimes between 400 and 700"""
    twolist = []
    while nmbofitems != 0:
<<<<<<< HEAD
        newjob = random.randint(400, 700)
        yield newjob
=======
        newjob = random.randint(400,700)
        nmbofitems -= 1
        twolist.append(newjob)
    
>>>>>>> 775debe136ff050e558f9dba71e41d067b66ecdf


# ---------------------------------------------------------------I M P L E M E N T A T I O N   O F   G E N E T I C   A L G O R I T H M -------------------------------------

def generate_population_from_genes(listofgenomes):
    """This function generates individuals from the list of genomes that is passed into it. it returns a list of individuals which is the new population.
    This function can be used universally across all experiments
    
    INPUT: A list of chromosoms
    
    OUTPUT: A list of individuals (population)"""
    population = []
    indexofgenomes = len(listofgenomes) - 1
    while indexofgenomes != -1:
        genome = listofgenomes[indexofgenomes]
        newindividual = individual(genome, 0)
        newindividual.update_fitness()
        population.append(newindividual)
        indexofgenomes -= 1

    return population
<<<<<<< HEAD


def generate_initial_population(numberofgenes, numberofmachines):
=======
        
    
    
    
    
def generate_initial_population(numberofindividuals):
>>>>>>> 775debe136ff050e558f9dba71e41d067b66ecdf
    """This function generates a random list of chromosoms that is equivalent to the number of individuals.
    in the list, there are chromosoms, (or in other words the individual's genes) with a random number in the range between 1 and the number of machines
    this function is only called once per experiment, as one only needs one initial population. the initial population is then manipulated by other functions such
    as the recombination function, the selection function or the mutation function
    
    INPUT: 
    Number of individuals per population (user defined in another function)
    Number of genes. This is equivalent to the total number of jobs to distribute
    Number of machines. This is important to distribute the integer range of single genes. In our case, this is always 20
    
    OUTPUT: A list of random individuals (first population) which corresponds to individuals with"""

    initialgenes = []
<<<<<<< HEAD
=======
    genecount = len(joblist)
    
>>>>>>> 775debe136ff050e558f9dba71e41d067b66ecdf
    for individual in range(numberofindividuals):
        genome = []
        genes = genecount
        while genes != 0:
            genome.append(random.randint(1, numberofmachines))
            genes -= 1
        initialgenes.append(genome)
<<<<<<< HEAD

    return initialgenes

x = generate_initial_population(numberofmachines=20, )
print(x)
=======
    initialpop = generate_population_from_genes(initialgenes)
    
    return initialpop



def mutation(population):
    probability = 0.06
    populationsize = len(population)

#if the mutationprobability is matched we mutate the chromosome
    for i in range(populationsize):
        mutation = random.uniform(0,1)
        if mutation <= probability:
            if mutation1:
                mutateRandomResetting(population[i])
            elif mutation2:
                mutateReverse(population[i])
    print(population)

#mutates a specific machine to an other at a random place
#mutates a random allel in a chromosome
def mutateRandomResetting(chromosome):
    mutateMachine = random.randint(0,numberofmachines)
    mutatePlace = random.randint(0,len(chromosome)-1)

#making sure that w do not mutate the one machine to the same machine
    while chromosome[mutatePlace] == mutateMachine:
        mutateMachine = random.randint(0,numberofmachines)

    chromosome[mutatePlace] = mutateMachine

def mutateReverse(chromosome):
    '''
    choose two random points and flip array in between 
    '''
    #save length for quick access
    chromosomesize = len(chromosome)

    m1 = -1
    m2 = -1
    #as long as m2 is smaller than m1 and make sure that they are at least 2 numbers appart 
    while m2-m1 <= 2 :
        #create points randomly
        m1 = random.randint(0,chromosomesize-1)
        m2 = random.randint(0,chromosomesize-1)
    print(m1)
    print(m2)
    #flip the sublist 
    sublist = chromosome[m2:m1:-1]
    
    #put sublist in chromosome at the respective position 
    for i in range(m1+1,m2):
        chromosome[i] = sublist[i-m1]

    return  chromosome





#---------------------------------------------------------------I M P L E M E N T A T I O N   O F   U S E R   I N P U T   A N D   E X E C U T I O N -----------------------------------------
def user_input():
    return False

def initalize():
    global joblist
    global numberofmachines
    numberofmachines = 20
    joblist = gen_rand_standard(200) + gen_rand_one(100)
    pop = generate_initial_population(100)
    for index in pop:
        print(index.fitness)
        
    
    
    
initalize()
    
    
    
    
>>>>>>> 775debe136ff050e558f9dba71e41d067b66ecdf
