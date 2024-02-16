import graph
import path
import sys
import getopt

debug = False
calls = 0


def dfs(G, v, curr, shortest, cities, outfile):
    global calls
    calls += 1
    curr.path_push_vertex(v, G)
    G.graph_mark_visited(v)

    for w in range(G.graph_vertices()):
        if (curr.path_length() >= shortest.path_length()
                and shortest.path_length() != 0):
            continue

        if G.graph_has_edge(v, w) and not G.graph_visited(w):
            dfs(G, w, curr, shortest, cities, outfile)

        if (curr.path_vertices() == G.graph_vertices()
                and G.graph_has_edge(v, 0)):
            curr.path_push_vertex(0, G)

            if (shortest.path_length() == 0
                    or curr.path_length() < shortest.path_length()):

                shortest.path_copy(shortest, curr)

            curr.path_pop_vertex(None, G)

    curr.path_pop_vertex(v, G)
    G.graph_mark_unvisited(v)


def main():
    infile = open(sys.argv[1], "r")
    outfile = sys.stdout
   

    undirected = False

    argumentList = sys.argv[2:]
    (arguments, _) = getopt.getopt(argumentList, "uo:")

    if debug:
        print(arguments)

    for curArg, curVal in arguments:
        if curArg in "-u":
            undirected = True
        elif curArg in "-o":
            outfile = open(curVal, "w")

    n = int(infile.readline())

    if n > 26:
        return

    if n <= 1:
        outfile.write("There's nowhere to go.\n")
        return

    cities = []
    for i in range(n):
        line = infile.readline().rstrip()
        if not line:
            break
        cities.append(line)

    G = graph.Graph(n, undirected)

    while True:
        line = infile.readline().rstrip()

        if not line:
            break
        
        line = line.split(" ")

        if len(line) < 3:
            sys.stderr.write("Error: malformed edge.\n")
            return
        
        i = int(line[0])
        j = int(line[1])
        k = int(line[2])

        G.graph_add_edge(i, j, k)

    curr = path.Path()
    shortest = path.Path()

    dfs(G, 0, curr, shortest, cities, outfile)
    outfile.write("Path length: " + str(shortest.path_length()) + "\n")
    outfile.write("Path: ")
    shortest.path_print(outfile, cities)
    outfile.write("Total recursive calls: " + str(calls) + "\n")

    infile.close() 
    outfile.close()


if __name__ == "__main__":
    main() 
