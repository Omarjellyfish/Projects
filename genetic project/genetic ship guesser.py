import random
#didnt use gloabal variables because i wanted to make pure functions that depend only on their parameters
#avoiding the use of global vars and relying on parameters only made the code more portable
#python is an implicity language so no need to mention the data type
#max number of ships around 200
def generate_unique_coordinates(locations):
    while True:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        if (x, y) not in locations:  #unique ship
            return (x, y)

def init_population(numofships,population_size):
    geneset=[]
    #nested scoping
    def generate_gene(): #generating a single gene 
        chromosome=[]
        for _ in range(numofships):
            location=generate_unique_coordinates(chromosome)
            chromosome.append(location)
        return chromosome
    
    for i in range(population_size): #generating the geneset
        geneset.append(generate_gene())
    return geneset

def get_fitness(target,hg):
    genesetWithFitness={}
    #making use of hashing to make the geneset with fitness and deal with it
    for key in hg.keys():
        fitness=0
        gene=hg[key]
        
        for location in gene:
            if location in target:
                fitness+=1 
        genesetWithFitness[key]=fitness

    return genesetWithFitness

def individual_fitness(target,individual):
    fitness=0
    individual=set(individual)#to avoid counting repeated locations
    for location in individual:
        if location in target:
            fitness+=1
    return fitness
        
#selection
def roulette_wheel_selection(geneset_fitness, num_selections):
    total_fitness = sum(geneset_fitness.values())
    selection_probs = {key: fitness / total_fitness for key, fitness in geneset_fitness.items()}#need to fix the issue with total fitness=0

    selected_indices = set()
    selected_genes = []

    while len(selected_indices) < num_selections:
        random_number = random.uniform(0, 1)
        cumulative_prob = 0

        for key, prob in selection_probs.items():
            cumulative_prob += prob
            if random_number <= cumulative_prob and key not in selected_indices:
                selected_indices.add(key)
                selected_genes.append(key)
                break

    return tuple(selected_genes)

def single_point_crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2
#treating the parents as list made the code of crossover and mutation more general and can be used in other programmes
def uniform_crossover(parent1, parent2, crossover_prob=0.5):
    child1 = []
    child2 = []
    
    for gene1, gene2 in zip(parent1, parent2):
        if random.random() < crossover_prob:
            child1.append(gene1)
            child2.append(gene2)
        else:
            child1.append(gene2)
            child2.append(gene1)
    
    return child1, child2

def randomMutation(individual, mutation_rate):
    
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            x = random.randint(0, 7)
            y = random.randint(0, 7)
            if (x,y) not in individual:
                individual[i] = (x, y)  
    return individual


def weak_parent_replacement(geneset_with_fitness, new_individual, hashed_geneset, target):
    weakest_key = min(geneset_with_fitness, key=geneset_with_fitness.get)
    newkey=max(hashed_geneset.keys())+1
    hashed_geneset[weakest_key] = new_individual
    geneset_with_fitness[weakest_key] = individual_fitness(target, new_individual)




def tournament_selection(geneset_fitness, num_selections, tournament_size):
    selected_genes = []

    while len(selected_genes) < num_selections:
        tournament = random.sample(list(geneset_fitness.keys()), tournament_size)
        tournament_fitness = {key: geneset_fitness[key] for key in tournament}
        winner = max(tournament_fitness)
        selected_genes.append(winner)

    return tuple(selected_genes)

def genetic_algorithm(target): #functional binding
    max_iterations = 100000  # Maximum number of iterations
    target_fitness = len(target)  # Fitness threshold to stop the algorithm
    best_fitness = 0
    iterations=0
    mRate=0.1
    hashed_geneset={}
    test=init_population(num_ships,120)
    for i in range(len(test)):
        hashed_geneset[i]=test[i]
    gensetWithFitness=get_fitness(target,hashed_geneset)

    
    while len(target) > max(gensetWithFitness.values()) and iterations < max_iterations:
        iterations += 1
        index1, index2 = tournament_selection(gensetWithFitness, 2, 50)  # Increased tournament size
        child1, child2 = uniform_crossover(hashed_geneset[index1], hashed_geneset[index2])
        child1 = randomMutation(child1, mRate) 
        child2 = randomMutation(child2, mRate)
        weak_parent_replacement(gensetWithFitness, child1, hashed_geneset, target)
        weak_parent_replacement(gensetWithFitness, child2, hashed_geneset, target)

        # Calculate best fitness in the current population
        best_fitness = max(gensetWithFitness.values())
        print("Iteration:", iterations, "Best Fitness:", best_fitness)
        best_solution_key = max(gensetWithFitness, key=gensetWithFitness.get)
        best_solution = hashed_geneset[best_solution_key]
        print("Best solution found with fitness:", max(gensetWithFitness.values()))
        print("Best solution:", best_solution)
        # Terminate if target fitness is reached
        if best_fitness >= target_fitness:
            break
    
    return gensetWithFitness, hashed_geneset

#python abstracts memory management
#relied heavliy on the hashmap (dict in python) datastructure due to its speed and flexability
#the use of multiple hashmaps caused a bad readability in code due to them overlapping

#generate random ships
num_ships=30 #runtime most of the vars here because python
ships=[]
for _ in range(num_ships):
    new_ship = generate_unique_coordinates(ships)
    ships.append(new_ship)

x,y=genetic_algorithm(ships)
best_solution_key = max(x, key=x.get)
best_solution = y[best_solution_key]
print("Best solution found with fitness:", max(x.values()))
print("Best solution:", best_solution)

print(ships,'target')
print('end')
#binding  objects occurs  at runtime because dynamically bound /python is dynamically typed
#variables lifetime depend on their scope 
#(name, address, value, type, lifetime, and scope).