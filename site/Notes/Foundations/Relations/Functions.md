# Functions

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

Cardinality broadly refers to the "number of elements" in a set. The rigorous definition, however, is defined in terms of two sets having the "same cardinality" if and only if there exists a bijection between them.

> [!info] Cardinality
> Two sets, say, $X$ and $Y$ have the same **cardinality** if and only if there exists a bijection between them. We denote the cardinality **relation** (see proof below) by two vertical pipes (e.g $|A|$).

This allows us to define the notion of a "finite set" with cardinality $n$.

> [!info] Cardinality of a Finite Set
> Suppose $A$ is a set. Then we say $A$ is finite if and only if there exists a bijection between $A$ and $\{ 1, \dots, n \mid n \in \mathbb{N} \}$.

This deceptively simple definition lets us prove some intuitive properties which are nonetheless difficult to formally deduce:

> [!warning]
> This proof is fairly complicated.

> [!abstract] Theorem
> If $A, B$ are finite, disjoint sets, then $|A \cup B| = |A| + |B|$.
>
> TODO

## Inverse

We say $f$ has an inverse if and only if it is a bijection. The intuitive reasoning behind this is that if it were not the case that $f$ was a bijection, then the relation computing its pre-image would not be well-defined. In other words, $f^{-1}$ (pre-image) would not meet the requirements to be a function.

> [!info] Function Inverse
> Suppose $f: X \to Y$ is a bijection. Then we define its inverse to be:
> $$
> f^{-1} = \{ (y, x) \in Y \times X \mid f(x) = y \}
> $$

We now prove that because of the properties of a bijective function, that $f^-1$ is well-defined.

> [!abstract] Theorem.
> If $f: X \to Y$ is a bijection, then its inverse, $f^{-1}$ is well-defined.
>
> Proof.
> Suppose $f: X \to Y$ is bijective and further suppose $y \in f^{-1}$. Then by surjectivity of $f$, $\exists x \in X$ such that $f(x) = y$. Now see that for $x_1, x_2 \in X$, if $f(x_1) = f(x_2) = y$, then $x_1 = x_2$ by injectivity of $f$. Hence, $f^{-1}$ is well-defined by definition of a function.
>
> $\blacksquare$

## Composition

Function composition is intuitively similar to [[Relations#Manipulation|relation composition]].

> [!info] Function Composition
> Suppose $f: A \to B, g: B \to C$ are well-defined. Then
>$$
>g \circ f = \{ (a, c) \in A \times C \mid f(a) = b, \; g(b) = c \}
>$$

> [!abstract] Theorem.
> If $f: A \to B, g: B \to C$ are functions, then $g \circ f$ is well-defined.
>
> Proof.
> Suppose $f: A \to B, g: B \to C$ are well-defined and further suppose $a \in A$. Then $f(x) = b$ by definition and $g(b) = c$ by the same token. So then by definition of composition $g(f(a)) = g \circ f (a) = c$.
>
> Next suppose $(a, c_1),(a, c_2) \in g \circ f$. By definition of function composition $\exists a \in A \mid f(a) = b_1, \; f(a) = b_2$ and $g(b_1) = c_1, \; g(b_2) = c_2$. Then because $f$ is a function $b_1 = b_2$ and similarly $g(b_1) = g(b_2) \implies c_1 = c_2$ and so we have that $g \circ f$ is well-defined.
>
> $\blacksquare$

## Proofs of Properties under Composition

Many properties hold under composition, depending on the properties of $g$ and $f$.

### Injectivity

> [!abstract] Theorem.
> If $f: A \to B$ and $g: B \to C$ are injective, then so is $g \circ f: A \to C$.
>
> Proof.
> Suppose $f, g$ are injective and further suppose $a_1, a_2 \in A$ and $f(a_1) = f(a_2)$ Then by definition of function $\exists b_1, b_2 \in B \mid f(a_1) = b_1, f(a_2) = b_2$. Now see that $g(f(a_1)) = g(b_1) = c_1$ and $g(f(a_2)) = g(b_2) = c_2$ by definition of composition. But then by injectivity of $f$ and $g$, we have $a_1 = a_2, b_1 = b_2$ so then since $g(f(a_1)) = g(f(a_2)) = c_1 = c_2$, we see that $g \circ f$ is also injective.
>
> $\blacksquare$

### Surjectivity

> [!abstract] Theorem.
> If $f: A \to B$, $g: B \to C$ are surjective, then so is $g \circ f$.
>
> Proof.
> Suppose $b \in B, c \in C$. Then by definition of onto, $\exists a \in A$ such that $f(a) = b$ and $g(b) = c$. But then by definition of composition $g \circ f (a) = c$ and so $g \circ f$ is also onto.
>
> $\blacksquare$

### Identity and Equality of Inverse

> [!abstract] Theorem.
> Suppose $f: A \to B$ is a bijection and $g : A \to B$. Then $g = f^{-1}$ if and only if $g \circ f = i_A$.
>
> Proof.
> Suppose $g = f^{-1}$ and suppose $a \in A$. Then by definition of inverse and composition $g(f(a)) = a$ and so $g \circ f = i_A$ by definition of function equality.
>
> Now suppose $g \circ f = i_A$. Then $g(f(a)) = a$ by definition of identity, and so by definition of inverse $g = f^{-1}$.
>
> $\blacksquare$
