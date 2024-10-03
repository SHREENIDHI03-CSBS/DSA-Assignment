class Graph:
    # Initialize the graph as undirected 
    def __init__(self):
        # Initialize an empty dictionary to store the graph
        self.graph = {}

    def addVertex(self, vertex):
        # If the vertex is not already in the graph, add it
        if vertex not in self.graph:
            self.graph[vertex] = []

    def addEdge(self, source, destination):
        # Add source and destination vertices if not present
        self.addVertex(source)
        self.addVertex(destination)
        # Add the edge from source to destination (undirected)
        self.graph[source].append(destination)
        # Add reverse direction from destination to source
        self.graph[destination].append(source)  

    def displayGraph(self):
        # Display the graph 
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

    # DFS traversal :
    def dfs(self, node, visited=None):
        if visited is None:
            visited = []

        # Mark the current node as visited
        visited.append(node)
        print(node, end=" ")  # Print the node being visited

        # Visit all the neighbors of the current node
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

if __name__ == "__main__":
    # Create a new graph object
    g = Graph()

    # Add edges between nodes
    g.addEdge(0, 1)
    g.addEdge(0, 6)
    g.addEdge(1, 2)
    g.addEdge(2, 4)
    g.addEdge(2, 3)
    g.addEdge(3, 5)
    g.addEdge(4, 5)
    g.addEdge(5, 6)

    # Perform DFS starting from node 0
    
    print("DFS traversal starting from node 0:")
    g.dfs(0)
    
    print("\nDFS traversal starting from node 1:")
    g.dfs(1)

    print("\nDFS traversal starting from node 2:")
    g.dfs(2)

    print("\nDFS traversal starting from node 3:")
    g.dfs(3)
    
    print("\nDFS traversal starting from node 4:")
    g.dfs(4)

    print("\nDFS traversal starting from node 5:")
    g.dfs(5)

    print("\nDFS traversal starting from node 6:")
    g.dfs(6)
