class Graph:
    def __init__(self):
        self.graph = {}

    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def addEdge(self, source, destination):
         
        self.addVertex(source)
        self.addVertex(destination)
        self.graph[source].append(destination)

    def displayGraph(self):
         
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")

    def dfs(self, node, visited, stack):
        
        visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, stack)

        stack.append(node)

    def topologicalSort(self):
        
        visited = set()
        stack = []

       
        for vertex in self.graph:
            if vertex not in visited:
                self.dfs(vertex, visited, stack)
        stack.reverse()
        return stack


if __name__ == "__main__":
    g = Graph()

    
    g.addEdge(0, 1)
    g.addEdge(0, 6)
    g.addEdge(1, 2)
    g.addEdge(2, 4)
    g.addEdge(2, 3)
    g.addEdge(3, 5)
    g.addEdge(4, 5)
    g.addEdge(5, 6)

    
    print("Topological Sort of the graph:")
    topological_order = g.topologicalSort()
    print(topological_order)
