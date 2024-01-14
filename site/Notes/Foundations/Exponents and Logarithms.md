# Exponents and Logarithms

Exponentiation is defined as repeated multiplication of some base. We denote "x raised to the yth power" as $x^y$.

## Exponent Laws

Laws used in the manipulation of expressions that contain exponents. We use these to demonstrate the logarithmic identities below.

- $x^0 = 1$
- $(ab)^y = a^yb^y$
- $(\frac a b)^n = \frac {a^n} {b^n}$
- $x^a * x^b = x^{a + b}$
- $(x^a)^b = x^{ab}$
- $\frac {x^a} {x^b} = x^{a-b}$
- $x^{-n} = \frac 1 {x^n}$

> [!abstract] Equality of Powers
> For $a \neq 1$ and $x,y \in \mathbb{R}$ we have
> $$
> a^x = a^y \implies x = y
> $$
>
> Proof.
> We use the fact that the power function is strictly monotonic. If $a$ is 0 or 1, then the proposition is vacuously true. Assume without loss of generality that $a \gt 1$ and $a^x = a^y$. Further suppose $x \neq y$ by way of contradiction. Then by cases of inequality, we must have either $x \lt y$ or $x \gt y$.
>
> Suppose $x \lt y$. Since the power function is strictly increasing for $a \gt 1$ we have $a^x < a^y$, contradicting our assumption that $a^x = a^y$. Similarly, for $x \gt y$ we arrive at $a^x \gt a^y$. Hence in both cases we have a arrived at a contradiction and so $x$ must equal $y$.
>
> $\blacksquare$

## Logarithmic Identities

In all of the identities below, assume $a \neq 1$ and the inputs to the log function are positive reals (logarithms are undefined for $x \leqslant 0$).

> [!info] Logarithm
> For a given base $a$ and positive real $y$, if $\log_a x = y$ we say that $a^y = x$. In other words, $\log_a x$ is the power to which $a$ must be raised to equal $x$.

Some important logarithmic identities follow from the application of the exponent laws:

> [!abstract] Identity
> Despite the awkward notation, taking the logarithm with base $a$ of $a^x$ is trivially shown to be $x$.
> $$
> \log_a a^x = x
> $$
> This follows directly from the definition of logarithm, but we prove it anyway.
>
> Proof.
> If $\log_a a^x = y$ then $a^y = a^x$. So by equality of powers $x = y$.
>
> $\blacksquare$

> [!abstract] Scalar Multiplication
> $$
> c \log_a x = \log_a x^c
> $$
>
> Proof.
> See that $\log_a x = y$ and $\log_a x^c = z$ implies that $a^y = x$ and $a^z = x^c$. Then $(a^y)^c = a^z$ and by equality of powers $cy = z$. But then $cy = c \log_a x = z = \log_a x^c$.
>
> $\blacksquare$

> [!abstract] Addition
> $$
> \log_a x + \log_a y = \log_a xy
> $$
>
> Proof.
> Notice that if $\log_a x = c$ and $\log_a y = d$, then $a^c = x, a^d = y$. But then $xy = a^c \cdot a^d = a^{c + d}$ by exponent laws. By definition of the logarithm, we have $\log_a xy = c + d = \log_a x + \log_a y$.
>
> $\blacksquare$

> [!abstract] Subtraction
> $$
> \log_a x - \log_a y = \log \frac x y
> $$
>
> Proof.
> We provide two proofs for the subtraction of logarithms. The first is a direct application of the exponent laws and the second uses the previously shown identities of logarithms.
>
> 1. Suppose $\log_a x = c$ and $\log_a y = d$. Then $a^c = x$ and $a^d = y$, hence $\frac x y = \frac {a^c} {a^d} = a^{c - d}$. But then by definition of the log function $\log_a \frac x y = c - d = \log_a x - \log_a y$. $\blacksquare$
> 2. Notice that $\log_a x - \log_a y = \log_a x + -\log_a y$. By scalar multiplication and the addition rule we have $\log_a x + \log_a y^{-1} = \log_a xy^{-1} = \log_a \frac x y$. $\blacksquare$

> [!abstract] Change of Base
> This identity allows the computation of a log given an arbitrary base by using a known logarithm.
> $$
> \log_a c = \frac {\log_b c} {\log_b a}
> $$
>
> Proof.
> See that $\log_a c = x$ $\log_b a = y$ and so $a^x = c, \; b^y = a$ and so $a^x = b^{xy} = c$. Now if $b^{xy} = c$, then $\log_b c = xy$ so we have
> $$
> \log_b c = \log_a c \cdot \log_b a \\
> \iff \log_a c = \frac {\log_b c} {\log_b a}
> $$
>
> $\blacksquare$