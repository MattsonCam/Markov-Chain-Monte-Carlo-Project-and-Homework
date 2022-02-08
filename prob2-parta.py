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
connected = bool(False)


# Creates a connected bipartite graph Part a:
while (not connected):
    B = bipartite.random_graph(uvert,vvert, edgepr, seed = 101)
    connected = nx.is_connected(B)

bottom_nodes, top_nodes = bipartite.sets(B) # Should create two set partitions

# Computes the lengths of the vertex partitions:
botlen = len(bottom_nodes) # U length
toplen = len(top_nodes) # V length
# Creates lists of the vertex partitions:
bottom_nodes = list(bottom_nodes) # Convertes the nodes to a list
top_nodes = list(top_nodes)

nx.draw_networkx(B, pos = nx.drawing.layout.bipartite_layout(B, bottom_nodes))
plt.title('Connected Bipartite Graph')
plt.savefig('parta.png')
adjmat = nx.adjacency_matrix(B, weight=None).toarray() # The adjacency matrix should have 1s where there are neighbors and zero otherwise.
# Saves my data for use in the other parts of problem 2
np.save('adjacency_matrix.npy',adjmat)
np.save('bottom_nodes.npy',bottom_nodes)
np.save('top_nodes.npy',top_nodes)
