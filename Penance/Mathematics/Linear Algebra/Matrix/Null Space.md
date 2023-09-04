The null space of a matrix can represent the solution sets of [[Homogeneous Linear Systems]] represented by:

$$
A * x = 0
$$

Where $A$ is a matrix and $x$ is a vector-variable.

> [!info] Null Space
> The **Null Space** of matrix $A$ is the set $\{ v : A *  v = 0 \}$. We denote the null space of $A$ as Null $A$.

> [!example]
> $$
> A = 
> \begin{bmatrix}
> 1 & 4 & 5 \\
> 2 & 5 & 7 \\
> 3 & 6 & 9
> \end{bmatrix}
> $$
> 
> We notice that the 3rd column is the sum of the first two. Symbolically: $a + b = c \implies a + b - c = 0$. So then we can construct a vector $v = [1, 1, -1]$ such that $A * v = 0$. So $v$ is in Null $A$.

## Properties of the Null Space

We will prove similar properties of [[Linear Systems]] with respect to unique solutions.

> [!abstract] Lemma
> For any $R \times C$ matrix $A$, and $C$-vector $v$, a vector $z$ is in Null $A$ if and only if $A * (v + z) = A * v$.
> 
> Proof.
> Suppose $z$ is in Null $A$, then by definition, $A * z = 0$. Then we have:
> $A * (v + z) = A * v + A * z = A * v$ by previous theorem.
> 
> Now suppose $A * (v + z) = A * v$. Again, $A * v = A * v + A * z$ and so $A * z = 0$ which implies $z$ is in Null $A$.  
> 
> $\blacksquare$

We want to prove some results about matrix-vector multiplications representing linear systems.

> [!danger] Review the following proof carefully next time I see this note.

> [!abstract] Corollary
> Suppose $u_1$ is a solution to $A * x = b$. Then $u_2$ is also a solution if and only if $u_1 - u_2$ is in Null $A$.
> 
> Proof.
> Suppose $u_2$ is a solution to $A * x = b$. Then by assumption, $A * u_1 = A * u_2 = b$. Let $v$ = $u_2$, $z = u_1 - u_2$ and notice $z + v = u_1$:
> $$
> A * u_2 = A * (z + v) = A * u_1 
> $$
> 
> Now suppose $u_1 - u_2$ is in Null $A$. Then by definition, $A * (u_1 - u_2) = 0$, and so by distribution.
> $$
> A * (u_1 - u_2) = A * u_1 - A * u_2 = 0
> $$
> 
> and so $A * u_1$ = $A * u_2$, and thus $u_2$ is a solution.
> 
> $\blacksquare$.