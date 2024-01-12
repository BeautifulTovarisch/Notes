We want to look at the relationship between solution sets of **homogeneous linear systems** and the [[Span]] of a set of vectors.

> [!info] Homogeneous Linear Equation/System
>  [[Linear Equations]] with right-hand side equal to 0 are called **homogeneous linear equations**. A linear system composed entirely of homogeneous linear equations is called a **homogeneous linear system**.

## Comparison to Spans

$\text{Span}([1, 0, 1.65], [0, 1, 1])$ can be represented as:

$$
\begin{align}
&\{ (x, y, z) \in \mathbb{R}^3 : 1.65x + y - z = 0 \} \\
&= \\
&\{ [x, y, z] \in \mathbb{R}^3 : [1.65, 1, -1] \cdot [x, y, z] = 0 \}
\end{align}
$$

$\text{Span}([3, 2])$ can be represented as:

$$
\{ [x, y] \in \mathbb{R}^2 : 2x - 3y = 0 \}
$$

$\text{Span}([-1, 2.2])$ can be represented as a pair of homogeneous linear equations:

$$
\{ [x, y, z] \in \mathbb{R}^3 : [4, -1, 1] \cdot [x, y, z] = 0, [0, 1, 1] \cdot [x, y, z] = 0\}
$$

"The line consisting of the set of triples, $[x, y, z]$ that satisfy the linear system"

## Uses of the Multiple Representations

In certain scenarios, one representation of the [[Geometry of Sets of Vectors|flat]] may be easier to apply than the other.

Suppose we want to find the plane containing $\text{Span}([4, -1, 1])$ and $\text{Span}([0, 1, 1]$. We can trivially combine these representations to get:

$$
\text{Span}([4, -1, 1], [0, 1, 1])
$$

and so our solution naturally lent itself to using the Span representation.

On the other hand, suppose we want to find the intersection between planes: $\{[x, y, z] \in \mathbb{R}^3 : [4, -1, 1] \cdot [x, y, z] = 0\}$, and $\{[x, y, z] \in \mathbb{R}^3 : [0, 1, 1] \cdot [x, y, z] = 0\}$. Then we simply find the intersection of these two sets:

$$
\{[x, y, z] \in \mathbb{R}^3 : [4, -1, 1] \cdot [x, y, z],[0, 1, 1] \cdot [x, y, z] = 0\}
$$

> [!tip] We learn how to convert between the two later.