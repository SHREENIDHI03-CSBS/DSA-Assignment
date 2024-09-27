class Graph:
    # Initialize graph with an option to set it as directed or undirected
    def __init__(self, directed=False):
        # Initialize an empty dictionary to store the graph
        self.graph = {}
        # Set the graph as directed or undirected based on the parameter
        self.directed = directed

    def addVertex(self, vertex):
        # If the vertex is not already in the graph, add it
        if vertex not in self.graph:
            self.graph[vertex] = []

    def addEdge(self, source, destination):
        # Add source and destination vertices if not present
        self.addVertex(source)
        self.addVertex(destination)
        # Add the edge from source to destination
        self.graph[source].append(destination)
        # If the graph is undirected, add the reverse edge (destination to source)
        if not self.directed:
            self.graph[destination].append(source)

    def displayGraph(self):
        # Display the graph in adjacency list format
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

# Creating an undirected graph (default)
G1 = Graph()
G1.addEdge('A', 'B')
G1.addEdge('A', 'D')
G1.addEdge('A', 'C')
G1.addEdge('A', 'E')
G1.addEdge('B', 'C')
G1.addEdge('C', 'E')
G1.addEdge('C', 'D')
G1.addEdge('D', 'E')

print("Undirected Graph:")
G1.displayGraph()

# Creating a directed graph
G2 = Graph(directed=True)
G2.addEdge('A', 'B')
G2.addEdge('A', 'C')
G2.addEdge('B', 'D')
G2.addEdge('C', 'D')

print("\nDirected Graph:")
G2.displayGraph()
