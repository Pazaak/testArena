__author__ = 'Luis Fabregues de los Santos'
from combat_methods import battle
from header_classes import Battler
import random

# Ranking method, here the subjects will use a tournament style ranking
def ranking(population, formula):
    for i in xrange(0, len(population)-1, 2):
        battle(population[i], population[i+1], formula)
    # neoPopulation will contain the subjects that survived the ranking
    neoPopulation = []
    for subject in population:
        if subject.HP > 0:
            neoPopulation.append(subject)
    return neoPopulation


# crossover method that takes each pair of subjects and switch around their attributes
# hp will be recalculated to prevent unfeasible children
# we will use an uniform crossover
def crossover(population):
    neoPopulation = []
    for i in xrange(0, len(population)-1, 2):
        pa_ = population[i+1].PA
        pd_ = population[i].PD
        ma_ = population[i+1].MA
        md_ = population[i].MD
        v_ = population[i+1].V
        hp_ = 100-pa_-pd_-ma_-md_-v_
        if hp_ <= 0:
            pa_ = int(pa_*0.5)
            pd_ = int(pd_*0.5)
            ma_ = int(ma_*0.5)
            md_ = int(md_*0.5)
            v_ = int(v_*0.5)
            hp_ = 100-pa_-pd_-ma_-md_-v_
        neoPopulation.append(Battler(hp_, pa_, pd_, ma_, md_, v_))
        pa_ = population[i].PA
        pd_ = population[i+1].PD
        ma_ = population[i].MA
        md_ = population[i+1].MD
        v_ = population[i].V
        hp_ = 100-pa_-pd_-ma_-md_-v_
        if hp_ <= 0:
            pa_ = int(pa_*0.5)
            pd_ = int(pd_*0.5)
            ma_ = int(ma_*0.5)
            md_ = int(md_*0.5)
            v_ = int(v_*0.5)
            hp_ = 100-pa_-pd_-ma_-md_-v_
        neoPopulation.append(Battler(hp_, pa_, pd_, ma_, md_, v_))
    return neoPopulation

# we'll use a non-uniform mutation scheme
def mutation(children, mutation_factor, mutation_probability):
    for i in xrange(mutation_factor):
        if random.random() < mutation_probability:
            choosen = int(random.random()*len(children))
            atribute = int(random.random()*6)
            if atribute == 0 and children[choosen].PA > 1 and children[choosen].PD > 1:
                children[choosen].maxHP += 2
                children[choosen].HP += 2
                children[choosen].PA -= 1
                children[choosen].PD -= 1
            if atribute == 1 and children[choosen].HP > 1 and children[choosen].PD > 1:
                children[choosen].maxHP -= 1
                children[choosen].HP -= 1
                children[choosen].PA += 2
                children[choosen].PD -= 1
            if atribute == 2 and children[choosen].HP > 1 and children[choosen].PA > 1:
                children[choosen].maxHP -= 1
                children[choosen].HP -= 1
                children[choosen].PA -= 1
                children[choosen].PD += 2
            if atribute == 3 and children[choosen].MA > 1 and children[choosen].MD > 1:
                children[choosen].MA -= 1
                children[choosen].MD -= 1
                children[choosen].V += 2
            if atribute == 4 and children[choosen].MA > 1 and children[choosen].V > 1:
                children[choosen].MA -= 1
                children[choosen].MD += 2
                children[choosen].V -= 1
            if atribute == 5 and children[choosen].MD > 1 and children[choosen].V > 1:
                children[choosen].MA += 2
                children[choosen].MD -= 1
                children[choosen].V -= 1
    return children


def genetics(population, formula):
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
        population = population + mutation(neoPopulation, mutation_factor, mutation_probability)
        mutation_probability -= 0.0001
    population = ranking(population, formula)

    return population

