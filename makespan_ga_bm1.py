import numpy as np
import random


# Benchmark Problem 1: Uniformly Randomized

# For testing
pop = [[2, 3, 4, 6], [1, 2, 3, 6], [3, 4, 5, 7]]


def generate_machines(number_of_machines):
    # Generate 20 machines with random speed values in seconds


    """Args:
            number_of_machines(int) - Number og machines to be considered
       Returns:
            speed_of machines(list) - List of speed of machines
             """
    speed_of_machines = random.sample(range(300), number_of_machines)

    return speed_of_machines


speed_of_machines = generate_machines(20)


def generate_jobs():
    # Generate jobs (300 job's processing time) as given by the Benchmark Problem 1

    """Args:
            number_of_jobs(int) - Number of jobs to be performed
        Returns:
            processing_time_of_jobs(list) - List of 300 jobs and their corresponding speed
    """

    processing_time_of_jobs_200 = random.sample(range(10, 1000), 200)
    processing_time_of_jobs_100 = random.sample(range(100, 300), 100)

    return random.sample((processing_time_of_jobs_200 + processing_time_of_jobs_100),
                         (len(processing_time_of_jobs_100) + len(processing_time_of_jobs_200)))


def partition_jobs(generated_jobs):
    """Args:
            generated_jobs(list) - List of jobs processing time
        Returns:
            divided_jobs(array) - List of lists that corresponds to jobs for machines. size(divided_jobs) = total_jobs/number_of_machines
    """

    divided_jobs = [generated_jobs[job:job + 20] for job in range(0, len(generated_jobs), 20)]
    return divided_jobs


def generate_chromosomes(jobs, number_of_chromosomes):
    # Generate chromosomes by shuffling the task "number_of_chromosomes" times
    """ Args:
         task(list) - List of 20 jobs processing times
         number_of_chromosomes(int) - Length of population
        Returns:
         population(array) - List of lists that corresponds to candidate solutions in current generation
    """

    population = [random.sample(job, len(jobs)) for _ in range(number_of_chromosomes)]

    return population


def get_fittest(population, machines):
    # Evaluate each individual in the population
    # Choose the fittest candidate among the population using fitness values

    """
        Args:
            population(array) - List of lists that corresponds to candidate solutions of current generation
            machines(list) - List of speed of machines
        Returns:
            fittest_candidate(list) - Fittest candidate solution in population
    """

    fitness_values = []

    for candidate in population:
        fitness_value = [job_processing_time * machine_speed for job_processing_time, machine_speed in
                         zip(candidate, machines)]
        fitness_value = np.sum(fitness_value)
        fitness_values.append(fitness_value)
    fittest_idx = fitness_values.index(min(fitness_values))
    fittest_candidate = population[fittest_idx]

    return fittest_candidate


def roulette_wheel_selection(population, machines):
    # Evaluate each individual in the population
    # Choose the fittest candidate among the population using fitness values

    """
        Args:
            population(array) - List of lists that corresponds to candidate solutions of current generation
            machines(list) - List of speed of machines
        Returns:
            fittest_candidate(list) - Fittest candidate solution in population
    """

    # Measure the fitness
    fitness_values = []

    for candidate in population:
        fitness_value = [job_processing_time * machine_speed for job_processing_time, machine_speed in
                         zip(candidate, machines)]
        fitness_value = np.sum(fitness_value)
        fitness_values.append(fitness_value)

    # Create roulette wheel. Reference, wikipedia

    for i in range(0, len(population)):
        prob_survival = [fitness_value / np.sum(fitness_values) for fitness_value in fitness_values ]
        # Generate intervals between the prob_survivals
        prob_intervals = [sum(prob_survival[:i+1]) for i in range(len(prob_survival))]

    print("rouletter wheel", prob_intervals)
    # Rotate the wheel and get the new population
    new_population = []
    for _candidate in range(0, len(population)-1):
        rand_num = np.random.rand()
        for i, candidate in enumerate(population):
            # print(rand_num, prob_intervals[i])
            if rand_num < prob_intervals[i]:
                new_population.append(candidate)
                break

    return new_population

machines = [1,1,1,1]
print(roulette_wheel_selection(pop,machines))

def mutate(population):
    # Choose a candidate in popuation and mutate it by randomly choosing two genes and swap them

    """
        Args:
             population(array) - List of lists that corresponds to candidate solutions of current generation
        Returns:
            mutated_population(array) - List of lists that corresponds to candidate solutions for next generation
    """

    # Choose random candidate

    mutate_candidate_idx = random.randint(0, len(population)-1)
    mutate_candidate = population[mutate_candidate_idx]
    generate_random_idx = random.sample(range(0, len(mutate_candidate) - 1), 2)
    gene_idx1, gene_idx2 = generate_random_idx[0], generate_random_idx[1]
    mutate_candidate[gene_idx2], mutate_candidate[gene_idx1] = mutate_candidate[gene_idx1], mutate_candidate[gene_idx2]

    return mutate_candidate


# print(mutate(pop))

def crossover(fittest, luckiest):  # I opt to choose best and the worst performing individuals as parents for crossover

    # Apply one point crossover and generate 2 offsprings
    """
        Args:
            fittest(list) - Fittest candidate in the population
            luckiest(list) - Low scored candidate in the population

        Return:
            offsprings(array) - List of offsprings

    """
    idx = random.randint(1, len(fittest)-1)

    offspring1, offspring2 = ([fittest[:idx] + luckiest[idx:]], [luckiest[:idx] + fittest[idx:]])

    return offspring1, offspring2

# print(crossover(pop[0], pop[2]))

