# Integration to Compute the Average of a Function

A useful application of the definite integral is to compute the average of a function over an interval. The intuition behind the formula is to divide $f(x)$ into $n$ equal sub-intervals over $[a, b]$.

## Average Value of a Function over $[a, b]$

We suppose $f$ is a step function constant over $n$ equal sub-intervals and show that its arithmetic mean is equal to the integral of $f$ divided by the length of the interval.

> [!abstract] Average Value of a Function
> Suppose $f$ is a step function constant over $n$ equal sub-intervals of $[a, b]$. Then the average value of $f$ over $[a, b]$ is given by:
> $$
> \frac 1 n \sum_{k=1}^n f(x_k) = \frac 1 {b - a} \int_a^b f(x) \; dx
> $$
>
> Proof.
> Since $f$ is a step function, we have $f(x) = x_k$ if $x_{k-1} < x < x_k$. Let $x_k$ be the $k$-th sub-interval of $[a, b]$ given by $x_k = a + \frac {b -a} n \cdot k$ and notice that $x_k - x_{k-1} = \frac {b - a} n$. By definition of the integral of a step function we have:
> $$
> \begin{align}
> \frac 1 {b-a} \int_a^b f(x) \; dx &=
> \frac 1 {b-a} \sum_{k=1}^n f(x_k) (x_k - x_{k-1}) \\
> &= \frac 1 {b-a} \sum_{k=1}^n f(x_k) \frac {b-a} n \\
> &= \frac 1 n \sum_{k=1}^n f(x_k) \\ \\
> &&\blacksquare
> \end{align}
> $$

### Weighted Average

We can weight an average by computing the integral of the product of a weight function, $w(x)$, and $f(x)$ divided by the integral of $w(x)$

> [!todo]
> Find out why this is.

$$
\frac {\sum_{k=1}^n w_k a_k} {\sum_{k=1}^n w_k} =
\frac {\int_a^b w(x) f(x)} {\int_a^b w(x)}
$$

This has the implication that when all of $w_k$ are equal, we have the arithmetic mean.