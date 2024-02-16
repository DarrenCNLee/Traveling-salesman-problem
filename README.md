This program implements a depth-first search function that solves
the Traveling Salesman Problem and finds the shortest 
Hamiltonian Path for a graph  if it exists. The program accepts a maximum 
of 26 vertices for a graph.

## Running
	$ ./tsp [infile] [-u] [-o outfile]
	
	-u Specifies that the graph is undirected
	-o outfile Specifies the file for output, default is stdout
## Cleaning
	$ make clean
## Files
	graph.py - Contains the program code for the graph ADT and its functions

	path.py - Contains the program code for the path ADT and its functions

	tsp.py - Contains program code for the dfs and main functions and the solution
	to the Traveling Salesman Problem
