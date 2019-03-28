# Travelling Salesman
# RMHC for TSP2 longest path
# run 1

import numpy as np
import random
import math as mt
# import matplotlib.pyplot as plt


x = np.array([])
y = np.array([])

with open('TSP2.txt', 'r') as points1: 
    reader = np.loadtxt(points1, delimiter = ',')
    for row in reader:
        x = np.append(x, row[0])
        y = np.append(y, row[1])

#comb = []
#for b in range(len(x)):
#    comb.append([x[b], y[b]])

def distance(A, B):
    d = np.array([])
    for i in range(len(A)-1):
        d = np.append(d, mt.sqrt((A[i+1] - A[i])**2 + ((B[i+1] - B[i])**2)))
    d = np.append(d, mt.sqrt((A[-1] - A[0])**2 + ((B[-1] - B[0])**2)))          
    totald = np.sum(d)
    return totald 

def runRMHC(C, D):
    best1 = C
    best2 = D
    dis = np.array([])
    evals = np.array([])
    bestpointsx = np.array([])
    bestpointsy = np.array([])
    # bestdiss = np.array([])
    min_distance = distance(C, D)
    dis = np.append(dis, min_distance)
    evals = np.append(evals, 1)
    
    for z in range(0,999999):
        evals = np.append(evals, z+2)
        best1 = np.array(C)
        best2 = np.array(D)
        
        min_distance = distance(C,D)
        
        index1 = random.randint(0, len(C)-1)
        index2 = random.randint(0, len(C)-1)
        best1[index1], best1[index2] = best1[index2], best1[index1]
        best2[index1], best2[index2] = best2[index2], best2[index1]
        
        new_min_distance = distance(best1, best2)
        dis = np.append(dis, new_min_distance)
        
        # minimum_distance = min(dis)
        if new_min_distance > min_distance:
            #dis2 = np.append(dis2, new_min_distance)
            min_distance = new_min_distance
            C = np.array(best1)
            D = np.array(best2)
            bestpointsx = np.append(bestpointsx, best1)
            bestpointsy = np.append(bestpointsy, best2)
            # bestdiss = np.append(bestdiss, distance(bestpointsx,bestpointsy))
        # print (z)
    
    bestx = C
    besty = D
    # print (len(evals))
    # print (len(dis))
    # print (min(dis))


    csvfile = open("hc2l_run1.txt", "a")
    for tick in range(len(evals)):
        csvfile.write(str(evals[tick]) + ',')
        csvfile.write(str(dis[tick]) + '\n')
    csvfile.close()

    csvfile1 = open("hc2l_bestpointsrun1.txt", "a")
    for t in range(len(bestpointsx)):
        csvfile1.write(str(bestpointsx[t]) + ',')
        csvfile1.write(str(bestpointsy[t]) + '\n')
    csvfile.close()

    # csvfile2 = open("hc1s_bestdistancerun1.txt", "a")
    # for ti in range(len(bestdiss)):
    #     csvfile2.write(str(bestdiss[ti]) + '\n')
    # csvfile.close()

    csvfile3 = open("hc2l_bestpathrun1.txt", "a")
    for tic in range(len(bestx)):
        csvfile3.write(str(bestx[tic]) + ',')
        csvfile3.write(str(besty[tic]) + '\n')
    csvfile.close()

    # plt.figure(0)
    # plt.plot(evals, dis)
    # plt.xlabel('evaluations')
    # plt.ylabel('distance')
    # plt.title('Travelling Salesman 1 RMHC shortest path run1')
    # plt.show()

    # plt.figure(1)
    # plt.plot(bestx, besty, '-xb')
    # plt.title('path')
    # plt.show()

    # csvfile1 = open("gradient1.txt", "a")
    # for t in range(len(gradient)):
    #     csvfile1.write(str(gradient[t]) + '\n')
    # csvfile1.close()

    # x1 = []
    # y1 = []
    # for h in range(len(shortestpath)):
    #     x1.append(shortestpath[h][0])
    #     y1.append(shortestpath[h][1])

    # plt.plot(x1, y1, 'xb-')
    # plt.xlabel('x-axis')
    # plt.ylabel('y-axis')
    # plt.title('Travelling Salesman 1 RMHC shortest path run1')
    # plt.show()

    # plt.plot(evals, gradient)
    # plt.xlabel('evaluations')
    # plt.ylabel('distance')
    # plt.title('HC run 1 gradient evals')
    # plt.show()

if __name__ == "__main__":
    runRMHC(x, y)