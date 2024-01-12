# Derivatives of Inverse Functions

We want to prove that the property of differentiability transfers to a function's inverse. Additionally, we prove that the derivative of a function is the reciprocal of the derivative of its inverse

> [!abstract] Differentiability of an Inverse
> Assume $f$ is strictly increasing and continuous on $[a, b]$ and let $g$ be the inverse of $f$. If $f'(x)$ exists and is nonzero at a point $x \in (a, b)$, then the derivative $g'(y)$ exists and is given by:
> $$
> g'(y) = \frac 1 {f'(x)}
> $$
>
> Proof.
> Assume $x \in (a, b)$ and $f'(x) \neq 0$. Let $y = f(x)$. We must show that
> $$
> \lim_{k \to 0} \frac {g(k + y) - g(y)} k \to \frac 1 {f'(x)}
> $$
>
> Let $h = g(k + y) - g(y)$ and notice that $h + x = g(k + y)$ and $f(g(y + k)) = f(x + h) = y + k$. Hence $k = f(x + h) - y = f(x + h) - f(x)$. Rewriting,
> $$
> \frac {g(y + k) - g(y)} k = \frac h k = \frac h {f(x + h) - f(x)}
> $$
>
> Therefore, as $k \to 0$, the left-hand side approaches $g'(y)$ and the right-hand size approaches $\frac 1 {f'(x)}$ as $h \to 0$.
>
> $\blacksquare$

This property is used heavily in the derivation of [[The Inverse Trigonometric Functions]].