import networkx as nx
import matplotlib.pyplot as plt
from node import Node, dijkstra, search_shortest_path

# Create the graph
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")

A.add_child(B, 7)
A.add_child(C, 9)
A.add_child(D,14)

B.add_child(C, 10)
B.add_child(F, 15)
B.add_child(A, 7)
C.add_child(B, 1)
C.add_child(D, 2)
C.add_child(F, 11)

D.add_child(E, 3)

E.add_child(F, 6)
F.add_child(G, 9)
graph = [A, B, C, D,E,F]

# Apply Dijkstra's algorithm
dijkstra(B, graph)


# Print the shortest distances from source node A to other nodes
for node in graph:
    print(f"Shortest distance from B to {node.get_id()}: {node.get_distance()}")


path = search_shortest_path(E)
print(f"Shortest path from B to E: {' -> '.join(path)}")

# Draw the graph
G = nx.DiGraph()

# Add nodes
for node in graph:
    G.add_node(node.get_id())

# Add edges
for node in graph:
    for child, weight in node.get_children().items():
        G.add_edge(node.get_id(), child.get_id(), weight=weight)

# Draw the graph with labels
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})

# Show the graph
plt.show()