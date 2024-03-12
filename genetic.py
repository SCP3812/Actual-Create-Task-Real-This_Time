import random
import math
import statistics

# https://editor.p5js.org/Koala_Sloth/sketches/Q4IbqVQhN
#create a program which simulates the downfall of western civilization

GOAL = 50000
NUM_MEN = 20 
INITIAL_MIN_WT = 200
INITIAL_MAX_WT = 600
INITIAL_MODE_WT = 300 
MUTATE_ODDS = 0.01
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
FAMILY_SIZE = 8
FAMILIES_PER_YEAR = 10
GENERATION_LIMIT = 500

class human:
    def __init__(name, weight)
        self.name = name
        self.weight = weight
    def create(a,b,c):
        fc = (c - a)/(b - a)
        u = random()
        var x = 0
        if u < fc:
            x = (b-a) * (c-a)
            self.weight = math.floor(a + math.sqrt(x*u))
        else:
            x = (b-a) * (b-c)
            self.weight = math.floor(b - math.sqrt(x*(1.0-u)))
    def breeding_weight(femal_wt, mal_wt):
        self.weight = randrange(femal_wt, mal_wt)  
    def mutate(mutate_min, mutate_max):
        self.weight = math.ceil(self.weight * randrange(mutate_min, mutate_max))  

if(NUM_MEN % 2 != 0):
    NUM_MEN+=1

def populate(num_men, min_wt, max_wt, mode_wt):
    parents = []
    n = 0
    while n < num_men:
        man = human(n, min_wt)
        parents.append(man)
        n+=1
    n1 = 0
    for men in parents:
        men.create(min_wt, max_wt, mode_wt)
    return parents
    
def fitness(population, goal):
    place_hold = []
    for ppl in population
        place_hold.append(population[i].weight)
    ave = statistics.mean(place_hold)
    return ave/goal

def selector(population, to_retain, truf):
    sorted_population = sorted(population)
    if len(sorted_population) > to_retain:
        sorted_population = sorted_population.slice(-to_retain)
    to_retain_by_sex = math.floor(to_retain/2)
    members_per_sex = math.floor(len(sorted_population)/2)
    females = sorted_population[0:members_per_sex]
    males = sorted_population[members_per_sex:len(sorted_population)]
    selected_females = females.slices(-to_retain_by_sex)
    selected_males = males.slice(-to_retain_by_sex)
    if truf == true:
        return selected_females
    elif truf == false:
        return selected_males

def breed(males, females, family_size):
    
    return

def mutate(children, mutate_odds, mutate_min, mutate_max)
    return

def main():
    return



