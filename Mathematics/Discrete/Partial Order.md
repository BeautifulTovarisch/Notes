A partial order is a [[Relations|relation]] that enforces some ordering on **comparable** elements. In other words, we want to establish a relation such that, for two elements, either one precedes the other or they are **unrelated**.

> [!info] Partial Order
> A **partial order** $R$ on a set $X$ is a relation that is
> 1. Reflexive
> 2. Transitive
> 3. Antisymmetric
>
> We call $X$ a **partially ordered set** or **poset**. A partial order is often denoted by the generic symbol $\preceq$.

We prove that $\subseteq$ is a partial order.

> [!abstract] Theorem.
> Let $A$ be any set of sets over the universal set $U$. Then $A$ is a poset under $\subseteq$.
> 
> Proof.
> Suppose $a \in A$. Then by definition of subset, $a \subseteq a$, and so $\subseteq$ is reflexive. Now suppose $a, b, c \in A$ and further that $a \subseteq b$, $b \subseteq c$. Then by transitivity of $\subseteq$, $a \subseteq c$, and so $\subseteq$ is transitive. Finally, for $a, b \in A$, if $a \subseteq b$ and $b \subseteq a$, then $a = b$ by definition of set equality, and so $\subseteq$ is antisymmetric. Therefore, $\subseteq$ is a partial order, and so $A$ is a poset.
> 
> $\blacksquare$

## Comparability

For a given set and partial order $\preceq$, we want to define the concept of two elements being "comparable" under $\preceq$. Elements that are not comparable are unrelated by $\preceq$ (i. e the ordered pair $(a, b) \not \in \preceq$). Additionally, once we have an ordering, we want to define the notion of "greatest" or "least" elements.

> [!info] Comparability
> Given a partial order $\preceq$ over set $A$, we say that $a, b \in A$ are **comparable** if and only if $a \preceq b$ or $b \preceq a$. If $a$ and $b$ are unrelated under $\preceq$, we say $a$ is **"incomparable"** to $b$. Additionally, we define the following terms:
> 
> - **maximal**: $a \in A$ is a **maximal** element if $\forall b \in A, b \preceq a$ or $a$ and $b$ are incomparable.
> - **minimal**: $a \in A$ is a **minimal** element if $\forall b \in A, a \preceq b$ or $a$ and $b$ are incomparable.
> - **maximum**: $a \in A$ is **the maximum** element if $\forall b \in A, b \preceq a$
> - **minimum**: $a \in A$ is **the maximum** element if $\forall b \in A, a \preceq b$
> 
> A poset may have **at most** minimum/maximum, but must have **at least** one minimal/maximal element.

We establish a lemma showing that if we remove one element from a poset, we still have a poset.

> [!abstract] Lemma
> If $A$ is a poset under partial order $\preceq$, then $A - \{ a \}$ is a poset under partial order $\preceq - \{(b, c) \in \preceq : b = a \; \text{or} \; c = a \}$
> 
> Proof. 
> Suppose $A$ is a poset under $\preceq$ and define $A' = A - \{a\}$ and $\preceq'$ to be $\preceq - \{ (b, c) \in \preceq : b = a \; \text{or} \; c = a \}$. We must show $\preceq'$ is a partial order.
> 
> Suppose $b \in A'$. Then by definition of set subtraction, $b \in A, b \neq a$ and so $b \in \preceq'$. By reflexivity of $\preceq$, $(b, b) \in \preceq'$, and so it is reflexive.
> 
> Next, suppose $b, c, d \in A'$ and $b \preceq' c, c \preceq' d$. Then $b, c, d \in A$ by definition of set difference and so $b \preceq c, c \preceq d \implies b \preceq d$ by transitivity. Also, $b \neq a, d \neq a$ by set difference, and so $b \preceq' d$. Hence $\preceq'$ is transitive.
> 
> Finally, suppose $b, c \in A'$, $b \preceq' c, c \preceq' d$. Then again by set difference $b, c \in A$ and by antisymmetry of $\preceq$, $b = c$. Thus, $\preceq'$ is antisymmetric, and so the relation is a partial order.
> 
> $\blacksquare$