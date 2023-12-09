We consider a [[Line Segments#Segments Through the Origin|line through the origin]], which forms a [[Vector Spaces|vector space]], say, $\mathcal{V}$. Take some vector $a$ and add it to every vector in $\mathcal{V}$ to obtain:

$$
\{ a + v : v \in \mathcal{V} \}
$$

which we abbreviate as $a + \mathcal{V}$. Then the resulting set is a [[Line Segments#Arbitrary Line Segments|line through a]], **not the origin.**

> [!example]
> We want to show that for $u_1 = [1, 0, 4.4], u_2 = [0, 1, 4], u_3 = [0, 0, 3]$, for $\mathcal{V} = \text{Span}(a, b)$, $u_1 + \mathcal{V}$ is the unique plane through points $u_1, u_2, u_3$.
> Define $a = u_2 - u_1$, $b = u_3 - u_1$ and notice $u_1 + \mathcal{V}$ contains:
> 1. $u_1$ since $\mathcal{V}$ is a span, which contains the zero vector ($u_1 + 0 = u_1$)
> 2. $u_2$ since $u_1 + a = u_2$
> 3. $u_3$ since $u_1 + b = u_3$
>
> Then since $\mathcal{V}$ contains $u_1, u_2, u_3$, it must be the **unique plane** through these points.

## Affine Combinations

Recall that [[Line Segments#Affine Combinations]] are [[Linear Combination|Linear Combinations]] whose coefficients sum to 1.

> [!example] Affine Combination
> $2[10, 20] + 3[0, 10] - 4[30, 40]$ is **affine** because $2 + 3 - 4 = 1$.

> [!example]
> $\mathcal{V} = \text{Span}(a, b)$
> We want to show that $u_1 + \mathcal{V}$ is affine.
> $$
> \begin{align}
> u_1 + \mathcal{V} &= \alpha (u_2 - u_1) + \beta (u_3 - u_1) \\
> &= u_1 - u_1(\alpha + \beta) + \alpha u_2 + \beta u_3 \\
> &= (1 - \alpha + \beta)u_1 + \alpha u_2 + \beta u_3 \\
> &= \gamma u_1 + \alpha u_2 + \beta u_3 &\gamma = (1 - \alpha - \beta).
> \end{align}
> $$
>
> The final expression is known as an **affine hull**.

> [!info] Affine Hull
> The set of affine combinations of a collection of vectors is called an **affine hull**.

### Examples

> [!example]
> Affine Hull of $\{ [0.5, 1], [3.5, 3] \}$
> $$
> \{ \alpha [0.5, 1] + \beta [3.5, 3] : \alpha, \beta \in \mathbb{R}, \alpha + \beta = 1\}
> $$
> This is again a [[Line Segments#Arbitrary Line Segments]].

> [!example]
> Affine Hull of $\{ [1, 2, 3] \}$ = $\{ \alpha [1, 2, 3], \alpha = 1 \}$

> [!example]
> Affine Hull of $\{ [2, 3], [3, 4], [4, 5]\}$.  Plotting these points, we see they form a line rather than the [[Geometry of Sets of Vectors#General Pattern|expected flat]] for $k = 3$.

## Affine Space

An affine space is simply the result of translating a vector space, $\mathcal{V}$ by some vector. Recall:

> [!info] Affine Space
> $$
> \{ a + v : v \in \mathcal{V} \}
> $$

Thus, we see that a **flat** is an **affine space** that is a **subset** of $\mathbb{R}^n$.

Now we determine whether the affine combination of vectors (affine hull) always forms an affine space.

### Does an Affine Hull form an Affine Space?

> [!abstract] Lemma a.
> For any vectors, $u_1, \dots, u_n$:
> $$
> \{ \alpha_1 u_1 + \dots + \alpha_n u_n : \sum_{i=1}^n a_i = 1 \} = \{ u_1 + v : v \in \text{Span}(u_2 - u_1, \dots, u_n - u_1) \}
> $$
> Proof. Suppose we have a vector, say $v \in \text{Span}(u_2 - u_1, \dots, u_n - u_1)$ can be written:
> $$
> v = \alpha_2 (u_2 - u_1) + \dots + \alpha_n (u_n - n_1)
> $$
> Then,
> $$
> \begin{align}
> u_1 + v &= \\
> &= u_1 + \alpha_2 (u_2 - u_1) + \dots + \alpha_n (u_n - u_1) \\
> &= u_1 - (\alpha_2 u_1 - \dots - \alpha_n u_1) + \alpha_2 u_2 + \dots + \alpha_n u_n \\
> &= (1 - \alpha_2 - \dots - \alpha_n)u_1 + \alpha_2 u_2 + \dots + \alpha_n u_n &\text{(i)}
> \end{align}
> $$
> and so we see we have an affine combination. If we let $\alpha_1 = 1 - \alpha_2 - \dots - \alpha_n$, we have:
> $$
> \alpha_1 u_1 + \alpha_2 u_2 + \dots + \alpha_n u_n
> $$
> and clearly $\sum_{i=1}^n a_i = 1$, so we have shown that every vector $u_1 + v$ is in the left-hand set.
>
> Conversely, since we are given $\sum_{i=1}^n a_i = 1$, we can choose $\alpha_1 = 1 - \alpha_2 - \dots - \alpha_n$ and write equation $\text{(i)}$, and so every element in the affine combine of the LHS is also in the right.
> $\blacksquare$

We see that affine spaces, similar to [[Vector Spaces#Solution Set]], can be represented as an affine hull or as the solution set to a **non-homogeneous** [[Linear Systems|linear system]].