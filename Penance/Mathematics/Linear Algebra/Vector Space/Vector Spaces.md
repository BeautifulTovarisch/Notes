We want to look at the common properties between the [[Span]] and [[Homogeneous Linear Systems]] representations of flats. We notice that a subset $\mathcal{V} \subseteq \mathbb{F}^D$ in either form has three properties:

1. **Zero Vector** - The subset must contain the zero vector.
2. **Closed under Multiplication** - for every vector $v$,  if $v \in \mathcal{V}$, then so is $\alpha v, \alpha \in \mathbb{F}$
2. **Closed under Vector Addition** - for vectors $u, v$, if $u, v \in \mathcal{V}$, then so is $u + v$.

> [!info] Trivial Vector Space
> A vector space consisting of only the **zero vector** is called a **trivial vector space**.

## Span

> [!abstract] A Span is a Vector Space
> Proof. Suppose $\mathcal{V} = \text{Span}(v_1, v_2, \dots, v_n)$. We will show that $\mathcal{V}$ satisfies all three of the above properties.
> 1. **Zero Vector.** By definition, $\mathcal{V}$ contains all linear combinations of $v1, \dots, v_n$. Then clearly $0v_1, 0v_2, \dots, 0v_n$ is in $\mathcal{V}$, and so it contains the zero vector.
> 2. **Closed under Multiplication**. Let  $v = \beta_1v_1, \beta_2v_2, \dots, \beta_nv_n$, then $\alpha v = \alpha\beta_1v_1, \alpha\beta_2v_2, \dots, \alpha\beta_nv_n$
> 3. **Closed under Vector Addition**. Let
> $$
> \begin{align}
> &u = \alpha_1v_1, \alpha_2v_2, \dots, \alpha_nv_n \\
> &v = \beta_1v_1, \beta_2v_2, \dots, \beta_nv_n \\ \\
> &u + v = (\alpha_1 + \beta_1)v_1, (\alpha_2 + \beta_2)v_2, \dots, (\alpha_n + \beta_n)v_n
> \end{align}
> $$
> $\blacksquare$

## Solution Set

>[!abstract] A Solution Set of a Homogeneous Linear System is a Vector Space
>Proof. Suppose $\mathcal{V} = \{ x: a_1 \cdot  x = 0, \dots, a_m \cdot x = 0 \}$.
>1. **Zero Vector**. Then $\mathcal{V}$ contains the zero vector since, $a_1 \cdot 0 = 0, \dots, a_m \cdot 0 = 0$.
>2. **Closed under Multiplication**. If $a_1 \cdot v_1 = 0, \dots, a_m \cdot v_m = 0$ then $\alpha (a_1 \cdot v_1) = 0, \dots, \alpha (a_m \cdot v_m) = 0$ and so $a_1 (\alpha \cdot v_1) = 0, \dots, a_m (\alpha \cdot v_m) = 0$
>3. **Closed under Vector Addition**. If
>$$
>\begin{align}
>&u = a_1 \cdot u, \dots, a_m \cdot u = 0 \\
>&v = a_1 \cdot v, \dots, a_m \cdot v = 0 \\ \\
>&u + v = a_1 \cdot (u + v), \dots, a_m \cdot (u + v)
>\end{align}
>$$
>$\blacksquare$

## Subspaces

If a vector space is a subset of another, it is called a subspace.

> [!info] Vector Subspace
> If $\mathcal{V}, \mathcal{W}$ are vector spaces, and $\mathcal{V} \subseteq \mathcal{W}$, then $\mathcal{V}$ is a **subspace** of $\mathcal{W}$

### Examples

- The only subspace of $\{ [0, 0] \}$ is itself.
- $[0,0]$ is a subspace of $\{ \alpha[2, 1]: \alpha \in \mathbb{R}^2 \}$, which is a subspace of $\mathbb{R}^2$.
- $\mathbb{R}^2$ **is not** a subspace of $\mathbb{R}^3$, since there are **no 2-vectors** in $\mathbb{R}^3$.

## Example

We want to show that a given subspace with certain properties is equal to $\mathbb{R}^2$

> [!abstract] $\mathcal{V} = \mathbb{R}^2$
> Proof. Suppose $\mathcal{V}$ is a subspace of $\mathbb{R}^2$ containing some non-zero vector $[a, b]$ and some other vector $[c, d]$ not in the $\text{Span}([a, b])$. We will show that $\mathcal{V} = \mathbb{R}^2$.
> > [!abstract] Lemma a. $ad \neq bc$
> > Proof. Since $[a, b] \neq [0, 0]$ by assumption, either of $a$ or $b$ or both are nonzero. Consider the following cases:
> >
> > **($a \neq 0$):** Since $[c, d]$ is not in the Span of $[a, b]$, then $[c, d] \neq \alpha [a, b]$. Let $\alpha = \frac c a$.  Then we have $[c, d] \neq [c, \alpha b] \implies d \neq \alpha b$, so $d \neq \frac c a b$. Multiplying through we find $ad \neq bc$.
> >
> > **($b \neq 0$):** Let $\alpha = \frac d b$. Then similarly, we have $[c, d] \neq [\alpha a, d] \implies c \neq \alpha a$, so $c \neq \frac d b a$. Multiplying by $b$ we have: $ad \neq bc$.
> >
> > Thus, in either case we find that $ad \neq bc$.
>
> Now we want to show that every vector in $\mathbb{R}^2$ can be written as a linear combination of $[a, b], [c, d]$. Then we must choose scalars $\alpha, \beta$ such that for some $[p, q] \in \mathbb{R}^2$, we have
> $$
> [p, q] = \alpha[a, b] + \beta[c, d]
> $$
> Let $\alpha = \frac {dp - cq} {ad - bc}, \beta = \frac {aq - bp} {ad - bc}$(by Lemma a, $ad - bc \neq 0$), then we have:
> $$
> \begin{align}
> [p, q] &= \alpha[a, b] + \beta[c, d] \\
> &= \frac {dp - cq} {ad - bc}[a, b] + \frac {aq - bp} {ad - bc}[c, d] \\
> &= \frac 1 {ad - bc}[adp - bcp, adq = bcq] \\
> &= \frac 1 {ad - bc}[(ad - bc)p, (ad - bc)p] \\
> &= [p, q]
> \end{align}
> $$
> Therefore, we have written an arbitrary vector, $[p, q]$, in terms of $[a, b], [c, d]$, and so all of $\mathbb{R}^2$ must be in $\text{Span}([a, b], [c, d])$. Moreover, since, $\mathbb{R}^2$ contains every 2-vector, it must also include all of $\mathcal{V}$, and so both sets are subsets of one another and thus $\mathbb{R}^2 = \mathcal{V}$.
> $\blacksquare$