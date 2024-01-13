# Manipulation

Our goal is to find closed forms of summations which allow either more efficient computation or easier analysis. These notes use the bizarre notation introduced by Knuth.

## Notation

In order to make manipulating sums easier, we use an unusual notation which lets us cleverly avoid the complexities of changing indices.

> [!info] Notation
> $$
> \sum_{k=1}^n a_k
> = \sum_{1 \leqslant k \leqslant n} a_k
> = \sum_{1 \leqslant k + 1 \leqslant n}^n a_{k+1}
> $$
>
> We see that the rightmost summations allow the trivial substitution of $k + 1$ for $k$ without worrying about adjusting the term. We consider the bounds of the summation in terms of some **predicate** rather than upper and lower limits per se.

### Iverson Notation

The Iverson brackets expand upon the idea of using a predicate to specify the terms of a summation. This is similar to treating the terms of a summation as vector and taking the [[Dot Product]] with a [[Vectors over GF(2)]] (or the Kroenecker Delta from Calculus).

> [!info] Iverson Bracket
> Let $P(k) = 1$ if $P(k)$ holds and 0 otherwise. We write:
> $$
> \sum_{k \; \text{if} \; P(k)} a_k = \sum_k a_k[P(k)]
> $$

This notation has a kind of algebra to it, which comes in handy for manipulating indices.

## Manipulating Sums

We can see the advantage of the new notation when adding indices.

### Adding Indices

> [!abstract] Theorem.
> $$
> \sum_{k \in K} a_k + \sum_{k \in K'} a_k
> = \sum_{k \in K \cap K'} a_k + \sum_{k \in K \cup K'} a_k
> $$
>
> Proof.
> Writing each sum in iverson notation, we have:
> $$
> \begin{align}
> \sum_{k \in K} a_k + \sum_{k \in K'} a_k
> &= \sum_k a_k [k \in K] + \sum_k a_k [k \in K'] \\
> &= \sum_k a_k [k \in K] + [k \in K'] &\text{Additivity of Sums} \\
> &= \sum_k a_k [k \in (K \cup K') + (K \cap K')] &\text{Def of Union} \\
> &= \sum_k a_k [k \in (K \cup K')] + \sum_k a_k [k \in (K \cap K')] &\text{Additivity of Sums} \\
> &= \sum_{k \in K \cap K'} a_k + \sum_{k \in K \cup K'} a_k &\text{Iverson}
> \end{align}
> $$

Thus we see we can treat indices of summations as objects that can be manipulated using some set theory.

> [!example]
> Consider the following sums whose indices are non-disjoint
> $$
> \begin{align}
> \sum_{k=1}^m a_k + \sum_{k=m}^n a_k
> &= \sum_k a_k [1 \leqslant k \leqslant m] + \sum_k a_k [m \leqslant k \leqslant n] \\
> &= \sum_k a_k [1 \leqslant k \leqslant m] \cup [m \leqslant k \leqslant n]
> + \sum_k a_k [1 \leqslant k \leqslant m] \cap [m \leqslant k \leqslant n] \\
> &= \sum_k a_k [1 \leqslant k \leqslant n] + \sum_k a_k [k = m] \\
> &= \sum_{1 \leqslant k \leqslant n} a_k + a_m
> \end{align}
> $$
>
> Where we see that the new indices follow from taking the union and intersection of the indices, respectively.

### Perturbing the Sum

The main idea here is to extract the first and last terms of a summation and manipulate the corresponding expression to solve for the summation.

> [!info] Perturbing the Sum
> Suppose $S_n = \sum_{0 \leqslant k \leqslant n} a_k$. We begin by adding first term and $n + 1$st term to $S_n$:
> $$
> \begin{align}
> S_n + (n+1) &= a_0 + \sum_{1 \leqslant k \leqslant n+1} a_k \\ \\
> &= a_0 + \sum_{1 \leqslant k+1 \leqslant n+1} a_{k+1} &k \to k+1 \\ \\
> &= a_0 + \sum_{0 \leqslant k \leqslant n} a_{k} &\text{idx - 1}
> \end{align}
> $$
>
> We now have a sum in terms of $S_n$ and can manipulate it to hopefully achieve a closed form.

> [!example] Perturbing a Geometric Series
> Let $S_n = \sum_{0 \leqslant k \leqslant n} ax^k$. We use the perturbation method to derive the well-known formula
> $$
> \begin{align}
> S_n + ax^{n+1}
> &= a + \sum_{1 \leqslant k \leqslant n+1} ax^k \\ \\
> &= a + \sum_{1 \leqslant k+1 \leqslant n+1} ax^{k+1} &k \to k+1 \\ \\
> &= a + \sum_{0 \leqslant k \leqslant n} ax^{k+1} \\ \\
> &= a + \sum_{0 \leqslant k \leqslant n} ax^{k+1} + ax^{n+1} \\ \\
> &= a + x\sum_{0 \leqslant k \leqslant n} ax^k + ax^{n+1} &\text{factoring $x$} \\ \\
> &= a + xS_n + ax^{n+1} \\ \\
> \iff \\ \\
> S_n(1 - x) &= a(1 - x^{n+1}) \\ \\
> \iff \\ \\
> S_n &= \frac {a(1 - x^{n+1})} {1 - x} \\ \\
> &&\blacksquare
> \end{align}
> $$

> [!example] Harder Example
> Let $S_n = \sum_{0 \leqslant k \leqslant n} k 2^k$. Perturbing the sum:
> $$
> \begin{align}
> S_n + (n+1)2^{n+1} &= \sum_{1 \leqslant k \leqslant n+1} k 2^k \\ \\
> &= \sum_{1 \leqslant k+1 \leqslant n+1} (k+1) 2^{k+1} &k \to k+1 \\ \\
> &= \sum_{0 \leqslant k \leqslant n} (k+1) 2^{k+1} \\ \\
> &= \sum_{0 \leqslant k \leqslant n} k 2^{k+1} +
> \sum_{0 \leqslant k \leqslant n} 2^{k+1} \\ \\
> &= 2 S_n + \frac {2 - 2^{n+2}} {1 - 2} \\ \\
> &= 2 S_n +  2^{n+1} - 2 \\ \\
> \iff \\ \\
> S_n &= (n+1) 2^{n+1} - 2^{n+2} + 2 \\ \\
> &= (n+1) 2^{n+1} - 2(2^{n+1}) + 2 \\ \\
> &= (n-1)2^{n+1} + 2 \\ \\
> &&\blacksquare
> \end{align}
> $$