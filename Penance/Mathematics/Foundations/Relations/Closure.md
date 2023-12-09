## Transitive Closure

We want to find the **smallest relation** $R^T$ that expresses transitivity over a relation $R$.

> [!info] Transitive Closure
> Suppose $R$ is a relation defined over a set $A$. Then the **transitive closure** of $R$, $R^T$ is defined by the following rules:
> 1. $R^T$ is transitive
> 2. $R \subseteq R^T$
> 3. For any transitive set $S$, if $R \subseteq S$, then $R^T \subseteq S$

> [!abstract] Theorem.
> The transitive closure of relation $R$ is unique.
>
> Proof.
> Suppose $S, T$ are relations that satisfy the criteria for transitive closure. Then $S, T$ are transitive by property 1 and $R \subseteq S, R \subseteq T$ by property 2. Then by property 3, since $R \subseteq S$, $T \subseteq S$, and also $S \subseteq T$ by the same argument. Therefore $S = T$ by definition of set equality.
>
> $\blacksquare$

We now provide a definition of the transitive closure of $R$ by introducing an [[Induction#Iterated DeMorgan's|iterated union]] of relations.

> [!abstract] Theorem
> If $R$ is a relation over set $A$, then,
> $$
> R^\infty = \bigcup_{i=1}^\infty R^i = \{ (x, y) : \exists i \in \mathbb{N}, (x, y) \in R^i \}
> $$
> $R^\infty$ is the transitive closure of $R$.
>
> Proof.
> Suppose $R$ is a relation over set $A$ and further suppose $a, b, c \in A, \; (a, b), (b, c) \in R^\infty$. Then by definition $\exists i, j \in \mathbb{N}$ such that $(a, b) \in R^i$, $(b, c) \in R^j$ and by definition of [[Relations#Properties of Relations | relation composition]] $R^j \circ R^i = R^{i+j}$. So then because $R^{i+j} \subseteq R^\infty$, $R^\infty$ is transitive.
>
> Now suppose $a, b \in A$ and $(a, b) \in R$. Since $R = R^1$, we know that $(a, b) \in R^\infty$ and so $R \subseteq R^\infty$.
>
> For the third part of the definition, suppose $S$ is a transitive relation over $A$ and $R \subseteq S$. We will proceed by induction on $i$ to show that $R^\infty \subseteq S$. Suppose $i = 1$, then $R^i = R^1 = R \subseteq S$ by assumption. Hence $\exists I \in \mathbb{N} \geq 1$ such that $R^I \subseteq S$.
>
> Suppose $I = i + 1$. Then for $R^{i+1}$ we notice that $\exists j, k \in \mathbb{N}, j,k \lt i + 1$ such that $R^j \circ R^k = R^{i+1}$, and so for some $c \in A$, $(a, b) \in R^k$ $(b, c) \in R^j$ and hence $(a, b), (b, c) \in S$ by inductive hypothesis. Since $S$ is transitive, $(a, c) \in S$ and therefore $R^\infty \subseteq S$ and therefore $R^\infty$ is the transitive closure of $R$.
>
> $\blacksquare$

> Proof makes no damn sense.

## Reflexive Closure

The reflexive closure is defined similarly:

> [!info] Reflexive Closure
> Suppose $R$ is a relation on $A$. We define the **reflexive closure**, $R^R$ as the relation satisfying the following:
> 1. $R^R$ is reflexive.
> 2. $R \subseteq R^R$
> 3. For reflexive relation $S$, if $R \subseteq S$, then $R^R \subseteq S$.
>
> That is, $R^R$ is the minimal reflexive superset of $R$.

We identify and prove the unique reflexive closure of $R$.

> [!abstract] Theorem.
> If $R$ is a relation over set $A$, then $R \cup I_A$ is the unique reflexive closure over $R$.
>
> Proof.
> Suppose $R$ is a relation over $A$ and let $R^R = R \cup I_A$. By definition of $I$, $(a, a) \in R U I_A$ for every $a \in A$ so $R^R$ is reflexive. Next see, that by set laws $R \subseteq R \cup I_A$. Hence, $R^R$ satisfies properties 1 and 2.
>
> Now consider a reflexive relation $S$ and assume $R \subseteq S$. Then $R \cup I_A \subseteq S$, (since $S$ is reflexive it must contain all of $I_A$). Hence $R^R \subseteq S$ and satisfies the 3rd property.
>
> To show that $R^R$ is unique, we proceed by similar argument to the uniqueness of the transitive closure. Assume $S, T$ are reflexive closures of $R$. Then by the properties of the reflexive closure, $R \subseteq S \implies T \subseteq S$ and $R \subseteq T \implies S \subseteq T \implies S = T$.
>
> $\blacksquare$

## Symmetric Closure

> [!info] Symmetric Closure
> Suppose $R$ is a relation over set $A$. We define the **symmetric closure** as a relation such that:
> 1. $R^S$ is symmetric
> 2. $R \subseteq R^S$
> 3. For any symmetric relation $S$, if $R \subseteq S$, then $R^S \subseteq S$.

> [!abstract] Theorem.
> $R \cup R^{-1}$ is the **unique** symmetric closure of $R$.
>
> Proof.
> Suppose $R$ is a relation over set $A$. Then by $R \subseteq R \cup R^{-1}$ by set laws and by definition of inverse for all $(a, b) \in R$, $(b, a) \in R \cup R^{-1}$, so the union is symmetric and so properties 1 and 2 are satisfied.
> Next suppose $S$ is a symmetric relation and $R \subseteq S$. Since $S$ is symmetric, $R^{-1} \subseteq S$ and so $R \cup R^{-1} \subseteq S$ by properties of set union.
>
> To show the symmetric closure is unique we suppose $S, T$ are symmetric closures over $R$. Then by properties 1 and 2, $R \subseteq S$, $R \subseteq T$, and both relations are symmetric. Then by property 3, $S \subseteq T$ and $T \subseteq S$. Hence $S = T$.
>
> $\blacksquare$

```Python
def isRelated(a, b, relation):
    if relation == []:
        return False

    return (a, b) == relation[0] or isRelated(a, b, relation[1:])

def missingPairs(relation):
	'''
	missingPairs(relation) computes the "missing" symmetric pairs required to satsify symmetry for [relation].

	Parameters:
		relation (tuple[]): A list of ordered-pairs forming a relation R.

	Output:
		The ordered-pairs required to make [relation] symmetric or [] if [relation] is already symmetric.
	'''
    def testOnePair(p, rel):
        if rel == []:
            return []

        (a, b) = p

        if not isRelated(b, a, relation):
            return [(b, a)]

        return testOnePair(p, rel[1:])

    def recur(rel):
        if rel == []:
            return []

        return testOnePair(rel[0], relation) + recur(rel[1:])

    return recur(relation)

def symmetricClosure(relation):
	'''
	symmetricClosure(relation) computes the unique symmetric closure of [relation]

	Parameters:
		relation (tuple): A list of ordered-pairs defining a relation.

	Output:
		The unique symmetric closure of [relation]
	'''
    pairs = missingPairs(relation)

    if pairs == []:
        return relation

    return symmetricClosure(pairs + relation)
```