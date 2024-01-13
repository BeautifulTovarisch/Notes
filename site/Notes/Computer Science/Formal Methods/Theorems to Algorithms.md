# Theorems to Algorithms

[Constructive Proofs](https://en.wikipedia.org/wiki/Constructivism_(philosophy_of_mathematics)) Are particularly helpful in computer science as the mechanism of the proof produces a correct algorithm.

## Constructing the Division Algorithm

We recall the [[Correctness of Algorithms#Quotient Remainder Theorem]], $n = d*q + r, 0 \leq r \lt d$, and derive the following constraints:

$$
\left .
\begin{array}{c}
n = dq + r &\text{loop invariant}\\
r \geq 0 &\text{loop invariant}\\
r \lt d &\text{termination condition}
\end{array}
\right \} \text{Program Conditions}
$$

We want to construct a loop that maintains these invariants.

For initial values, we make an educated guess that $q = 0, r = n$ satisfies the first two conditions, since for $q = 0, n = 0 + r = n$. Then all that remains is the tasks of mutating $r$ and $q$ each iteration such that the algorithm reaches the third condition eventually while maintaining the invariants.

Notice that before the termination condition is met, $r \geq d$, then $\exists y \in \mathbb{Z}, r = d + y$. Using the Q.R.T:

$$
\begin{align}
n &= dq + r \\
&= dq + d + y \\
&= d(q + 1) + y
\end{align}
$$

Now we wish to compute $r_{n+1}, q_{n+1}$ in terms of $r_n, q_n$, respectively:

$$
\begin{align}
&r_{n+1} = y = r_n - d \\
&q_{n+1} = q_n + 1 \\
\end{align}
$$

And so we arrive at $n = dq_{n+1} + r_n$. Since our computation of $r_{n+1},q_{n+1}$ maintains the required conditions, our algorithm is correct.

## Euclidean Algorithm

We want to compute the Greatest Common Divisor (gcd) of two integers.

> [!info] Greatest Common Divisor
> Suppose $a, b \in \mathbb{Z}$, then there is some $d \in \mathbb{Z}^+$ such that:
> 1. $d | a, d | b$
> 2. For all $c$ such that $c|a, a|b$, $c|d$
>
>  In other words, $d$ is the **greatest integer** that **divides both** $a$ and $b$.

### Mathematical Foundation

As before, we start with two Lemma:

> [!abstract] Lemma (i).
> If $a \in \mathbb{Z}$, then $gcd(a, 0) = a$.
> **Proof**.
> Suppose $d = gcd(a, 0)$, then $d|0, d|a$. Since every integer divides zero, we must show that $d$ is the greatest integer that divides $a$. But since an integers greatest divisor is always itself, $d$ must equal $a$.
>
> $\blacksquare$

> [!abstract] Lemmma (ii).
> If $a, b \in \mathbb{Z}, \; q, r \in \mathbb{Z}^{nn}$ and $a = bq + r$, then
> $$
> gcd(a, b) = gcd(b, r)
> $$
> **Proof**.
> We will show the equality holds by proving $gcd(a, b) \leq gcd(b, r)$ and
> $gcd(b, r) \leq gcd(a, b)$ and therefore the values are equal.
>
> $gcd(a, b) \leq gcd(b, r)$:
>
> Suppose $d = gcd(a, b)$, then $a = dk, b = dj$. Substituting:
> $$
> \begin{align}
> a &= bq + r \\
> &= dk = djq + r \\
> &= d(k - jq) = r.
> \end{align}
> $$
> And so because $k - jq \in \mathbb{Z}$, we see that $d | r$. Now by assumption, $d | b$. Hence $d$ is a divisor for both $b$ and $r$, and so it must be less than or equal to the greatest such divisor.
>
> $gcd(b,r) \leq gcd(a, b)$:
>
> Similarly, let $d = gcd(b, r) \implies dk = b, \; dj = r$. Substituting:
> $$
> \begin{align}
> a &= bq + r \\
> &= a = dkq + dj \\
> &= a = d(kq + j).
> \end{align}
> $$
> And so as before, $d | a$, and since $d$ also divides $b$ by assumption, we see that $d$ must be less than or equal to $gcd(a, b)$. Thus, $gcd(a, b) \leq gcd(b, r)$ and $gcd(b, r) \leq gcd(a, b)$, and so $gcd(a, b) = gcd(b, r)$.
>
> $\blacksquare$

### Building up the Algorithm

We start by noticing that Lemma (a) yields a **value**, rather than another form of the equation. We can reason this might be a good **termination condition**.

```Python
def gcd(a, b):
	while b > 0:
		# Mutate a and b

	return a
```

We now look at Lemma (b) for an idea of a loop invariant:

$$
gcd(a, b) = gcd(b, r)
$$

which gives us an idea about how to mutate $a, b$ during the body of the loop. Clearly $a = b$ in the above equation. For $b = r$ we recall the definition of $r = a \mod b$.  Noting the values of $a, b$ on the $n+1$st iteration:

$$
\begin{align}
&a_{n+1} = b_n \\
&b_{n+1} = a_n \mod b_n
\end{align}
$$

So completing the algorithm we have:

```Python
def gcd(a, b):
	while b > 0:
		# Caution: b_n+1 = a_n mod b_n, so we need to compute this first
		r = a % b
		a = b
		b = r

	return a
```

## Euclidean Algorithm (Using Recursion)

Combining the two Lemmas, we arrive at a concise definition for $gcd$:

$$
gcd(a,b) =
\begin{cases}
a & \text{if b = 0} \\
gcd(b, r = a \mod b) & \text{otherwise}
\end{cases}
$$

this lends itself almost verbatim to an equivalent **recursive algorithm**:

```Python
def gcd(a, b):
	if b == 0:
		return a

	return gcd(b, a % b)
```

which is more concise and easier to reason about mathematically.

## Examples

### Exponentiation

Using the following Lemmas, we construct an algorithm for exponentiation ($x^y$).

> [!abstract] Exponentiation
> **Lemma a**: If $a, b \in \mathbb{Z}$ then $a \cdot b^0 = a$
> **Lemma b**: If $a, b, n \in \mathbb{Z}, a \cdot b^n = (a \cdot b)b^{n-1}$
> **Lemma c**: If $a, b, n \in \mathbb{Z}$ and $n$ is even. Then $a \cdot b^n = a(b^2)^{n/2}$

As before, we look to Lemma a for a termination condition: $n = 0$ and to guide our choice of initial values. This also helps establish our invariant of $a \cdot b^n = x^y$. Choosing $a = 1, b = x, n = y$ we clearly see $a \cdot b^n = x^y$.

```Python
def exp(x, y):
	a = 1
	b = x
	n = y

	# TODO: Need to determine why termination is > 1 rather than > 0
	while n > 1:
		# ...

	# Lemma a.
	return a
```

Next, we see Lemmas b and c, we divide the mutation of $a, n$ into two cases:
1. n is even, then $a_{k+1} = a_k \cdot b^2$, $n_{k+1} = n_k / 2$
2. n is odd, then $a_{k+1} = a_k \cdot b$, $n_k{+1} = n - 1$

So we finish the algorithm:

```Python
def exp(x, y):
	a = 1
	b = x
	n = y

	while n > 1:
		if n % 2 == 1:
			# Lemma b.
			a = a * b
			n = n - 1
		else:
			# Lemma c
			a = a * b * b
			n = n // 2

	# Lemma a.
	return a
```