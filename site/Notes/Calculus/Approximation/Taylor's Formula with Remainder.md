# Taylor's Formula with Remainder

As with the [[Polynomial Approximation of the Logarithm#Error Component]], we want to bound the size of the error in order to determine the precision of the approximation.

We begin by defining the error term and later rewrite it as an integral.

$$
E_n(x) = f(x) - T_n f(x) \iff f(x) = T_n f(x) + E_n(x)
$$

## Error as an Integral

The next theorem is shown by induction. We prove the definition of the error for $n = 1$ and then use it to show the inductive step for $n \geqslant 1$ immediately after.

> [!todo]
> Consolidate the cases of this proof into one proof by induction. Not sure why the author proved the first theorem as the basis for the other...

> [!abstract] Theorem
> Assume $f$ has a second derivative $f''(x)$ in some [[Continuity of Functions#Precise Definition of a Limit|neighborhood of a]]. Then for every $x \in N(a)$ we have
> $$
> f(x) = f(a) + f'(a)(x - a) + E_1(x)
> $$
> where $E_1(x) = \int_a^x (x-t) f''(t) \; dt$ and in general $E_n(x) = \frac 1 {n!} \int_a^x (x-t)^n f^{(n+1)} (t) \; dt$
>
> Proof.
> By definition of $E_1$ we have
> $$
> \begin{align}
> E_1(x) &= f(x) - T_1 f(x) \\ \\
> &= f(x) - \sum_{k=0}^1 \frac {f^{(k)}(a)} {k!} (x-a)^k \\ \\
> &= f(x) - f(a) + f'(a)(x - a) \\ \\
> &= \int_a^x f'(t) \; dt + \int_a^x f'(a) \; dt \; &\text{FTC} \\ \\
> &= \int_a^x [f'(t) + f'(a)] \; dt
> \end{align}
> $$
>
> Integrating by parts we let $u = f(t) - f'(a), dv = dt$. Additionally, we choose $v = t - x$ with $-x$ as a convenient $C$ since $\frac d {dx} t - x = dt$ and find:
> $$
> \begin{align}
> &\int_a^x [f'(t) - f'(a)] \; dt
> \\ &= (t-x)[f'(t) - f'(a)] \Big|_a^x - \int_a^x (t - x) f''(t) \; dt \\
> &= (t-x)[f'(t) - f'(a)] \Big|_a^x + \int_a^x (x - t) f''(t) \; dt \\
> &= \int_a^x (x - t) f''(t) \; dt
> \end{align}
> $$
>
> Where the final equality comes from the fact that the first term is zero when evaluated at the limits of integration.
>
> Now we show the inductive case by taking $E_{n+1} (x)$ and $E_n(x)$. We write:
> $$
> \begin{align}
> E_{n+1} (x) - E_n (x) &= f(x) - T_{n+1} f(x) - f(x) + T_n f(x) \\
> &= T_n f(x) - T_{n+1} f(x) \\ \\
> &\iff \\ \\
> E_{n+1} &= E_n - \frac {f^{(n+1)(a)}} {(n+1)!} (x-a)^{n+1} \\
> &= \frac 1 {n!} \int_a^x (x-t)^n f^{(n+1)}(t) \; dt - \frac {f^{(n+1)}(a)} {(n+1)!} (x-a)^{n+1} &\text{IH}
> \end{align}
> $$
>
> Now we notice $\int_a^x (x-t)^n \; dt = \frac {(x-t)^{n+1}} {n+1} \Big|_a^x = \frac {(x-a)^{n+1}} {n+1}$. So then our equation becomes:
> $$
> \begin{align}
> E_{n+1} &= \frac 1 {n!} \int_a^x (x-t)^n f^{(n+1)}(t) \; dt -
> \frac {f^{(n+1)}} {n!} \int_a^x (x-t)^n \; dt \\
> &= \frac 1 {n!} \int_a^x (x-t)^n [f^{(n+1)}(x) - f^{(n+1)}(a)] \; dt
> \end{align}
> $$
>
> Finally, integrating by parts, we take $u = [f^{(n+1)(x)} - f^{(n+1)}(a)]$ and $v = (t-x)^n$ so that:
> $$
> \begin{align}
> E_{n+1}(x)
> &= (t-x)^n[f^{(n+1)(x)} - f^{(n+1)}(a)] \Big|_a^x
> - \frac 1 {(n+1)!} \int_a^x (t-x)^{n+1} f^{(n+2)} (t) \; dt  \\
> &= \frac 1 {(n+1)!} \int_a^x (x-t)^{(n+1)} f^{(n+2)} (t)  \; dt
> \end{align}
> $$
>
> Hence the inductive case is shown and the proof is complete.
>
> $\blacksquare$
