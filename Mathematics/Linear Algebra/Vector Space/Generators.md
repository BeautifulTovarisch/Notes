If a set of vectors can be used to construct (or **generate**) the [[Span]] of a set, then we call that set a **generating set** and its elements **generators**. More formally:

> [!info] Generating Set
> Let $\mathcal{V}$ be a set of vectors. If $v_1, \dots, v_n$ are vectors such that $\mathcal{V} = \text{Span}\{ v_1, v_2, \dots, v_n \}$, we say $\{ v_1, \dots, v_n \}$ is a **generating set** of $\mathcal{V}$ and its vectors are called **generators** of $\mathcal{V}$

> [!example] Generating Set of $\mathbb{R}^3$
> We want to demonstrate how **every vector** in $\mathbb{R}^3$ can be written as a [[Linear Combination]] of vectors: $[3, 0, 0], [0, 2, 0], [0, 0, 1]$ and thus these vectors span $\mathbb{R}^3$.
> 
> We must show two things:
> 1. Every linear combination is a vector in $\mathbb{R}^3$
> 2. Every vector in  $\mathbb{R}^3$ can be written as a linear combination of the above vectors.
> 
> (1) follows from the fact that $\mathbb{R}^3$ contains all 3-vectors (and every linear combination we could construct would be a 3-vector).
> To show (2), we need to find coefficients that satisfy the following for all $[x, y, z] \in \mathbb{R}^3$
> $$
> [x, y, z] = \alpha [3, 0, 0] + \beta [0, 2, 0] + \gamma [0, 0, 1]
> $$
> we can see that for $\alpha = \frac x 3$, $\beta = \frac y 2$, and $\gamma = z$, we can construct the vector $[x, y, z]$ from a linear combination of our choice vectors.
> 
> Therefore, $\{ [3, 0, 0], [0, 2, 0], [0, 0, 1] \}$  is a generating set for $\mathbb{R}^3$.

## Linear Combinations of Other Linear Combinations

We can use the previous example to show that $\{ [1, 0, 0], [1, 1, 0], [1, 1, 1] \}$ is also a generating set of $\mathbb{R}^3$.

$$
\begin{align}
[3, 0, 0] &= 3 [1, 0, 0] \\
[0, 2, 0] &= 2 [1, 1, 0] + -2 [1, 0, 0] \\
[0, 0, 1] &= [1, 1, 1] - [1, 1, 0] \\
\end{align}
$$

We can then write the linear combination from the previous example in terms of the new vectors:

> [!abstract] Proof.
> $$
> \begin{align}
> [x, y, z] &= \frac x 3 [3, 0, 0] + \frac y 2 [0, 2, 0] + z [0, 0, 1] \\
> &= \frac x 3 (3 [1, 0, 0]) = \frac y 2 (2 [1, 1, 0] - 2[1, 0, 0]) + z([1, 1, 1] - [1, 1, 0]) \\
> &= x [1, 0, 0] + y [0, 1, 0] + z [0, 0, 1] \\
> &&\blacksquare
> \end{align}
> $$

## Standard Generators

**Standard Generators** are the "simplest" or "most natural" set of generators for a set.

> [!info] Standard Generators
> For any positive integer $n$, the standard generators of $\mathbb{R}^n$ are:
> $$
> \begin{align}
> &e_0 &= [1, 0, \dots, 0] \\
> &e_1 &= [0, 1, \dots, 0] \\
> &\vdots \\
> &e_{n-1} &= [0, \dots, 0, 1] \\
> \end{align}
> $$

We can also define standard generators in terms of functions:

> [!info] Standard Generators (Function)
> For any **finite** domain $D$ and field $\mathbb{F}$, there are standard generators defined for $\mathbb{F}^D$ as:
> 
> For all $k \in D$, let $e_k$ be the function mapping $k \to 1$ and all other $d \in D, d \neq k$ mapped to 0.
