# Graph

Graphs are defined formally as a set of vertices and edges, $G = (V, E)$, where $e \in E$ is represented as a tuple containing two connected vertices. 

```tikz
\usetikzlibrary{positioning}
\begin{document}

\begin{tikzpicture}[
vertex/.style={circle, draw, fill=white, thick, minimum size=20},
]

\node[vertex] (a1) at (1,2) {1};  
\node[vertex] (a2) at (2,5)  {2}; 
\node[vertex] (a3) at (3,7)  {3};  
\node[vertex] (a4) at (3,2.5) {4};  
\node[vertex] (a5) at (5,6)  {5};  
\node[vertex] (a6) at (5,3)  {6};  
\node[vertex] (a7) at (7,5)  {7};  
  
\draw (a1) -- (a2);
\draw (a2) -- (a3);  
\draw (a2) -- (a4);  
\draw (a4) -- (a6);  
\draw (a3) -- (a5);  
\draw (a6) -- (a7);  
\draw (a5) -- (a7);

\end{tikzpicture}
\end{document}
```

For example, the graph above is defined as follows:

$$
\begin{align}
V &= \{ 1, 2, 3, 4, 5, 6, 7 \} \\ \\
E &= \{ (1, 2), (2, 3), (2, 4), (4, 6), (3, 5), (6, 7), (5, 7) \}
\end{align}
$$

## Glossary

Graphs are described with considerable and (often conflicting) terminology. This glossary summarizes some common definitions.