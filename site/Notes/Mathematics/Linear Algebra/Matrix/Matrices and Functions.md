> This section defines a linear transformation in a non-traditional way.

For every matrix $M$, we define a function $x \mapsto M * x$ called $f_M$:

> [!info] Definition
> If $M$ is an $R \times C$ matrix over a field $\mathbb{F}$, then $f_M : \mathbb{F}^C \to \mathbb{F}^R$ is defined by $f_M(x) = M * x$, where $x$ is a $C$-vector.

## From Function to Matrix

Given $f : \mathbb{F}^A \to \mathbb{F}^B$ we would like to compute $M$ such that $f_M(x) = M *x$. We start by determining the dimension of $M$ and $x$. Since $x \in \mathbb{F}^A$, it is an $A$-vector, and because the co-domain of $f$ is $\mathbb{F}^B$, $M$ must be a $B \times A$ matrix (since the product must produce a vector in the domain of $M$'s rows).

We attempt to use to the [[Generators#Standard Generators]] of $A$ to work backwards to find $M$.

### Examples Deriving a Matrix

> [!warning] We learn after this section that one of the examples is **invalid**. I've included the proof alongside the example below.

> [!example]
> Let $S(.)$, $S: \mathbb{R}^2 \to \mathbb{R}^2$ be defined by $S([x, y]) = [2x, y]$. Assume $S([x, y]) = M * [x, y]$. Using our standard generators for $\mathbb{R}^2$, $S([1, 0]) = [2, 0]$, and $S([0, 1]) = [0, 1]$.  Then
>$$
>M =
>\begin{bmatrix}
>2 & 0 \\
>0 & 1
>\end{bmatrix}
>$$


> [!example]
> Let $r_{90}(.)$ be the function from $R^2 \to R^2$ that rotates points by $90\degree$ counterclockwise about the origin. Assume $r_{90}(v) = M * v$. Rotating the standard generators by $90\degree$ we have $[1, 0] = [0, 1]$ and $[0, 1] = [-1, 0]$. So we have
> $$
> M =
> \begin{bmatrix}
> 0 & -1 \\
> 1 & 0
> \end{bmatrix}
> $$

> [!example]
> For an angle $\theta$, let $r_\theta(.)$ be the function from $R^2 \to R^2$ that rotates points counterclockwise by $\theta$. Then by trigonometry, $r_\theta([1, 0]) = [cos \theta, sin \theta]$, $r_\theta([0, 1]) = [-sin \theta, cos \theta]$ so then
> $$
> M =
> \begin{bmatrix}
> cos\theta & -sin\theta \\
> sin\theta & cos \theta
> \end{bmatrix}
> $$


> [!example]
> Let $t: R^2 \to R^2$ be defined as $t(.)$ such that $t$ translates the $x$ component of a vector one to the right and the $y$ component two up. Then $t([1, 0]) = [2, 2]$ and $t([0, 1]) = [1, 3]$ so then
> $$
> M =
> \begin{bmatrix}
> 2 & 1 \\
> 2 & 3
> \end{bmatrix}
> $$
>
> Let $v = [2, 3]$, then $M * v = 2[2, 2] + 3[1, 3] = [7, 13]$

> [!warning] Counterexample
> In the [[Linear Functions|next section]] we determine the properties for which an function can be written in terms of a matrix-vector multiplication. We show that $t(.)$ above **does not** meet the requirements to be a linear transformation:
>
> Counterexample.
> Suppose $u = [1, 0], v = [0, 1]$, then $u + v = [1, 1]$, so then $t(u + v) = [2, 3]$, but $t(u) + t(v) = [2, 2] + [1, 3] = [3, 5]$.