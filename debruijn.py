import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

# Input data
sequence = "ATGGAAGTCGCGGAATC"
k = 3

# Graph to be generated
graph = nx.DiGraph()

# Generates k-mers and adds them as edges to the graph
for i in range(len(sequence)-k):
    kmer_a = sequence[i:i+k]
    kmer_b = sequence[i+1:i+k+1]
    graph.add_edge(kmer_a, kmer_b)

# Draws the graph on an output file in the same directory
nx.draw(graph, with_labels=True, font_weight='bold')
plt.savefig("output.png")
