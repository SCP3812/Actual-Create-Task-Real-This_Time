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
    def __init__(self, weight):
        self.weight = weight
    def create(self,a,b,c):
        fc = (c - a)/(b - a)
        u = random.random()
        x = 0
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
        man = human(min_wt)
        parents.append(man)
        n+=1
    n1 = 0
    for men in parents:
        men.create(min_wt, max_wt, mode_wt)
    return parents
    
def fitness(population, goal):
    place_hold = []
    for ppl in population:
        place_hold.append(ppl.weight)
        print(ppl.weight)
    print(place_hold)
    ave = statistics.mean(place_hold)
    return ave/goal

def selector(population, to_retain, truf):
    sorted_population = sorted(population, key = lambda x: x.weight, reverse=True)
    if len(sorted_population) > to_retain:
        sorted_population = sorted_population.slice(-to_retain)
    to_retain_by_sex = math.floor(to_retain/2)
    members_per_sex = math.floor(len(sorted_population)/2)
    females = sorted_population[0:members_per_sex]
    males = sorted_population[members_per_sex:len(sorted_population)]
    selected_females = females[to_retain_by_sex:len(females)]
    selected_males = males[to_retain_by_sex:len(males)]
    if truf == True:
        return selected_females
    elif truf == False:
        return selected_males

def breed(males, females, family_size):
    random.shuffle(males)
    random.shuffle(females)
    ave_length = math.floor((len(males) + len(females))/2)
    children = []
    n=0
    while n < ave_length:
        n+=1
        n1=0
        while n < 0:
            n1+=1
            child = human(n1, INITIAL_MIN_WT)
            child.breeding_weight(females[n1].weight, males[n1].weight)
            children.append(child)
    return children

def mutate(children, mutate_odds, mutate_min, mutate_max):
    n=0
    while n < len(children):
        n+=1
        if mutate_odds >= math.random():
            children[i].mutate(mutate_min, mutate_max)
        else :
            children[i] = children[i]
    return children

generations = 0
parents = populate(NUM_MEN, INITIAL_MIN_WT, INITIAL_MAX_WT, INITIAL_MODE_WT)
init_pop_wts = []

n=0
while n < NUM_MEN:
    init_pop_wts.append(parents[n].weight)
    n+=1
    

print("initial population weights = " + str(init_pop_wts))
popl_fitness = fitness(parents, GOAL)
print("initial population fitness = " + str(popl_fitness))
print("number to retain = " + str(NUM_MEN))

ave_wt = []

while popl_fitness < 1 and generations < GENERATION_LIMIT:
    selected_females = selector(parents, NUM_MEN, True)
    selected_males = selector(parents, NUM_MEN, False)
    children = breed(selected_males, selected_females, FAMILY_SIZE)
    weight_hold = []
    children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
    place_hold = selected_males + selected_females
    parents = place_hold + children
    for i in parents:
        weight_hold.append(i.weight)
    popl_fitness = fitness(parents, GOAL)
    print("Generation " + generations + " fitness: " + popl_fitness)
    ave_wt.append(math.floor(statistics.mean(weight_hold)))
    generations+=1
print("average weight per generation = " + ave_wt)
print("number of generation = " + generations)
print("number of years = " + Math.floor(generations / LITTERS_PER_YEAR))




