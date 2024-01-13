# Area as a Set Function

The treatment of integration begins by defining a function from Cartesian coordinates in a plane to the real numbers. We say this *set* of points is mapped by a *set function* which produces the area.

> [!info] Measurable Sets
> We say a set $S$ of coordinates is **measurable** if a set function $a: S \mapsto \mathbb{R}$ maps $S$ to an area. (Best attempt at a definition). We denote the set of all such **measurable sets** by $\mathcal{M}$, and we say that if $m \in \mathcal{M}$, then it is **measurable**.

## Axiomatic Definition of Area

We define the axioms of measurable sets here and analytically derive key results that (eventually) lead to a theory of integration.

> [!abstract] Axioms of Area
> Suppose there exists a class $\mathcal{M}$ of measurable sets in the plane and a set function $a$ with domain $\mathcal{M}$ that exhibits the following properties:
>
> 1. **Nonnegative**: For every $S \in \mathcal{M}, a(S) \geqslant 0$
> 2. **Additive**: For $S, T \in \mathcal{M}$, $S \cup T$ and $S \cap T$ are in $\mathcal{M}$ and $a(S \cup T) = a(S) + a(T) - a(S \cap T)$
> 3. **Difference**: For $S, T \in \mathcal{M}$ and if $S \subseteq T$, then $T - S \in \mathcal{M}$ and $a(T - S) = a(T) - a(S)$.
>> [!info] Note
>> The first axiom implies this difference is nonnegative and hence a subset of a measurable set cannot have area greater than its superset.
>
> 4. **Invariance Under Congruence**: If $S \in \mathcal{M}$ and $S$ is congruent to $T$, then $T \in \mathcal{M}$ and $a(S) = a(T)$.
> 5. **Choice of Scale**: Every rectangle $R = \{ (x, y) \mid 0 \leqslant x \leqslant h, 0 \leqslant y \leqslant k \}$ is in $\mathcal{M}$ and has area $a(R) = hk$.
> 6. **Exhaustion**: Let $S \subseteq Q \subseteq T$, then if there exists a unique $c \in \mathbb{R}$ such that $a(S) \leqslant c \leqslant a(T)$, then $a(Q) = c$.

## Partitions over an Interval

A partition over an interval is a subdivision into $n$ sub-intervals (via introduction of $n-1$ points of separation). We'll use this idea in the rigorous definition of a step function, which we'll then be able to finally integrate.

Suppose we have an interval $[a, b]$. We introduce $n-1$ division points, $x_1, x_2, \dots x_{n-1}$ such that $a=x_0 \lt x_1 \lt x_2 \dots \lt x_{n-1} \lt b=x_n$. We call the resulting closed sub-intervals a **partition** over $[a, b]$:

$$
P = \{ (a=x_0, x_1), (x_1, x_2), \dots, (x_{n-1}, x_n=b) \}
$$

Finally, we denote the **kth sub-interval** of $P$ by $[x_{k-1}, x_k]$.