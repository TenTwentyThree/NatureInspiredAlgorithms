# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:27:24 2017

@authors:
    Johannes
    Marieke
    Saran
    Till
    Yannic
"""

import numpy as np
import random as rnd
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# - - - - - - - - - - - - - - - I N D I V I D U A L   D E F I N I T I O N - - - - - - - - - - - - - - - - - -

class individual():
    def __init__(self, genome, revenue):
        self.genome = np.array(genome)
        self.revenue = revenue

    def update_revenue(self):

        self.revenue = calculate_profit(self.genome)


# - - - - - - - - - - - - - - - P O P U L A T I O N   I N I T I A L I Z A T I O N - - - - - - - - - - - - - - -

def initialise(agentnmbr):
    #by Till, modded by Johannes
    """
    input: agentnmbr = number of agents defined by the user (for our problem 20 should be more than sufficient)
    output: either none, or if needed the array of agents. I would suggest however to make the array global.

    creates as many agents as user defines. randomly assigns values to the number of powerplants.
    randomly divides the overall energy created over all the markets
    takes the price of the market (m1,m2,m3) as given as a global variable
    """
    m1 = rnd.uniform(0.0, 0.45)
    m2 = rnd.uniform(0.0, 0.25)
    m3 = rnd.uniform(0.0, 0.20)
    kwh1 = 50000
    kwh2 = 600000
    kwh3 = 4000000
    population = []
    for i in range(0,agentnmbr):
        p1 = rnd.randint(0,100)
        p2 = rnd.randint(0,50)
        p3 = rnd.randint(0,3)
        #randomly choosing how many powerplants we have for each agent

        ttlsum = p1*kwh1 + p2*kwh2 + p3*kwh3
        s1 = rnd.randint(0,ttlsum)
        #print(sum)
        s2 = rnd.randint(0,ttlsum)
        #print(sum)
        s3 = rnd.randint(0,ttlsum)
        #assigning random values for each market, depending on the overall produced energy
        new_agent = individual([p1,p2,p3,s1,s2,s3,m1,m2,m3],0)
        #print(new_agent)
        population.append(new_agent)

    return population


# - - - - - - - - - - - - - - - M A I N - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def __MAIN__():
   #by Johannes, Yannic, Till, Saran, Marieke

    # 1. userinput of type List: [crossoverRate,scalingFactor,populationSize]
    userinput = user_input()
    global CostPrice
    global upper_energy_bound

    #for plotting
    iterations = []

    md1 = problem.market(1).maxDemand
    md2 = problem.market(2).maxDemand
    md3 = problem.market(3).maxDemand

    upper_energy_bound = md1 + md2 + md3


    crossoverRate = userinput[0]
    scalingFactor = userinput[1]
    populationSize = userinput[2]
    CostPrice = userinput[3]

    counter = 0

    popcounter = 0

    # 2. Mainloop
    population = initialise(populationSize)

    current_best = rnd.choice(population)

    while counter < 500:

        target_and_donors_list = donor_selection(population)

        trial = trial_generation(target_and_donors_list, scalingFactor, crossoverRate)

        population = selection(trial)

        generations_best = find_best(population)


        if current_best.revenue >= generations_best.revenue:
            counter += 1
        else:
            current_best = generations_best
            counter = 0
            iterations.append(generations_best.revenue)
        popcounter += 1

    print("\n")
    print("####----------------------------------------------------------###")
    print("Convergence termination reached after",popcounter,"generations.")
    print("####----------------------------------------------------------###")
    print("some Data:")
    print("\n")
    print(current_best.genome)
    print("total energy produced: ",current_best.genome[0] + current_best.genome[1] + current_best.genome[2] ,"units of energy")
    print("\n")
    print("Plant 1 produced ",current_best.genome[0],"units of energy")
    print("Plant 2 produced ",current_best.genome[1],"units of energy")
    print("Plant 3 produced ",current_best.genome[2],"units of energy")
    print("\n")
    print("total energy distributed: ",current_best.genome[3] + current_best.genome[4] + current_best.genome[5] ,"units of energy")
    print("Market 1 received ",current_best.genome[3],"units of energy for a price of ",current_best.genome[6])
    print("Market 2 received ",current_best.genome[4],"units of energy for a price of ",current_best.genome[7])
    print("Market 3 received ",current_best.genome[5],"units of energy for a price of ",current_best.genome[8])
    print("\n")
    print("leaving ",(current_best.genome[0] + current_best.genome[1] + current_best.genome[2])-(current_best.genome[3] + current_best.genome[4] + current_best.genome[5]),"of energy units undistributed!!")
    print("\n")
    print("Best value attained: ",int(round(current_best.revenue)))
    print("")
    print("Crossover Rate: ",crossoverRate)
    print("Scaling Factor: ",scalingFactor)
    print("Population Size: ",populationSize)
    print("Cost Price: ",CostPrice)
    print("")
    print("####----------------------------------------------------------###")

    plot(current_best,iterations,userinput)

def plot(current_best,iterations,userinput):
    #by Yannic

    #set Iteration list global
    global it
    it = iterations

    #BarChart
    if userinput[4] == 0:
        #config Plot
        plt.figure(figsize=(17,2))
        #hold indices for chart
        index = np.arange(3)
        bar_width = 0.3

        #Plot Genome 0-2 in subplot 1
        plt.subplot(1,3,1)
        plt.bar(index, current_best.genome[0:3], bar_width)
        plt.xticks(index, current_best.genome[0:3]);
            #Title
        plt.title('Produced with Plant 1, 2 ,3')
        plt.ylabel('Units of kwh')

        #Plot Genome 3-5 in subplot 2
        plt.subplot(1,3,2)
        plt.bar(index,current_best.genome[3:6], bar_width)
        plt.xticks(index, current_best.genome[3:6]);
            #Title
        plt.title('Selled to Marked 1, 2 ,3')

        #Plot Genome 6-8 in subplot 3
        plt.subplot(1,3,3)
        plt.bar(index,current_best.genome[6:9], bar_width)
        plt.xticks(index, current_best.genome[6:9]);
            #Title
        plt.title('Price per kwh for market 1, 2, 3 (Close Window to Terminate)')
        plt.ylabel('Price')

        #output the subplots
        plt.show()

    #Graph
    if userinput[5] == 0:
        #configurate plot
        fig = plt.figure(figsize=(10,5))
        #ad subplot
        ax1 = fig.add_subplot(1,1,1)

        #function to determine the next y value
        def getNewPrice(count):
            if count < len(it):
                return it[count]
            else:
                return it[len(it)-1]

        #some Values for the animation
        global t,counter
        counter = 0
        price = [100]
        t = [0]

        def animate(i):
            """
            i : frame
            """
            global counter
            #initialize x,y values
            x = t
            y = price
            #add counter
            counter += 1
            #add iteration(counter) to x values
            x.append(counter)
            #add new price to y values
            y.append(getNewPrice(counter))
            ax1.clear()
            #set color of graph and plot it
            plt.plot(x,y,color="blue")
            #set title of plot, if 'it' is end, stop the animation
            if counter < len(it):
                best = str(int(it[counter]))
                ax1.set_title(r'Profit over Iterations | Curren Best: '+ best)
            else:
                best = str(int(it[len(it)-1]))
                cnt = str(counter)
                ax1.set_title(r'Profit over Iterations | Best Profit: '+ best +' found after '+cnt+' iterations.  (Close Window to Terminate)')
                ani.event_source.stop()
            #set x,y labels
            plt.ylabel('Profit')
            plt.xlabel('Iteration')

        #execute animation
        ani = animation.FuncAnimation(fig,animate,interval=50)
        #show animation
        plt.show()


# - - - - - - - - - - - - - - - D O N O R   S E L E C T I O N - - - - - - - - - - - - - - - - - - - - - - - -
def donor_selection(population):
    #by Johannes
    """

    This function basically generates a number of permutations of the population where one element is chosen as the target vector and the others as donors or bases


    INPUT: Population, a list of objects containing vectors as a representation for genome projecting into the search-space
    OUTPUT: A list of tuples. Each tuple contains the target at position 1 (0) and the list of donor objects at position 2 (1)
    """
    target_position = 0
    target_and_donors_list = []
    #this is the output list, which contains tuples with the target at postion 1 and all donor individuals at 2
    while target_position != len(population):
        target_donors = list(population)
        target = population[target_position]
        del target_donors[target_position]
        target_and_donors = (target, target_donors)
        target_and_donors_list.append(target_and_donors)
        target_position += 1
    return target_and_donors_list

# - - - - - - - - - - - - - - - T R I A L   G E N E R A T I O N - - - - - - - - - - - - - - - - - - - - - - - -
def trial_generation(target_and_donors, scaling_factor, crossover_rate):
    #by Johannes
    """

    for each target vector (all vectors in our population are defined as target vectors), we select a base
    the base vector is then removed from the available population pool and two other individuals (except target and base)
    are chosen. These then provide the donor vector for the trial vector / trial individual.
    The trial vector is then generated and its coordinates (genes) are recombined with the genes of the target to form a child
    The program then returns a list with tuples containing the target vector and the generated offspring to be evaluted by a selection function

    INPUT:
    - A list of tuples which contain the target and a list of base vectors
    - A constant scaling factor to be applied to the difference between base and target to generate trial objects
    OUTPUT:
    - A list containing tuples
    - tuples contain the original target as well as a trial individual that then can be compared by the revenue function
    """


    target_trial_associated_list = []
    for target_donor_tuple in target_and_donors:
        #because the input for this function is a touple of an object and a list of object, we split the tuple for easy handling
        target = target_donor_tuple[0]
        all_other_vectors = target_donor_tuple[1]
        #Select a base randomly from the list of potential bases (all other vectors than the target vector)
        base = rnd.choice(all_other_vectors)
        all_other_vectors.remove(base)
        #Choose donor vector 1
        x1 = rnd.choice(all_other_vectors)
        #and remove it from the list of potential vectors to choose as donor vectors
        all_other_vectors.remove(x1)
        #choose donor vector 2
        x2 = rnd.choice(all_other_vectors)
        #calculate the distance between the two vectors and scale it by the scaling factor
        donor_vector = np.subtract(x1.genome,x2.genome)
        donor_vector * scaling_factor
        #now create a new individual from the base.
        final_donor = np.add(target.genome, donor_vector)



        # R E C O M B I N A T I O N   S T A R T S   H E R E

        target_genome = target.genome
        gene_pos = 0
        new_genome = []
        while gene_pos != len(target_genome):
            crossover = rnd.uniform(0,1)
            if crossover < crossover_rate:
                new_genome.append(final_donor[gene_pos])
            else:
                new_genome.append(target_genome[gene_pos])
            gene_pos += 1
        child = individual(new_genome, 0)
        child.update_revenue()
        newtuple = (target, child)
        target_trial_associated_list.append(newtuple)

    return target_trial_associated_list


# - - - - - - - - - - - - - - - S E L E C T I O N - - - - - - - - - - - - - - - - - - - - - - - -
def selection(overpopulation):
    #by Johannes
    """
    This function selects between the original target vector and a child generated by trial_generation.

    INPUT:
    - A list of tuples, each containing a pair of original target vector and a child

    OUTPUT:
    - new population that contains the fittest individuals
    """
    new_population = []
    m1p = problem.market(1).maxPrice
    m2p = problem.market(2).maxPrice
    m3p = problem.market(3).maxPrice
    
    

    for pair in overpopulation:

        target = pair[0]
        child = pair[1]
        
        genecounter = 0
        original_genes = child.genome

        child_gene = []

        for gene in original_genes:

            if genecounter <= 5:
                if gene > upper_energy_bound or gene < 0:
                    new_gene = random.randint(0,upper_energy_bound)
                    child_gene.append(new_gene)
                else:
                    child_gene.append(gene)

            if genecounter == 6:
                if gene > m1p or gene < 0:
                    new_gene = random.randint(0,m1p)
                    child_gene.append(new_gene)
                else:
                    child_gene.append(gene)

            if genecounter == 7:
                if gene > m2p or gene < 0:
                    new_gene = new_gene = random.randint(0,m2p)
                    child_gene.append(new_gene)
                else:
                    child_gene.append(gene)

            if genecounter == 8:
                if gene > m3p or gene < 0:
                    new_gene = new_gene = random.randint(0,m3p)
                    child_gene.append(new_gene)

                else:
                    child_gene.append(gene)
            
                    
            genecounter += 1
        
        child.genome = child_gene


        target.update_revenue()
        child.update_revenue()

        if target.revenue > child.revenue:
            new_population.append(target)
        else:
            new_population.append(child)

    return new_population


# - - - - - - - - - - - - - - - F I N D  B E S T  I N D I V I D U A L - - - - - - - - - - - - - - - - - - - - - -

def find_best(population):
    #by Johannes
    """
    This function simply iterates through a population and returns the fittest individual
    INPUT:
    - A list of individuals, the population
    OUTPUT:
    - An object of the type "individual" that has the highest revenue value
    """

    best = rnd.choice(population)
    best.update_revenue()

    for individual in population:
        individual.update_revenue()

        if individual.revenue > best.revenue:
            best = individual

    return best



# - - - - - - - - - - - - - - - HIGH LEVEL PROFIT MODEL - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    profit = revenue - totalCost
    revenue = soldQuantitiy * sellingPrice
    totalCost = plantTypeCost(all types) + purchasingCost
    productionCost = generatedQuantity * costFactor
    puchasingCost = max(soldQuantity - generatedQuantity, 0) * costPrice

    sellingPrice = price at which we sell the energy to customers
    plantTypeCost = cost we will have to build n plants of type p
    purchasingCost = what we pay if we don't produce enough and have to buy energy from other suppliers
    costPrice = what it costs us to produce the energy
"""
def calculate_profit(individual):
    #by Johannes , Yannic
    genes = individual

    energy_produced = genes[:3]
    market_distribution = genes[3:6]
    price_distribution = genes[6:9]

    plant1 = problem.powerplant(1)
    plant2 = problem.powerplant(2)
    plant3 = problem.powerplant(3)

    market1 = problem.market(1)
    market2 = problem.market(2)
    market3 = problem.market(3)


    total_energy_produced = sum(energy_produced)
    total_energy_distributed = sum(market_distribution)

    purchasing_cost = 0
    if total_energy_produced < total_energy_distributed:
        difference_in_production = total_energy_distributed - total_energy_produced
        purchasing_cost = difference_in_production * CostPrice

    productioncosts = plantTypeCost(energy_produced[0],plant1)
    productioncosts += plantTypeCost(energy_produced[1],plant2)
    productioncosts += plantTypeCost(energy_produced[2],plant3)

    cost = purchasing_cost + productioncosts

    total_revenue = price_distribution[0]* min(market_distribution[0], demand(price_distribution[0],market1))
    total_revenue += price_distribution[1]* min(market_distribution[1], demand(price_distribution[1],market2))
    total_revenue += price_distribution[2]* min(market_distribution[2], demand(price_distribution[2],market3))

    profit = total_revenue - cost

    return profit



