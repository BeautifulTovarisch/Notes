Combinatorics is a methodology for computing the enumeration, permutation etc. of sets of elements and relations.

## Proofs of Basic Counting Principles

These proofs allow us to build up a theory surrounding the cardinality of sets and hence allow for sophisticated counting of elements.

Recall from [[Set Theory#Laws]] that if $A, B$ are finite, $|A \cup B| = |A| + |B|$.

> [!abstract] Difference Rule.
> If $A, B$ are finite, and $B \subseteq A$, then $|A - B| - |A| - |B|$ 
> 
> Proof.
> By previous exercise, $(A - B) \cup B = A$ since $B \subseteq A$, and by another previous exercise we know $(A - B)$ and $B$ are disjoint. So then we can apply the rule from [[Functions#Cardinality]]:
> $$
> |(A - B) \cup B| = |A - B| + |B| = |A|
> $$
> Subtracting $|B|$ from both sides we have $|A - B| = |A| - |B|$. $\blacksquare$

> [!abstract] Inclusion Exclusion Rule.
> If $A, B$ are finite and not necessarily disjoint, then $|A \cup B| = |A| \cup |B| - |A \cap B|$
> 
> Proof.
> By previous exercise $A$ and $B - (A \cap B)$ are disjoint, hence we have:
> $$
> \begin{align}
> |A \cup B| &= |A \cap B - (A \cap B)| \\
> &= |A| + |B - (A \cap B)| \\
> &= |A| + |B| - |A \cap B| &\text{Difference Rule} \\ \\
> &&\blacksquare
> \end{align}
> $$

> [!abstract] Addition Rule
> If $A$ is finite and $A_1, A_2, \dots A_n$ form a partition of $A$, then $|A| = \sum_{i=1}^n |A_i|$.
> 
> Proof.
> By induction on $n = |A|$. Suppose $n = 1$, then $A = A_1$ and so $|A| = |A_1|$ by reflexivity of cardinality. Hence $\exists N \geq 1$ such that $\sum_{i=1}^N = |A|$.
> 
> Now suppose $n = N + 1$ and let $A' = A - A_{n+1}$. Then by inductive hypothesis, $\sum_{i=1}^n |A_i| + |A_{n+1}| = |A'| + |A_{n+1}|$. Since $A_{n+1}$ is a subset of a partition of $A$, it is disjoint with $A$ and so we have $\sum_{i=1}^{n+1} = |A' \cup A_{n+1}| = |A|$. 
> 
> $\blacksquare$

> [!abstract] Multiplication Rule
> If $A_1, \dots, A_n$ are finite, then $|A_1 \times A_2 \times \dots A_n| = \prod_{i=1}^n |A_i|$.
> 
>> [!abstract] Lemma.
>> If $A, B$ are finite sets, then $|A \times B| = |A| * |B|$.
>> 
>> Proof.
>> Since $A, B$ are finite there exist bijections $f : A \to \mathbb{N}_n$, $g: B \to \mathbb{N}_m$. Define $h: A \times B \to \mathbb{N}_{nm}$ by
>> $$
>> h(a, b) = n(f(a) - 1) + g(b)
>> $$
>> To show $h$ is injective, let $h(a_1, b_1) = h(a_2, b_2)$. Then by injectivity of $f, g$, we see $f(a_1) - 1 + g(b_1) = f(a_2) - 1 + g(b_1)$ implies $a_1 = a_2$ and $b_1 = b_2$, and so $h$ is injective.
>> 
>> To see the $h$ is surjective, suppose $k \in \mathbb{N}_{nm}$ and notice:
>> $$
>> \begin{align}
>> 0 \leqslant f(a) \leqslant n \\
>> &\implies -1 \leqslant f(a) - 1 \leqslant n - 1 \\
>> &\implies -m \leqslant n(f(a) - 1) \leqslant m(n - 1) \\
>> &\implies 0 \leqslant n(f(a) - 1) + g(b) \leqslant mn
>> \end{align}
>> $$
>> Hence, the image of $h$ is equal to $\mathbb{N}_{nm}$. 
>
> Proof.
> 
> By induction on $n$. Suppose $n = 1$. By reflexivity of cardinality, $\prod_{i=1}^1 |A_i| = |A_1| = |A|$. Hence $\exists N \geqslant 1$ such that the proposition holds.
> 
> Now suppose $n = N + 1$. Then by inductive hypothesis we have $\prod_{i=1}^{n+1} |A_i| = |A \times \dots \times A_n| * |A_{n+1}|$. By the above lemma, we see that $|A \times \dots \times A_n| * |A_{n+1}| = |A \times \dots \times A_{n+1}|$.
> 
> $\blacksquare$
