Modern [[Set Theory|Set Theory]] is carefully constructed to avoid paradoxes arising from its axioms. One such paradox is Russel's Paradox:

Suppose $S$ is a set, and construct $R_s$ as follows:

$$
R_s = \{ a \in S : a \not \in a \}
$$

Take $S$ to be the "set of all sets". We notice that $R_s \in S$ since $S$ contains all sets by assumption. Now because $R_s$ is defined as the set of elements in $S$ that do not contain themselves, we see a contradiction arises:

Since $R_s \in S$, we want to know if $R_s \in R_s$.

> [!tip]
> It was helpful for me to visualize $S = \{\dots, R_s, \dots\}$, and make the direct connection that if $R_s \in S$, then it could be substituted for $a$ in
> $$
> R_s = \{ a = R_s \in S : a \not \in a \}
> $$
> which is where we arrive at the paradox.

1. Suppose not, then $R_s \not \in R_s$, but since $R_s \in S$, and by assumption, $R_s$ does not contain itself, then it must be in $R_s$, a contradiction.
2. Suppose $R_s \in R_s$, then $R_s$ must be an element of $S$ that does not contain itself, again contradicting our assumption.

## Can a Set contain its Powerset?

> [!abstract] Theorem 13.1. If $A$ is a set, then $\mathcal{P}(A) \not \subseteq A$.
> Proof.
> Suppose $A$ is a set, and suppose $\mathcal{P}(A) \subseteq A$. Let $B = \{ a \in A : a \not \in a\}$. Then $B \in \mathcal{P}(A)$ since $B \subseteq A$ by definition, and so $B \in A$.
> Now we consider two cases of $B \in B$:
> 1. Suppose $B \in B$, then $B$ is an element of $A$ that contains itself, a contradiction.
> 2. Suppose $B \not \in B$, then $B \in A$, but does not contain itself, another contradiction.
>
> Thus we have arrived at a contradiction, and therefore $\mathcal{P}(A) \not \subseteq A$. $\blacksquare$