class problem():
    #by Marieke
    class powerplant():
        def __init__(self, planttype):
            if planttype == 1:
                self.kwhPerPlants = 50000
                self.costPerPlant = 10000
                self.maxPlants = 100

            if planttype == 2:
                self.kwhPerPlants = 600000
                self.costPerPlant = 80000
                self.maxPlants = 50

            if planttype == 3:
                self.kwhPerPlants = 4000000
                self.costPerPlant = 400000
                self.maxPlants = 3

    class market():
        def __init__(self, market):
            if problemType == 1 or problemType == 2:
                if market == 1:
                    self.maxPrice = 0.45
                    self.maxDemand = 2000000
    
                if market == 2:
                    self.maxPrice = 0.25
                    self.maxDemand = 30000000
    
                if market == 3:
                    self.maxPrice = 0.2
                    self.maxDemand = 20000000
                           
            if problemType == 3: 
                if market == 1:
                    self.maxPrice = 0.5
                    self.maxDemand = 1000000
    
                if market == 2:
                    self.maxPrice = 0.3
                    self.maxDemand = 5000000
    
                if market == 3:
                    self.maxPrice = 0.1
                    self.maxDemand = 5000000

# - - - - - - - - - - - - - - - MARKET MODEL - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def plantTypeCost(s, plant):
    """
    calculates the cost we will have to build n plants of type p

    INPUT
    - s (desired amount of energy)
    - planttype

    """
    kwhPerPlant = plant.kwhPerPlants
    maxPlants =  plant.maxPlants
    costPerPlant = plant.costPerPlant
    # if s non-positive, return 0
    if(s <= 0):
        return 0

    #if x larger than possible generation, return infinite
    psblgen = kwhPerPlant * maxPlants
    if(s > psblgen):
        return float('inf')

    #otherwise find amount of plants needed to generate s
    plantsNeeded = math.ceil(s / kwhPerPlant)

    #return cost (amount of plants * cost per plant)
    return plantsNeeded * costPerPlant

