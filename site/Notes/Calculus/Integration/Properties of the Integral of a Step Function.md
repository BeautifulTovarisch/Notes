# Properties of the Integral of a Step Function

Using the properties of summations, we can establish helpful manipulations of the [[Step Functions#Definite Integral of a Step Function]], which end up generalizing to other functions later on.

> [!abstract] Additive Property
> For step functions $s, t$, we have
> $$
> \int_a^b [s(x) + t(x)] \; dx = \int_a^b s(x) \; dx + \int_a^b t(x) \; dx
> $$
>
> Proof.
> Let $P = \{ x_0, x_1, \dots, x_n \}$ be a partition over interval $[a, b]$ such that functions $s, t$ are constant over every open sub-interval of $P$. Assume $s(x) = s_k, t(x) = t_k$ if $x_{k-1} \lt x \lt x_k$, where $k \in \mathbb{N}$. By definition of the integral of a step function:
> $$
> \begin{align}
> \int_a^b [t(x) + s(x)] \; dx &= \sum_{k=1}^n s_k (x_k - x_{k-1}) + t_k (x_k - x_{k-1}) \\
> &= \sum_{k=1}^n s_k (x_k - x_{k-1}) + \sum_{k=1}^n t_k (x_k - x_{k-1}) &\text{Additivity of Sum} \\
> &= \int_a^b s(x) \; dx + \int_a^b t(x) \; dx  &\text{By Definition} \\
> &&\blacksquare
> \end{align}
> $$

> [!abstract] Homogeneous Property
> For a step function $s$ we have
> $$
> \int_a^b c \cdot s(x) \; dx = c \cdot \int_a^b s(x) \; dx
> $$
>
> Proof.
> $$
> \begin{align}
> \int_a^b c \cdot s(x) \; dx &= \sum_{k=1}^n c \cdot s_k (x_k - x_{k-1}) &\text{Definition} \\
> &= c \sum_{k=1}^n s_k (x_k - x_{k-1}) &\text{Homogeneity of Sums} \\
> &= c \int_a^b s(x) \; dx &\text{Definition} \\
> &&\blacksquare
> \end{align}
> $$

> [!abstract] Linearity Property
> For step functions $s, t$
> $$
> \int_a^b [c_1 s(x) + c_2 t(x)] \; dx = c_1 \int_a^b s(x) \; dx + c_2 \int_a^b t(x) \; dx
> $$
>
> Proof.
> $$
> \begin{align}
> \int_a^b [c_1 s(x) + c_2 t(x)] \; dx &= \sum_{k=1}^n c_1 \cdot s_k (x_k - x_{k-1}) + \sum_{k=1}^n c_2 \cdot t_k (x_k - x_{k-1}) &\text{Additivity} \\
> &= c_1 \sum_{k=1}^n s_k (x_k - x_{k-1}) + c_2 \sum_{k=1}^n t_k (x_k - x_{k-1}) &\text{Homogeneity} \\
> &= c_1 \int_a^b s(x) \; dx + c_2 \int_a^b t(x) \; dx \\
> &&\blacksquare
> \end{align}
> $$

> [!abstract] Comparison
> Assume step functions $s, t$. If $\forall x \in [a, b], \; s(x) \leqslant t(x)$ then,
> $$
> \int_a^b s(x) \; dx \leqslant \int_a^b t(x) \; dx
> $$
>
> Proof.
> By monotonicity of summations:
> $$
> \int_a^b s(x) \; dx = \sum_{k=1}^n s_k (x_k x_{k-1}) \leqslant \sum_{k=1}^n t_k (x_k x_{k-1}) = \int_a^b t(x) \; dx
> $$
> Hence,
> $$
> \int_a^b s(x) \; dx \leqslant \int_a^b t(x) \; dx
> $$
> $\blacksquare$

> [!abstract] Additivity with Respect to the Interval of Integration
> Let $s$ be a step function. Then if $a \lt b \lt c$
> $$
> \int_a^b s(x) \; dx + \int_b^c s(x) \; dx + \int_a^c s(x) \; dx
> $$
>
> Proof.
> Suppose $P_1 = \{ a, x_1, \dots, b \}$ $P_2 = \{ x_{k+1}, x_{k+2}, \dots, c\}$ where $b < x_{k+1}$ and let $s$ be constant over the open sub-intervals of $P_1$ and $P_2$. Then $s$ is also constant over the common refinement $P = P_1 \cup P_2$. Hence, $\int_a^b s(x) \; dx + \int_b^c s(x) \; dx$ gives the integral of $s$ over $P$ and since $P$ is a partition of $[a, c]$, this value must be equal to $\int_a^c s(x) \; dx$.
>
> $\blacksquare$

> [!abstract] Invariance Under Translation
> Let $s$ be a step function defined over interval $[a, b]$. Then
> $$
> \int_{a+c}^{b+c} s(x) \; dx = \int_{a}^{b} s(x - c) \; dx
> $$
>
> Proof.
> Suppose $s$ is constant over the open sub-intervals of $P = \{x_0 + c, x_1 + c, \dots, x_n + c \}$ which partitions $[a + c,  b + c]$. Then the integral of $s$ over $[a + c, b + c]$ is given by $\int_{a + c}^{b + c} s(x) \; dx$. Next, notice that $s(x - c)$ is constant over the open sub-intervals of $P' = \{ x_0, x_1, \dots, x_n \}$ over $[a, b]$ and so the integral over $P'$ is given by $\int_a^b s(x - c) \; dx$. Finally, by definition of translation, the areas formed by the ordinate sets of $s$ and $s(x - c)$ are congruent, and hence their integrals are equal.
> $\blacksquare$

> [!abstract] Expansion/Contraction of the Interval of Integration
> Let $s$ be a step function over $[a, b]$. Then
> $$
> \int_{ka}^{kb} s(\frac x k) \; dx = k \int_a^b s(x) \; dx
> $$
>
> Proof.
> Let $P = \{ x_0, x_1, \dots, x_n \}$ be a partition of $[a, b]$ such that $s$ is constant on the open sub-intervals of $P$ and assume $s(x) = s_i$ if $x_{i-1} < x < x_i$. Let $t(x) = s(\frac x k)$ if $ka \leqslant x \leqslant kb$. Then $t(x) = s_i$ if $x \in (x_{i-1}, x_i)$, hence $P' = \{ kx_0, kx_1, \dots, kx_n \}$ is a partition over $[ka, kb]$ and $t$ is constant on the open subintervals of $P'$. Thus:
> $$
> \int_{ka}^{kb} t(x) \; dx = \sum_{i=1}^n s_i (kx_i - kx_{i-1}) = k \sum_{i=1}^n s_i (x_i - x_{i-1}) = k \int_a^b s(x) \; dx
> $$
