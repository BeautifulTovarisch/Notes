Sets represent unordered, arbitrary collections.

> [!info] Axiomatic Foundations
> 1. Existence: There is a set with no elements called the empty (or null) set.
> 2. Extensionality: If every $x \in X$ is also in $Y$ and every $y \in Y$ is also in $X$, then $X = Y$

A fun proof that follows from the previous axioms:

> [!abstract] Theorem.
> There is only one empty set
> 
> Proof.
> Suppose the contrary, that there is more than one empty set, say $\emptyset_1, \emptyset_2$. By axiom 1, we have that there is no element in either $\emptyset_1$ nor in $\emptyset_2$. But then by axiom 2 we notice that 
> $$\forall x \in \emptyset_1, x \in \emptyset_2$$
> $$\forall y \in \emptyset_1, y \in \emptyset_2$$
> which implies $\emptyset_1 = \emptyset_2$ and so we have contradicted the assumption that there is more than one empty set. 
> $\blacksquare$

## Basic Definitions

> I've omitted the trivial set operations, such as union and intersection, but may add them later.

$$
\begin{align}
X^\complement &= \{ x \mid x \not \in X \} &\text{Complement} \\ \\
X - Y &= \{ x \mid x \in X, x \not \in Y \} &\text{Difference} \\ \\
\mathcal{P}(A) &= \{ A' \mid A' \subseteq A \} &\text{Power Set} \\ \\
X \times Y &= \{ (x, y) \mid x \in X, y \in Y \} &\text{Cartesian Product}
\end{align}
$$

[Powerset Implementation](./powerset.ipynb)

## Laws

Much like integrals, having a cookbook of set identities is very helpful when trying to reduce a more complicated proof into known forms.

> [!abstract]- Associativity of Intersection and Union
> 
> > [!abstract] Union
> > $A \cup (B \cup C) = (A \cup B) \cup C$
> > 
> > Proof.
> > Suppose $x \in A \cup (B \cup C)$, then either $x \in A$ or $x \in (B \cup C)$. Suppose $x \in A$, then by definition of union $x \in (A \cup B)$ and so $x \in (A \cup B) \cup C$. Now suppose $x \in (B \cup C)$, then either $x \in (A \cup B)$ or $x \in C$, and so again $x \in (A \cup B) \cup C$.
> > 
> > Now to show the converse, suppose $x \in (A \cup B) \cup C$. Then $x \in (A \cup B)$ or $x \in C$. Then if $x \in C$, $x \in (B \cup C)$ and so is in the union on the left, and similarly if $x \in (A \cup B)$ it is also in the union.
> > 
> > Therefore, by definition of set equality $A \cup (B \cup C) = (A \cup B) \cup C$.
> 
> > [!abstract] Intersection
> > $A \cap (B \cap C) = (A \cap B) \cap C$
> > 
> > Proof.
> > Suppose $x \in A \cap (B \cap C)$, then $x \in A$ and $x \in (B \cap C)$. Then by definition of intersection, $x \in A, x \in B$, and so $x \in (A \cap B)$, and similarly since $x \in C$, $x \in (A \cap B) \cap C$.
> > 
> > Now to show the converse, suppose $x \in (A \cap B) \cap C$, then $x \in (A \cap B), x \in C$. So by definition of intersection, $x \in A, x \in B, x \in C$, and so $x \in A \cap (B \cap C)$. 
> > 
> > Therefore, by definition of set equality $A \cap (B \cap C) = (A \cap B) \cap C$.

> [!abstract]- $A \cap B \subseteq B$
> 
> Proof.
> By definition of intersection, $x \in A, x \in B$. But then clearly $x \in B$ and so $A \cap B \subseteq B$. $\blacksquare$

> [!abstract]- $X \cup (Y \cap Z) = (X \cup Y) \cap (X \cup Z)$ 
> 
> Proof.
> Suppose $a \in X \cup (Y \cap Z)$. Then by definition of union, we have $a \in X$ or $a \in Y, a \in Z$.
> 
> Suppose $a \in X$, then clearly $a \in (X \cup Y)$ and $a \in (X \cup Z)$ again by definition of union, so then $a \in (X \cup Y) \cap (X \cup Z)$ by definition of intersection. Now suppose $a \in (Y \cap Z)$. Then $a \in (X \cup Y)$ and $a \in (X \cup Z)$ by definition of union, and so by definition of intersection $a \in (X \cup Y) \cap (X \cup Z)$.
> 
> Thus, we see in either case, an arbitrary element from the left-hand side will be a member of the right-hand side, and so be definition of subset, $X \cup (Y \cap Z) \subseteq (X \cup Y) \cap (X \cup Z)$.
> 
> To prove the converse, suppose $a \in (X \cup Y) \cap (X \cup Z)$. Then $a \in X$, or $a \in Y, a \in Z$. By similar argument, $a \in (Y \cap Z)$ implies $a$ is in the left-hand side by definition of union, and likewise if $a \in X$. Thus $(X \cup Y) \cap (X \cup Z) \subseteq X \cup (Y \cap Z)$, and so by definition of set equality, the equivalence holds.
> 
> $\blacksquare$

