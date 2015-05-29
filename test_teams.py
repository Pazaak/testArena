__author__ = 'Luis Fabregues de los Santos'
import gnt_teams
import random
from header_classes import Battler, proxyBattler
import combat_methods

size_teams = 5

# //////////////////////////////////////////////////
# make the stats of the classes global data and make
# the objects reference that data
# //////////////////////////////////////////////////



# we'll create a matrix of each class stats (keeping it short to index)
cls = []
f = open('classes')
line = f.readline()
while len(line) > 0:
    cont = line.split()
    cls.append(Battler(int(cont[0]), int(cont[1]), int(cont[2]), int(cont[3]), int(cont[4]), int(cont[5]), int(cont[6])
                       , cont[7]))
    line = f.readline()


# generate a random population of 200 with sum of stats equal to 100
population = []
for i in xrange(20):
    team = []
    for j in xrange(size_teams):
        team.append(proxyBattler(cls[int(random.random()*8)]))
    population.append(team)
# here we call the genetic algorithm with the desired damage formula
final_population = gnt_teams.genetics(population, 0, cls)
for subject in final_population:
    for battler in subject:
        print str(battler)
    print "----------------"
