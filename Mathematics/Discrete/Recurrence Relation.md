Recurrence relations are sequences defined in terms of previous elements. In other words, for some sequence (function with domain of $\mathbb{N}$), a recurrence relation is way to compute the "current" element by looking at the results of previous computations.

> [!info] Recurrence Relation
> A **recurrence relation** is a formula that, for some $N$, relates each term $k$ to a certain number of its predecessors (i.e) $a_{k-1}, a_{k-2}, \dots, a_{k-i}$ where $i \in \mathbb{N}$ and $k - i \geq 0$.
> 
> A recurrence relation also defines **initial conditions**, $a_0, \dots, a_m$, $m \in \mathbb{N}$.

## Fibonacci

The Fibonacci sequence comes from a bizarre puzzle created by [an Italian](https://en.wikipedia.org/wiki/Fibonacci). The puzzle was to compute the pairs of rabbits on a fictional island after $n$ months, given a 1 month gestation period and other criteria.

Starting with 1 male and female newborn rabbits and $n = 0$:

| $n$ | Pairs |
| --- | ----- | 
| 0   | 1     | 
| 1   | 1     | 
| 2   | 2     | 
| 3   | 3     | 
| 4   | 5     | 

and so on. We can see that the current $n$ is computed by adding the values for $n - 1$ and $n - 2$. We use this finding to construct a recurrence relation:

$$
f(n) = 
\begin{cases}
1 & \text{if $n \leq 1$} \\
f(n-1) + f(n-2) & \text{otherwise}
\end{cases}
$$

Which leads naturally to a [recursive algorithm](./fibonacci.ipynb).