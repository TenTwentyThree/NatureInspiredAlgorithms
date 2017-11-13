import numpy as np
import random


def roulette_wheel_selection_(population):

    """
    Args:
        population(list): List of objects which include  tuple of individuals(genome, fitness)
    Returns:
        new_population(list): List of objects selected for next generation
    """

    # Create roulette wheel. Reference, wikipedia

    # genomes = [individual[0] for individual in population]
    fitness_values = [individual[1] for individual in population]

    prob_intervals = None
    for i in range(0, len(population)):

        prob_survival = [fitness_value / np.sum(fitness_values) for fitness_value in fitness_values]

        # Generate intervals between the prob_survivals
        prob_intervals = [sum(prob_survival[:i + 1]) for i in range(len(prob_survival))]

        # prev_prob = 0
        # generate i prob_intervals prev_prob+prob_survival

    # Rotate the wheel and get the new population
    new_population = []
    for _ in range(0, len(population)):
        rand_num = np.random.rand()
        for i, candidate in enumerate(population):
            # print(rand_num, prob_intervals[i])
            if rand_num < prob_intervals[i]:
                new_population.append(candidate)  # Index of fitness in fitness values corresponds to individual in
                break

    return new_population

# Test
pop = [([1, 2, 3], 1.5), ([1, 1, 1], 1), ([2, 2, 2], 2.1), ([3, 2, 3], 1.1), ([1, 3, 3], 5)]
new_pop = roulette_wheel_selection_(pop)
print(new_pop)