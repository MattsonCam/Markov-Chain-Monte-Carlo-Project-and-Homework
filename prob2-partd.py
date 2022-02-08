# Change the steps variable value for each subpart of Part d for steps = 20, 10, and 100
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
steps = 20 # Number of steps. This needs to be changed for each subpart so that steps = 10 and 100 also.
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

def limlazywalk(steplen): # Part d
    steps = steplen
    global vertcount
    startval = randint(1,4) # Generates a random number between 1 and 4 inclusive

    if startval <= pr: # If true, the first vertex will be in the U partition
        randind = randint(0,botlen-1)
        startver = bottom_nodes[randind]

    else: # Otherwise, the first vertex will be in the V partition
        randind = randint(0,toplen-1)
        startver = top_nodes[randind]
            
    for step in range(0,steps):
        prswitchval = randint(1,4)
        if prswitchval != pr:
            indvec = np.where(adjmat[startver,:] == 1)[0] # Vector of vector containing indices that have 1 values
            neilen = len(indvec) # degree of start vertex
            randnei = indvec[randint(0,neilen-1)] # the random neighbor index choosen
            startver = randnei # The new start vertex is the random neighbor index
        vertcount = vertcount + 1
        
        if step == (steps-1):
            uvertcount[startver] = uvertcount[startver] + 1
            
# Change the steps variable value for each subpart of Part d for steps = 20, 10, and 100
for walk in range(0,walks):
    limlazywalk(steps) # Part d
                
uvertcount = np.asarray(uvertcount)
uvertcount = uvertcount[:] / (walks)

# Code used to generate the figures:
fig1, ax1 = plt.subplots()
plt.bar(xax,uvertcount,align='center')
plt.xticks(np.arange(1,(uvert+vvert)+1))
plt.xlabel('Vertex')
plt.ylabel('Fraction of trials for the ' + str(steps) + 'th step')
#plt.title('Fraction of trials that the final step was a particular vertex for the ' + str(steps) + 'th step')
plt.savefig('partd3.png')
