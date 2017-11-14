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
            
            


        
def gen_rand_standard(nmbofitems):
    """This generator generates jobs for experiment 1&2"""
    standardlist = []
    while nmbofitems != 0:
        newjob = random.randint(10,1000)
        standardlist.append(newjob)
        nmbofitems -= 1
    return standardlist
        
        
def gen_rand_one(nmbofitems):
    """This generator generates jobs for the FIRST experiment involing runtimes between 100 and 300"""
    onelist = []
    while nmbofitems != 0:
        newjob = random.randint(100,300)
        onelist.append(newjob)
        nmbofitems -= 1
    return onelist
        
def gen_rand_two(nmbofitems):
    """This generator generates jobs for the SECOND experiment involing runtimes between 400 and 700"""
    twolist = []
    while nmbofitems != 0:
        newjob = random.randint(400,700)
        nmbofitems -= 1
        twolist.append(newjob)
    

#---------------------------------------------------------------I M P L E M E N T A T I O N   O F   P O P U L A T I O N   G E N E R A T I O N -------------------------------------
        
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

      
    

    
    
def generate_initial_population(numberofindividuals):
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
    genecount = len(joblist)
    
    for individual in range(numberofindividuals):
        genome = []
        genes = genecount
        while genes != 0:
            genome.append(random.randint(1, numberofmachines))
            genes -= 1
        initialgenes.append(genome)
    initialpop = generate_population_from_genes(initialgenes)
    
    return initialpop

#--------------------------------------------------------------- S E L E C T I O N   D E F I N I T I O N -------------------------------------

