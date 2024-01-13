# Values of Continuous Functions

We develop from Bolzano's theorem a result helpful in proving several properties of functions continuous over some $[a, b]$.

## Bolzano's Theorem

Bolzano's theorem states that if a continuous function $f$ over $[a, b]$ changes sign, it must have crossed the x-axis at some point. We use this fact later in order to establish the Intermediate Value Theorem, but Bolzano's theorem can be helpful when trying to narrow down roots of a polynomial.

> [!abstract] Bolzano's Theorem
> Let $f$ be continuous at each point in an interval $[a, b]$ and assume for some $x_1 \lt x_2, \; f(x_1) = -f(x_2)$. Then there is at least one point $c \in (x_1, x_2)$ such that $f(c) = 0$.
>
> Proof.
> We first prove a lemma that show there is always a some neighborhood of a continuous function such that all points in the neighborhood share the same sign.
>
>> [!abstract] Lemma (Sign-Preserving Theorem)
>> Let $f$ be continuous at a point $c$ and suppose that $f(c) \neq 0$. Then there is an interval $(c - \delta, c + \delta)$ in which $f$ takes on the same sign as $f(c)$.
>>
>> Proof.
>> Assume without loss of generality that $f(c) > 0$. By continuity we have for every $\epsilon, \delta > 0$
>> $$
>> |f(x) - f(c)| \lt \epsilon, \; \text{whenever} \; |x - c| \lt \delta
>> $$
>> Take $\epsilon = \frac {f(c)} 2$ and notice:
>> $$
>> 0 \lt f(c) - \frac {f(c)} 2 \lt f(x) \lt f(c) + \frac {f(c)} 2
>> $$
>> which implies that $f(x) \gt 0$ and thus is the same sign as $f(c)$. The same proof holds if we assume $f(c) \lt 0$ and take $\epsilon = -  \frac {f(c)} 2$.
>>
>> $\blacksquare$
>>
> To see that Bolzano's theorem holds, assume without loss of generality that $f(a) \gt 0$ and $f(b) \lt 0$ and let $x$ be the minimum value in $[a, b]$ for which $f(x) = 0$. Let $S = \{ (x, y) \mid a \leqslant x \leqslant b, f(x) \leqslant 0\}$ (there must be at least one such point since $f(a) \lt 0$). By construction, all of $S$ lies within $[a, b]$ and since it is bounded, we may take $c$ to be its supremum. We will show that $f(c) = 0$.
>
> Consider the cases of $f(c) \neq 0$ by way of contradiction:
>
> ($f(c) \gt 0$): By the sign-preserving property of continuous functions, there is some interval $(c - \delta, c + \delta)$ such that $f \gt 0$, but then no points in $S$ may lie to the right of $c - \delta$, making it an upper bound for $S$. Thus since $c - \delta \lt c$ we have contradicted the fact that $c$ is the *least* upper bound of $S$.
>
> ($f(c) \lt 0$): Similarly, we have by the sign-preserving property of continuous functions an interval $(c - \delta, c + \delta)$ in which $f(c) \lt 0$. Then we have $f(x) \lt 0$ for some $c + \delta \gt c$, contradicting the fact that $c$ was an upper bound for $S$.
>
> Thus, the only remaining possibility is for $f(c) = 0$, and the proof is shown.
>
> $\blacksquare$

## Intermediate Value Theorem

Extending Bolzano's theorem to an arbitrary sub-interval over which a continuous function is defined. Intuitively this works if we imagine translating the graph of a function until the left endpoint of the interval were below the x-axis and the right-endpoint above (or vice-versa) and repeatedly applying Bolzano's.

> [!abstract] Intermediate Value Theorem
> Let $f$ be continuous on $[a, b]$ and choose $x_1 \lt x_2$ in $[a, b]$ such that $f(x_1) \lt f(x_2)$. Then $f$ takes on every value between $f(x_1)$ and $f(x_2)$.
>
> Proof.
> Suppose without loss of generality that $f(x_1) \lt f(x_2)$. We will show that for some $k \in (f(x_1), f(x_2))$, there is some $c$ such that $f(c) = k$ (We show this is true for over the closed in interval since the result is trivial if $k$ is equal to either of the endpoints).
>
> Define $g(x) = f(x) - k$ and notice $f(x_1) - k \lt 0, \; f(x_2) \gt 0$. Then we may apply Bolzano's theorem to see that there is some $c \in [a, b]$ such that $g(c) = f(c) - k = 0$, and thus $f(c) = k$.
>
> $\blacksquare$