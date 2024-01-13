# Estimates for the Error in Taylor's Formula

Given a Taylor Polynomial representing some function, we want to determine the bounds on the [[Taylor's Formula with Remainder#Error as an Integral|error component]] $E_n$.

## Bounds Using the N+1st Derivative

We can take advantage of the fact that if $m \leqslant f^{(n+1)}(x) \leqslant M$, then the error will be proportional to those bounds:

> [!abstract]- Theorem
> Suppose $f$ has order $n+1$ derivatives and further suppose:
> $$
> m \leqslant f^{(n+1)}(x) \leqslant M
> $$
>
> Then for every $x$ in an interval containing $a$, we have:
> $$
> m \frac {(x-a)^{n+1}} {(n+1)!} \leqslant
> E_n(x)
> \leqslant M \frac {(x-a)^{n+1}} {(n+1)!}
> $$
>
> if $x > a$ and
>
> $$
> m \frac {(a - x)^{n+1}} {(n+1)!}
> \leqslant (-1)^{n+1} E_n(x)
> \leqslant M \frac {(a-x)^{n+1}} {(n+1)!}
> $$
>
> if $x < a$.
>
> Proof.
> Recall that $E_n = \int_a^x (x-t)^n f^{(n+1)} (t) \; dt$ and notice that for $x > a$ over $[a, x]$, $(x-t)^n$ is nonnegative for every $t$. We write:
> $$
> \begin{align}
> &m \leqslant f^{(n+1)}(x) \leqslant M \\ \\
>
> &\implies m \frac {(x-t)^n} {n!}
> \leqslant \frac {(x-t)^n} {n!} f^{(n+1)}(x)
> \leqslant M \frac {(x-t)^n} {n!} \\ \\
>
> &\implies m \frac {(x-a)^{n+1}} {(n+1)!}
> \leqslant \frac 1 {n!} \int_a^x (x-t)^n f^{(n+1)}(t) \; dt
> \leqslant M \frac {(x-a)^{n+1}} {(n+1)!} \\ \\
>
> &\implies m \frac {(x-a)^{n+1}} {(n+1)!}
> \leqslant E_n(x)
> \leqslant M \frac {(x-a)^{n+1}} {(n+1)!} \\ \\
> \end{align}
> $$
>
> Now for $x < a$, we see for every $t \in [x, a]$, $(x - t) \leqslant 0$, and so:
> $$
> \begin{align}
> &m \leqslant f^{(n+1)}(x) \leqslant M \\ \\
>
> &\implies m \frac{(t-x)^n} {n!}
> \leqslant \frac{(t-x)^n} {n!} f^{(n+1)}(x)
> \leqslant M \frac{(t-x)^n} {n!} \\ \\
>
> &\implies m \frac{(a-x)^{n+1}} {(n+1)!}
> \leqslant \frac 1 {n!} \int_x^a (t-x)^n f^{(n+1)}(x)
> \leqslant M \frac{(a-x)^{n+1}} {(n+1)!} \\ \\
>
> &\implies m \frac{(a-x)^{n+1}} {(n+1)!}
> \leqslant (-1)^n \frac 1 {n!} \int_x^a (x-t)^n f^{(n+1)}(x)
> \leqslant M \frac{(a-x)^{n+1}} {(n+1)!} \\ \\
>
> &\implies m \frac{(a-x)^{n+1}} {(n+1)!}
> \leqslant (-1)^n E_n(x)
> \leqslant M \frac{(a-x)^{n+1}} {(n+1)!}
>
> \end{align}
> $$
>
> Where $(t-x)^n = (-1)^n (x-t)^n$.
>
> $\blacksquare$

### Estimating the error for $e^x$

> [!tip]
> See [[Cheatsheet]] for more example approximations.

> [!example]
> Let $f(x) = e^x, a = 0$. Then using Taylor's formula:
> $$
> \begin{align}
> e^x &= \sum_{k=0}^n \frac {x^k} {k!} + E_n(x) \\
> &= \sum_{k=0}^n \frac {x^k} {k!} + \int_0^x (x-t)^n f^{(n+1)} \; dt \\
> &= \sum_{k=0}^n \frac {x^k} {k!} + \int_0^x (x-t)^n e^t \; dt &\text{$(e^x)' = e^x$}
> \end{align}
> $$
>
> We know that $e^x$ is monotonic and increasing on $[a, b]$ and so we can choose bounds $m = e^0 \leqslant e^x \leqslant M = e^x$ and choose $x = b = 1$. Then we have $x > a$ and so:
> $$
> \begin{align}
> &m \frac {(x-a)^{n+1}} {(n+1)!} \leqslant
> E_n(x)
> \leqslant M \frac {(x-a)^{n+1}} {(n+1)!} \\ \\
>
> \implies &\frac {x^{n+1}} {(n+1)!} \leqslant
> E_n(1)
> \leqslant e \frac {x^{n+1}} {(n+1)!} \\ \\
>
> \implies &\frac 1 {(n+1)!} \leqslant
> E_n(1)
> \leqslant e \frac 1 {(n+1)!} \\ \\
>
> \implies &\frac 1 {(n+1)!} \leqslant
> E_n(1)
> \lt \frac 3 {(n+1)!} &\text{$e \lt 3$} \\ \\
>
> \end{align}
> $$