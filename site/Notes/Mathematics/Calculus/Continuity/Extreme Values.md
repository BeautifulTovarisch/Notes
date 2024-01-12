# Extreme Values

We can use the [[Values of Continuous Functions#Intermediate Value Theorem]] to show that a continuous function is bounded and always contains an absolute maximum and minimum along a given interval. This lets us establish that such a function is integratable and leads to a helpful technique for estimating the integral of certain products of functions.

## Extrema

We introduce the notion of an **absolute maximum** (and minimum), which we then prove are guaranteed to exist.

> [!info] Absolute Maximum
> A real-valued function $f$ defined over $[a, b]$ is said to have an **absolute** maximum if there is at least one point $c \in [a, b$ such that
> $$
> \forall x \in [a, b], \; f(x) \leqslant f(c)
> $$

## Bounded Functions

First we establish that a continuous function over a closed interval must be bounded, that is:

> [!info] Bounded Function
> A function $f$ over $[a, b]$ is bounded if and only if there is some constant, say, $C$ such that $|f(x)| \lt C$ for all $x \in [a, b]$.

To show that a continuous function is bounded, we use a proof technique called **successive bisection** in which we repeatedly half the intervals of $[a, b]$ and show that eventually the $nth$ sub-interval must exhibit some desired property.

> [!abstract] Boundedness of a Continuous function on $[a b]$
> Let $f$ be continuous over a closed interval $[a, b]$. Then $f$ is bounded on $[a, b]$. In other words, there exists a constant $c \in [a, b]$ such that $|f(x)| \lt c$.
>
> Proof.
> Assume $f$ is unbounded over the interval. We proceed by successive bisections on $[a, b]$ in order to demonstrate a contradiction. Let $c$ be the midpoint of $[a, b]$. Without loss of generality, assume $f$ is unbounded on "left" bisection, $[a, c]$.
>
> Continue the procedure until the $nth$ subdivision, denoted $[a_n, b_n]$ and notice that $c_n = \frac {b - a} {2^n}$. Let $S$ be the set containing the left endpoints of each successive subdivision and let $\alpha = \sup S$. By continuity of $f$ there is an $n$ such that $|f(x) - f(\alpha)| \lt 1$ whenever $|x - \alpha| \lt c_n$ and so $f(\alpha) - 1 \lt f(x) \lt f(\alpha) + 1$, contradicting our assumption that $f$ was unbounded.
>
> $\blacksquare$

## Extreme Value Theorem

With the boundedness of a function established, we can use the concepts of suprema and infima to show that a continuous $f$ must take on these values within a closed interval.

>[!abstract] Extreme Value Theorem
> Assume $f$ is continuous on a closed interval $[a, b]$. Then there are points $c, d$ within $[a, b]$ such that
> $$
> f(c) = \sup f \; \text{and} \; f(d) = \inf f
> $$
>
> Proof.
> Because $f$ is continuous, we know that it is bounded on $[a, b]$, and therefore has a supremum. It suffices to show that $f(c) = \sup f$ since $\inf f = \sup {-f}$. Assume by way of contradiction that there is no $x \in [a, b]$ such that $f(x) = M = \sup f$.
>
> Define $g(x) = M - f(x)$. We know that $g(x) \gt 0$ since by assumption no $f(x) = M$ and so the equality is strict, and so we may take the reciprocal, $\frac 1 g(x)$ to be defined and continuous over the interval. Thus, we have that $\frac 1 g$ is bounded by some $C \in [a, b]$.  But then we have that
> $$
> \frac 1 g \lt C \iff g \gt \frac 1 C \iff 0 \lt M - f(x) \gt \frac 1 C
> $$
> Rearranging the final inequality, we find that $f(x) \lt M - \frac 1 C$, contradicting the assumption that $f$ was unbounded.
>
> $\blacksquare$