We can use certain polynomials to approximate the value of the logarithm to an arbitrary precision. Via a series of substitutions, we can obtain an approximation which contains an integral and error component.

## Motivating Example

We begin with a simple substitution:

$$
\log(x) \to \log(1 - x) = \int_1^{1-x} \frac 1 t \; dt
$$

Letting $u = 1 - t, du=-dx$, we have:

$$
\begin{align}
\log(1-x) &= \int_1^{1-x} \frac 1 t \; dt \\ \\
&= -\int_{u(1)}^{u(1-x)} \frac 1 {1 - u} \; du  \\ \\
&= -\log(1-x)
\end{align}
$$

From $(1 - u^2)$, we get

$$
\begin{align}
(1 - u^2) &= (1 + u)(1 - u) \\ \\
\implies \frac 1 {1 - u} &= \frac {1 + u} {1 - u^2} = 1 + u + \frac {u^2} {1 - u}
\end{align}
$$

Thus we have:

$$
-log(1-x) = x + \frac {x^2} 2 + \int_0^x \frac {u^2} {1-u} \; dx
$$

We can generalize this process to an arbitrary level of precision based on the degree of the polynomial.

## Polynomial Component

In the previous example, we arrived at the term: $x + \frac {x^2} 2$, which is a polynomial of degree 2. For more precise approximations, we may take this polynomial to an arbitrary degree $n$.

>[!abstract] Theorem
> Let $P_n(x)$ denote the polynomial:
> $$
> P_n(x) = x + \frac {x^2} 2 + \frac {x^3} 3 + \dots + \frac {x^n} n
> $$
>
> Then for every $x \gt 1, n \geqslant 1$ we have:
> $$
> -\log(1-x) = P_n(x) + \int_0^x \frac {u^n} {1-u} \; du
> $$
>
> Proof.
> Starting with the identity:
> $$
> \begin{align}
> \frac {1-u^n} {1-u} &= 1 + u + u^2 + \dots + u^{n-1} \\ \\
> &= \frac 1 {1-u} - \frac {u^n} {1-u} \\ \\
> &\implies \frac 1 {1-u} = 1 + u + u^2 + \dots + u^{n-1} + \frac {u^n} {1-u}
> \end{align}
> $$
>
> Taking the integral with $u = 1-x$, we have:
> $$
> \int_0^x \frac 1 {1-x} \; du = -\log(1-x) = x + \dots \frac {x^n} n + \int_0^x \frac {u^n} {1-u} \; dx = P_n(x) + \int_0^x \frac {u^n} {1-u} \; du
> $$
>
> $\blacksquare$

## Error Component

We can denote the integral $\int_0^x \frac {u^n} {1-u} \; du$ by a function representing the error. Let $E_n(x) = \int_0^x \frac {u^n} {1-u}$.  We would like to know the sign and the size of this error in general.

> [!abstract] Theorem
> Let $E_n(x) = \int_0^x \frac {u^n} {1-u} \; du$. Then we have:
>
> 1. If $0 \lt x \lt 1$
> $$
> \frac {x^{n+1}} {n+1} \leqslant E_n(x) \leqslant \frac 1 {1-x} \frac {x^{n+1}} {n+1}
> $$
>
> 2. If $x \lt 0$, then $E_n(x)$ has the same sign as $(-1)^{n+1}$ and
> $$
> 0 \lt (-1)^{n+1} E_n(x) \leqslant \frac {|x|^{n+1}} {n+1}
> $$
>
> Proof.
> Assume $0 \lt x \lt 1$. We have $0 \leqslant u \leqslant x$ (todo: determine why) and so $1-x \leqslant 1 -u \leqslant 1$


## Program to Approximate the Natural Logarithm

```python
def naturalLog(x, m):
	'''
	naturalLog(x, m) estimates the ln(x) by polynomial approximation.

	Parameters:
		x (float): An arbitrary postive real
		m (int): The degree of the polynomial used to approximate ln(x)

	Output:
		(lower, upper) (float, float): Bounds such that

			lower < ln(x) <= upper
	'''
	c = (1+x) / (1-x)

	def approx(c):
		# Compute the integral of a polynomial of degree [m]:
		s = sum([(c ** i) / i for i in range(1, 2*m, 2)])

		power = (2 * m) + 1
		lower = (x ** power) / power

		upper = (2-x)*(1-x) * lower

		return (s + lower, s + upper)

	return approx(c)
```