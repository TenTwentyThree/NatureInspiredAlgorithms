# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 08:39:05 2017

@author: JoJo
"""

import random

#---------------------------------------------------------------P R E D E F I N I T I O N   O F   E X P E R I M E N T   A N D   O B J E C T S --------------------
class individual:
    """an indivdual is a python object that has the values "genome" and "fitness"
    The genome is a list of integer between 1 and 20, encoding job distribution. Its length is determined by the number of jobs
    fitness is the eucledian distance between all total machine runtimes. If the distance is low, the fitness is high."""
    def __init__(self, genome, fitness):
        self.genome = genome
        self.fitness = fitness
        """the fitness of an individual is updated with simply calling individual.update_fitness()"""
    def update_fitness()

        
def gen_rand_standard(nmbofitems):
    """This generator generates jobs for experiment 1&2"""
    while nmbofitems != 0:
        newjob = random.randint(10,1000)
        yield newjob
        
def gen_rand_one(nmbofitems):
    """This generator generates jobs for the FIRST experiment involing runtimes between 100 and 300"""
    while nmbofitems != 0:
        newjob = random.randint(100,300)
        yield newjob
        
def gen_rand_two(nmbofitems):
    """This generator generates jobs for the SECOND experiment involing runtimes between 400 and 700"""
    while nmbofitems != 0:
        newjob = random.randint(400,700)
        yield newjob

#---------------------------------------------------------------I M P L E M E N T A T I O N   O F   G E N E T I C   A L G O R I T H M -------------------------------------
        
def generate_population_from_genes(listofgenomes):
    """This function generates individuals from the list of genomes that is passed into it. it returns a list of individuals which is the new population.
    This function can be used universally across all experiments
    
    INPUT: A list of chromosoms
    
    OUTPUT: A list of individuals (population)"""
    population = []
    indexofgenomes = len(listofgenomes) - 1
    while indexofgenomes != -1:
        genome = listofgenomes[indexofgenomes]
        fit = evalfitness(genome)
        newindividual = individual(genome, fit)
        population.append(newindividual)
        indexofgenomes -= 1
        
    return population
        
    
    
    
    
def generate_initial_population(numberofindividuals, numberofgenes, numberofmachines):
    """This function generates a random list of chromosoms that is equivalent to the number of individuals.
    in the list, there are chromosoms, (or in other words the individual's genes) with a random number in the range between 1 and the number of machines
    this function is only called once per experiment, as one only needs one initial population. the initial population is then manipulated by other functions such
    as the recombination function, the selection function or the mutation function
    
    INPUT: 
    Number of individuals per population (user defined in another function)
    Number of genes. This is equivalent to the total number of jobs to distribute
    Number of machines. This is important to distribute the integer range of single genes. In our case, this is always 20
    
    OUTPUT: A list of random individuals (first population)"""
    initialgenes = []
    for individual in numberofindividuals:
        genome = []
        genes = numberofgenes
        while genes != 0:
            genome.append(random.randint(1, numberofmachines))
            numberofgenes -= 1
        initialgenes.append(genome)
    
    return initialgenes
    