def demand(sellingPrice, market):
    #by Marieke

    """
    gives us the open demand of a market

    INPUT
    - sellingPrice (the price at which we sell energy)
    - maxPrice (maximum price customers are willing to pay)
    - maxDemand (total demand of a market)

    OUTPUT
    -

    """

    maxPrice = market.maxPrice
    maxDemand = market.maxDemand

    #if the selling price is greater than what customers want to pay, return 0
    if (sellingPrice > maxPrice):
        return 0

    #if selling price is below zero, return 0 (ignore negative values)
    if sellingPrice < 0:
        return 0

    #if we give the energy for free, return maxDemand
    if (sellingPrice == 0):
        return maxDemand

    #else determine the demand based on the selling price
    demand = maxDemand - sellingPrice**2 * maxDemand / maxPrice**2

    return demand





# - - - - - - - - - - - - - - - U S E R   I N P U T - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def user_input():
    #by Yannic
    """
    Output List with control Parameters: [crossoverRate,scalingFactor,populationSize]
    """

    #Our three Control Parameters
    crossoverRate = -1
    scalingFactor = -1
    populationSize = -1
    costprice = -1
    barChart = -1
    graph = -1
    
    global problemType
    problemType = -1
    #output = [crossoverRate,scalingFactor,populationSize,barChart,graph
    output = []
    
    if problemType == -1:
        problemType = int(input("Please specify Problem Type [1,2,3]: "))
    else:
        problemType = int(input("Population Size must be in [1,2,3]: "))

    default = int(input("Do yo want to use default values? [0]Yes [else]No: "))

    if default == 0:
            #crossoverRate
            output.append(0.5)
            #scalingFactor
            output.append(0.32)
            #populationSize
            output.append(50)
            #Costprice
            if problemType == 2:
                output.append(0.1)
            else:
                output.append(0.6)
            #print bar chart
            output.append(0)
            #print graph
            output.append(0)
    else:
        print("")
        #Crossover Rate Cr e [0,1]
        while (crossoverRate < 0) or (crossoverRate > 1):
            if crossoverRate == -1:
                crossoverRate = float(input("Please specify Crossover Rate in [0,1]: "))
            else:
                crossoverRate = int(input("Crossover rate must be must be in [0,1]: "))
        output.append(crossoverRate)
        print("")
        #Scaling factor F e (0,1)
        while (scalingFactor <= 0) or (scalingFactor >= 1):
            if scalingFactor == -1:
                scalingFactor = float(input("Please specify Scaling Factor in [0,1]: "))
            else:
                scalingFactor = float(input("Scaling Factor must be must be in [0,1]: "))
        output.append(scalingFactor)
        print("")
        #population size N > 4
        while (populationSize < 5):
            if populationSize == -1:
                print("Recommended Population size: 5-10 times the dimension of the problem.")
                populationSize = int(input("Please specify Population Size: "))
            else:
                populationSize = int(input("Population Size must be bigger than 4: "))
        output.append(populationSize)
        #Costprice
        if problemType == 2:
            output.append(0.1)
        else:
            output.append(0.6)

        #BarChart [0]
        if barChart == -1:
            barChart = float(input("Do you want to print Genome [0]yes [else]no: "))
        output.append(barChart)

        #graph [0]
        if graph == -1:
            graph = float(input("Do you want to print Graph [0]yes [else]no "))
        output.append(graph)



    return output


__MAIN__()
