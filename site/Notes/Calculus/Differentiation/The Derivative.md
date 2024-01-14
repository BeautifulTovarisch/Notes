# The Derivative

> [!todo]
> Plot a tangent line:
> - Either use fancy gnuplot hacks or
> - Literally plot some random function and its derivative

The derivative is used to produce a function that gives the **instantaneous rate of change** at a given point for some continuous function. The derivative has enormously broad applications in the sciences, and is also helpful in simplifying certain problems in the analysis of algorithms.

## Formal Definition

We introduce a ratio called the **difference quotient**. Historically this computed the **average velocity** over some interval of time, $[t, t + h]$, but was generalized to the **average rate of change** of a function over some interval.

> [!info] Difference Quotient
> Suppose an arbitrary interval over the real numbers and further suppose $t, t + h$ lie within such an interval, where $h \neq 0$. We define the **difference quotient** of $f$
> $$
> \frac {f(x + h) - f(x)} h
> $$
> and say that the quotient measures the **average rate of change** of $f$ on $[x, x + h]$

The concept of the derivative follows from narrowing the distance between $x$ and $x + h$ until the quantities are arbitrarily close. This mechanism is described by the [[Continuity of Functions#Precise Definition of a Limit]], and so our definition follows naturally:

> [!info] Definition of Derivative
> The derivative $f'(x)$ is defined
> $$
> \lim_{h \to 0} \frac {f(x + h) - f(x)} h
> $$
> where it exists.

## Examples

> [!example] Constant Function
> Suppose $f(x) = c$ for all $x$. Then
> $$
> \lim_{h \to 0} \frac {f(x + h) - f(x)} h =
> \lim_{h \to 0} \frac {c - c} h = 0
> $$

> [!example] Linear Function
> Suppose $f(x) = mx + b$. Then
> $$
> \lim_{h \to 0} \frac {f(x + h) - f(x)} h =
> \lim_{h \to 0} \frac {m(x + h) + b - mx + b} h =
> \lim_{h \to 0} \frac {mh} h = m
> $$

> [!example] Sine
> Suppose $f(x) = \sin x$, then
> $$
> \begin{align}
> &\lim_{h \to 0} \frac {f(x + h) - f(x)} h \\ \\
> &= \lim_{h \to 0} \frac {\sin(x + h) - \sin(x)} h \\ \\
> &= \lim_{h \to 0} \frac {\sin x \cos h + \cos x \sin h - \sin(x)} h &\sin(x + y) \\ \\
> &= \lim_{h \to 0} \frac {\sin x(\cos h - 1) + \cos x \sin h} h \\ \\
> &= \lim_{h \to 0} \frac {\sin x(\cos h - 1)} h + \frac{\sin h} h \cdot \cos x \\ \\
> &= \cos x &\lim_{h \to 0} \frac {\sin h} h = 1  \\
> \end{align}
> $$

### Continuity

If a function $f$ has a derivative, we know it must be continuous.

> [!warning]
> The converse statement, that if $f$ is continuous it must have a derivative, does not hold in general.

> [!abstract] Theorem
> If $f$ is differentiable at $x$, then it is continuous at $x$.
>
> Proof.
> Suppose a function $f$ has derivative $f'(x)$. We can manipulate the difference quotient of $f$ as follows:
> $$
> \frac {f(x + h) - f(x)} h \to
> h \left( \frac {f(x + h) - f(x)} h \right) \to
> f(x) + h \left( \frac {f(x + h) - f(x)} h \right)
> $$
> in order to receive the equation:
> $$
> f(x + h) = f(x) + h \left( \frac {f(x + h) - f(x)} h \right)
> $$
> Taking the limit of both sides, we have:
> $$
> \begin{align}
> &\lim_{h \to 0} f(x + h) =
> \lim_{h \to 0} \left[ f(x) + h \left( \frac {f(x + h) - f(x)} h \right) \right] \\ \\
> &\iff \\ \\
> &f(x) = f(x) + 0 \cdot f'(x)
> \end{align}
> $$
>
> This shows that $f(x + h) \to f(x)$ as $h \to 0$, which shows that $f$ is continuous.