> [!abstract]- $A \times (B \cup C) = (A \times B) \cup (A \times C)$
> 
> Proof.
> Suppose $(x, y) \in A \times (B \cup C)$. By definition of Cartesian product, $x \in A$ and $y \in B$ or $y \in C$. Suppose $y \in B$, then $(x, y) \in A \times B$ and so it is in the right-hand side by definition of union. Similarly, if $y \in C$, then $(x, y) \in A \times C$ and so it is also in the union. Thus, but definition of subset, $A \times (B \cup C) \subseteq (A \times B) \cup (A \times C)$.
> 
> Now suppose $(x, y) \in (A \times B) \cup (A \times C)$, then in either case $x \in A$, so we consider the cases of $y \in B$ and $y \in C$. Suppose $y \in B$, then $y \in (B \cup C)$ and so $(x, y) \in A \times (B \cup C)$. Similarly, if $y \in C$, then $y \in B \cup C$ and $(x, y) \in A \times (B \cup C)$. Thus $(A \times B) \cup (A \times C) \subseteq A \times (B \cup C)$.
> 
> Therefore, by definition of set equality: $A \times (B \cup C) = (A \times B) \cup (A \times C)$.
> 
> $\blacksquare$

> [!abstract]- $A \setminus B \subseteq \overline B$
> 
> Proof.
> Suppose $x \in A \setminus B$. Then $x \in A, x \not \in B$. Hence, by definition of set complement $x \in \overline B$. $\blacksquare$

> [!abstract]- $A \cap \overline B = A \setminus B$
> 
> Proof.
> Suppose $x \in A \cap \overline B$. Then $x \in A, x \not \in B$, by definition of set complement and intersection. But then by definition of set difference, $x \in A \setminus B$. 
> 
> Now suppose $x \in A \setminus B$, then by definition of set difference, $x \in A, x \not \in B$. But then by definition of set complement and intersection, $x \in A \cap \overline B$.
> 
> Therefore, since both sets are subsets of one another, $A \cap \overline B = A \setminus B$
> 
> $\blacksquare$

> [!abstract]- $A \cup (A \cap B) = A$
> 
> Proof.
> Suppose $x \in A \cup (A \cap B)$, then by definition of union, $x \in A$ or $x \in (A \cap B)$, and so $x \in A$ in either case.
> 
> Now suppose $x \in A$. Then clearly $x \in A \cup (A \cap B)$, by definition of union. $\blacksquare$

> [!abstract]- $\overline{A \cup B} = \overline A \cap \overline B$
> 
> Proof.
> Suppose $x \in \overline{A \cup B}$. Then by definition of union and set complement, $x \not \in A \cup B$, so then $x \not \in A$ and $x \not \in B$. But then by definition of complement and intersection, since $x \in \overline A, x \in \overline B \implies x \in \overline{A \cap B}$.
> 
> $\blacksquare$

> [!abstract]- $A \cup (A \cap B) = A$
> 
> Proof.
> Suppose $x \in A \cup (A \cap B)$. Then $x \in A$ in either situation, and so $A \cup (A \cap B) \subseteq A$. Now suppose $x \in A$. Then by definition of union $x \in A \implies x \in (A \cup (A \cap B)$ and so $A$ is also a subset of the left-hand side. $\blacksquare$

> [!abstract]- $A \cup (B - (A \cap B)) = \emptyset$
> 
> > [!abstract] Lemma.
> > $B - (A \cap B) = \overline A$ .
> > 
> > Proof.
> > Suppose $x \in B - (A \cap B)$. Then by definition, $x \in B, x \not \in A \cap B$. So then if $x \not \in (A \cap B)$, then either $x \not \in A$, or $x \not \in B$, but from the above, $x \in B$, so then $x \not \in A$ and by definition of set complement $x \in \overline A$.
> > 
> > Now we show the converse by supposing that $x \in \overline A$. Then by definition of set difference and set complement, $x \in B, x \not \in (A \cap B)$, and so $x \in B - (A \cap B)$.
> > 
> > Therefore, by set equality, $B - (A \cap B) = \overline A$. 
> > 
> > $\blacksquare$
>
> Proof.
> By the above lemma and previous results, $B - (A \cap B) = \overline A$ and $A \cup \overline A = \emptyset$.
> 
> $\blacksquare$

> [!todo]
> Collect set laws here