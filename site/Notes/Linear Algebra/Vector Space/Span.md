# Span

> [!info] Span
> The set of **all** linear combinations of $v_1, \dots, v_n$ = $\text{Span} \{ v_1, \dots, v_n \}$

>[!example]
>$\text{Span} \{ [1, 1], [0, 1] \} =$
>$$
>\begin{align}
>[0, 0] = 0 * [1, 1] + 0 * [0, 1] \\
>[1, 1] = 1 * [1, 1] + 0 * [0, 1] \\
>[0, 1] = 0 * [1, 1] + 1 * [0, 1] \\
>[1, 0] = 1 * [1, 1] + 1 * [0, 1] \\
>\end{align}
>$$
>$= \{ [0, 0], [0, 1], [1, 0], [1, 1] \}$

If we know some vector $\hat x$ satisfies a [[Linear Equations#System of Equations | Linear System]],

$$
\begin{align}
&\alpha_1 \cdot x = \beta_1 \\
&\alpha_2 \cdot x = \beta_2 \\
&\vdots \\
&\alpha_n \cdot x = \beta_n \\
\end{align}
$$

we can compute the [[Dot Product]] with $\hat x$ over any vector $a$ in the span $a_1, \dots, a_m$ ($a$ is a [[Linear Combination]]):

Suppose $a = \alpha_1 a_1 + \dots + \alpha_m a_m$, then

$$
\begin{align}
a \cdot x &= (\alpha_1 a_1 + \dots + \alpha_m a_m) \cdot x \\
&= \alpha_1 a_1 \cdot x + \dots + \alpha_m a_m \cdot x &\text{Dist.} \\
&= \alpha_1 (a_1 \cdot x) + \dots + \alpha_m (a_m \cdot x) &\text{Hom.} \\
&= \alpha_1 \beta_1 + \cdots + \alpha_m \beta_m
\end{align}
$$

Therefore, a system of linear equations implies a linear equation of the form $a \cdot x = \beta$ where $a \in Span\{ a_1, \dots, a_m \}$.