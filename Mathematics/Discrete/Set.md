> [!todo]
> Need to review this entire section and jot down descriptive notes, proofs, laws etc. for posterity.

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

## Basic Definitions

$$
\begin{align}
X^\complement &= \{ x \mid x \not \in X \} &\text{Complement} \\ \\
X - Y &= \{ x \mid x \in X, x \not \in Y \} &\text{Difference} \\ \\
\mathcal{P}(A) &= \{ A' \mid A' \subseteq A \} &\text{Power Set} \\ \\
X \times Y &= \{ (x, y) \mid x \in X, y \in Y \} &\text{Cartesian Product}
\end{align}
$$

## Laws

> [!abstract]- Distributivity
> $$
> X \cup (Y \cap Z) = (X \cup Y) \cap (X \cup Z)
> $$
> 
> Proof.


> [!todo]
> Collect set laws here


## Miscellaneous

### Program to Compute Powerset

```python
def powerset(A):
	'''
	powerset(A) computes the powerset of set [A]

	Parameters:
		A (list): An arbitrary set of elements

	Output:
		The powerset of [A]

	Example:
		A = [1, 2, 3]

		powerset(A) 
		=> [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
	'''
	pset = [[]]

	for a in A:
		for s in pset:
			pset = pset + [[a] + s]

	return pset

def addToSets(x, AA):
	'''
	addToSets(x, AA) appends element [x] to each set in [AA]

	Parameters:
		x (T): Arbitrary element
		AA (list[]): A list of sets

	Output:
		The set AA such that every element in AA has [x] appended

	Example:
		addToSets(1, [[0], [2, 3], [1, 2, 3]])
		=> [[0, 1], [2, 3, 1], [1, 2, 3, 1]]
	'''
	if AA == []:
		return []

	return [A[0] + x] + addToSets(x, AA[1:])	

# Recursive implementation. The trick to understanding this is to think about the powerset as a union between the sets that contain some arbitrary element a and those that do not.
def powerset_recur(A):
	if A == []:
		return [[]]

	return powerset_recur(addToSets(A[0], A[1:])) + powerset_recur(A[1:])
```