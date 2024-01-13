# Geometry of Sets of Vectors

We look at geometric representations of the span of a set of vectors.

## Geometry of Span $\mathbb{R}$

We consider the set of all linear combinations of a vector $v$:

$$
\text{Span}(v) = \{ \alpha v : \alpha \in \mathbb{R} \}
$$

we see as in [[Line Segments#Arbitrary Line Segments]] that this forms **a line** through the origin and vector $v$.

Next, see that $\text{Span}([1, 0], [0, 1])$ spans $\mathbb{R}^2$, forming **a plane** through the origin. Also notice that **not every** span of distinct vectors will form a plane:

$$
\begin{align}
&\text{Span}([1, 2], [2, 4]) \\
&= \alpha_1 [1, 2] + \alpha_2 [2, 4] \\
&= \alpha_1 [1, 2] + (2 \alpha_2)[1, 2] \\
&= (\alpha_1 + 2 \alpha_2) [1, 2]
\end{align}
$$

and so the span of these vectors forms a line, **not a plane**.

> [!info] Trivial Combination
> The span of any set of vectors must contain the origin. This is called the **trivial combination.**

## Dimension of a Span of Vectors

We would like to predict the dimension of the **flat** formed by a span of vectors.

> [!info] Flat
> We define a flat to be a **geometric object**.

> [!question] Hypothesis
> The span of $k$ vectors over $\mathbb{R}$ forms a $k$-dimensional flat containing the origin or a flat of lower dimension containing the origin.

## General Pattern

> [!info] Geometric Objects Represented by the Span of $k$ vectors.
> - $k = 0$ : The span of zero vectors forms a point (the origin).
> - $k = 1$ : The span of one vector forms a line
> - $k = 2$ : The span of two vectors forms a plane
> - $k = 3$ : The span of three vectors forms a 3D flat.
