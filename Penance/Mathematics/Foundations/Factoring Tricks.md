Clever factorization of ugly polynomials can help reduce a problem into something that's more manageable (or possible).

## Basic Identities

These should become second nature. Often the solution to an inscrutable problem involves recognizing the expanded form of a basic identity.

$$
\begin{align}
&(a + b)^2 = a^2 + 2ab + b^2 &\text{Square of Sum} \\ \\
&(a - b)^2 = a^2 - 2ab + b^2 &\text{Square of Difference} \\ \\
&(a^2 - b^2) = (a + b)(a - b) &\text{Difference of Squares} \\ \\
&(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3 &\text{Cube of Sum}
\end{align}
$$

### Splitting Apart a Monomial

There is not necessarily a recognizable pattern to when this trick might work, however it's straightforward and easy to attempt:

$$
\begin{align}
a^4 + 2a^2b^2 + b^4 &= a^4 + a^2b^2 + b^4 + a^2b^2 \\
&= a^2(a^2 + b^2) + b^2(a^2 + b^2) \\
&= (a^2 + b^2)^2
\end{align}
$$

Other situations arise when a monomial is "very close" to being factored evenly.

### Adding Zero

This trick is wildly useful and applicable in various scenarios throughout all of mathematics. Several factoring tricks arise from adding back "annihilated terms" to a polynomial.

$$
\begin{align}
x^5 + x + 1 &= x^5 + x^4 + x^3 + x^2 - x^4 - x^3 - x^2 + 1 \\
&= x^3(x^2 + x + 1) - x^2(x^2 + x + 1) + x^2 + x + 1 \\
&= (x^3 - x^2 + 1)(x^2 + x + 1)
\end{align}
$$

## $(a^n - b^n)$

We build up to the general solution by considering a few concrete examples. Notice the repeated use of adding back the annihilated terms.

$$
\begin{align}
a^3 - b^3 &= a^3 + a^2b + ab^2 - a^2b - ab^2 - b^3 \\
&= (a^3 - a^2b) + (a^2b - ab^2) + (ab^2 - b^3) \\
&= a^2(a - b) + ab(a - b) + b^2(a - b) \\
&= (a-b)(a^2 + ab + b^2) \\ \\
a^4 - b^4 &= a^4 + a^3b + a^2b^2 + ab^3 - a^3b - a^2b^2 - ab^3 - b^4 \\
&= (a^4 - a^3b) + (a^2b^2 - ab^3) + (a^3b - a^2b^2) + (ab^3 - b^4) \\
&= a^3(a - b) + ab^2(a - b) + a^2b(a - b) + b^3(a - b) \\
&= (a - b)(a^3 + a^2b + ab^2 + b^3)
\end{align}
$$

Generalizing, we have:

$$
\begin{align}
a^n - b^n = (a - b)(a^{n-1} + a^{n-2}b + \dots + ab^{n-2} + b^{n-1})
\end{align}
$$

> [!tip]
> An extremely common situation is when $b = 1$:
>
> $$
> a^n - 1 = a^n - 1^n = (a - 1)(a^{n-1} + a^{n-2} + \dots + 1)
> $$

## $(a^n + b^n)$ and $n$ is odd

Here we can simply substitute $(-b)$ in the formula for $a^n - b^n$ since the sign preserved for odd powers. We'll do the derivation the hard way for posterity beginning with some helpful examples. Once again we employ the "add zero" trick:

$$
\begin{align}
(a^3 + b^3) &= a^3 + a^2b + ab^2 - a^2b - ab^2 + b^3 \\
&= (a^3 + a^2b) + (-a^2b - ab^2) + (ab^2 + b^3) \\
&= a^2(a + b) + (-ab)(a + b) + b^2(a + b) \\
&= (a + b)(a^2 - ab + b^2) \\ \\
(a^5 + b^5) &= a^5 + a^4b + a^3b^2 + a^2b^3 + ab^4 - a^4b - a^3b^2 - a^2b^3 - ab^4 + b^5 \\
&= (a^5 + a^4b) + (-a^4b - a^3b^2) + (a^3b^2 + a^2b^3) + (-a^2b^3 - ab^4) + (ab^4 + b^5) \\
&= a^4(a + b) (-a^3b)(a + b) + a^2b^2(a + b) + (-ab^3)(a + b) + b^4(a + b) \\
&= (a + b)(a^4 - a^3b + a^2b^2 - ab^3 + b^4)
\end{align}
$$

Generalizing, we have:

$$
(a^n + b^n) = (a + b)(a^{n-1} - a^{n-2}b + a^{n-2}b^2 - \dots - ab^{n-2} + b^{n-1})
$$

## $(a^{2n} + b^{2n})$

> [!warning]
> The following derivation holds for all except $a^2 + b^2$ under $\mathbb{R}$ (since we do not wish to involve the complex field for now.)

We can break $2n$ down into cases of $n$ being even or odd and apply a previous rule. The general idea is to recognize that $2n$ can be reduced into one of the two forms above.

### $n$ is Odd

Some examples. To make them a little easier to follow, we've used $u$ and $v$ to abstract over the term being raised to the desired power.

> [!tip]
> This is also a useful integration technique in Calculus, and in general for focusing on the broader structure of a problem.

$$
\begin{align}
(a^6 + b^6) &= (a^2)^3 + (a^2)^3 \\
&= (u^3 + v^3) &(u = a^2, v = b^2) \\
&= (u + v)(u^2 - uv + v^2) &(a^3 + b^3) \\
&= (a^2 + b^2)(a^4 - a^2b^2 + b^4) \\ \\
(a^{10} + b^{10}) &= (a^2)^5 + (a^2)^5 \\
&= (a^2 + b^2)(a^4 - a^3b + a^2b^2 - ab^3 + b^4)
\end{align}
$$

Thus we see the general pattern:

$$
(a^{2n} + b^{2n}) = (a^2 + b^2)(a^{n-1} - a^{n-2}b + a^{n-3}b^2 + \dots - ab^{n-2} + b^{n-1})
$$

### $n$ is Even

When $n$ is even, we want to find some monomial we can square and then take to the $n$th power. The reason for this is so we can reduce the problem into a difference of squares.

$$
\begin{align}
(a^4 + b^4) &= a^4 + 2a^2b^2 + b^4 - 2a^2b^2 \\
&= (a^2 + b^2)^2 - 2a^2b^2 &(a + b)^2 = a^2 + 2ab + b^2 \\
&= (a^2 + b^2)^2 - (\sqrt 2 ab)^2 \\
&= (a^2 + b^2 + \sqrt2 ab)(a^2 + b^2 - \sqrt 2 ab) &\text{Difference of Squares} \\
(a^8 + b^8) &= a^8 + 2a^4b^4 + b^8 - 2a^4b^4 \\
&= (a^4 + b^4)^2 - (\sqrt 2 a^2b^2)^2 \\
&= (a^4 + b^4 + \sqrt2 a^2b^2)(a^4 + b^4 - \sqrt 2 a^2b^2)
\end{align}
$$

And so in general we have

$$
(a^{2n} + b^{2n}) = (a^{2n} + b^{2n} + \sqrt2 (a^n)(b^n))(a^{2n} + b^{2n} - \sqrt 2 (a^n)(b^n))
$$