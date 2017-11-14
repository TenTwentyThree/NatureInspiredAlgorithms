import random

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
