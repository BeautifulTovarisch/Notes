# Applications of Integration

Computing the integral has applications for the calculation of:
- Area
- Work
- Averages, etc.

## Area of a Region between two Functions

In order to compute the integral of the region between two graphs, we simply apply subtract the ordinate set of the "lower" function from that of the "upper".

> [!abstract] Theorem (2.1)
> Assume $f, g$ are integrateable on $[a, b]$ and $f(x) \leqslant g(x)$. Then the region $S$ between their graphs is measurable and its area is given by $a(S) = \int_a^b [g(x) - f(x)] \; dx$.
>
> Proof.
> Assume without loss of generality that $f$ and $g$ are nonnegative (If a subset of the ordinate set is negative, we may simply translate $f$ and $g$ by some constant such that the area of the new functions is congruent). Let $G = ord(g), F = ord(f)$ and notice that $F \subseteq G$ and the region between $G$ and $F$ is given by $S = G - F$. But then by the difference axiom of area $S$ is measurable and its area is given by $a(S) = a(G) - a(F)$. By integratability of $f$ and $g$ we have $a(S) - \int_a^b g(x) \; dx - \int_a^b f(x) \; dx = \int_a^b [g(x) - f(x)] \; dx$.
>
> $\blacksquare$

### Area of a Circular Disk

We see that a circular disk can be thought of as the union of two graphs (and their ordinate sets), each giving the equation for a semicircle over $[-r, r]$:

$$
\begin{align}
g(x) &= \sqrt {r^2 - x^2} &\text{Upper Semicircle} \\
f(x) &= -\sqrt {r^2 - x^2} &\text{Lower Semicircle}
\end{align}
$$

We want to compute the area between $g$ and $f$, but (currently) lack the integration techniques to do so directly. Instead we notice the following:

$$
\begin{align}
\int_{-r}^r [g(x) - f(x)] &= \int_{-r}^r \sqrt {r^2 - x^2} \; dx +
\int_{-r}^r \sqrt {r^2 - x^2} \; dx \\
&= 2 \int_{-r}^r \sqrt {r^2 - x^2} \; dx \\
&= 2r \int_{-1}^1 \sqrt {r^2 - x^2 r^2} &\text {Contraction} \\
&= 2r^2 \int_{-1}^1 \sqrt {1 - x^2} \; dx &\text {Factoring $r^2$} \\
&= \pi r^2 &\text{Area of a unit circle be $\pi$} \\ \\
&&\blacksquare
\end{align}
$$

### Using Area to Compute an Integral

If we can compute the area under a curve geometrically, we can use this information in order to derive the integral.

> [!todo]
> Find a way to plot this.

> [!abstract] Theorem 2.2
> $\int_a^b x^{1/n} \; dx = \frac {b^{1/n + 1} - a^{1/n + 1}} {1/n + 1}$
>
> Do this proof later.
