# Polynomial Approximation

Polynomials exhibit properties which often make them easier to deal with than other functions (as was the case for [[Polynomial Approximation of the Logarithm]]. In particular, we may use polynomials of arbitrary degree to approximate the value of other types of functions whose computation may be difficult.

## Background

The objective is to find a polynomial $P$ such that for some differentiable function $f$ we have:

$$
P(0) = f(0), P'(0) = f'(0), \dots, P^{(n)}(0) = f^{(n)}(0)
$$

In other words, the function $f$ and polynomial $P$ agree for at least $n$ derivatives.

### The Exponential Function

We use the [[The Exponential Function]] as a starting point because $(e^x)' = e^x$ for all $n$. Therefore, we notice that $e^0 = (e^x)'(0) = 1$ always. Our task is to find a polynomial with similar properties.

Start by considering the polynomial $P(x) = 1 + x$, specifically chosen since $P(0) = 1 = e^0$ and $P'(0) = 1 = (e^x)'(0)$. Following this pattern, we choose:

$$
P(x) = c_0 + c_1x + c_2x^2 \dots + c_nx^n
$$

and work out a general form for the summation:

$$
\begin{array}{c c c}
P(0) = c_0 &\iff& f(0) = c_0 \\
P'(0) = c_1 &\iff& f'(0) = c_1 \\
P''(0) = 2c_2 &\iff& \frac {f''(0)} 2 = c_2 \\
P'''(0) = 6c_3 &\iff& \frac {f'''(0)} {3!} = c_3 \\
&\dots \\
P^{(n)}(0) = n!c_n &\iff& \frac {f^{(n)}(0)} {n!} = c_n \\
\end{array}
$$

Thus we have for each coefficient in $P(x)$

$$
c_k = \sum_{k=0}^n \frac {f^{(n)}} {n!}
$$

Therefore, we arrive at:

$$
P(x) = \sum_{k=0}^n \frac {f^{(n)}} {n!} x^k
$$

We call such a polynomial a [[Taylor Polynomial]].

> [!tip]
> I like to think of starting with $1 + x$ and repeatedly integrating (e.g $\int 1 + x \; dx = C + x + \frac {x^2} 2$ where $C = 1$) in order to increase the "precision" of the approximation.