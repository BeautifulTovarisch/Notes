# Spanning Tree

A spanning tree is an important bread-and-butter data structure in a variety of disciplines including computer networking, city planning, social media, etc.

> [!info] Spanning Tree
> Suppose $G$ is a graph. A **spanning tree**, $T$ is a subgraph of $G$ that contains no loops or cycles (hence a **tree**) and that contains all the nodes of $G$.  We say that $T$ "spans" the nodes of $G$.

> [!tip]
> This is a similar usage of [[Span]] as found in Linear Algebra

## Minimum Spanning Tree

Often times we need to find an "optimal" route through a particular graph, such as when performing path-finding or navigation. Over the years, several algorithms have been invented or discovered (often independently) to compute the minimum spanning tree.

> [!info] Minimum Spanning Tree
> Suppose $G$ is a graph. A **minimum spanning tree** of $G$ is a spanning tree of $G$ containing minimally weighted edges.

The algorithms that follow illustrate the historical challenge of limiting computing resources; The original algorithm by Otakar Borůvka was created before the existence of computing machines altogether.

### Robert Prim's Algorithm

- Assume an efficient way to detect cycles
- At each node, perform a linear search of its neighboring edges and choose the edge with minimal weight.
	- A more advanced version may elect to use a priority queue to reduce the cost of the linear search

This algorithm is simple to understand and implement (assuming cycle-detection), but requires an $O(n)$ search per node of the minimal path to take.

### Joseph Kruskal's Algorithm

- First order the edges by ascending weight
- Process the edges in order, adding an edge to the solution if it does not create a cycle

The time to sort the edges is bound by $O(n \lg n)$ and the processing of the list is linear modulo the time to check for cycles. This implementation is simpler than Prim's in that a sorted list requires no maintenance whereas a priority queue must be re-balanced.

### Borůvka's Algorithm

- Each node starts as a "solution"
- The lightest edges that would connect two "components" (clusters of nodes) are chosen
- Components are then merged into a final output, the desired MST

 Both Prim's and Kruskal's algorithms required a centralized data structure to be maintained, meaning they were difficult to parallelize (due to a need to synchronize access). The historical limitations of the time prevented the parallel algorithm from being implemented until modern advances in computing were able to support it.

  > [!todo]
  > Add notebook or simple diagram illustrating this/these algorithm(s).
