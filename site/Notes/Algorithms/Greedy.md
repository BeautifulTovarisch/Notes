# Greedy

The greedy algorithm design paradigm produces straightforward and fast solutions to certain problems. Usually, however, greedy algorithms do not produce correct results, and great care must be taken to prove their correctness.

In general, the strategy is to choose a locally optimal solution in the hopes that it produces a globally optimal (and correct) output. Proofs of correctness and optimality usually involve an exchange argument and/or induction.

## Dijkstra's Shortest Path Algorithm

The canonical greedy algorithm. Dijkstra's algorithm computes the shortest paths from a starting vertex by choose the least costly edge spanning a graph "cut" or partition incident to the visited nodes. In other words, the edge that minimizes the distance traveled from the starting vertex is the one chosen.

```tikz
\usetikzlibrary{positioning}
\begin{document}

\begin{tikzpicture}[
vertex/.style={circle, draw, fill=white, thick, minimum size=20},
]

% Vertices
\node[vertex] (S) {$S$};
\node[vertex] (V) [above right=of S] {$V$};
\node[vertex] (W) [below right=of S] {$W$};
\node[vertex] (T) [below right=of V] {$T$};

% Edges
\draw[->, thick] (S) to node[above] {1} (V);
\draw[->, thick] (S) to node[below] {4} (W);
\draw[->, thick] (V) to node[right] {2} (W);
\draw[->, thick] (V) to node[above] {6} (T);
\draw[->, thick] (W) to node[below] {3} (T);
\end{tikzpicture}
\end{document}
```

 The shortest path algorithm outputs the following when starting from $S$:

|Vertex     |Shortest Path |
| --------- | ------------ |
|S          |0             |
|V          |1             |
|W          |3             |
|T          |6             |

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

```tikz
\usetikzlibrary{positioning}
\begin{document}

\begin{tikzpicture}[
vertex/.style={circle, draw, fill=white, thick, minimum size=20},
]

% Vertices
\node[vertex] (a) {$a$};
\node[vertex] (b) [right=of a] {$b$};
\node[vertex] (c) [below=of a] {$c$};
\node[vertex] (d) [below=of b] {$d$};

% Edges
\draw[-, thick] (a) to node[above] {1} (b);
\draw[-, thick] (a) to node[above] {3} (d);
\draw[-, thick] (a) to node[left] {4} (c);
\draw[-, thick] (b) to node[right] {2} (d);
\draw[-, thick] (c) to node[below] {5} (d);
\end{tikzpicture}
\end{document}
```

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

Kruskal's algorithm adopts a different approach, instead opting to choose the minimum edge that would not introduce a cycle.

```tikz
\usetikzlibrary{positioning}
\begin{document}

\begin{tikzpicture}[
vertex/.style={circle, draw, fill=white, thick, minimum size=20},
]

% Vertices
\node[vertex] (a) {$a$};
\node[vertex] (b) [right=of a] {$b$};
\node[vertex] (c) [below=of a] {$c$};
\node[vertex] (d) [below=of b] {$d$};

% Edges
\draw[-, thick] (a) to node[above] {1} (b);
\draw[-, thick] (a) to node[above] {3} (d);
\draw[-, thick] (a) to node[left] {4} (c);
\draw[-, thick] (b) to node[right] {2} (d);
\draw[-, thick] (c) to node[below] {5} (d);
\end{tikzpicture}
\end{document}
```

Kruskal's algorithm would execute the following steps:

1. Choose $(a, b)$, since it is the minimum cost edge
2. Choose $(b, d)$, since no cycle is produced 
3. Choose $(d, e)$, since $(a, c)$ would produce a cycle
4. The chosen edges form a spanning tree of minimum cost!

```tikz
\usetikzlibrary{positioning}
\begin{document}

\begin{tikzpicture}[
vertex/.style={circle, draw, fill=white, thick, minimum size=20},
]

% Vertices
\node[vertex] (a) {$a$};
\node[vertex] (b) [right=of a] {$b$};
\node[vertex] (c) [below=of a] {$c$};
\node[vertex] (d) [below=of b] {$d$};

% Edges
\draw[-, thick] (a) to node[above] {1} (b);
\draw[-, thick] (a) to node[left] {4} (c);
\draw[-, thick] (b) to node[right] {2} (d);
\end{tikzpicture}
\end{document}
```

