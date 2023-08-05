A function $f$ is a relation defined as a mapping from a domain to a co-domain. It imposes the stricter requirement such that each element in the domain is mapped to exactly one in the co-domain (i.e f(x) = exactly one y).

> [!info] Well-Defined Relation
> We say a relation over $A \times B$ is **well-defined** if and only if every $a \in A$ is related to **exactly one** $b \in B$. We call $A$ the **domain** and $B$ the **co-domain**. Such a relation meets the qualifications to be a **function**, written $f : A \to B$ and whose definition is denoted $f(x)$. 

> [!example]
> Let $A = \{ 1, 2, 3 \}$, $B = \{ 5, 6, 7\}$, and $f = \{ (1, 5), (2, 5),(1, 7) \}$. Then $f$ **is not** a function for two reasons:
> 
> 1. $1 \in A$ is related to both $5, 7 \in B$
> 2. $3 \in A$ is not related to any $b \in B$

> [!info] Equality
> We say two functions $f, g$ are equal if and only if they map the same domain to the same co-domain. In other words, $\forall x \in X \; f(x) = g(x)$.

> [!abstract] Example
> $f(x) = x^2 - 4$ is equal to $g(x) = \frac {(2x - 4)(x + 2)} 2$
> 
> Proof.
> By algebra:
> $$
> \begin{align}
> f(x) &= x^2 - 4 \\
> &= (x + 2)(x - 2) &\text{completing the square} \\
> &= \frac 2 2 (x + 2)(x - 2) &\text{identity} \\
> &= \frac {(2x + 4)(x - 2)} 2 = g(x) \\
> &&\blacksquare
> \end{align}
> $$

## Image

The image of a function differs from the co-domain in that it is the subset of values that are *actually* mapped under $f$. In other words, the image is the values in the co-domain for which $f(x)$ exists.

> [!info] Image of a Function
> Suppose $f : X \to Y$ is a function. We say the **image** of $f$, denoted $f(X)$ is the set
> $$
> f(X) = \{ y \in Y : \exists x \in X, f(x) = y \}
> $$
> We note that $f(X) \subseteq Y$.
> 
> We define the **inverse image** or **pre-image** of $f$, written $f^{-1}(Y)$ as
> $$
> f^{-1} = \{ x \in X, f(x) \in Y \}
> $$
> 
> In other words, the set of values in $X$ that map to the **image**

## Properties of Functions

### Injectivity

We say a function is **one to one** or **injective** if the mapping from its domain to its co-domain is **unique**. In other words, for a given element in the co-domain, there is exactly one corresponding element in the domain.

> [!info] One-to-One (Injective)
> Suppose $f: X \to Y$ is well-defined. We say $f$ is **one-to-one** or **injective** if and only if for $x_1, x_2 \in X$, if $f(x_1) = f(x_2)$, then $x_1 = x_2$.
> 
> The contrapositive form is also useful in proofs and understanding the concept:
> If $x_1 \neq x_2$, then $f(x_1) \neq f(x_2)$.

### Surjectivity

When a function is **surjective** or **onto**, the image of its domain is the **entire co-domain**. In other words, every element in the co-domain is sent from some element in the domain.

> [!info] Onto (Surjective)
> Suppose $f: X \to Y$ is well-defined. We say $f$ is **onto** if and only if for every $y \in Y, \; \exists x \in X, f(x) = y$.

When a function is both injective and surjective, we say it is bijective or a one-to-one correspondence.

## Cardinality

## Inverse