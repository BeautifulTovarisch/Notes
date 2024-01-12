If $A, B$ are sets, we define a **relation** $R$ as a subset of $A \times B$. For $a \in A, \; b \in B$, if $(a, b) \in R$, we say "$a$ is related to $b$".

## Manipulation

Some objects that can be computed from a given relation:

$$
\begin{align}
&I_A = \{ (a, a) : a \in A \} &\text{Identity} \\ \\
&\mathcal{I}_R = \{ b \in B : (a, b) \in R \} &\text{Image} \\ \\
&R^{-1} = \{ (b, a) \in B \times A : (a, b) \in R \} &\text{Inverse} \\ \\
& R \circ S = \{ (a, c) : \exists b \in B, \; (a, b) \in R, (b, c) \in S \} &\text{Composition}
\end{align}
$$

## Properties of Relations

$$
\begin{align}
&\forall x \in X, (x, x) \in R &\text{Reflexive} \\ \\
&\forall x,y \in X, Y, \; \text{if} (x, y) \in R, \; (y, x) \in R &\text{Symmetric} \\ \\
&\forall x,y,z \in X, \; (x, y) \in R, (y, z) \in R, \text{then} \; (x, z) \in R &\text{Transitive} \\ \\
&\forall x,y \in X, (x, y) \in R \; \text{and} \; (y, x) \in R \implies x = y &\text{Antisymmetric}
\end{align}
$$

> [!info] Equivalence Relation
> An **equivalence relation** is a relation that is **reflexive**, **symmetric**, and **transitive**.

### Proofs using Properties of Relations

> [!abstract] The divides relation on $\mathbb{Z}^+$ is reflexive.
> **Proof**.
> Suppose $a \in \mathbb{Z}^+$. Clearly $a | a$, since $ak = a, k =1$. Therefore, the divides relation on $\mathbb{Z}^+$ is reflexive. $\blacksquare$
>
> **Corollary**. The divides relation is not reflexive on $\mathbb{Z}$
> Take $a = 0$, then $a \not \mid a$ since division by zero is undefined. $\blacksquare$

> [!abstract] The divides relation on $\mathbb{Z}$ is transitive.
> **Proof.**
> Suppose $a, b, c \in \mathbb{Z}$, and that $a \mid b$, $b \mid c$. We will show that $a \mid c$. By definition of divisibility:
> $$
> \begin{align}
> &b = ak \\
> &c = bj \\
> &= (ak)j \\
> &= a(kj)
> \end{align}
> $$
> and so because $k, j \in \mathbb{Z}$, we have $a \mid c$.
>
> $\blacksquare$

## Equivalence Relations

- $R$ on $\mathbb{Z}$ such that if $(a, b) \in R$, both $a, b$ are even or both are odd.
- Congruence modulo $n$
- $(f(x), g(x)) \in R$ if $f'(x) = g'(x)$

> [!abstract] Theorem.
> Let $R$ be a relation on $\mathbb{Z}$ defined as $(a, b) \in R$ if $a + b$ is even. Then $R$ is an equivalence relation.
>
> **Proof**. We must show that $R$ is reflexive, symmetric, and transitive. Suppose $a \in \mathbb{Z}$, then $(a, a) \in R$ since $a + a = 2a$, an even number and so $R$ is reflexive.. Now suppose $a, b \in \mathbb{Z}$, then if $(a, b) \in R$, so is $(b, a)$ because $a + b = b + a$ by commutativity, so then $R$ is symmetric. Finally, suppose $(a, b), (b, c)$ in $R$. Then $a + b = 2k$, $b + c = 2j$ and so $a + c = 2(k + j - b)$, which shows $R$ is transitive. Therefore $R$ is an equivalence relation.
>
> $\blacksquare$

> [!abstract] Theorem.
> If $R$ is an equivalence relation, then $R = R^{-1}$
> Proof.
> Suppose $R$ is an equivalence relation and recall:
> $$
> R^{-1} = \{ (b, a) \in B \times A : (a, b) \in R \}
> $$
> Suppose $(a, b) \in R$, then $(b, a) \in R$ because $R$ is symmetric by definition of equivalence relation. But then $(a, b) \in R^{-1}$ by definition of inverse. Now suppose $(b, a) \in R^{-1}$, by similar argument, $(b, a) \in R$ by symmetry and definition of inverse. Therefore, since $R \subseteq R^{-1}$ and $R^{-1} \subseteq R$, $R = R^{-1}$.
>
> $\blacksquare$

### Equivalence Relations and Partitions

The next theorem requires definitions that can be somewhat tricky:

> [!info] Relation Induced
> Let $X$ be a set and $P = \{ X_1, X_2, \dots X_n \}$ be a partition of $X$. Let $R$ be the relation defined such that if $(a, b) \in R$, then $\exists X_i \in P : a,b \in X_i$. We call $R$, the **relation induced** by $P$.

> I like to think of this as $aRb$ if they are both in the same set in $P$.

> [!info] Equivalence Class
> Suppose $R$ is an equivalence relation over $A$, and define $[a]$ to be the **image** of $a \in A$ under $R$. We call $[a]$ the **equivalence class** of $a$ under $R$. In other words, if $x \in [a]$, then $xRa$.

We want to use these definitions to prove the bidirectional relationship between partitions and collections of equivalence classes.