def selectionTurnament(population):
    competitors = population
    #fitnessValues = []
    matingpool = []

    '''
    #for each individum in the population mapp the fitnessvalue in a list
    for individum in competitors:
        currentfitness = individum.fitness
        fitnessValues.append(currentfitness)
    '''

    #defines how many individuals are in the matingpool needs to be an even number 
    sizeMatingPool = (len(population) // 3) * 2
    if sizeMatingPool % 2 == 1:
        sizeMatingPool -= 1
    if len(competitors) % 2 == 1:
        del competitors[random.randint(0,len(competitors) - 1)]
        
    while sizeMatingPool > 0:
        #store population length for quick exces
        sizeCompetitors = len(competitors)
        #set parents to invalid values
        p1_index = -1
        p2_index = -1
        #choose differnet parents untill they are not the same individuals
        while p1_index == p2_index:
            p1_index = random.randint(0,sizeCompetitors - 1)
            p2_index = random.randint(0,sizeCompetitors - 1)

        p1_fit = competitors[p1_index].fitness
        p2_fit = competitors[p2_index].fitness
        #p1 is fitter than p2
        if p1_fit > p2_fit:
            #append the matingpool with the fitter parent
            matingpool.append(competitors[p1_index])
            #delete the winnging parent, because he is no longer a competitor
            competitors.pop(p1_index)
            #shrink the size of the matingpool, because we have found a parent
            sizeMatingPool -= 1
        #p2 is fitter than p1
        if p1_fit < p2_fit:
            #append the matingpool with the fitter parent
            matingpool.append(competitors[p2_index])
            #delete the winnging parent, because he is no longer a competitor
            competitors.pop(p2_index)
            #shrink the size of the matingpool, because we have found a parent
            sizeMatingPool -= 1
        # if nothing holds we have a sting, booth are equaly fit, so we do nothing 
        if p1_fit == p2_fit:
            matingpool.append(competitors[p2_index])
            matingpool.append(competitors[p1_index])
            competitors.pop(p2_index)
            competitors.pop(p1_index)
            sizeMatingPool -= 2
            
    return matingpool
#---------------------------------------------------------------M U T A T I O N   F U N C T I O N S -------------------------------------
        

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
    return population

#mutates a specific machine to an other at a random place
#mutates a random allel in a chromosome
def mutateRandomResetting(chromosome):
    mutateMachine = random.randint(0,numberofmachines)
    mutatePlace = random.randint(0,len(chromosome)-1)

#making sure that w do not mutate the one machine to the same machine
    while chromosome[mutatePlace] == mutateMachine:
        mutateMachine = random.randint(0,numberofmachines)

    chromosome[mutatePlace] = mutateMachine
    return chromosome

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

#---------------------------------------------------------------R E C O M B I N A T I O N   O P E R A T I O N S------------------------
        

def onepoint(p1,p2):
    '''
    Generate a crossover point and then copy sublist 1 of p1 in c1 and of p2 in c2 and then copy sublist 2 of p1 in c2 and of p2 in c1
    INPUT:
    p1: List of Parent one for crossover operation
    p2: List of Parent two for crossover operation 
    
    OUTPUT:
    c1: List of Child one, offspring of p1,p2
    c2: List of Child two, offspring of p1,p2
    '''
    parentlength = (len(p1)-1)
    #create children 1 and 2
    c1 = []
    c2 = []
    #generate random cuttpoint
    cutpoint = random.randint(1,parentlength)
    #Copy Sublist into respective parents
    c1, c2 = (p1[:cutpoint] + p2[cutpoint:], p2[:cutpoint] + p1[cutpoint:])
    return c1,c2

def uniformCrossover(p1,p2):
    '''
    Generate a random template and if if value of template is bigger than threshold
    copy gene from p1 in c1 else p2 (and respectively for c2)
    INPUT:
    p1: List of Parent one for crossover operation
    p2: List of Parent two for crossover operation 
    
    OUTPUT:
    c1: List of Child one, offspring of p1,p2
    c2: List of Child two, offspring of p1,p2
    '''
    #save parentlenth for quick exces
    parentlength = (len(p1))
    #define a treshold to choose from which parent you take the genom
    threshold = 0.5
    c1=[]
    c2=[]

    #create a random template of length parentlength with values (0,1)
    template = []
    for i in range(parentlength):
        template.append(random.uniform(0,1))

    '''
    iterate though the parents, if value of template is bigger than threshold
    copy gene from p1 in c1 else p2 (and respectively for c2)
    '''
    for i in range(parentlength):
        if template[i] > threshold:
            c1.append(p1[i])
            c2.append(p2[i])
        else:
            c1.append(p2[i])
            c2.append(p1[i])
    #return the new children
    return c1,c2

def recombine(matingpool):
    '''
    Generates new offsprings from the matingpool
    INPUT:
    matingpool: List of individuals selcted for the mating process
    OUTPUT:
    children: List of generated offsprings from the matingpool
    '''
    children = []
    #which reombination method we want to use, untill now just 1
    recomMethod = 1

    #recombine 2 parents from the matingpool untill the mating pool ist empty
    while len(matingpool) > 0:
        #in every iteration compute the matingpool size again, because its shrinking
        sizeMatingPool = len(matingpool)-1
        choice1 = -1
        choice2 = -1

        #select two random differnet parents from the mating pool
        while choice1 == choice2:
            choice1 = random.randint(0,sizeMatingPool)
            choice2 = random.randint(0,sizeMatingPool)

        #save the two parents
        parent1 = matingpool[choice1]
        parent2 = matingpool[choice2]

        #execute the recombination method of your choice and save the new children in c1 and c2
        if recomMethod == 1:
            c1,c2 = onepoint(parent1,parent2)
        elif recomMethod == 2:
            c1,c2 = uniformCrossover(parent1,parent2)

        #add new children to the set of all children
        children.append(c1)
        children.append(c2)
        #remove the parents from the matingpool
        matingpool.remove(parent1)
        matingpool.remove(parent2)


    return children


#--------------------------------------------------------------- R E P L A C E R -------------------------------------------------------------------------------

def delete_all(population):
    

#---------------------------------------------------------------I M P L E M E N T A T I O N   O F   U S E R   I N P U T   A N D   E X E C U T I O N -----------------------------------------
def user_input():
    individuals = int(input("Please enter the number of individuals per generation: "))
    return individuals
    
def initalize():
    global mutation1
    global mutation2
    global joblist
    global numberofmachines
    mutation1 = True
    mutation2 = False
    numberofmachines = 20
    joblist = gen_rand_standard(200) + gen_rand_one(100)
    
    usercommands = user_input()
    print("Initializing population with",usercommands,"individuals.")
    pop = generate_initial_population(usercommands)
    
    
        
    
    
    
initalize()