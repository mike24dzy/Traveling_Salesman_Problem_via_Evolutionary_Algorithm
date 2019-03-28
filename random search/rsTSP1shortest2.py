# MECS 4510 HW1
# Travelling Salesman

# For random search TSP1 
# Shortest path run 2
 
import numpy as np
import math as mt
import matplotlib.pyplot as plt

x = []
y = []

with open('TSP1.txt', 'r') as points1: 
    reader = np.loadtxt(points1, delimiter = ',')
    for row in reader:
        x.append(row[0])
        y.append(row[1])

# print ('x values = ', x)
# print ('y values = ', y)

plt.scatter(x, y, label = 'locations', color = 'black')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Travelling Salesman 1')

# plt.show()

comb = []
for b in range(len(x)):
    comb.append([x[b], y[b]])

def distance(X):
    d = []
    for i in range(len(X)-1):
        d.append(mt.sqrt((X[i+1][0] - X[i][0])**2 + ((X[i+1][1] - X[i][1])**2)))
    d.append(mt.sqrt((X[-1][0] - X[0][0])**2 + ((X[-1][1] - X[0][1])**2)))          
    totald = np.sum(d)
    return totald    

def runRS(R):
    dis = []
    evals = []
    combd1 = distance(R)
    dis.append(combd1)
    evals.append(1)
    allbetterS = []
    allbetterSd = []
    for z in range(0, 999999):
        evals.append(z+2)
        np.random.shuffle(R)
        D = distance(R)
        dis.append(D)
        if D < combd1:
            currentcomb = R
            allbetterS.append(currentcomb)
            currentd = distance(currentcomb)
            allbetterSd.append(currentd)
        print (z)
    bestSd = min(allbetterSd)
    bestSdindex = allbetterSd.index(bestSd)
    bestS = allbetterS[bestSdindex]
    print (bestS)
    print (bestSd)
    print (len(evals))
    print (len(dis))

    csvfile = open("ed2.txt", "a")
    for tick in range(len(evals)):
        csvfile.write(str(evals[tick]) + ',')
        csvfile.write(str(dis[tick]) + '\n')
    csvfile.close()

        
    x1 = []
    y1 = []
    for h in range(len(bestS)):
        x1.append(bestS[h][0])
        y1.append(bestS[h][1])

    plt.plot(x1, y1, 'xb-')
    plt.show()


if __name__ == "__main__":
    runRS(comb)