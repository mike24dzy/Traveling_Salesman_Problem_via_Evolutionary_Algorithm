# Travelling Salesman
# Varation Genetic Algorthm for TSP1 longest path
# run 3

import numpy as np
import random
import math as mt
# import matplotlib.pyplot as plt

x = []
y = []

with open('TSP1GA.txt', 'r') as points1:
    reader = np.loadtxt(points1, delimiter = ',')
    for row in reader:
        x.append(row[0])
        y.append(row[1])

comb = []
for b in range(len(x)):
    comb.append([x[b], y[b]])

def distance(C):
    d = []
    for i in range(len(C)-1):
        d.append(mt.sqrt((C[i+1][0] - C[i][0])**2 + ((C[i+1][1] - C[i][1])**2)))
    d.append(mt.sqrt((C[-1][0] - C[0][0])**2 + ((C[-1][1] - C[0][1])**2)))          
    totald = np.sum(d)
    return totald 

# now I have the original points combination
# now let's do crossover first 

def crossover(p1, p2):
#     np.random.shuffle() # now we first create 2 parents which is shuffling the comb
#     p1 = P
#     np.random.shuffle(P) 
#     p2 = P
    c11 = []
    c22 = []
    # now lets randomly take a portion from both parents 1 and 2 but the portion size is 500
    n1 = random.randint(0, 792)
    n2 = n1 + 200
    indices = list(range(n1, n2))
    # print(len(indices))
    for index in indices:
        c11.append(p1[index]) # this is what we take from parent 1
        c22.append(p2[index])
#     print(np.shape(indices))


    # now we want to delete any points we have in c11 from parent 2 (p22)
    p2new = []
    p1new = []
    for i in range(0, 993):
        if p2[i] not in c11: # compare p2 with the portion we took out from parent 1
            p2new.append(p2[i]) # now we append a new list called p2new which is the ones that not equal to the ones in c11
        if p1[i] not in c22:
            p1new.append(p1[i]) # now we have a new list p1new with no repeated points in c22
    # now we can combine the child 1 by adding p2new and c11 and child 2 by adding p1new and c22
    p2new.extend(c11)
    p1new.extend(c22)
    child1 = p2new
    child2 = p1new
    child.append(child1)
    child.append(child2)
    
#     print (p1)
#     print (p2)
#     print (len(c11))
#     print (len(c22))
#     print (child1)
#     print (child2)

def mutation(c1, c2):
    n = random.randint(0,9)
    if n < mutate_rate:
        cm1 = c1
        cm2 = c2
        r1 = random.randint(0,992)
        r2 = random.randint(0,992)
        cm1[r1], cm1[r2] = cm1[r2], cm1[r1]
        cm2[r1], cm2[r2] = cm2[r2], cm2[r1]
        dcm1 = distance(cm1)
        dcm2 = distance(cm2)
        int_pop.append(cm1)
        int_pop.append(cm2)
        dis.append(dcm1)
        dis.append(dcm2)
    else:
        int_pop.append(c1)
        int_pop.append(c2)
        dc1 = distance(c1)
        dc2 = distance(c2)
        dis.append(dc1)
        dis.append(dc2)

def picknextgen(M, N):
    disindex = np.argsort(N)
    sortedpop = []
    for a in range(0, 200):
        sortedpop.append(M[disindex[a]])
    newpop = sortedpop[100:]
    short = []
    for v in range(0, 100):
        disevals.append(distance(newpop[v]))
        short.append(distance(newpop[v]))
    shortest.append(min(short))
    del M[:]
    del child[:]
    del N[:]
    for b in range(0, 100):
        M.append(newpop[b])
        N.append(short[b])


# generate a population of 100 parents
if __name__ == "__main__":
    mutate_rate = 5
    int_pop = []
    child = []
    dis = []
    disevals = []
    evals  = list(range(1000001))
    del evals[0]
    shortest = []
    for q in range(0,100):
        combination = comb
        np.random.shuffle(combination)
        int_pop.append(combination)
        d = distance(combination)
        dis.append(d)
        disevals.append(d)
#     print (len(dis))
#     print (len(int_pop[0]))
    # now we have 100 initial population of parents
    # now we can start with the next for loop to run 1 million times which contains the genetic process

    for z in range(0, 9999):
        for m in np.arange(0, 100, 2):
            crossover(int_pop[m], int_pop[m+1])
            mutation(child[m], child[m+1])
            # after the loop, the int_pop would have 200 populatopns with parents and children
            # and dis[] will have 200 populations and 200 corresponding distances
            # print (len(int_pop))
#             print (len(child))
#             print (len(dis))
        picknextgen(int_pop, dis)
    # print (z)
    bestpath = int_pop[99]

    csvfile = open("va1l_ed3.txt", "a")
    for tick in range(len(evals)):
        csvfile.write(str(evals[tick]) + ',')
        csvfile.write(str(disevals[tick]) + '\n')
    csvfile.close()

    csvfile1 = open("va1l_bestpoints3.txt", "a")
    for tic in range(len(shortest)):
        csvfile1.write(str(shortest[tic]) + '\n')
    csvfile1.close()    

    csvfile2 = open("va1l_bestpath3.txt", "a")
    for ti in range(len(bestpath)):
        csvfile2.write(str(bestpath[ti]) + '\n')
    csvfile2.close()    
    
    # plt.figure(0)
    # plt.plot(evals, disevals)
    # plt.xlabel('evals')
    # plt.ylabel('distance')
    # plt.title('genetic algorithm dis vs evals')
    # plt.show()

    # plt.figure(1)
    # x1 = []
    # y1 = []
    # for l in range(0, 993):
    #     x1.append(bestpath[l][0])
    #     y1.append(bestpath[l][1])
    # plt.plot(x, y, '-xb')
    # plt.title('best path found')
    # plt.show()