# Mean Value Theorem

We continue [[Extreme Values|previous efforts]] to prove properties about continuous functions over a closed interval. In order to build up the foundations for the Mean Value Theorem, we first establish that continuous functions are integratable over the interval.

## Integratability

We begin by establishing the small span theorem, which states that we can choose an arbitrarily small sub-interval such that its **span** is less than some $\epsilon$. This allow us to construct two step functions which approximate some function and show that it can be integrated.

> [!abstract] Small Span Theorem
> Suppose $f$ is continuous over a closed interval $[a, b]$. By [[Extreme Values#Extreme Value Theorem]], $f$ has an absolute maximum and minimum. We define the **span** of $f$ over $[a, b]$ as
> $$
> \text{Span} \; f = \max(f) - \min(f)
> $$
>> Not to be confused with the Linear Algebra "Span"
>
> For every $\epsilon \gt 0$ there is a sub-interval of $[a, b]$ such that $\text{Span} \; f \lt \epsilon$.
>
> Proof.
> We once again assume no such sub-interval can be constructed and proceed by successive bisections on $[a, b]$. Assume there is some $\epsilon_0$ such that $\text{Span} \; f \geqslant \epsilon_0$. Continue the bisection process as before and assume without loss of generality that the left sub-interval contains the minimum span at each stage of the process. Let $S$ be the set of left endpoints of each sub-interval and $\alpha = \sup S$. By continuity of $f$, there exists an interval about $\alpha$, $(\alpha - \delta, \alpha + \delta)$ such that $\text{Span} \; f \; \lt \epsilon_0$. Moreover, we know this interval about $\alpha$ is within $[a, b]$ whenever $\delta \lt \frac {b - a} {2^n}$, contradicting the assumption that the span of $f$ was at least $\epsilon_0$ over $[a, b]$.
>
> $\blacksquare$

We can now use the small span theorem to prove that $f$ is integratable.

> [!abstract] Theorem (3.14)
> If $f$ is continuous on $[a, b]$, then it is integratable on $[a, b]$.
>
> Proof.
> Since $f$ is bounded on $[a, b$, we know it has upper and lower integrals $\underline I = \int_a^b f(x) \; dx$, and $\overline I = \int_a^b f(x) \; dx$. Choose an arbitrary positive integer $N$ and let $\epsilon = \frac 1 N$. By the small span theorem, we may construct a partition of $[a, b]$ such that the span of $f$ in each of $n$ sub-intervals is less than our choice of $\epsilon$. Denote the endpoints of such intervals by $\min(f_k), \max(f_k)$, respectively, for $1 \leqslant k \leqslant n$ and notice
> $$
> \max(f_k) - \min(f_k) \lt \epsilon
> $$
> Define step functions, $s, t$ as follows:
> $$
> \begin{align}
> &s_n(x) = \min(f(x)) \; \text{if} \; x_{k-1} \lt x \leqslant x_{k+1} \\
> &t_n(x) = \max(f(x)) \; \text{if} \; x_{k-1} \leqslant x \lt x_{k+1}
> \end{align}
> $$

> [!todo]
> Do the rest of the boring algebra later

## Mean Value Theorem

We now have everything set up to prove the mean value theorem. We want to show that a continuous function $f$ is equal to its average at some point over the interval.

> [!abstract] Mean Value Theorem
> If $f$ is continuous on $[a, b]$, then for some $c \in [a, b]$ we have
> $$
> f(c) = \frac 1 {b - a} \int_a^b f(x) \; dx \iff (b-a)f(c) = \int_a^b f(x) \; dx
> $$
>
> Proof.
> By the [[Extreme Values#Extreme Value Theorem]], we know that $f$ has a maximum and minimum on $[a, b]$. Let $m = \min(f)$ and $M = \max(f)$ on the interval and write:
> $$
> \begin{align}
> &\int_a^b m \; dx \leqslant \int_a^b f(x) \; dx \leqslant \int_a^b M \; dx \\ \\
> &= m(b-a) \leqslant \int_a^b f(x) \; dx \leqslant M(b-a) \; dx \\ \\
> &= m \leqslant \frac 1 {b-a} \int_a^b f(x) \; dx \leqslant M
> \end{align}
> $$
> So clearly the arithmetic mean of $f$ lies between its maximum and minimum and the proof is complete.
>
> $\blacksquare$