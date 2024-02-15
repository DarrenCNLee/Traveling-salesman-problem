import graph

VERTICES = 26


class Path:

    def __init__(self):
        self.vertices = []
        self.length = 0

    def path_push_vertex(self, v, G):

        if self.vertices:
            top = self.vertices[-1]
            self.vertices.append(v)
            if v != top:
                self.length += G.graph_edge_weight(top, v)

        else:
            self.vertices.append(v)
        return True

    def path_pop_vertex(self, v, G):
        if not self.vertices:
            return False

        if len(self.vertices) > 1:
            v = self.vertices.pop()
            top = self.vertices[-1]
            if v != top:
                self.length -= G.graph_edge_weight(top, v)
        else:
            self.vertices.pop()
        return True

    def path_vertices(self):
        return len(self.vertices)

    def path_length(self):
        return self.length

    def path_copy(self, dst, src):
        if dst:
            dst.vertices = src.vertices.copy()
            dst.length = src.length

    def path_print(self, outfile, cities):
        for i in range(len(self.vertices)):
            outfile.write(cities[self.vertices[i]])
            if i + 1 != len(self.vertices):
                outfile.write(" -> ")

        outfile.write("\n")

    def path_print_debug(self, cities):
        for i in range(len(self.vertices)):
            print(cities[self.vertices[i]], end="")
            if i + 1 != len(self.vertices):
                print(" -> ", end="")

        print("\n")
