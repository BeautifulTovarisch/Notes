Expressions of the form $ax^2 + bx + c$ are called **quadratic**. The graph of a quadratic expression is called a parabola. Often times we're interested in values of $x$ (roots) for which the expression equals zero.

> [!info] Quadratic Expression
> An expression of the form $ax^2 + bx + c$ where $a \neq 0$. We say an equation of the form $x^2 + px + q$ is a **reduced quadratic**.

## Finding Roots of a Quadratic Equation

Solving an equation, $ax^2 + bx + c = 0$ is often referred to as finding the roots of the quadratic. This technique is widely used to reason about problems that are modeled nicely by quadratic equations. Several techniques are available to us:

### Factoring

From the factor theorem, we know that a polynomial of degree 2 has at most two roots and can be represented as:

$$
P(x) = (x - \alpha)(x - \beta)
$$

Clearly, when $x$ is equal to one of its roots, then the equation is zero.

> [!example]
> $x^2 - 4 = (x - 2)(x + 2) = 0 \iff x = \pm 2$

[[Factoring Tricks]] are incredibly helpful here.

### Completing the Square

If we have a **reduced quadratic** equation, we can manipulate the expression by noticing:

$$
\begin{align}
x^2 + px + q &=
x^2 + 2 * \frac p 2 x + (\frac p 2)^2 - \frac {p} {2}^2 + q \\
&= (x + \frac p 2)^2 - (\frac p 2)^2 + q &(a + b)^2 \\
&\implies (x + \frac p 2)^2 = (\frac p 2)^2 - q
\end{align}
$$

We observe some results that arise from the value of $(\frac p 2)^2 - q$:

- $(\frac p 2)^2 - q > 0 \implies 2 \; \text{solutions}$
- $(\frac p 2)^2 - q = 0 \implies x = -\frac p 2$
- $(\frac p 2)^2 - q > 0 \implies \; \text{no solutions}$



> [!example]
> $$
> \begin{align}
> x^2 - 14x + 9 &=
> (x^2 - 7x - 49) - 49 - 9 \\
> &= (x - 7)^2 - 40 \\
> &= (x - 7 \pm \sqrt 40) &\text{Difference of Squares}
> \end{align}
> $$

### Vieta's Theorem

A theorem that follows naturally from the technique of completing the square lets us discover the relationship between the roots of an equation.

> [!abstract] Vieta's Theorem
> If a quadratic expression $x^2 + px + q$ has distinct roots $\alpha, \beta$, then
>
> $$
> \begin{align}
> &\alpha + \beta &= -p \\
> &\alpha \beta &= -q
> \end{align}
> $$
>
> **Corollary**
> If $x^2 + px + q$ has two distinct roots $\alpha, \beta$ then $x^2 + px + q = (x - \alpha)(x - \beta)$. This follows from the fact that:
> $$
> (x - \alpha)(x - \beta) = x^2 - (\alpha + \beta)x + \alpha \beta
> $$
>
> Proof (Theorem):
> Consider the equation $x^2 + px + q = 0$. Completing the square, we discover roots $\alpha, \beta$ such that (without loss of generality) $\alpha = -\frac p 2 + \sqrt{\frac {p^2} 4 - q}$ $\beta = -\frac p 2 - \sqrt{\frac {p^2} 4 - q}$. Hence, letting $D = \frac {p^2} 4 - q$:
> $$
> \begin{align}
> \alpha + \beta &= -\frac p 2 + -\frac p 2 + \sqrt D - \sqrt D &= -p \\ \\
> \alpha \beta &= (-\frac p 2 + \sqrt D)(-\frac p 2 - \sqrt D) \\
> &= -\frac {p^2} 4 + D \\
> &= -\frac {p^2} 4 + \frac {p^2} 4 - q \\
> &&= -q \\ \\
> &&\blacksquare
> \end{align}
> $$
>
> Proof (Corollary):
> By factor theorem, if $\alpha, \beta$ are roots of $P(x)$ (having degree at most two), then $P(x) = x^2 + px + q = (x - \alpha)(x - \beta)Q(x)$. Now since $P$ has degree at most two, $Q$ must have be a constant, and since the coefficients of $P$ are unmodified by $Q$, it must be equal to one. Hence, $(x - \alpha)(x - \beta) = x^2 - (\alpha + \beta) + \alpha \beta = x^2 + px + q$.
>
> $\blacksquare$

> [!todo]
> State and prove an extension of Vieta's theorem for cubic equations.

### The Quadratic Formula

We consider equations of the form $ax^2 + bx + c$. We can use the technique of completing the square and a little algebraic manipulation to arrive at a concrete formula for finding roots:

$$
ax^2 + bx + c = x^2 + \frac b a x + \frac c a
= x^2 + px + q
\; \text{where} \; p = \frac b a, q = \frac c a
$$

$$
\begin{align}
x &= - \frac b {2a} \pm \sqrt{\frac {b^2} {4a^2} - \frac c a } \\
&= - \frac b {2a} \pm \sqrt {\frac {b^2 - 4ac} {4a^2}} \\
&= - \frac b {2a} \pm \frac {\sqrt {b^2 - 4ac}} {2a} \\
&= - \frac {-b \pm \sqrt {b^2 - 4ac}} {2a}
\end{align}
$$
