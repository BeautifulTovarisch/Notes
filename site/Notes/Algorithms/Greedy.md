# Greedy

The greedy algorithm design paradigm produces straightforward and fast solutions to certain problems. Usually, however, greedy algorithms do not produce correct results, and great care must be taken to prove their correctness.

In general, the strategy is to choose a locally optimal solution in the hopes that it produces a globally optimal (and correct) output. Proofs of correctness and optimality usually involve an exchange argument and/or induction.

```tikz
\begin{document}

\begin{tikzpicture}
  [scale=.8,auto=left,every node/.style={circle,fill=white!20}]
  \node (n6) at (1,10) {6};
  \node (n4) at (4,8)  {4};
  \node (n5) at (8,9)  {5};
  \node (n1) at (11,8) {1};
  \node (n2) at (9,6)  {2};
  \node (n3) at (5,5)  {3};

  \foreach \from/\to in {n6/n4,n4/n5,n5/n1,n1/n2,n2/n5,n2/n3,n3/n4}
    \draw (\from) -- (\to);

\end{tikzpicture}

\end{document}
```

## Dijkstra's Shortest Path Algorithm

The canonical greedy algorithm. Dijkstra's algorithm computes the shortest paths from a starting vertex by choose the least costly edge spanning a graph "cut" or partition incident to the visited nodes. In other words, the edge that minimizes the distance traveled from the starting vertex is the one chosen.

> TODO: Learn Tikz

```pseudo
	\begin{algorithm}
	\caption{Dijkstra's Shortest-Path}
	\begin{algorithmic}
	\Require $G = (V, E)$ has nonnegative edge weights
	\State $X = \{s\}$
	\State len(s) = 0, len(v) = $+\infty$ for every $v \neq s$ \\\\
	\While{There exists an edge $(v, w) \; v \in X, w \not \in X$ }
	\State $(v', w')$ = edge minimizing $len(v) + l_{vw}$
	\State Add $w'$ to $X$
	\State len(w') = len(v') + $l_{v'w'}$ \\\\
	\Return len
    \EndWhile
	\end{algorithmic}
	\end{algorithm}
```

### Analysis

The cost of repeatedly selecting the minimum edge via brute force dominates the runtime of the algorithm. For $G = (V, E)$, we traverse $|V|$ nodes, each time performing $O(|E|)$ work to select the minimum edge crossing the cut. Therefore, the naive version of Dijkstra's runs in $O(|E||V|)$.

Using a [[Heap]] this algorithm can be sped up significantly, achieving $O((|E| + |V|)\log|V|)$ runtime.

## Prim's MST Algorithm

Prim's algorithm for computing a minimum-spanning tree. The algorithm functions almost identically to Dijkstra's algorithm in that the minimum incident edge is always chosen for the solution.

```pseudo
	\begin{algorithm}
	\caption{Prim's MST Algorithm}
	\begin{algorithmic}
	\State $X = \{s\}$
	\State $T = \empty$
	\While{There is an edge $(v, w)$ s.t $v \in X$, $w \not \in X$}
	\State $(v', w')$ = minimum cost edge \\\\
	\State Add $w'$ to $X$
	\State Add $(v', w')$ to $T$
	\EndWhile
	\Return $T$
	\end{algorithmic}
	\end{algorithm}
```

### Analysis

Once again the cost of repeatedly selecting the minimum edge dominates the runtime of the algorithm leading to $O(|V||E|)$ worst-case runtime.

We can employ the same technique of using a [[Heap]] as in Dijkstra's algorithm to achieve a runtime of $O(|E|\log|V|)$.

## Kruskal's MST Algorithm

## Huffman Codes
