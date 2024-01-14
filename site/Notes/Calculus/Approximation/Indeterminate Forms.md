# Indeterminate Forms

Taylor approximations can help evaluate limits which would otherwise be in some indeterminate form.

## Taylor Expansion

> [!example]
> Suppose we want to take the following limit.
> $$
> \lim_{x \to 0} \frac {a^x - b^x} x = \frac 0 0
> $$
>
> Evaluation results in an indeterminate form of $\frac 0 0$, however, we can use the Taylor expansion for $e^x$ to eliminate the indeterminate form. We start by rewriting the numerator:
> $$
> a^x - b^x = e^{x \log a} - e^{x \log b} = 1 + x \log a + o(x) - (1 + x \log b + o(x))
> $$
> And so our limit becomes:
> $$
> \lim \frac {x(\log a - \log b) + o(x)} x = \log \frac a b
> $$

## L'Hopital's Rule

L'Hopital's rule can be used to resolve indeterminacy in the cases where the numerator and denominator both approach 0 or $\pm inf$.

> [!abstract] L'Hopital's Rule for $\frac 0 0$ Indeterminancy
> Suppose $f, g$ are both differentiable for each $x \in (a, b)$ and
> $$
> \lim_{x \to a+} f(x) = \lim_{x \to a+} g(x) = 0
> $$
> Also suppose $g'(x) \neq 0$ for each $x \in (a, b)$. Then
> $$
> \lim_{x \to a+} \frac {f(x)} {g(x)} = L
> \iff
> \lim_{x \to a+} \frac {f'(x)} {g'(x)} = L
> $$
>
> Proof.
> We start by recalling Cauchy's Mean Value Theorem:
> $$
> \frac {f(b) - f(a)} {g(b) - g(a)} = \frac {f'(c)} {g'(c)}
> $$
>
> We want to use the fact that $f$ and $g$ are continuous to show that $f(a) \to 0$ and $g(a) \to 0$ so that we may manipulate the equality above, however, $f, g$ may be undefined at $x = a$. To mitigate this, we introduce functions $F, G$ such that:
> $$
> F(x) =
> \begin{cases}
> f(x) & \text{if } x \neq a \\
> 0 & \text{otherwise}
> \end{cases}
> $$
>
> $$
> G(x) =
> \begin{cases}
> g(x) & \text{if } x \neq a \\
> 0 & \text{otherwise}
> \end{cases}
> $$
>
> Now we use the fact that $F$ and $G$ are continuous everywhere on $[a, x]$ where $a \lt x \lt b$ to see that:
> $$
> \frac {F(x) - F(a)} {G(x) - G(a)} = \frac {f'(c)} {g'(c)}
> \iff
> \frac {f(x)} {g(x)} = \frac {f'(c)} {g'(c)}
> $$
>
> Where the initial division by $g'(c)$ is legal due to the fact that $g'(c) \neq 0$ over $(x, a)$ and the final equality follows from $F(a) = G(a) = 0$.
>
> $\blacksquare$

## L'Hopital's Rule for Infinite Limits

First we want to define the concept of an **infinite limit** and show how L'Hopital's rule extends to handle indeterminate forms in that situation.

> [!info] Infinite Limits
> Suppose $f(x) \to \infty$ as $x \to a$. We denote this fact with:
> $$
> \lim_{x \to a} f(x) = \pm \infty
> $$
> And say that
> > $f$ takes on arbitrarily large (or large negative) values as $x$ approaches $a$.
>
> Formally, we say for every $M \gt 0$ there exists a $\delta \gt 0$ such that
> $$
> f(x) \gt M \iff 0 < |x - a| < \delta
> $$
>
> Additionally we have:
> $$
> \begin{array}{c c c}
> \lim_{x \to a+} f(x) = +\infty & \iff & f(x) > M \;; 0 < x - a < \delta \\ \\
> \lim_{x \to a-} f(x) = +\infty & \iff & f(x) > M \;; 0 < a - x < \delta
> \end{array}
> $$