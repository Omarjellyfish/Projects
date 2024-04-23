import random
def orderedCrossOver(parent1,parent2):
    crossover_point1 = random.randint(0, len(parent1) - 1)
    crossover_point2 = random.randint(crossover_point1 + 1, len(parent1))
    print('start Inclusive',crossover_point1,crossover_point2,'end Exclusive')
    child1 = parent1[crossover_point1:crossover_point2]
    child2=parent2[crossover_point1:crossover_point2]
    
    for gene in parent2:
        if gene not in child1: #adding as they appear in parents
            child1.append(gene)
    for gene in parent1:
        if gene not in child2:
            child2.append(gene)
    return child1,child2
parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
parent2 = [9, 3, 7, 8, 2, 6, 5, 1, 4]
print('parent1:  ',parent1)
print('parent2:  ', parent2)
child1,child2=orderedCrossOver(parent1,parent2)
print('ordered crossover')
print('Child1:  ',child1)
print('child2:  ',child2)

#other version for ordered (better version)
def orderedCrossOver2(parent1,parent2):
    crossover_point1 = random.randint(0, len(parent1) - 1)
    crossover_point2 = random.randint(crossover_point1 + 1, len(parent1))
    print('start Inclusive',crossover_point1,crossover_point2,'end Exclusive')
    child1=parent1[:crossover_point1]+parent2[crossover_point1:crossover_point2]+parent1[crossover_point2:]
    child2=parent2[:crossover_point1]+parent1[crossover_point1:crossover_point2]+parent2[crossover_point2:]
    for index in range(crossover_point1,crossover_point2):
        child1=child1[:crossover_point1]+sorted(child1[crossover_point1:crossover_point2],key=parent1.index)
        child2=child2[:crossover_point1]+sorted(child2[crossover_point1:crossover_point2],key=parent2.index)
    return child1,child2


print('parent1:  ',parent1)
print('parent2:  ', parent2)
child1,child2=orderedCrossOver(parent1,parent2)
print('ordered crossover2')
print('Child1:  ',child1)
print('child2:  ',child2)

def PMX(parent1,parent2):
    p1={}
    p2={}
    for index,item in enumerate(parent1):
        p1[index]=item
    for index,item in enumerate(parent2):
        p2[index]=item
    crossover_point1 = random.randint(0, len(parent1) - 1)
    crossover_point2 = random.randint(crossover_point1 + 1, len(parent1))
    print('start Inclusive',crossover_point1,crossover_point2,'end Exclusive')
    child1=parent1[:crossover_point1]+parent2[crossover_point1:crossover_point2]+parent1[crossover_point2:]
    child2=parent2[:crossover_point1]+parent1[crossover_point1:crossover_point2]+parent2[crossover_point2:]
    for i in range(len(child1)):
        if child1[i] in parent2[crossover_point1:crossover_point2]:
            child1[i]=p2[i]
    for i in range(len(child2)):
        if child2[i] in parent1[crossover_point1:crossover_point2]:
            child1[i]=p1[i]
    return child1,child2


child1,child2=PMX(parent1,parent2)
print('pmx cross')
print('Child1:  ',child1)
print('child2:  ',child2)