> [!abstract] Theorem.
> Let $A$ be a set, $P$ be a partition of $A$, and $R$ by the relation induced by $P$ over $A$. Then $R$ is an equivalence relation.
> **Proof.**
>
> Let $a \in A$, then $\exists A_i \in P : a \in A_i$. By definition of partition, $A_i$ is the unique subset containing $a$. But then by definition of relation induced, $(a, a) \in R$, and so $R$ is reflexive.
>
> Now suppose $a, b \in A$, $(a, b) \in R)$. then $a, b \in A_i : A_i \in P$ by definition of relation induced. Also, $(b, a) \in R$ by definition of relation induced, and so $R$ is symmetric.
>
> Finally, let $a, b, c \in A$, $(a, b), (b, c) \in R$ and so $a,b \in A_i, \; b, c \in A_j$ by relation induced. Further suppose $i \neq j$. We will show this leads to a contradiction, and therefore $(a, c) \in R$. By assumption $b \in A_i \cap A_j$, but by definition of partition, $A_i \cap A_j = \emptyset$, so $A_i = A_j$, and so by definition of relation induced, $(a, b), (b, c), (a, c) \in R$ and so it is transitive.
>
> $\blacksquare$

The following proof establishes as lemmas the fact that equivalence classes are disjoint (or equal).

> [!abstract] Theorem.
> Let $A$ be a set and $R$ be an equivalence relation on $A$. Then $\{ [a]: a \in A \}$ forms a partition over $A$.
>
> > [!abstract] Lemma a.
> > If $a, b \in A$, $aRb$, then $[a] = [b]$.
> >
> > **Proof.**
> > Suppose $a, b \in A$, $aRb$. We will show $[a] \subseteq [b]$, and $[b] \subseteq [a]$.
> >
> > $[a] \subseteq [b]$:  Suppose $x \in [a]$, then $xRa$ by definition. By assumption, $aRb$, so then $xRb \implies x \in [b]$ by transitivity, and so $[a] \subseteq [b]$.
> >
> > $[b] \subseteq [a]$: Suppose $x \in [b]$. By similar argument, $xRb, bRa \implies xRa \implies x \in [a]$ by symmetry and transitivity of $R$. Hence, $[b] \subseteq [a]$ and the proof is complete. $\blacksquare$
>
> Now we establish that distinct equivalence classes are disjoint:
>
>> [!abstract] Lemma b.
> > Suppose $[a], [b]$ are equivalence classes under equivalence relation $R$ defined over set $A$. Then either $[a] = [b]$ or $[a] \cap [b] = \emptyset$.
> >
> > **Proof.**
> > We will show that if $[a] \cap [b] \neq \emptyset$, then $[a] = [b]$. Suppose $a, b \in A$ and $[a] \cap [b] \neq \emptyset$, then $\exists x \in [a] \cap [b]$. But then $xRa, xRb$, so by symmetry and transitivity, $aRx, xRb \implies aRb$. Therefore by Lemma a. $[a] = [b]$. $\blacksquare$
> >
>
> Now we consider the set $\{ [a]: a \in A \}$. By the above lemmas, each $[a_1] : a_1 \in A$ is disjoint with every other $[a_i]: a_i \in A$, and so the set forms a partition of $A$.
>
> $\blacksquare$

## Computing Transitivity

This section concluded with a recursive algorithm for determining whether a relation is transitive.

> I found the book's algorithm to be needlessly confusing. This may be due to SML's pattern-matching which relies on method signature overriding rather than a distinct language construct.

```Python
def isRelated(a, b, relation):
	'''
	isRelated(a, b, relation) determines whether (a, b) is in [relation].

	Parameters:
		a, b (T): Arbitrary elements of sets A, B, respectively
		relation ([]tuple): List of ordered pairs defining some relation R over
		A x B

	Output:
		Whether (a, b) is in [relation]
	'''
    if relation == []:
        return False

    return (a, b) == relation[0] or isRelated(a, b, relation[1:])

def isTransitive(relation):
	'''
	isTransitive(relation) determines if [relation] is transitive.

	Parameters:
		relation ([]tuple): List of ordered pairs defining some relation R over
		A x B

	Output:
		Whether [relation] is transitive.
	'''
	def testOne(p, rel):
		if rel == []:
			return True

		(a, b) = p
		(c, d) = rel[0]

		rest = rel[1:]

		return (not b == c) or (isRelated(a, d, relation)) and testOne(p, rest)

	def recur(rel):
		if rel == []:
			return True

		return testOne(rel[0], relation[1:]) and recur(rel[1:])

	return recur(relation)
```

We produce another program which produces the pairs for which transitivity is not satisfied. In other words, if $(a, b), (c, d), b = c$, but $(a, d)$ is not found.

```Python
def isTransitive(relation):
	'''
	isTransitive(relation) determines if [relation] is transitive.

	Parameters:
		relation ([]tuple): List of ordered pairs defining some relation R over
		A x B

	Output:
		[] if [relation] is transitive. Otherwise a list of ordered pairs for
		which transitivity fails.
	'''
	def testOne(p, rel):
		if rel == []:
			return []

		(a, b) = p
		(c, d) = rel[0]

		rest = rel[1:]

		if (b == c) and not isRelated(a, d, relation):
			return [(a, d)]

		return testOnePair(p, rest)

	def recur(rel):
		if rel == []:
			return []

		return testOne(rel[0], rel[1:]) + recur(rel[1:])

	return recur(relation)
```