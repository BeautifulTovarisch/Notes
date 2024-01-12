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

Which leads naturally to a [recursive algorithm](fibonacci.ipynb).

## Tower of Hanoi

Another famous puzzle is the Tower of Hanoi, invented by a [frenchman](https://en.wikipedia.org/wiki/Tower_of_Hanoi).

> This section in Concrete Mathematics is a wild ride

We can consider the problem of moving $k$ disks from the first peg to the 3rd as the solution to the following subproblems:

1. Move the top $k-1$ disks to the middle disk.
2. Move the $kth$ disk to the right disk.
3. Move the to $k-1$ disks from the middle to the right.

Then we can formulate the number of moves required to solve the puzzle by:

$$
m(k) =
\begin{cases}
1 & \text{if k = 1} \\
2f(k-1) + 1 & \text{otherwise}
\end{cases}
$$

Computed by the algorithm:

```python
def hanoi(n):
	'''
	hanoi(n) computes the number of moves required to solve the tower of hanoi given [n] disks.

	Paramters:
		n (int) - The number of disks to be moved

	Output:
		The number of moves required to move [n] disks to the third peg.
	'''
	if n == 1:
		return 1

	return 2 * hanoi(n-1) + 1
```

We can prove a closed form of the above recurrence relation so that the results are computationally more efficient to achieve:

> [!abstract] Closed form of Hanoi Recurrence Relation
> $$
> m_k = 2m_{k-1} + 1 = 2^k - 1
> $$
>
> Proof.
> By induction on $k$. Suppose $k = 1$. Then by the initial conditions on $m$, $m_0 = 1 = 2^1 - 1$. Hence $\exists K \geq 1$ such that $m_k = 2^k - 1$.
>
> Now suppose $K = k + 1$, then we have:
> $$
> \begin{align}
> m_{k+1} &= 2m_k + 1 \\
> &= 2(2m_{k-1} + 1) &\text{Def of m} \\
> &= 2(2^k - 1) + 1 &\text{I.H} \\
> &= 2^{k+1} - 1 &\text{Algebra}
> \end{align}
> $$
>
> $\blacksquare$