import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

# Input data
sequence = "ATGGAAGTCGCGGAATC"
k = 3

# Graph to be generated
graph = nx.DiGraph()

# Weights represents the number of connections between two edges
weights = defaultdict(int)

# Generates k-mers and adds them as edges to the graph
for i in range(len(sequence) - k):
    kmer_a = sequence[i:i + k]
    kmer_b = sequence[i + 1:i + k + 1]
    weights[kmer_a+kmer_b] += 1
    graph.add_weighted_edges_from([(kmer_a, kmer_b, weights[kmer_a+kmer_b])])

# Draws the graph on an output file in the same directory
# The numbers on the edges represents the number of edges between the two nodes
pos = nx.circular_layout(graph)
nx.draw(graph, pos, with_labels=True, font_weight='bold')
edge_labels = dict([((u, v), d['weight']) for u, v, d in graph.edges(data=True)])
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, label_pos=0.3, font_size=7)
plt.savefig("output.png")
