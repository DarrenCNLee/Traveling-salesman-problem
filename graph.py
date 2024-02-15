VERTICES = 26
startVertex = 0


class Graph:

    def __init__(self, vertices, undirected):
        self.vertices = vertices
        self.undirected = undirected
        self.visited = [False for _ in range(VERTICES)]
        self.matrix = [[0 for _ in range(VERTICES)] for _ in range(VERTICES)]

    def graph_create(self, vertices, undirected):
        G = Graph()
        G.undirected = undirected
        G.vertices = vertices

        for i in range(vertices):
            G.visited[i] = False
            for j in range(vertices):
                G.matrix[i][j] = 0

        return G

    def graph_vertices(self):
        return self.vertices

    def graph_add_edge(self, i, j, k):
        if i >= self.vertices or j >= self.vertices:
            return False
        self.matrix[i][j] = k
        if self.undirected:
            self.matrix[j][i] = k

        return True

    def graph_has_edge(self, i, j):
        if i < self.vertices and j < self.vertices: 
            return self.matrix[i][j]
        
        return False 
    
    def graph_edge_weight(self, i, j): 
        if i >= self.vertices or j >= self.vertices: 
            return 0 
        return self.matrix[i][j] 
    
    def graph_visited(self, v): 
        return self.visited[v] 
    
    def graph_mark_visited(self, v): 
        if v < self.vertices: 
            self.visited[v] = True 
            
    def graph_mark_unvisited(self, v): 
        if v < self.vertices: 
            self.visited[v] = False 
            
    def graph_print(self): 
        for i in range(self.vertices): 
            for j in range(self.vertices): 
                if self.matrix[i][j]:
                    print(i, j, self.matrix[i][j])