# The Matrix

A traditional matrix is a two-dimensional array whose entries are elements of the same field.

$$
\begin{bmatrix}
1 & 2 & 3 \\
10 & 20 & 30
\end{bmatrix}
$$

The above is a 2 x 3 matrix, since it has two rows and three columns.

> [!info] M x N matrix.
> In general, an $n \times m$ matrix $A$ has $n$ rows and $m$ columns. We say $A_{ij}$ is the entry at the **ith** row and **jth** column.

```Python
# Basic list comprehension to generate a 3 x 4 zero-matrix:
[[0 for _ in range(4)] for _ in range(3)]

'''
[
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0]
]
'''

# Another comprehension for comparison to column-major order. Notice that
# they are the transposes of one another:

# Row-Major
[[i-j for j in range(4)] for i in range(3)]

'''
[
	[0, -1, -2, -3],
	[1, 0, -1, -2],
	[0, 1, 2, 3]
]
'''

# Column-Major
[[i-j for i in range(3)] for j in range(4)]

'''
[
	[0, 1, 2],
	[-1, 0, 1],
	[-2, -1, 0],
	[-3, -2, -1]]
'''
```

## Rows, Columns, and Entries

We can represent the rows and columns of a matrix as vectors. Formally:

> [!info] Rows, Columns, and Entries
> - $M_{rc}$ - For an $R \times C$ matrix $M$, and for $r \in R, c \in C$, the $r,c$ element of $M$ is defined to be the image of $(r, c)$ and is written as $M_{rc}$
> - Rows - For $r \in R$, row $r$ is the $C$**-vector** such that $r = M_{r,}$
> - Columns - For $c \in C$, column $c$ is the $R$**-vector** such that $c = M_{,c}$

## Identity Matrix

> Essentially a square matrix with 1s in the diagonal positions

$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{bmatrix}
$$

> [!info] Identity Matrix
> For a finite set $D$, the $D \times D$  identity matrix is the matrix whose row-label set and column-label set are both $D$ and in which every $(d, d) = 1$ with all other entries zero.

## Column Space and Row Space

There are two vector spaces, the **column space** and **row space** associated with a matrix.

> [!info] Column Space and Row Space
> For a matrix $M$,
> - The column space of $M$, $\text{Col} \; M$ is the [[Vector Spaces]] spanned by $M$'s columns
> - The row space of $M$, $\text{Row} \; M$ is the spanned by $M$'s rows

> [!example] Row and Column Spaces
> Let
> $$
> M =
> \begin{bmatrix}
> 1 & 2 & 3 \\
> 10 & 20 & 30
> \end{bmatrix}
> $$
> then,
> $$
> \begin{align}
> \text{Col} \; M &= \text{Span}([1, 10], [2, 20], [3, 30])  \\
> &= \alpha [1, 10] + \beta [2, 20] + \gamma [3, 30] \\ \\
> \text{Row} \; M &= \text{Span}([1, 2, 3], [10, 20, 30]) \\
> &= \alpha [1, 2, 3] + \beta [10, 20, 30]
> \end{align}
> $$
>
> In the above examples, we could reduce the column space to $\text{Span}([1, 10])$ and row space to $\text{Span}([1, 2, 3])$.

## Transpose

Taking the transpose of a matrix means "flipping" its rows and columns.

> [!info] Transpose
> The **transpose** of a $P \times Q$ matrix, $M^T$ is a $Q \times P$ matrix such that $(M^T)_{j,i} = M_{i, j}$. We say a matrix is **symmetric** if $M = M^T$.

> [!example] Symmetric Matrix
> Let
> $$
> M =
> \begin{bmatrix}
> 1 & 2 \\
> 2 & 4
> \end{bmatrix}
> =
> \begin{bmatrix}
> 1 & 2 \\
> 2 & 4
> \end{bmatrix}
> = M^T
> $$