This program implements a depth-first search function that solves
the Traveling Salesman Problem and finds the shortest 
Hamiltonian Path for a graph  if it exists. The program accepts a maximum 
of 26 vertices for a graph.

## Running
	$ python ./tsp [input-file] [-u] [-o output-file]
	
	-u Specifies that the graph is undirected
	-o output-file Specifies the file for output, default is stdout

## Files
	graph.py - Contains the program code for the graph ADT and its functions

	path.py - Contains the program code for the path ADT and its functions

	tsp.py - Contains program code for the DFS and main functions and the solution
	to the Traveling Salesman Problem
