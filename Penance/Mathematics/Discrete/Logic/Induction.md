Induction is a proof technique which shows that for some $n \in \mathbb{Z}, I(n) \implies I(n+1)$. The idea is to establish a basis and proof the next step can be reached by assuming $I(n)$.

> [!info] General Structure of an Inductive Proof
> **Proof**. {reformulation of the theorem in terms of $n$}. "By induction on $n$"
> **Basis**: Suppose $n = 0$, ...{base case shown}... Hence, $\exists N \in \mathbb{N} \geq 0, I(N)$
> **Inductive Case**: Suppose $n = N + 1$. {show that the **inductive hypothesis** leads to $I(N+1)$} 
> $\blacksquare$

## Famous Counterexample

> [!abstract] All cows are the same color
> Proof. Let $I(n)$ be the proposition:
> > For any set of Cows, $C$, $\forall c_1, c_2 \in C, c_1 \neq c_2$, $c_1$ is the same color as $c_2$
> 
> **Basis**. Suppose we have one cow. Then clearly $I(1)$ holds because a cow is the same color as itself. Hence $\exists N \geq 1, I(N)$.
> 
> **Inductive Case**. Suppose we have a set of cows, $C$ such that $|C| = N+1$.  Notice for a arbitrary cow $c_1 \in C, |C - \{c_1\}| = N$, and so all the cows in $C - \{c_1\}$ are the same color by inductive hypothesis. Now choose $c_2 \in C$. We conclude the same about $C - \{c_2\}$ using the inductive hypothesis.
> > [!note]
> > There must be at least two cows since $N \geq 1 \implies N + 1 \geq 2$.
> 
> Thus, since both $c_1$ and $c_2$ are the same color as every cow in $C$, they too must also be the same color, and so we have shown $I(N+1)$ holds. $\blacksquare$

The issue with the above is that the use of the inductive hypothesis presumes $I(2)$ before establishing the inductive step, in other words, we "skip" over the case of $n = 2$ and presume the set $C$ has at least three cows before pulling one out and applying the inductive hypothesis. We can see for $n = 1$:

$C - \{c_1\}$ leaves only $c_2$, reducing us to the **basis**. The basis alone is not sufficient to conclude the inductive step between $n = 1$ and $n + 1 = 2$ (since clearly the claim is nonsensical) and so we cannot invoke the inductive hypothesis and the proof is invalid.

## Iterated DeMorgan's

We use induction to prove some DeMorgan's laws on a **iterated unions** and **intersections**.

>[!info] Iterated Union and Intersection
>$$
>\begin{align}
>&\bigcup_{i=1}^{n} A_i = A_1 \cup A_2 \cup \dots \cup A_n &\text{Iterated Union} \\ \\
>&\bigcap_{i=1}^{n} A_i = A_1 \cap A_2 \cap \dots \cap A_n &\text{Iterated Intersection}
>\end{align}
>$$

We want to prove that the complement of these iterated operations is structurally identical to DeMorgan's laws concerning propositional logic.

> [!abstract] Theorem. $\overline{\bigcup_{i=1}^n A_i} = \bigcap_{i=1}^n \overline{A_i}$
> Proof. By induction on $n$. Suppose $n = 1$, then trivially:
> $$
> \overline{\bigcup_{i=1}^1 A_i} = \overline{A_1} = \bigcap_{i=1}^1 \overline{A_i}
> $$
> Hence $\exists N \geq 1$ such that the proposition holds.
> Now suppose $A_1, A_2, \dots, A_{n+1}$ is a collection of $n+1$ sets. Then
> $$
> \begin{align}
> \overline{\bigcup_{i=1}i^{n+1} A_i} &= \overline{\bigcup_{i=1}i^n A_i \cup A_{n+1}} \\
> &= \overline{\bigcup_{i=1}^n A_i} \cap \overline{A_{n+1}} &\text{<Set Law>} \\
> &= \bigcap_{i=1}^n \overline{A_i} \cap \overline{A_{n+1}} &\text{I.H.} \\
> &= \bigcap_{i=1}^{n+1} \overline{A_i} &\text{By Definition}
> \end{align}
> $$

Therefore we have shown that $I(N+1)$ holds under mathematical induction. $\blacksquare$

## Example

A fun example. Noting this down since I keep forgetting the "add zero" trick of manipulating expressions.

> [!abstract] $x - 1 | x^n-1$ for all $n \in \mathbb{N}$
> Proof. By induction on $n$. Let $n = 0$, then:
> $$
> \begin{align}
> x^n - 1 &= x^0 - 1 = 0
> \end{align}
> $$
> so $x - 1 | x^n - 1$ since every integer divides 0. Hence $\exists N \geq 0, I(N)$.
> Now suppose $n = N + 1$. Then,
> $$
> \begin{align}
> x^{n+1} - 1 &= x^{n+1} + x^n - x^n - 1 \\
> &= (x-1)x^n + x^n - 1
> \end{align}
> $$
> Now $x-1|(x-1)x^n$, and by inductive hypothesis $x-1|x^n-1$, so we must show that $a|b, a|c \implies a | b + c$.
> 
> > [!abstract] Lemma a. $a|b, a|c \implies a | b + c$
> > Proof. Suppose $a, b, c \in \mathbb{N}$, and $a|b, \; a|c$. Then,
> > $\exists k, j \in \mathbb{N}$ such that, $ak = b, aj = c$. So then, $b + c = ak + aj = a(k + j)$.
> > $\blacksquare$
> 
> Now by Lemma a. we have shown that if $x-1|x^n -1$ and $x-1|(x-1)x^n$ implies $x-1|(x-1)x^n + x^n - 1$, and so the theorem holds by mathematical induction.
> $\blacksquare$.
