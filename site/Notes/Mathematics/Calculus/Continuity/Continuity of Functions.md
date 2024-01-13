# Continuity of Functions

Intuitively, we say a function is continuous of there are no "gaps", "kinks" or asymptotes in its graph. In order to rigorously define continuity, however, we need the notion of a limit.

> [!todo]
> Include some plots from `gnuplot`

## Limit of a Function

We think of a limit of a function as a value the function "approaches" as $x$ approaches some point $p$.

> [!info] Definition of a Limit
> Let $f$ be a function defined in some open interval containing a point $p$. We say the **"limit of $f$ as $x$ approaches $p$"** is represented by the following notation:
> $$
> \lim_{x \to p} f(x) = A \iff f(x) \to A \; \text{as} \; x \to p
> $$

In general terms, this conveys the notion that we let $f(x)$ get as "close" to $A$ as we want as $x$ gets "close" to $p$.

### Precise Definition of a Limit

A more rigorous definition of limits requires us to define the concept of a neighborhood.

> [!info] Neighborhood of $x$
> We refer to any open interval with $x$ as its midpoint as a **neighborhood** of $x$.

We express the definition of a limit in terms of arbitrarily narrow neighborhoods:

> [!info] Neighborhood Definition of a Limit
> Let $N(A)$ be a neighborhood of $A$ and $N(p)$ be a neighborhood of $p$. We say that $\lim_{x \to p} f(x) = A$ if and only if $\forall N(A) \; \exists N(p)$ such that
> $$
> f(x) \in N(A) \; \text{whenever} \; x \in N(p)
> $$

### Epsilon-Delta

We can express the idea of neighborhoods more compactly by letting $\epsilon$ and $\delta$ represent the **radii** of $N(A)$ and $N(p)$, respectively.

> [!info] Epsilon-Delta Definition of a Limit
> We say that $\lim_{x \to p} f(x) = A$ if and only if
> $\forall \epsilon > 0 \; \exists \delta > 0$ such that
> $$
> |f(x) - A| < \epsilon \; \text{whenever} \; |x - p| < \delta
> $$

In other words, for every (arbitrarily small) interval we can choose for the value of $f$ at $x$, there must be another arbitrarily small distance between $x$ and $p$.

## Algebraic Properties of the Limit

Limits exhibit similar properties to the integral. These directly imply the continuity of certain expressions as shown in the next section. For each of the following properties, assume $f$ and $g$ are functions with limits $A$ and $B$, respectively.

> [!abstract] Addition Rule
> $$
> \lim_{x \to p} f(x) + \lim_{x \to p} g(x) = \lim_{x \to p} [f(x) + g(x)]
> $$
>
> Proof.
> Suppose for functions $f$ and $g$ we have:
> $$
> \begin{align}
> &0 < |f(x) - L_1| < \frac \epsilon 2, &0 < |x - p| < \delta_1 \\
> &0 < |g(x) - L_2| < \frac \epsilon 2, &0 < |x - p| < \delta_2 \\
> \end{align}
> $$
> Adding these inequalities:
> $$
> 0 < |f(x) - L_1| + |g(x) - L_2| < \epsilon \; |x-p| < \min(\delta_1, \delta_2)
> $$
> by Triangle Inequality:
> $$
> \begin{align}
> 0 < |f(x) + g(x) - (L_1 + L_2)| < \epsilon \; |x-p| < \delta
> \end{align}
> $$
> From the final inequality, we see that $\lim_{x \to p} [f(x) + g(x)] = L_1 + L_2$.
>
> $\blacksquare$


> [!abstract] Difference Rule
> $$
> \lim_{x \to p} f(x) - \lim_{x \to p} g(x) = \lim_{x \to p} [f(x) - g(x)]
> $$
>
> Proof.
> Equality follows immediately from the addition rule:
> $$
> \lim_{x \to p} f(x) - \lim_{x \to p} g(x) = \lim_{x \to p} f(x) + -\lim_{x \to p} g(x) = \lim_{x \to p}[f(x) - g(x)]
> $$
>
> $\blacksquare$

> [!abstract] Product Rule
> $$
> \lim_{x \to p} f(x) \cdot \lim_{x \to p} g(x) = \lim_{x \to p} [f(x) \cdot g(x)]
> $$
>
> Proof.

> [!abstract] Quotient Rule
> $$
> \frac {\lim_{x \to p} f(x)} {\lim_{x \to p} g(x)} = \lim_{x \to p} \frac {f(x)} {g(x)}
> $$
>
> Proof.

## Continuity

Using a limit, we can now precisely define what it means for a function to be continuous at a point.

> [!info] Continuity at a Point
> Let $f$ be a function and $p$ be an arbitrary point. Suppose $\lim_{x \to p} f(x) = A$. We say that $f$ is **continuous** at $p$ if and only if $f$ is **defined** at $p$ and
> $$
> \lim_{x \to p} f(x) = A = f(p)
> $$

### Squeeze Theorem

If we can find two functions that "squeeze" or bound another above and below then we can show their limits are equal. This is helpful when we happen to know a function is bounded by two others which either have known limits or those which are easier to evaluate.

> [!abstract] Squeeze Theorem
> Suppose that $f(x) \leqslant g(x) \leqslant h(x)$ for all $x \neq p$ in some $N(p)$. Suppose also that $\lim_{x \to p} f(x) = \lim_{x \to p} h(x) = a$. Then $\lim_{x \to p} g(x) = a$.
>
> Proof.
> Suppose $\epsilon > 0$ is given and notice that by assumption we have $|f(x) - a| < \epsilon$ whenever $0 < |x - p| < \delta$ and similarly for $h(x)$. Choose the minimum $\delta$ between the two inequality for $f$ and $h$ and write,
> $$
> \begin{align}
> &-\epsilon + a \lt f(x) \leqslant h(x) \lt \epsilon + a \\
> &\implies -\epsilon + a \lt f(x) \leqslant g(x) \lt h(x) \epsilon + a \\
> &\implies -\epsilon + a \lt g(x) \lt \epsilon + a
> \end{align}
> $$
> Whenever $0 < |x - p| < \delta$ and so by definition of the limit we have $\lim_{x \to p} g(x) = a$.
>
> $\blacksquare$

### Continuity of Indefinite Integrals

Using the fact that an integratable function over an interval $[a, b]$ is bounded by $|M|$, we can apply the $\epsilon-\delta$ definition to prove a function is continuous everywhere in the interval.

> [!abstract] Continuity of Indefinite Integrals
> Assume $f$ is integratable over $[a, b]$ and $A(x) = \int_a^x f(t) \; dt$. Then $A$ is continuous at each point in $[a, b]$.
>
> Proof.
> Choose $p$ to be an arbitrary point in $[a, b]$. We must show that $\lim_{x \to p} A(x) = A(p)$. Notice that $A(x) - A(p) = \int_0^x f(t) - \; dt \int_0^p f(t) \; dt = \int_p^x f(t) \; dt$ and also notice that since $f$ is bounded there are constants, say, $M$ and $-M$ which form the inequality:
> $$
> -M \leqslant f(t) \leqslant M \iff
> -M(x-p) \leqslant A(x) - A(p) \leqslant M(x-p)
> $$
> Where the right hand side of the inequality was obtained by taking the indefinite integral. But then we know the limit of the (identity) function $|M(x-p)|$ is $0$ and so by the squeeze theorem $\lim_{x \to p} [A(x) - A(p)] = 0 \iff \lim_{x \to p} A(x) = A(p)$ as was to be shown.
>
> $\blacksquare$