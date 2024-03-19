import random
import math
import statistics

# https://editor.p5js.org/Koala_Sloth/sketches/Q4IbqVQhN
#create a program which simulates the downfall of western civilization

GOAL = 500
NUM_UTOP = 20 
INITIAL_MIN_SOC = 50
INITIAL_MAX_SOC = 200
INITIAL_MODE_SOC = 100 
INITIAL_MIN_ULT = 50
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
    def __init__(self, sex, socialization, ultraviolence, libido):
        self.sex = sex
        self.socialization = socialization
        self.libido = libido
        self.ultraviolence = ultraviolence
    def create(self,a,b,c,x):
        fc = (c - a)/(b - a)
        u = random.random()
        y = 0
        if u < fc:
            y = (b-a) * (c-a)
            if x == "socialization":
                self.socialization = math.floor(a + math.sqrt(y*u))
            elif x == "ultraviolence":
                self.ultraviolence = math.floor(a + math.sqrt(y*u))
            elif x == "libido":
                self.libido = math.floor(a + math.sqrt(y*u))
        else:
            y = (b-a) * (b-c)
            if x == "socialization":
                self.socialization = math.floor(b - math.sqrt(y*(1.0-u)))
            elif x == "ultraviolence":
                self.ultraviolence = math.floor(b - math.sqrt(y*(1.0-u)))
            elif x == "libido":        
                self.libido = math.floor(b - math.sqrt(y*(1.0-u)))
    def breeding_stats(self, femal, mal, x):
            if femal == mal:
                if x == "socialization":
                    self.socialization = random.randrange(femal, mal+1) 
                elif x == "ultraviolence":
                    self.ultraviolence = random.randrange(femal, mal+1) 
                elif x == "libido":
                    self.libido = random.randrange(femal, mal+1) 
            elif femal > mal:
                if x == "socialization":
                    self.socialization = random.randrange(mal, femal) 
                elif x == "ultraviolence":
                    self.ultraviolence = random.randrange(mal, femal)  
                elif x == "libido":
                    self.libido = random.randrange(mal, femal)
            else:
                if x == "socialization":
                    self.socialization = random.randrange(femal, mal) 
                elif x == "ultraviolence":
                    self.ultraviolence = random.randrange(femal, mal) 
                elif x == "libido":
                    self.libido = random.randrange(femal, mal)   
    def mutate(self, mutate_min, mutate_max, x):
        if x == "socialization":
            self.socialization = math.ceil(self.socialization * random.uniform(mutate_min, mutate_max))  
        elif x == "ultraviolence":
            self.ultraviolence = math.ceil(self.ultraviolence * random.uniform(mutate_min, mutate_max))  
        elif x == "libido":
            self.libido = math.ceil(self.libido * random.uniform(mutate_min, mutate_max))  


if(NUM_UTOP % 2 != 0):
    NUM_UTOP+=1

def populate(num_utop, min_soc, max_soc, mode_soc, min_ult, max_ult, mode_ult, min_lib, max_lib, mode_lib):
    parents = []
    n = 0
    while n < num_utop:
        utopian = utopians("M", min_soc, min_ult, min_lib)
        parents.append(utopian)
        n+=1
    n1 = 0
    for utop in parents:
        utop.create(min_soc, max_soc, mode_soc, "socialization")
        utop.create(min_ult, max_ult, mode_ult, "ultraviolence")
        utop.create(min_lib, max_lib, mode_lib, "libido")

    return parents
    
def fitness(population, goal):
    place_hold = []
    for ppl in population:
        place_hold.append(ppl.socialization)
        place_hold.append(ppl.ultraviolence)
        place_hold.append(ppl.libido)
    ave = statistics.mean(place_hold)
    return ave/goal

def selector(population, to_retain, truf):
    sorted_population = sorted(population, key = lambda x: x.socialization, reverse=False)
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
            child = utopians("M", INITIAL_MIN_SOC, INITIAL_MIN_ULT, INITIAL_MIN_LIB)
            child.breeding_stats(females[n1].socialization, males[n1].socialization, "socialization")
            child.breeding_stats(females[n1].ultraviolence, males[n1].ultraviolence, "ultraviolence")
            child.breeding_stats(females[n1].libido, males[n1].libido, "libido")
            children.append(child)
        n1+=1
    return children

def mutate(children, mutate_odds, mutate_min, mutate_max):
    n=0
    while n < len(children):
        if mutate_odds >= random.random():
            children[n].mutate(mutate_min, mutate_max, "socialization")
            children[n].mutate(mutate_min, mutate_max, "ultraviolence")
            children[n].mutate(mutate_min, mutate_max, "libido")
        else :
            children[n] = children[n]
        n+=1
    return children

generations = 0
parents = populate(NUM_UTOP, INITIAL_MIN_SOC, INITIAL_MAX_SOC, INITIAL_MODE_SOC, INITIAL_MIN_ULT, INITIAL_MAX_ULT, INITIAL_MODE_ULT, INITIAL_MIN_LIB, INITIAL_MAX_LIB, INITIAL_MODE_LIB)
init_pop_soc = []
init_pop_ult = []
init_pop_lib = []


n=0
while n < NUM_UTOP:
    init_pop_soc.append(parents[n].socialization)
    init_pop_ult.append(parents[n].ultraviolence)
    init_pop_lib.append(parents[n].libido)
    n+=1
    

print("initial population socialization = " + str(init_pop_soc))
print("initial population ultraviolence = " + str(init_pop_ult))
print("initial population libido = " + str(init_pop_lib))
popl_fitness = fitness(parents, GOAL)
print("initial population fitness = " + str(popl_fitness))
print("number to retain = " + str(NUM_UTOP))

ave_soc = []
ave_ult = []
ave_lib = []

while popl_fitness < 1 and generations < GENERATION_LIMIT:
    selected_females = selector(parents, NUM_UTOP, True)
    selected_males = selector(parents, NUM_UTOP, False)
    children = breed(selected_females, selected_males, FAMILY_SIZE)
    soc_hold = []
    ult_hold = []
    lib_hold = []
    children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
    place_hold = selected_males + selected_females
    parents = place_hold + children
    for i in parents:
        soc_hold.append(i.socialization)
        ult_hold.append(i.ultraviolence)
        lib_hold.append(i.libido)
    popl_fitness = fitness(parents, GOAL)
    print("Generation " + str(generations) + " fitness: " + str(popl_fitness))
    ave_soc.append(math.floor(statistics.mean(soc_hold)))
    ave_ult.append(math.floor(statistics.mean(ult_hold)))
    ave_lib.append(math.floor(statistics.mean(lib_hold)))
    generations+=1
print("average amount of socialization per generation = " + str(ave_soc))
print("average likelihood of ultraviolence per generation = " + str(ave_ult))
print("average libido per generation = " + str(ave_lib))
print("number of generations = " + str(generations))
print("number of years = " + str(math.floor(generations / FAMILIES_PER_YEAR)))






