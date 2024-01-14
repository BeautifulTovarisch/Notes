# Integrals of more General Functions

We can now extend the [[Step Functions#Definite Integral of a Step Function]] definition to other functions by using two step functions to approximate.

## Approximation using Step Functions

For a given function $f$, we choose arbitrary step functions $s, t$ such that we can apply the [[Area as a Set Function#Axiomatic Definition of Area]] to show that $f$ is integratable.

- Choose a step function $s$ to be below $f$
- Choose a step function $t$ to be above $f$
- By comparison theorem, $\int_a^b s < \int_a^b t$
- Likewise, $\int_a^b f$ must fall between the integrals of $s$ and $t$.

> [!warning]
> The above procedure can only be applied for **bounded** functions.

## Definition of the Integral of a Bounded Function

Let $f$ be bounded and defined on interval $[a, b]$. Let $s, t$ denote arbitrary step functions defined on $[a, b]$ such that $s(x) \leqslant f(x) \leqslant t(x)$ for all $x \in [a, b]$. If there is exactly one number $I$ such that $\int_a^b s(x) \; dx \leqslant I \leqslant \int_a^b t(x) \; dx$, then $I = \int_a^b f(x) \; dx$ and we say that $f$ is integratable on $[a, b]$.

## Integratability of Bounded Monotonic Functions

Here we go through a rigorous proof using the above definition and properties of monotonicity to show that the upper and lower integrals are equal and equal to that of a function $f$.

> [!abstract] Theorem
> If $f$ is monotonic on $[a, b]$, then $f$  is integratable on $[a, b]$.
>
> Proof.
> Assume $f$ is increasing everywhere on $[a, b]$. We must show $\underline I(f) = \overline I(f)$. Let $P = \{x_0, x_1, \dots, x_n \}$ partition $[a, b]$ into equal subintervals, that is, of size $\frac {b - a} n$. Define step functions $s(x) = f(x_{k-1})$ and $t(x) = f(x_k)$ (because $f$ is increasing and by the comparison theorem, $s(x) \leqslant t(x)$ everywhere on $[a, b]$).
>
> Now consider
> $$
> \begin{align}
> \int_a^b t - \int_a^b s &= \sum_{k=1}^n f(x_k) (x_k - x_{k-1}) - \sum_{k=1}^n f(x_{k-1}) (x_k - x_{k-1}) \\
> &= \frac {b-a} n \sum_{k=1}^n f(x_k) - f(x_{k-1}) \\
> &= \frac {b-a} n (f(b) - f(a))
> \end{align}
> $$
>
> Now let $C = (b-a)(f(b) - f(a))$ and so sum of areas is $\frac C n$. Thus
> $$
> \begin{align}
> &\int_a^b s \leqslant \underline I(f) \leqslant \int_a^b t &\text{(i)} \\
> &\int_a^b s \leqslant \overline I(f) \leqslant \int_a^b t &\text{(ii)}
> \end{align}
> $$
>
> Multiplying $(i)$ by -1 and adding the result to $(ii)$ we have
> $$
> \begin{align}
> &\overline I(f) - \underline I(f) \leqslant \int_a^b t - \int_a^b s \\
> &\implies 0 \leqslant \overline I(f) - \underline I(f) \leqslant \frac C n \\
> &\implies \overline I(f) = \underline I(f) &\text{Archimedes}
> \end{align}
> $$
>
> Thus, we have shown $f$ is integratable on $[a, b]$. The proof for a decreasing function is nearly identical. $\blacksquare$

## Calculation of the Integral of a Bounded Monotonic Function

We now prove that the definition of the integral is the unique number "contained" between the approximating step functions. This proof follows almost immediately of the discover in the latter half of the previous proof in which we showed that $I$ was bounded by approximating step functions.

> [!abstract] Theorem.
> Assume $f$ is increasing over an interval $[a, b]$ and let $x_k = a + \frac {k(b-a)} n$ (the interval formed by $a$ and the $kth$ sub-interval of $[a, b]$) where $k \in \mathbb{N}$. If $I$ is any number such that:
> $$
> \frac {(b-a)} n \sum_{k=0}^{n-1} f(x_k) \leqslant I \leqslant \frac {(b-a)} n \sum_{k=1}^{n} f(x_k)
> $$
>
> Then $f$ is integratable on $[a,b]$ and $I = \int_a^b f(x) \; dx$.
>
> Proof.
> Let $s, t$ be approximating step functions as defined in the [[Integrals of more General Functions#Integratability of Bounded Monotonic Functions]] proof.  Then we know that $\int_a^b s \leqslant I \leqslant \int_a^b t$. But then by definition $I$ is a number that satisfies the inequality and following the same conclusion, we see that $I = \int_a^b f(x) \; dx$ $\blacksquare$