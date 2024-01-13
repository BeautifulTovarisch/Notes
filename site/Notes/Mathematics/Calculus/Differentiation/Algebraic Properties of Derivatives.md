# Algebraic Properties of Derivatives

Similar to the [[Continuity of Functions#Algebraic Properties of the Limit]], derivatives exhibit basic algebraic properties which allow them to be manipulated. This is often necessary to reduce a complicated derivative into one that can be evaluated more easily.

## Algebraic Properties

Let $f, g$ be two functions defined on a common interval. At each point where both have a derivative, the following properties hold.

> [!note]
> I've omitted the cumbersome limit notation since it doesn't add any value to the proofs. We'll pretend it's there.

> [!abstract] Addition Rule
> $$
> (f' + g') = f' + g'
> $$
>
> Proof.
> We prove by direct manipulation of the difference quotient of $(f' + g')$:
> $$
> \begin{align}
> (f' + g') &= \frac {(f + g)(x + h) - (f + g)(x)} h \\ \\
> &= \frac {f(x + h) + g(x + h) - f(x) + g(x)} h \\ \\
> &= \frac {f(x + h) - f(x)} h - \frac {g(x + h) - g(x)} h \\ \\
> &= f' + g' \\ \\
> &&\blacksquare
> \end{align}
> $$

> [!abstract] Difference Rule
> $$
> (f' - g') = f' - g'
> $$
>
> Proof.
> This can be trivially derived from the addition rule by letting $(f' - g') = (f' + (-g)'$. We'll prove it directly for posterity:
> $$
> \begin{align}
> (f' - g') &= \frac {(f - g)(x + h) - (f - g)(x)} h \\ \\
> &= \frac {f(x+h) - g(x+h) - f(x) - g(x)} h \\ \\
> &= \frac {f(x+h) - f(x)} h - \frac {g(x+h) - g(x)} h \\ \\
> &= f' - g' \\ \\
> &&\blacksquare
> \end{align}
> $$

> [!abstract] Product Rule
> $$
> (f' \cdot g') = f \cdot g' + f' \cdot g
> $$
>
> Proof.
> We begin as usual by expressing the product of the difference quotients of $f$ and $g$.
> $$
> (f' \cdot g') = \frac {f(x+h)g(x+h) - f(x)g(x)} h
> $$
>
> We perform a classic trick of adding zero in order to manipulate this quotient into the form we need.
> $$
> \begin{align}
> (f' \cdot g') &= \frac {f(x+h)g(x+h) - f(x)g(x)} h \\ \\
> &= \frac {f(x+h)g(x+h) - f(x)g(x) + g(x)f(x+h) - g(x)f(x+h)} h \\ \\
> &= \frac {f(x+h)g(x+h) - f(x)g(x) + g(x)f(x+h) - g(x)f(x+h)} h \\ \\
> &= g(x) \frac {f(x+h) - f(x)} h + f(x+h) \frac {g(x+h) - g(x)} h
> \end{align}
> $$
>
> We see that as $h \to 0$ the left term tends toward $g(x) \cdot f'(x)$ as desired, and the right term toward $f(x) \cdot g'(x)$, completing the proof.
>
> $\blacksquare$

Using the addition and product rules, we can prove differentiation exhibits linearity and therefore can be used to derive rules for computing the derivatives of polynomials.

> [!abstract] Quotient Rule
> $$
> \left( \frac f g \right)' = \frac {g \cdot f' - f \cdot g'} {g^2}
> $$
>
> Proof.
> We notice that for the special case of $f(x) = 1$, we may compute a helpful identity by assuming the quotient rule holds for $\frac 1 g$:
> $$
> \begin{align}
> (f \cdot \frac 1 g)' &= f' \cdot \frac 1 g + f \cdot (\frac 1 g)' \\ \\
> &= f' \cdot \frac 1 g - f \cdot \frac {g'} {g^2} \\ \\
> &= \frac {g \cdot f' - g' \cdot f} {g^2}
> \end{align}
> $$
>
> Therefore it is sufficient to prove $\left( \frac 1 g \right)' = \frac {g'} {g^2}$. We proceed via manipulation of the difference quotient of $\frac 1 g$:
> $$
> \begin{align}
> \frac {1/g(x+h) - 1/g(x)} h
> &= \frac 1 {h (g(x+h) - g(x))} \\ \\
> &= \frac 1 {h (g(x+h)} - \frac 1 {h g(x))} \\ \\
> &= \frac {g(x) - g(x+h)} h \cdot \frac 1 {g(x)g(x+h)} \\ \\
> &= - \frac {g(x+h) - g(x)} h \cdot \frac 1 {g(x)g(x+h)} \\ \\
> \end{align}
> $$
> Finally, we see as $h \to 0$, the given product tends to $-g'(x) \cdot \frac 1 {g^2}$, since $g(x + h) \to g(x)$.
>
> $\blacksquare$

## Bonus

As a treat, we derive the general rule for the derivative of a power function using the [[Binomial Theorem]].

> [!todo]
> Add a note or section to [[Counting Principles]] about the binomial theorem whenever it comes up.

> [!abstract] Derivative of a Power Function
> Let $f(x) = x^n$, then the derivative of $f$ at $x$ is given by the formula:
> $$
> f'(x) = nx^{n-1}
> $$
>
> Proof.
> We start by noticing $\Delta f = f(x + h) - f(x) = (x + h)^n - x^n$. We will show the expansion of $(x + h)^n$ yields the difference quotient for $x^n$ and finally that taking this limit produces the desired formula:
> $$
> \begin{align}
> (x + h)^n - x^n &= \sum_{k=0}^n {n \choose k} x^{n-k}h^k \\
> &= x^{n-1}h + \dots + {n \choose n-1}xh^{n-1} + h^n \\
> &= h(nx^{n-1} + \dots + {n \choose n-1}xh^{n-2} + h^{n-1}) \\ \\
> &\text{hence} \\ \\
> \frac {(x + h)^n - x^n} h &= nx^{n-1} + \dots + {n \choose n-1}xh^{n-2} + h^{n-1}
> \end{align}
> $$
>
> Taking the limit of both sides, we see that all terms except $nx^{n-1}$ tend to zero, thus completing the proof.
>
> $\blacksquare$