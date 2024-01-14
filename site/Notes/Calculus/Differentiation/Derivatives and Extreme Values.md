# Derivatives and Extreme Values

Computing the first and second derivatives of a function reveal important information about relative maxima and minima. This has direct applications in optimization problems and can be helpful in finding roots of polynomials.

> [!todo]
> Definitely need some plots here

## Vanishing Derivative

We begin with a proof showing that wherever there is a relative extremum for a function $f$, it's derivative (if it exists) is always zero for that value of $x$.

> [!abstract] Vanishing Derivative
> Let $f$ by defined on an open interval $I$ and assume that $f$ has an extremum at $c \in I$. If $f$ is differentiable over $I$, then $f'(c) = 0$.
>
> Proof.
> Assume $f$ is differentiable over an open interval $I$ and $f$ has an extremum at $x = c$. Define $Q(x) = \frac {f(x) - f(c)} {x - c}$ where $x \neq c$ and let $Q(c) = f'(c)$ and notice that because $f$ is differentiable, we know that $Q(x) \to Q(c)$ as $f(x) \to f(c)$. We proceed by way of contradiction to show that $Q(c) = 0$.
>
> First, assume $Q(c) \gt 0$. By the sign-preserving property of continuous functions, there exists some $(c-\delta, c+\delta)$ such that $f(x) - f(c) \gt 0$. But then $f(x) > f(c)$, contradicting the assumption that $f(c)$ is maximal. Similarly, if we assume $Q(c) \lt 0$, by sign-preservation we have some interval in which $f(x) \lt f(c)$, contradicting the fact that $f(c)$ was an extreme value. Thus, $Q(c) = 0$ wherever $f$ has an extermal value, and the proof is complete.
>
>$\blacksquare$

## Mean Value Theorem

Differential Calculus has an analog to the [[Mean Value Theorem]] for continuous function defined in terms of an integral. This time, we want to express that a function is equal to its **average rate of change** somewhere over an interval.

### Rolle's Theorem

Rolle's theorem states that if a function defined over some interval $[a, b]$ is equal at its endpoints, then it's derivative must be zero somewhere. The requirement that $f(a) = f(b)$ can be shown with a simple counterexample of $f(x) = x$, since $f'(x) = 1 \neq 0$ over any interval.

> [!todo]
> Need a plot here like seriously...

More subtly, if we know that $f(a) = f(b)$ at some point we know that the function is **not monotonic** and furthermore must take on a maximum and a minimum. To see this, we imagine starting at some $a$ in the interval and reaching $b$. Since the function is continuous, we two choices:

1. Remain constant
	1. ($f'(x)$ is trivially 0 in this case)
2. Some arbitrary sequence of increases or decreases
	1. Geometrically, this means the **slope of the tangent line** must equal 0 at some point because we must "change direction".

The following is a more rigorous proof of Rolle's Theorem:

> [!abstract] Rolle's Theorem
> Let $f$ be a function continuous everywhere on $[a, b]$, and assume $f$ is differentiable over the open interval $(a, b)$. Also assume $f(a) = f(b)$, then there is at least one point $c \in (a, b)$ such that $f'(c) = 0$.
>
> Proof.
> We argue by contradiction and use the vanishing derivative theorem to show $f'(c) = 0$. By the [[Extreme Values#Extreme Value Theorem]] $f$ must take on its absolute minimum and maximum somewhere in the interval $[a, b]$. But then the value cannot occur in the interior interval $(a, b)$ since otherwise the derivative would vanish, and so it must be the case that $f$ has its extrema at $a$ and $b$, but $f(a) = f(b)$ and so $f$ is constant, and its derivative is zero everywhere on $[a, b]$. Thus there must exist some $c$ in the interval such that $f'(c) = 0$.
>
> $\blacksquare$

### Proof of the Mean Value Theorem

In order to use Rolle's theorem, we need to define a function that takes on equal values at its endpoints. We then show that this function has a derivative and show that this leads to the desired equality.

> [!abstract] Mean Value Theorem
> Assume $f$ is continuous over $[a, b]$ and differentiable at each point in an open interval $(a, b)$. Then there is at least one $c \in (a, b)$ such that:
> $$
> f(b) - f(a) = f'(c)(b - a)
> $$
>
> Proof.
> We define a function $\phi$ to be the secant line through points $(a, f(a))$ and $(b, f(b))$. We show that derivative of $f$ is equal to the slope of this line at some point in the interval $(a, b)$:
> $$
> \phi(x) = f(x)(b-a) - x[f(b) - f(a)]
> $$
>
> Since $f$ is differentiable over the entire interval, $\phi'(x)$ must exist, and so we have $\phi'(x) = 0$ for some $c \in (a, b)$ by Rolle's Theorem. Rearranging the subsequent equation we find:
> $$
> \phi'(c) = f'(c)(b - a) - (f(b) - f(a)) = 0 \iff f'(c)(b - a) = f(b) - f(a)
> $$
>
> Which is the desired equation.
>
> $\blacksquare$
