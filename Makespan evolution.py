# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 08:39:05 2017

@author: JoJo
"""

import random


class individual:
    """an indivdual is defined by its genome and its fitness"""
    def __init__(self, genome, fitness):
        self.genome = genome
        self.fitness = fitness
        
        
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

        
        
def generate_population_from_genomes(listofgenomes):
    """This function generates individuals from the list of genomes that is passed into it. it returns a list of individuals which is the new population.
    This function can be used universally across all experiments"""
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
    """This function generates a random list of genomes that is equivalent to the number of individuals.
    in the list, there are lists of genes (the individuals genomes) with a random number in the range between 1 and the number of machines"""
    initialgenes = []
    for individual in numberofindividuals:
        genome = []
        genes = numberofgenes
        while genes != 0:
            genome.append(random.randint(1, numberofmachines))
            numberofgenes -= 1
        initialgenes.append(genome)
    
    return initialgenes

def evalfitness(genome):
    return 1
    