In a real program, we sort the edges of the input graph $G$ by weight as a pre-processing step to avoid quadratic searches for successive minimums.

```pseudo
	\begin{algorithm}
	\caption{Kruskal's Algorithm}
	\begin{algorithmic}
	\State $T = \empty$
	\State sort $E$ by edge weight \\\\
	\For{$(v, w) \in E$}
	\If{$(v, w)$ does not produce a cycle in $T$}
	\State add $(v, w)$ to $T$ \\\\
    \EndIf
    \EndFor
    \Return $T$
	\end{algorithmic}
	\end{algorithm}
```

### Analysis

Sorting the edges takes $O(n\log n)$ time. Cycle detection in the inner loop dominates the runtime of naive Kruskal's and therefore the overall runtime is subject to the implementation details. For a brute-force cycle detection approach, the inner loop runs $O(|E||E + V|) = O(|E||V|)$ time.

By using a [[Union-Find]] data structure, we can dramatically improve the runtime. In particular by implementing optimizations such as [[Union-Find#Path Compression]] and [[Union-Find#Union by Rank]].

> TODO: Do the detailed analysis later, (Inverse Ackermann)

## Huffman Codes

Invented by David Huffman in the 50s as a way to compute the optimal prefix-free variable length encoding for a (mathematical) language $\sum$. The algorithm works by constructing a tree from the "bottom up", repeatedly merging the least frequently occurring codes in order to ensure the most frequently occurring have minimum possible depth.

```pseudo
	\begin{algorithm}
	\caption{Huffman Encoding}
	\begin{algorithmic}
	\Comment{Preprocessing}
	\State $H = \empty$
	\For{symbol $\sigma \in \sum$}
	\State ${T_\sigma} = (\sigma, P_\sigma)$  
	\State $H = H \cup T_\sigma$
	\EndFor
	\While{There is more than one $T_\sigma \in H$}
	\State $T_1$ = tree with minimum frequency
	\State $T_2$ = tree with 2nd smallest frequency
	\State $T_3$ = \Call{MergeTrees}{$T_1, T_2$}
	\State $H = H \cup T_3$ \\\\
	\EndWhile
	\Return $H$
	\end{algorithmic}
	\end{algorithm}
```

For example, given the frequencies:


|Symbol     |Frequency     |
| --------- | ------------ |
|a          |0.60          |
|b          |0.25          |
|c          |0.10          |
|d          |0.05          |

Huffman's greedy algorithm will produce the following encoding tree

```tikz
\usetikzlibrary{positioning}
\begin{document}

\begin{tikzpicture}[
vertex/.style={circle, draw, fill=white, thick, minimum size=20},
]

% Vertices
\node[vertex] (r1) {};
\node[vertex] (a) [below left=of r1] {$a$};
\node[vertex] (r2) [below right=of r1] {};

\node[vertex] (b) [below left=of r2] {$b$};
\node[vertex] (r3) [below right=of r2] {};

\node[vertex] (c) [below left=of r3] {$c$};
\node[vertex] (d) [below right=of r3] {$d$};

% Edges
\draw[-, thick] (r1) to node[above left] {0} (a);
\draw[-, thick] (r1) to node[above right] {1} (r2);

\draw[-, thick] (r2) to node[above left] {0} (b);
\draw[-, thick] (r2) to node[above right] {1} (r3);

\draw[-, thick] (r3) to node[above left] {0} (c);
\draw[-, thick] (r3) to node[above right] {1} (d);
\end{tikzpicture}
\end{document}
```

which ensures that symbol $a$, the most frequently encountered will be the quickest to encode and decode since its depth in minimized in the output.

### Analysis

Preprocessing the nodes can be done quickly in $O(n)$ time. The inner loop of the algorithm is bound by the time it takes to select a minimum, therefore, repeated brute-force searching for minima each iteration leads to $O(n^2)$ runtime.

Once again, however, a [[Heap]] can be used to retrieve the minimum trees in constant time with $O(\log n)$ re-balance operations. This results in a much better runtime of $O(n \log n)$.