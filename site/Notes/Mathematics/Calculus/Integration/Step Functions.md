# Step Functions

We introduce a step function as a simple basis for computing the integral of more general functions later on. We build up the rigorous foundation for a step function by considering [[Area as a Set Function#Partitions over an Interval]].

> [!info] Step Function
> Let $P = \{ x_0, x_1, \dots, x_n \}$ be a partition over an interval $[a, b]$ and suppose $s$ is a function with domain $[a, b]$ and that $s$ is constant over every open subinterval $(x_{k-1}, x_k)$. Then we call $s$ a **step function** and write:
> $$
> s(x) = s_k, k \in \mathbb{N} \; \text{if} \; x_{k - 1} < x < x_k
> $$
> In other words, the value of $s$ at some $x$ contained in an open subinterval of $P$ is a corresponding constant $s_k$.

Understanding the underlying structure of the partition is important for deriving results related to integration later on.

## Sum and Product of Step Functions

Let $s, t$ be step functions as defined above and $P_1, P_2$ be the respective partitions over whose sub-intervals $s, t$ are constant. We want to show $s + t$ is a step function, and in particular is the sum of their image over some partition.

> [!abstract] Theorem.
> If $s, t$ are step functions constant over the open sub-intervals of respective partitions $P_1, P_2$ over an interval $[a, b]$, then $s + t$ is a step function defined by $s(x) + t(x)$.
>
> Proof.
> Let $P$ be $P_1 \cup P_2$ and let $u(x) = s(x) + t(x), a \leqslant x \leqslant b$. Then $u$ is constant over $P$ because $s, t$ are constant over $P_1, P_2$, respectively. Thus $u$ is a step function defined as the sum of $s$ and $t$.
>
> $\blacksquare$

A similar argument follows for $s \cdot t$, which produces a step function.

## Definite Integral of a Step Function

We now have enough information to define the definite integral of a step function and show that certain properties about the integral hold.

> [!info] Definite Integral of a Step Function
> Let $s$ be a step function constant over the open sub-intervals of a partition $P = \{ x_0, x_1, \dots, x_n \}$. We define the **definite integral** of $s$ as:
> $$
> \int_b^a s(x) \; dx = \sum_{k=1}^n s_k (x_k - x_{k - 1})
> $$

That is, we compute the product of the value of $s$ over a particular sub-interval and the length of that interval. We sum these values over the entirety of $P$.

> [!example]
> $\int_0^3 \lfloor 2x \rfloor \; dx = (1)(1 - 0.5) + (2)(1.5 - 1) + (3)(2 - 1.5) + (4)(2.5 - 2) + (5)(3 - 2.5) = 7.5$

> [!tip]
> In the situation that a step function $s$ is constant over the entire interval, the value of the integral become $s(x)(b - a)$ since
> $$
> \int_b^a s(x) \; dx = c \sum_{k=1}^n (x_k - x_{k-1}) = c (b - a)
> $$
> By the telescoping property of sums.