__author__ = 'Luis Fabregues de los Santos'
import gnt_damage
import random
from header_classes import Battler

# generate a random population of 200 with sum of stats equal to 100
population = []
for i in xrange(200):
    pa = int(random.random()*100)
    pd = int(random.random()*(100-pa))
    ma = int(random.random()*(100-pa-pd))
    md = int(random.random()*(100-pa-pd-ma))
    v = int(random.random()*(100-pa-pd-ma-md))
    hp = 100-pa-pd-ma-md-v
    population.append(Battler(hp, pa, pd, ma, md, v))

# here we call the genetic algorithm with the desired damage formula
final_population = gnt_damage.genetics(population, 0)
for subject in final_population:
    print subject.tostring()