import random
import math
import statistics

# https://editor.p5js.org/Koala_Sloth/sketches/Q4IbqVQhN
#create a program which simulates the downfall of western civilization

GOAL = 50000
NUM_UTOP = 20 
INIT_MIN_INT = 50
INITIAL_MAX_INT = 200
INITIAL_MODE_INT = 100 
INIT_MIN_SOC = 50
INITIAL_MAX_SOC = 200
INITIAL_MODE_SOC = 100 
INIT_MIN_ULT = 50
INITIAL_MAX_ULT = 200
INITIAL_MODE_ULT = 100 
INITIAL_MIN_LIB = 50
INITIAL_MAX_LIB = 300
INITIAL_MODE_LIB = 300
MUTATE_ODDS = 0.01
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
FAMILY_SIZE = 8
FAMILIES_PER_YEAR = 10
GENERATION_LIMIT = 500

class utopians:
    def __init__(self, sex, socialization, intelligence, ultraviolence, libido):
        self.sex = sex
        self.socialization = socialization
        self.intelligence = intelligence
        self.libido = libido
        self.ultraviolence = ultraviolence
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
    def breeding_weight(self, femal_wt, mal_wt):
            if femal_wt == mal_wt:
                self.weight = random.randrange(femal_wt, mal_wt+1) 
            else:
                self.weight = random.randrange(femal_wt, mal_wt)  
    def mutate(self, mutate_min, mutate_max):
        self.weight = math.ceil(self.weight * random.uniform(mutate_min, mutate_max))  
        



if(NUM_UTOP % 2 != 0):
    NUM_UTOP+=1

def populate(num_utop, min_wt, max_wt, mode_wt):
    parents = []
    n = 0
    while n < num_utop:
        utopian = utopians(min_wt, "M")
        parents.append(utopian)
        n+=1
    n1 = 0
    for utop in parents:
        utop.create(min_wt, max_wt, mode_wt)
    return parents
    
def fitness(population, goal):
    place_hold = []
    for ppl in population:
        place_hold.append(ppl.weight)
    ave = statistics.mean(place_hold)
    return ave/goal

def selector(population, to_retain, truf):
    sorted_population = sorted(population, key = lambda x: x.weight, reverse=False)
    if len(sorted_population) > to_retain:
        sorted_population = sorted_population[-to_retain::1]
    to_retain_by_sex = math.floor(to_retain/2)
    members_per_sex = math.floor(len(sorted_population)/2)
    females = sorted_population[0:members_per_sex]
    males = sorted_population[members_per_sex:len(sorted_population)]
    selected_females = females[-to_retain_by_sex::1]
    selected_males = males[-to_retain_by_sex::1]
    if truf == True:
        return selected_females
    elif truf == False:
        return selected_males

def breed(females, males, family_size):
    random.shuffle(males)
    random.shuffle(females)
    ave_length = math.floor((len(males) + len(females))/2)
    children = []
    n1=0
    while n1 < ave_length:
        n=0
        while n < FAMILY_SIZE:
            n+=1
            child = utopians(INITIAL_MIN_WT, "M")
            child.breeding_weight(females[n1].weight, males[n1].weight)
            children.append(child)
        n1+=1
    return children

def mutate(children, mutate_odds, mutate_min, mutate_max):
    n=0
    while n < len(children):
        if mutate_odds >= random.random():
            children[n].mutate(mutate_min, mutate_max)
        else :
            children[n] = children[n]
        n+=1
    return children

generations = 0
parents = populate(NUM_UTOP, INITIAL_MIN_WT, INITIAL_MAX_WT, INITIAL_MODE_WT)
init_pop_wts = []

n=0
while n < NUM_UTOP:
    init_pop_wts.append(parents[n].weight)
    n+=1
    

print("initial population weights = " + str(init_pop_wts))
popl_fitness = fitness(parents, GOAL)
print("initial population fitness = " + str(popl_fitness))
print("number to retain = " + str(NUM_UTOP))

ave_wt = []

stop = False

while popl_fitness < 1 and generations < GENERATION_LIMIT and stop == False:
    selected_females = selector(parents, NUM_UTOP, True)
    selected_males = selector(parents, NUM_UTOP, False)
    children = breed(selected_females, selected_males, FAMILY_SIZE)
    weight_hold = []
    children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
    place_hold = selected_males + selected_females
    parents = place_hold + children
    for i in parents:
        weight_hold.append(i.weight)
    popl_fitness = fitness(parents, GOAL)
    print("Generation " + str(generations) + " fitness: " + str(popl_fitness))
    ave_wt.append(math.floor(statistics.mean(weight_hold)))
    if math.floor(statistics.mean(weight_hold)) < 100:
        pop_wts = []
        n=0
        while n < NUM_MEN:
            pop_wts.append(parents[n].weight)
            n+=1
        print("population weights = " + str(pop_wts))
        stop = True
    generations+=1
print("average weight per generation = " + str(ave_wt))
print("number of generations = " + str(generations))
print("number of years = " + str(math.floor(generations / FAMILIES_PER_YEAR)))






