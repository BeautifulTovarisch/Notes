# Journey to the Natural Log

We want to define the natural log as an integral in order to take advantage of the [[Properties of the Integral of a Step Function]]. We start by examining a [[functional equation]] and reason about some characteristics of a solution.

## A Functional Equation

We consider the following **functional equation** in order to decide what properties our solution will have.

> [!tip]
> This is the most effective way I've been shown where the [[Exponents and Logarithms#Logarithmic Identities]] come from!

> [!todo]
> This is a good point to review the section in AOPS on functional equations

$$
f(xy) = f(x) + f(y)
$$

If we allow 0 to be in the domain of $f$, say $x = 0$, this forces $f$ to be the constant function $0$:

$$
f(0y) = f(0) = f(0) + f(y) \implies f(y) = 0
$$

So we consider solutions for which 0 is not in the domain.

We consider $x = y = 1$:

$$
f(xy) = f(1) = f(1) + f(1) \implies f(1) = 0
$$

And $x = y = -1$:

$$
f(1) = f(-1) + f(-1) \implies f(-1) = 0 = f(1)
$$

Which gives us a hint the function might be even. Let $y = -1$

$$
f(-x) = f(x) + f(-1) \iff f(x) = f(-x)
$$

Finally, let's assume that the derivative of $f$ exists everywhere except $x=0$ and take the derivative of both sides.

$$
\frac d {dx} \; f(xy) = \frac d {dx} [f(x) + f(y)] = yf'(xy) = f'(x)
$$

Evaluating at $x=1$:

$$
yf'(y) = f'(1) \implies f'(y) = \frac {f'(1)} {y}
$$

Finally we integrate this function (we can do so since $f'$ is monotonic) to arrive at a familiar formula:

$$
\int f'(t) \; dt = f'(1) \int \frac 1 t \; dt
$$

In summary, we would like our supposed solution to the functional equations to exhibit the above properties and be given by $\int_c^x \frac 1 t \; dt$.

## From the Integral

Continuing from the previous integral and using the Fundamental Theorem of Calculus:

$$
f(x) - f(c) = \int_c^x f'(1) \frac 1 t \; dt = f'(1) \int_c^x \frac 1 t \; dt
$$

We consider the sign of $x$ in order to find and upper limit that satisfies all such cases.

1. $x \gt 0$ - The equation holds for all $c \gt 0$
2. $x \lt 0$ - The equation holds for all $c \lt 0$

We choose $c = 1$ (why?) and consider cases 1. and 2. above:

$$
\begin{align}
&x \gt 0 &\implies f'(1) \int_1^x \frac 1 t \; dt \\ \\
&x \lt 0 &\implies f'(1) \int_1^{-x} \frac 1 t \; dt \\ \\
\end{align}
$$

Then the function is piecewise over $x$ and so we may abbreviate it with:

$$
f(x) = f'(1) \int_1^{|x|} \frac 1 t \; dt, \; x \neq 0
$$

Thus a solution to our functional equation differentiable everywhere except $x = 0$ must be given by the above integral.

### A Closer Look at Our Formula

We examine the possible values of $f'(1)$ in order to learn more about $f(x)$.

If $f'(1) = 0$, then clearly $f(x) = 0$ everywhere. By contraposition, if $f \neq 0$ then $f'(1) \neq 0$. Once again, a constant function $f = 0$ isn't very interesting, so we argue from the assumption that $f'(1) \neq 0$.

Let $g(x) = \frac {f(x)} {f'(1)}$ (since $f'(1) \neq 0$). We know that $g$ is a solution because for some constant $c$, $cf$ is a solution whenever $f$ is (In this case, we let $c = \frac 1 {f'(1)}$). So we conclude that **all solutions** may be obtained by multiplying $g(x)$ by some constant.

> [!tip]
> More profound foreshadowing at the relationship between logarithms of different bases.

Now that we've outlined the conditions our solution must satisfy, we can formalize a definition!