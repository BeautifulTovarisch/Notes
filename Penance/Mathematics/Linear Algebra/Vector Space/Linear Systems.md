The solution set to an arbitrary [[Linear Equations#System of Equations]], if it exists, is an [[Affine Spaces|affine space]]. We would like to know whether the solution is **unique**.

> [!abstract] Uniqueness of a solution to a linear system
> Let $u_1$ be a solution for:
> $$
> \begin{align}
> a_1 &\cdot x = \beta_1 \\
> &\vdots \\
> a_m &\cdot x = \beta_m \\
> \end{align}
> $$
>
> Then another vector, $u_2$ is a solution if and only if $u_2 - u_1$ is a solution to
> $$
> \begin{align}
> a_1 &\cdot x = 0 \\
> &\vdots \\
> a_m &\cdot x = 0 \\
> \end{align}
> $$
> **Proof.**
> For $i = 0, 1, \dots, m$, we consider the system:
> $$
> \begin{align}
> a_i \cdot u_1 = \beta_i \\
> a_i \cdot u_2 = \beta_i
> \end{align}
> $$
>
> Subtracting, we have:
> $$
> \begin{align}
> &a_i \cdot u_1 - a_i \cdot u_2 = \beta_i - \beta_i &\iff \\
> &a_i \cdot u_1 - a_i \cdot u_2 = 0 &\iff \\
> &a_i \cdot (u_1 - u_2) = 0 \\
> &&\blacksquare
> \end{align}
> $$

In other words, $u_2$ is a solution if and only if $u_2 - u_1 \in \mathcal{V}$, where $\mathcal{V}$ is the solution set to a [[Homogeneous Linear Systems|homogeneous linear system]].

Now let $v = u_2 - u_1$, so then $u_2 = u_1 + v$ and notice that because $\mathcal{V}$ is the solution set to a homogeneous linear system, it is a [[Vector Spaces|vector space]].  $u_1 + v = u_2$ is a solution to the first linear system if and only if $v \in \mathcal{V}$. But then we have:

$$
\{ u + v : v \in \mathcal{V} \}
$$

which is an [[Affine Spaces|affine space]]!

> [!tip] Quick Summary
> Every vector space is the solution set to a homogeneous linear system and every
> affine space is the solution set of a linear system.

## Examples

> [!example]
> $$
> [0, 0] \cdot x = 1
> $$
> has an empty solution set, since there is no such vector $x$ that satisfies the system.

> [!example]
> The solution set to
> $$
> \begin{align}
> [1, 0] \cdot x = 2 \\
> [0, 1] \cdot x = 5
> \end{align}
> $$
> is the singleton $\{ [2, 5] \}$, which can be written:
> $$
> \{ [2, 5] + v : v \in \{ [0, 0] \} \}
> $$