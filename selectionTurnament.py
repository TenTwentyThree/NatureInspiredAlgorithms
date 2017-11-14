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

    #defines how many individuals are in the matingpool
    sizeMatingPool = 100
    while sizeMatingPool > 0:
        #store population length for quick exces
        sizeCompetitors = len(competitors)
        #set parents to invalid values
        p1_index = -1
        p2_index = -1
        #choose differnet parents untill they are not the same individuals
        while p1_index == p2_index:
            p1_index = random.randint(0,sizePopulation-1)
            p2_index = random.randint(0,sizePopulation-1)

        p1_fit = competitors[p1_index].fitness
        p2_fit = competitors[p2_index].fitness
        #p1 is fitter than p2
        if p1_fit > p2_fit:
            #append the matingpool with the fitter parent
            matingpool.append(competitors[p1_index])
            #delete the winnging parent, because he is no longer a competitor
            competitors.pop(p1_index)
            #shring the size of the matingpool, because we have found a parent
            sizeMatingPool -= 1
        #p2 is fitter than p1
        elif p1_fit < p2_fit:
            #append the matingpool with the fitter parent
            matingpool.append(competitors[p2_index])
            #delete the winnging parent, because he is no longer a competitor
            competitors.pop(p2_index)
            #shring the size of the matingpool, because we have found a parent
            sizeMatingPool -= 1
        # if nothing holds we have a sting, booth are equaly fit, so we do nothing 

    return matingpool
