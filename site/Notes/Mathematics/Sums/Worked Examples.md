We work through some example derivations using the techniques of [[Finite Calculus]].

## Natural Log

To develop a finite analog of $\int \frac 1 x = \ln(x) + C$, we need a function such that

$$
\sum_a^b x^{\underline -1} = \sum_a^b \frac 1 {x + 1} = \Delta f(x) = f(x + 1) - f(x)
$$

We can choose the Harmonic number: $H_n = \frac 1 1 + \frac 1 2 + \dots + \frac 1 n$, since

$$
\Delta(H_x) = H_{x+1} - H_x = (1 + \dots + \frac 1 {x+1}) - (1 + \dots + \frac 1 x) = \frac 1 {x+1}
$$

Thus we arrive at the full definition of a definite summation:

$$
\sum_a^b x^{\underline m} \; \delta x =
\begin{cases}
\frac {x^{\underline {m+1}}} {m+1}, &m \neq -1 \\ \\
H_x \mid_a^b, &m = -1
\end{cases}
$$

## Analog for $e^x$

To develop an analog for $\frac d {dx} e^x = e^x$ we must find a function such that $\Delta f(x) = f(x)$, thus

$$
\Delta f(x) = f(x)
\iff
f(x + 1) - f(x) = f(x)
\iff
f(x + 1) = 2 f(x)
$$

This defines a simple recurrence in which the next term is two times the previous, hence we can choose $f(x) = 2^x$ as our analog. We notice then,

$$
\Delta (2^x) = 2^{x+1} - 2^x = 2^x(2 - 1) = 2^x
$$

Determining functions such as these can help in dealing with more complicated analyses (such as Quicksort).

## Finite Summation by Parts

An integral like $\int xe^x$ is usually computed using a technique called "integration by parts" ($\int u DV = uv - \int v Du$). We develop a finite analog here, which will allow use to compute sums such as $\sum k2^k$ more easily.

> [!abstract] Theorem
> $$
> \sum u \Delta v = uv - \sum Ev \Delta u
> $$
>
> Proof.
> $$
> \begin{align}
> \Delta(u(x)v(x)) &= u(x+1)v(x+1) - u(x)v(x) \\ \\
> &= u(x+1)v(x+1) + u(x)v(x+1) - u(x)v(x+1) - u(x)v(x) \\ \\
> &= u(x)\Delta v(x) + v(x+1) \Delta u(x) \\ \\
> &= u(x)\Delta v(x) + Ev \Delta u(x)
> \end{align}
> $$
>
> Taking the summation of both sides and rearranging, we find:
> $$
> \sum \Delta(uv) = \sum u \Delta v + \sum Ev \Delta u \iff \sum u \Delta v = uv - \sum Ev \Delta u
> $$
>
> $\blacksquare$

> [!example]
> We can now return to the summation $\sum x 2^x$. Let $u = x, \; \Delta v = 2^k$. Then we have:
> $$
> \sum x 2^x = x 2^x - E2^x (1) = x 2^x - 2^{x+1} = 2^x(x - 2) + C
> $$
>
> Using the formula for the indefinite summation, we can find the definite sum by affixing upper and lower limits:
> $$
> \begin{align}
> \sum_{k=0}^n k2^k &= \sum_0^{n+1} x 2^x \; \delta x  \\ \\
> &= 2^x(x - 2) \mid_0^{n+1}  \\ \\
> &= 2^{n+1}(n - 1) - 2^0(-2) \\ \\
> &= 2^{n+1}(n - 1) + 2
> \end{align}
> $$

> [!example]
>