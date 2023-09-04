# Line Segments as Vectors

We can use [[The Vector|vectors]] to represent line segments in a plane.

## Vectors as Arrows

We can represent vectors as arrows in $R^n$

> [!example]- 
> $u = {3, 1.5}$
> $u$ is a vector with its tail at the origin and head at $(3, 1.5)$

## Segments Through the Origin
Let $v = \{3, 2\}$ and consider the set of scalars: $\{0.1, 0.2, \dots, 0.9, 1.0\}$. For every scalar $\alpha$ in this set, $\alpha v$ is a vector shorter than $v$ and in the same direction. We represent a line segment between the origin and point $v$ as follows: 
$$
\{ \alpha v : \alpha \in \mathbb{R}, 0 \leqslant \alpha \leqslant 1\}
$$
A **line** through the origin is expressed as follows: 
$$
\{ \alpha v : \alpha \in \mathbb{R} \}
$$
(since the values of $\alpha \lt 0$ would "extend" the vector in the opposite direction.)

## Arbitrary Line Segments

We can combine [[The Vector#Vector Addition|vector addition]] and [[The Vector#Scalar Multiplication|scalar multiplication]] to produce arbitrary line segments in a plane: 
$$
\{\alpha u + v : \alpha \in \mathbb{R}, 0 \leqslant \alpha \leqslant 1\}
$$
where $u, v$ are vectors representing the endpoints of the line segment. The idea is to **translate** (via vector addition) a line segment from the origin to the desired position.

> [!example] Line through $u = (0.5, 1)$ and $v = (3.5, 3)$
> Suppose we wish to express a line segment from $u \to v$. This can be expressed by translating the segment $(0,0) \to (3, 2)$ by $(0.5, 1)$:
> $$
> \{ [0.5, 1] + \alpha [3, 2] : 
> \alpha \in \mathbb{R}, 
> 0 \leqslant \alpha \leqslant 1 \}
> $$

### Convex Combinations

Ideally, the expression of a line segment would reference both endpoints symmetrically:

>[!abstract] Line segment from $[0.5, 1] \to [3.5, 3]$
>We begin be noticing that $[3, 2] = [3.5, 3] - [0.5, 1]$. Write:
>$$ \begin{aligned}
> \alpha [3, 2] + [0.5, 1] &= \alpha ([3.5, 3] - [0.5, 1]) + [0.5, 1] \\
> &= \alpha [3.5, 3] - \alpha [0.5, 1] + [0.5, 1] \\
> &= \alpha [3.5, 3] + (1 - \alpha) [0.5, 1]
\end{aligned}
>$$
>Now letting $\beta = (1 - \alpha)$ we have
>$$
> \alpha [3.5, 3] + \beta [0.5, 1] 
>$$
>And so we describe the line segment from $[0.5, 1] \to [3.5, 3]$ as:
>$$
>\{ \alpha [3.5, 3] + \beta [0.5, 1] : \;
>	\alpha,\beta \in \mathbb{R}, \; 
>	\alpha,\beta \geqslant 0 \;
>	\alpha + \beta = 1\}
>$$

> [!info] Definition: Convex Combination
> We say that the combination $\alpha u + \beta v$ is **Convex** if $\alpha, \beta \geqslant 0, \; \alpha + \beta = 1$

### Affine Combinations

We define an affine combination similarly:

> [!info] Definition: Affine Combination
> We say the combination $\alpha u + \beta v$ is **Affine** if $\alpha + \beta = 1$ 

Notice that this implies $\alpha$ or $\beta$  may be negative.