import networkx as nx
import numpy as np
from random import seed
from random import randint
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import time

pr = 1
edgepr = 0.5 # probability of edge creation
uvert = 10 # Number of vertices in U partition
vvert = 10 # Number of vertices in V partition
steps = 20 # Number of steps
walks = 1000
uvertcount = [0] * (uvert+vvert) 
vertcount = 0
xax = np.arange(1,uvert+vvert + 1)

# Loads my saved graph data
adjmat = np.load('adjacency_matrix.npy')
bottom_nodes = np.load('bottom_nodes.npy')
bottom_nodes = bottom_nodes.tolist()
top_nodes = np.load('top_nodes.npy')
top_nodes = top_nodes.tolist()


def randwalk(): # Part b
    global vertcount
    startval = randint(1,4) # Generates a random number between 1 and 4 inclusive
    #print(startval)

    if startval == pr: # If true, the first vertex will be in the U partition
        randind = randint(0,botlen-1)
        startver = bottom_nodes[randind]

    else: # Otherwise, the first vertex will be in the V partition
        randind = randint(0,toplen-1)
        startver = top_nodes[randind]
            
    for step in range(0,steps):
        indvec = np.where(adjmat[startver,:] == 1)[0] # Vector of vector containing indices that have 1 values
        neilen = len(indvec) # degree of start vertex
        randnei = indvec[randint(0,neilen-1)] # the random neighbor index choosen
        startver = randnei # The new start vertex is the random neighbor index
        vertcount = vertcount + 1
        
        myind = 0
        match = bool(False)
        while (not match):
            if startver == bottom_nodes[myind]:
                match = bool(True)
                uvertcount[step] = uvertcount[step] + 1
                
            if myind == (botlen - 1):
                match = bool(True)
                
            myind = myind + 1
            
for walk in range(0,walks):
    randwalk() # Part b
                
uvertcount = np.asarray(uvertcount)
uvertcount = uvertcount[:] / (walks)

# Code used to generate the figure:

plt.bar(xax,uvertcount,align='center')
plt.xticks(np.arange(1,steps+1))
plt.xlabel('Step')
plt.ylabel('Fraction of trials that the vertex was in U')
#plt.title('Fraction of trials that the vertex was in U per Step')
plt.savefig('partb.png')
