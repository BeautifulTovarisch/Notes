# Graphs

Graphs are suitable for modeling an enormous variety of problems. Graph algorithms generally rely on the basic techniques of breadth-first and depth-first traversal as well as some basic data structures.

> Assume graphs are represented as adjacency lists.

## Depth-First Search

Depth-first search (DFS) explores paths of maximum depth before backtracking to a starting vertex. DFS is typically implemented via a straightforward recursive algorithm.

```pseudo
	\begin{algorithm}
	\caption{Depth-First Search}
	\begin{algorithmic}
	\Input{$G = (V, E)$, starting vertex $v$}
	\State visited = $\empty$
	\Procedure{DFS}{$v$}
	\State add $v$ to visited
	\For{$u \in V$ such that $(v, u) \in E$}
	\If{$u \not \in$ visited}
	\State DFS($u$)
    \EndIf
    \EndFor
    \EndProcedure
	\end{algorithmic}
	\end{algorithm}
```

## Analysis

Depth-first search explores each reachable node from starting vertex $v$ and traverses edge incident on $v$. Additionally, the check for whether a node has been visited before (using a hash) runs in expected $O(1)$ time.

Due to visiting every node, the runtime of DFS is $O(|V| + |E|)$.

## Breadth-First Search

Breadth-first search (BFS) proceeds to process the "levels" of a graph, proceeding only when every neighbor of the current node has been explored. Typical implementations enqueue the neighbors of a vertex in order to enforce a BFS discipline. 

```pseudo
	\begin{algorithm}
	\caption{Breadth-First Search}
	\begin{algorithmic}
	\Input{$G = (V, E)$, starting vertex $v$}
	\State $Q = \{v\}$
	\State visited = $\empty$
	\While{$Q$ is not empty}
	\State $u =$ dequeue($Q$)
	\For{$w \in V$ such that $(u, w) \in E$}
	\If{$w \not \in$ visited}
	\State add $w$ to visited
	\State enqueue($Q, w$)
    \EndIf
    \EndFor
    \EndWhile
	\end{algorithmic}
	\end{algorithm}
```

### Analysis

Similar to DFS, the runtime of BFS is $O(|V| + |E|)$ assuming an implementation of a queue which allows constant time add and remove operations.

## Topological Ordering

A Topological ordering in a directed graph is the order in which DFS explores vertices (formally called reverse post-order).  The topological sort algorithm computes a valid topological ordering of a directed graph $G$, if one exists.

Such orderings are typically used to determine whether a precedence graph is logically consistent, and if so, compute a correct sequence of operations.

```pseudo
	\begin{algorithm}
	\caption{TopoSort}
	\begin{algorithmic}
	\Input{$G = (V, E)$}
	\Require{$G$ is a directed acyclic graph}
	\State visited = $\empty$
	\State processing = $\empty$
	\State ordering = Stack \\\\
	\Procedure{DFS}{$v$}
	\State mark $v$ as visited
	\State processing(v) = \True
	\For{$u$ such that $(v, u) \in E$}
	\If{$u \not \in visited$}
	\State DFS($u$)
	\Elif{$u$ is a node currently being processed}
	\Return	"no topological ordering"
	\EndIf
    \EndFor
    \State processing(v) = \False
    \State ordering.push(v)
    \EndProcedure
    \State \\
    \For{$v \in V$}
    \If {$v \not \in visited$}
    \State DFS($v$)
    \EndIf
    \EndFor
    \State \\
    \Return ordering
    \end{algorithmic}
	\end{algorithm}
```

### Analysis

`TopoSort` owes its $O(|V| + |E|)$ runtime to the depth-first traversal in its implementation, assuming $O(1)$ insert operations onto the stack.

### Proof

> TODO

## Strongly Connected Components

We define "strongly-connected" as a relation between two vertices $u, v \in V$ such that $(u, v) \in R$ if there exists a path from $u$ to $v$ and a path from $v$ to $u$. Strongly connected components represent an [[Relations#Equivalence Relations|Equivalence Class]] of the vertices of that component.

Kosaraju's algorithm computes the strongly connected components of $G = (V, E)$ via two passes. The first past computes a "topological ordering" of the reverse of $G$, $G_{\text{rev}}$, which provides the ordering necessary to provide to an additional pass of DFS.

> Note that there cannot be a valid topological ordering in the strictest sense due to the fact that there must be a cycle in a directed graph in order for two vertices to be strongly connected.

```pseudo
	\begin{algorithm}
	\caption{Kosaraju-Sharir}
	\begin{algorithmic}
	\Input{$G = (V, E)$}
	\State scc = $\empty$
	\State count = 0
	\State visited = $\empty$
	\State ordering = \Call{TopoSort}{$G_{\text{rev}}$}
    \State \\
	\Function{DFS-SCC}{$G, v$}
	\State mark $v$ as visited
	\State scc($v$) = count
	\For{$u \in V$ such that $(v, u) \in E$}
	\If{$u \not \in$ visited}
	\State DFS-SCC($G, u$)
    \EndIf
    \EndFor
    \EndFunction
    \For{$v$ in ordering}
    \State DFS-SCC($G, v$)
    \State count = count + 1
    \EndFor
    \State \\
    \Return scc
	\end{algorithmic}
	\end{algorithm}
```

### Analysis


### Proof

> TODO