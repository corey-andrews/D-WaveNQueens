import networkx
import dwave_networkx

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

# implementation includes
from NQueensEdgeGenerator import getEdges
from DrawBoard import drawNQueensSolution
DIMENSION = 4

# a general sampler for handling an unstructured QUBO problem
my_sampler = EmbeddingComposite(DWaveSampler())

# generate the graph
Graph = networkx.Graph()
Graph.add_edges_from(getEdges(DIMENSION))

# library call for creating and calculating QUBO problem
Solution = dwave_networkx.maximum_independent_set(Graph, sampler = my_sampler)

# Visualization of the found solution
drawNQueensSolution(DIMENSION, Solution)
