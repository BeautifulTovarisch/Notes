A sequence is a list of terms defined by some rule, and the corresponding series is the summation of some sequence.

## Arithmetic

An arithmetic progression (so called due to its relationship to the arithmetic mean) has terms that differ by a constant $k$.

### Sequence

> [!info] Arithmetic Sequence
> An **arithmetic sequence** (or progression) is a sequence of the form:
> $$
> S = a, a + d, \dots, a + (n-1)d, \dots
> $$
> where $d$ denotes the **common difference**  between the terms.

### Series

> [!abstract] Sum of Arithmetic Sequence
> $$
> \sum_{i=0}^n A_i = \frac n 2 (2a + (n-1)d) = \frac {n (a + (n-1)d)} 2
> $$
>
> Proof.
> To find the summation of a (finite) arithmetic progression we employ a trick (supposedly) developed by Gauss:
>
> $$
> \begin{array}{c}
> & S & = & a & a + d & a + 2d & \dots & a + (n-1)d \\
> & S & = & a + (n-1)d & a + (n-2)d & a + (n-3)d & \dots & a
> \end{array}
> $$
>
> We find that
> $$
> S + S = 2a + (n-1)d, 2a + (n-1)d, \dots, 2a + (n-1)d = 2S
> $$
>
> which has $n$ terms all $2a + (n-1)d$. Hence, $S = \frac n 2 (2a + (n-1)d)$
>
> $\blacksquare$

> [!tip] Convergence
> An infinite arithmetic series **does not converge** unless $d = 0$.

## Geometric

A geometric progression has terms defined by repeated multiplication of a **common ratio** $r$.

### Sequence

> [!info] Geometric Sequence
> A **geometric sequence** is a sequence of the form:
> $$
> G = a, ar, ar^2, \dots, ar^{n-1}
> $$
> where $r \in \mathbb{R}, r \neq 1$ is called the **common ratio**.

### Series

We employ a similar trick to arrive at a closed form for a geometric series:

> [!abstract] Geometric Series
> Suppose $G$ is a geometric progression, then the sum of the terms of $G$ is given by
> $$
> \sum_{i=0}^n G_i = \frac {a - ar^n} {1 - r}
> $$
> In the following proof, we omit the summation notation for brevity.
>
> Proof.
> Let $G$ be some geometric progression and let $r$ be its common ratio. We notice that
> $$
> r \cdot G = r(a + ar + \dots + ar^{n-1}) = ar + ar^2 + \dots ar^n
> $$
>
> Subtract $r \cdot G$ from $G$ to get:
> $$
> \begin{array}{c}
> & G & = & a & ar & ar^2 & \dots & ar^{n-1} \\
> & r \cdot G & = & ar & ar^2 & ar^4 & \dots & ar^n
> \end{array}
> $$
>
> Rearranging, we have $G(1-r) = a - ar^n$ and finally for $r \neq 1$ we have
> $$
> G = \frac {a - ar^n} {1 - r}
> $$
>
> $\blacksquare$