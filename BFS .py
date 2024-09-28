class Graph:
    # Initialize the graph as undirected (no need for directed parameter)
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
        # Display the graph in adjacency list format
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

    # BFS traversal method
    def bfs(self, start_node):
        # Keep track of visited nodes
        visited = []
        # Queue for BFS (we'll visit nodes level by level)
        queue = []

        # Start by visiting the start_node
        visited.append(start_node)
        queue.append(start_node)

        # Loop until there are nodes to visit
        while queue:
            # Remove the first node from the queue and process it
            current_node = queue.pop(0)
            print(current_node, end=" ")    # Print the node being visited

            # Loop through all the neighbors
            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    # Mark the neighbor as visited
                    visited.append(neighbor) 
                    # Add the neighbor to the queue
                    queue.append(neighbor)   

if __name__ == "__main__":
    # a new graph object is created
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
    
    # Perform BFS starting from different nodes
    print("BFS traversal starting from node 0:")
    g.bfs(0)
    print("\nBFS traversal starting from node 1:")
    g.bfs(1)
    print("\nBFS traversal starting from node 2:")
    g.bfs(2)
    print("\nBFS traversal starting from node 3:")
    g.bfs(3)
    print("\nBFS traversal starting from node 4:")
    g.bfs(4)
    print("\nBFS traversal starting from node 5:")
    g.bfs(5)
    print("\nBFS traversal starting from node 6:")
    g.bfs(6)

