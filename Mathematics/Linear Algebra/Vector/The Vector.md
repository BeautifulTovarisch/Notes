## History
Vector analysis was invented by Josiah Gibbs. Previously quaternions, invented by *something something* Hamilton.

> [!note]- Quaternions 
> represent transformations in plane over the **Complex Field**
> > [!todo] Add mind map link

Vector analysis became more popular due to its convenience, but quaternions are still used in computer graphics (e.g gimbal-lock free rotations)

## What is a Vector?

> [!info] Definition 2.1.1
For a field $F$ and a positive integer $n$ , a vector with $n$ entries, each belonging to $F$ is called an $n$-vector over $F$. The set of $n$-vectors over $F$ is denoted $F^{n}$

### Vectors are Functions

We can treat vectors as a mapping from a **preimage** to an **image.**
> [!todo] Add mind map to (eventual) discrete math notes here.

#### Example
Consider a document to be a multiset of words. Let WORDS be the set of words. We have $$ f : WORDS -> R $$ defining a WORDS-vector over the Real Numbers.

#### Sparsity

We say a vector is sparse is most of its values are 0. If no more than $k$ entries are nonzero, we say the vector is $k$-sparse.

##### Applications of Sparsity
- Compression
- Low-rank matrix analysis
- Principal component analysis

> [!todo] Add links to descriptions of these

### What can we Represent as Vectors?

- Binary Strings:  10111011 $<=>$ an $n$-bit vector over $GF(2)$
- Attributes: name -> value
- State of a System: $\{(0,1): 1, (0,2): 0, ..., (0, n): 1\}$
- Probability Distribution
- Images: A pixel $(i, j)$ maps to the relative "intensity" at the point in the image: 
	- $f = \{(i, j) : 0 \leqslant i < 1024, 0 \leqslant j < 768 \}$
	- $f : R\times R \rightarrow R$
- Points in space

### Vector Addition

> [!info] Definition 2.4.1
> Given $n$-vectors $u, v$:
> $u + v = [u_1 + v_1, u_2 + v_2, ..., u_n + v_n]$

### Scalar Multiplication

> [!info] Definition 2.5.1
> Given $n$-vector $u$ and a scalar $\alpha$:
> $\alpha u = \alpha [u_1, u_2, ..., u_n] = [\alpha u_1, \alpha u_2, ..., \alpha u_n]$

#### Associativity

$\alpha (\beta u) = (\alpha \beta) u$

> [!abstract] Proof.
> By definition of scalar multiplication:
> $$\begin{aligned}
> \alpha (\beta u) &= \alpha [\beta u_1, ..., \beta u_n] \\
> &= [\alpha \beta u_1, ..., \alpha \beta u_n] \\
> &= (\alpha \beta) u
> \end{aligned}$$
> $\blacksquare$
