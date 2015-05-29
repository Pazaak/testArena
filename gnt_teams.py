__author__ = 'Luis Fabregues de los Santos'
from combat_methods import team_battle
from header_classes import proxyBattler
import random

# Ranking method, here the subjects will use a tournament style ranking
def ranking(population, formula):
    for i in xrange(0, len(population)-1, 2):
        team_battle(population[i], population[i+1], formula)
    # neoPopulation will contain the subjects that survived the ranking
    neoPopulation = []
    for subject in population:
        if subject[0].team == 0:
            neoPopulation.append(subject)
    return neoPopulation


# Here each pair of members of the population create a pair of children
# by exchanging their battlers. As the order is irrelevant, we'll use a simple
# uniform crossover
def crossover(population):
    neoPopulation = []
    for i in xrange(0, len(population)-1, 2):
        child1 = []
        child2 = []
        swap = True
        for battler in population[i]:
            if swap:
                child1.append(proxyBattler(battler.job))
            else:
                child2.append(proxyBattler(battler.job))
            swap = not swap
        for battler in population[i+1]:
            if swap:
                child1.append(proxyBattler(battler.job))
            else:
                child2.append(proxyBattler(battler.job))
            swap = not swap
        neoPopulation.append(child1)
        neoPopulation.append(child2)
    return neoPopulation

# we'll use a non-uniform mutation scheme
def mutation(children, mutation_factor, mutation_probability, cls):
    for i in xrange(mutation_factor):
        if random.random() < mutation_probability:
            choosen = int(random.random()*len(children))
            old_battler = int(random.random()*len(children[choosen]))
            children[choosen][old_battler] = proxyBattler(cls[random.random()*len(cls)])
    return children


def genetics(population, formula, cls):
    # variable to determine the number of times
    # we will try to mutate members of the population
    mutation_factor = int(len(population)*0.02)
    # this is the probability that a mutation happens and will be decreased each iteration
    mutation_probability = 1
    iterations = 0
    while iterations < 10000:
        iterations += 1
        population = ranking(population, formula)
        neoPopulation = crossover(population)
        population = population + mutation(neoPopulation, mutation_factor, mutation_probability, cls)
        mutation_probability -= 0.0001
    population = ranking(population, formula)

    return population

