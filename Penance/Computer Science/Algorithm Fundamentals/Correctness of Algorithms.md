We want to be able to prove that our algorithms are correct beyond the empirical evidence of automated testing or peer review. In general we want to establish **pre-conditions** and show that certain **post-conditions** hold throughout the execution of the algorithm.

> [!info] Definition
> - **pre-condition** - Propositions we expect to be true before execution
> > [!example]
> > $a$ is a nonnegative integer.
> - **post-condition** - Conditions that must hold after the algorithm is complete
> > [!example]
> > $s = \sum_{i=1}^n i$

If these propositions hold, then the algorithm is correct.

## Quotient Remainder Theorem

Consider the following algorithm that computes the remainder of $a/b$.

```Python
def remainder(a, b):
	q = a // b
	p = q * b
	r = a - p

	return r
```

We introduce a theorem in order to prove the above algorithm in mathematical terms:

> [!abstract] Quotient Remainder Theorem
> if $n,d \in \mathbb{Z}^+$, $\exists! q, r \in \mathbb{Z}$ such that $n = d * q + r, 0 \leq r \lt d$.

### Proving our Algorithm

We establish the following terminology for clarity:

$$
\begin{align}
&a \; div \; b &\text{quotient} \\
&a \; mod \; b &\text{remainder}
\end{align}
$$

Breaking down `remainder` line by line:

1. `q = q // b`. Then $q = a \; div \; b$ by assignment. By QRT and definition of $div$, $a = b * q + R, R \in \mathbb{Z}, 0 \leq R \le b$. By algebra:

$$
q = \frac {a-R} b
$$

2. `p = q * b`. By assignment, $p = q * b$. Then by substitution:

$$
p = \frac {a-R} b * b = a - R
$$

3. `r = a - p`. Then $r = a - p = a - a - R = R$ by assignment and substitution. Therefore, by definition of modulo, $r = a \mod b$ (remainder). $\blacksquare$

## Loops

For algorithms involving iteration, we want to establish a **loop invariant** and proceed to show this proposition holds for some initial conditions and after the loop terminates.

> [!info] Loop Invariant
> A predicate whose argument N is the number of iterations of the loop such that:
> - $I(0)$ establishes the **basis**.
> - $I(N) \implies I(N+1)$ using the **[[Induction|inductive hypothesis]]**.
> - $I(N)$ implies the post-condition of the algorithm
> - The loop terminates.

### Arithmetic Sum

Consider the following program that computes the sum $1 + 2 + \dots + n$ (arithmetic sum):

```Python
def arithSum(n):
	s = 0
	i = 1

	while i < n:
		s += i
		i += 1

	return s
```

Thus we establish the post-conditions of $s = \sum_{i=1}^N i$.

> [!abstract] for all $N \in \mathbb{Z}$, arithSum computes $\sum_{i=1}^N i$
> Proof. Suppose $n \in \mathbb{Z}$. For $n = 0$, $s = 0 = \sum_{i=1}^0 i$ by assignment. Hence, $I(0)$ holds and $\exists N \geq 0, I(N)$.
> Let $i_n, i_{n+1}$ be the value of $i$ after $n$ and $n+1$ iterations, respectively, and define $s_n, s_{n+1}$ similarly. Now consider
> $$
> \begin{align}
> s_{n+1} &= s_n + i_n \\
> &= \sum_{i=1}^n i + i_n &\text{I.H} \\
> &= \sum_{i=1}^n i + i + 1 &\text{Substiution} \\
> &= \sum_{i=1}^{n+1} i &\text{Definition}
> \end{align}
> $$
> Therefore, we have shown that $I(N) \implies I(N+1)$ and so the post-condition of the algorithm is satisfied.
> Finally, since $i_{N} = N + 1 \not \lt N$, the guard of the loop will fail and the algorithm will terminate. Thus the algorithm is correct.
> $\blacksquare$

### Find Minimum

Consider an algorithm that finds the minimum element in an array:

```Python
def findMin(A):
	min = A[0]
	i = 1

	while i < len(A):
		if min < A[0]:
			min = A[0]
		i++

	return min
```

> [!abstract] findMin(A) returns the minimum element of A
> Proof. Suppose A is a nonempty array of integers and define $A[i..j]$ as:
> $$
> A[i..j] = \{ A_k : i \leq k \lt j \}
> $$
> additionally define "minimum" as:
> $$
> x = min(A) \iff \forall y \in A, x \leq y
> $$
> Suppose $|A| = 1$, then $min = A[0]$ since clearly $A[0] \leq A[0]$. Hence $\exists n \geq 1$ such that $min$ is the minimum of $A[0..n]$
> Now define $min_n, min_{n+1}$ as the value of $min$ after $n$ and $n+1$ iterations, respectively and define $i_n, i_{n+1}$ the same way. Then for $min_{n+1}$ we consider the two cases over $min_n$ and $A[i_n]$.
>
> ($min_n \leq A[i_n]$): Then $min_{n+1} = min_n$. Let $x \in A[0..i_{n+1}]$, then either $x = A[i_n] = min_{n+1}$ (by substitution) or $x \in A[0..i_n]$ and so $min_{n+1} = min_n \leq x$ by inductive hypothesis.
>
> ($min_n \gt A[i_n]$): Then $min_{n+1} = A[i_n]$ by assignment. Clearly $min_{n+1} = A[i_n] \leq A[i_n]$, so let $x \in A[0..i_n]$. By the inductive hypothesis and substitution, $min_{n+1} \leq min_n \leq x$, and so $min_{n+1}$ is the minimum of $A[0..i_{n+1}]$.
>
> Thus, in either case $min_{n+1}$ is the minimum of $A[0..i_{n+1}]$ and so the inductive case is shown. Finally, after $N = |A|$ iterations, $i_{n+1} = i_{n} + 1 \implies i = N + 1 \not \lt N$, and so the loop terminates and the proof is complete.
> $\blacksquare$

## Additional Example

We prove `divisionAlg` the straightforward way to show that the constructivist methodology holds:

```Python
def divisionAlg(n, d):
	r = n
	q = 0

	while r >= d:
		r = r - d
		q = q + 1

	return (q, r)
```

> [!abstract] Correctness of divisionAlg
> **Proof.**
> Suppose $n, d \in \mathbb{Z}+ \; q, r \in \mathbb{Z}$ such that $n = dq + r$. By induction on $k$, where $k$ is the number of iterations of the loop. Suppose $k = 0$, then
> $$
> \begin{align}
> n &= dq + r \\
> &= d(0) + n \\
> &= n
> \end{align}
> $$
> Hence, the invariant holds for $k = 0$ and thus $\exists K \geq 0$ such that $n_K = dq_K + r_K$. Now consider $K = k + 1$. We must show that $n = dq_{k+1} + r_{k+1}$.
>
> We start by noticing the values of $q_{k+1}, r_{k+1}$:
> $$
> \begin{align}
> &r_{k+1} = r_k - d \\
> &q_{k+1} = q_k + 1
> \end{align}
> $$
> So then by substitution:
> $$
> \begin{align}
> dq_{k+1} + r_{k+1} &= d(q_k + 1) + r_k - d \\
> &= dq_k + r_k \\
> &= n &\text{I.H}
> \end{align}
> $$
> Thus we have shown the loop invariant holds for the inductive step, and the proof is complete.
>
> $\blacksquare$