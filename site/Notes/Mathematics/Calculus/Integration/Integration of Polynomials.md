# Integration of Polynomials

We use the [[Integrals of more General Functions#Calculation of the Integral of a Bounded Monotonic Function]] to prove an important result which will lead to us being able to integrate arbitrary polynomials.

## Definite Integral of $x^p$

We know that the integral exists because $x^p$ is bounded and increasing when $p > 0$. We can use a property of power functions to produce step functions allowing us to compute the integral of $x^p$.

> [!note]
> The following proof uses an analytical finding from the introduction section of the book.

> [!abstract]
> Theorem.
> If $p \in \mathbb{Z}^+$, then $\int_a^b x^p \; dx = \frac {b^{p+1}} {p+1}$.
>
> Proof.
> Notice that by the previous theorem,
> $$
> \sum_{k=1}^{n-1} k^p \leqslant \frac {n^{p+1}} {p+1} \leqslant \sum_{k=1}^{n} k^p, \; n \geqslant 1
> $$
> Multiplying by $\frac {b^{p+1}} {n^{p+1}}$ we get:
> $$
> \begin{align}
> &\frac {b^{p+1}} {n^{p+1}} \sum_{k=1}^{n-1} k^p \leqslant
> \frac {b^{p+1}} {p+1} \leqslant
> \frac {b^{p+1}} {n^{p+1}} \sum_{k=1}^{n} k^p, \; \\
> & \frac b n \sum_{k=1}^{n-1} \left(\frac {bk} {n}\right)^p \leqslant
> \frac {b^{p+1}} {p+1} \leqslant
> \frac b n \sum_{k=1}^{n} \left(\frac {bk} {n}\right)^p \\
> & \frac b n \sum_{k=1}^{n-1} f(x_k) \leqslant
> \frac {b^{p+1}} {p+1} \leqslant
> \frac b n \sum_{k=1}^{n} f(x_k)
> \end{align}
> $$
>
> Where in the final step we let $f(x) = x^p$ and $x_k = \frac {kb} n$. So then by the previous theorem we have $I = \frac {b^{p+1}} p+1 = \int_a^b x^p \; dx$ since it satisfies the desired inequality.
> $\blacksquare$

## Integration of Arbitrary Polynomials

Recall that a polynomial is defined

$$
\sum_{k=0}^n c_k \cdot x^k = c_0 x^0 + c_1 x^1 + \dots + c_n x^n
$$

but then by application of linearity and the previous result showing the integral of $x^p$, we can simply integrate the terms of polynomial independently.

First notice that by additivity of the interval of integration:

$$
\begin{align}
\int_a^b x^p \; dx &= \int_0^b x^p \; dx - \int_0^a x^p \; dx &[0, b] = [0, a] + [a, b] \\
&= \frac {b^{p+1} - a^{p+1}} {p+1} \\
&= \left. \frac {x^{p+1}} {p+1} \right|_a^b &\text{$\int_a^b x^p$}
\end{align}
$$

> [!example]
> $$
> \begin{align}
> \int_1^3 x^2 - 3x + 5 \; dx &=
> \left. [\frac {x^3} 3 - \frac 3 2 x^2 + 5x] \right|_1^3 \\
> &= \frac {3^3 - 1^3} {3} - \frac 3 2 (3^2 - 1^2) + (5(3) - 5(1)) \\
> &= \frac {26} 3 - 2 \\
> &= \frac {20} 3
> \end{align}
> $$

![[polynomial-integral.svg]]
> Area under the curve of $x^2 - 3x + 5$