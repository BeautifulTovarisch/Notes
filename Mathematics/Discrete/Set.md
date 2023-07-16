Sets represent unordered, arbitrary collections.

> [!info] Axiomatic Foundations
> 1. Existence: There is a set with no elements called the empty (or null) set.
> 2. Extensionality: If every $x \in X$ is also in $Y$ and every $y \in Y$ is also in $X$, then $X = Y$

A fun proof that follows from the previous axioms:

> [!abstract] There is only one empty set
> Proof.
> 
> Suppose the contrary, that there is more than one empty set, say $\emptyset_1, \emptyset_2$. By axiom 1, we have that there is no element in either $\emptyset_1$ nor in $\emptyset_2$. But then by axiom 2 we notice that 
> $$\forall x \in \emptyset_1, x \in \emptyset_2$$
> $$\forall y \in \emptyset_1, y \in \emptyset_2$$
> which implies $\emptyset_1 = \emptyset_2$ and so we have contradicted the assumption that there is more than one empty set. 
> $\blacksquare$

## Laws

> [!todo]
> Collect set laws here