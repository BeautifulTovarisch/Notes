We often want to find the inverse of a matrix as a means of "reversing" a linear transformation (such as decoding a [[Hamming Code#Linear Codes]]).

> [!info] Inverse of a Matrix
> Let $A$ be an $R \times C$ matrix over $\mathbb{F}$ and let $B$ be a $C \times R$ matrix over $\mathbb{F}$. Define $f: \mathbb{F}^C \to \mathbb{F}^R$ by $f_A(x) = A * x$ and $g: \mathbb{F}^R \to \mathbb{F}^C$ by $g_B(y) = B * y$. If $f$ and $g$ are inverses, we say $A$ and $B$ are **inverses** and we call the matrices **invertible**. The inverse is unique following from the uniqueness of an inverse function.
>
> Finally, we denote the inverse of matrix $A$ as $A^{-1}$.

> [!warning]
> The author's process for determining the inverses of the linear functions below is completely opaque and relies on general intuition rather than a systematic approach.

## Examples

> [!example]
> $$
> A =
> \begin{bmatrix}
> 2 & 0 & 0 \\
> 0 & 3 & 0 \\
> 0 & 0 & 4
> \end{bmatrix}
> $$
>
> Then $f: \mathbb{R}^3 \to \mathbb{R}^3$ is defined by $f([x, y, z]) = 2x + 3y + 4z$. Then, finding a polynomial such that $g \circ f  = id_{x,y,z}$, $g([x, y, z]) = \frac 1 2 x \frac 1 3 y \frac 1 4 z$. So finally,
> $$
> A^{-1} =
> \begin{bmatrix}
> \frac 1 2 & 0 & 0 \\
> 0 & \frac 1 3 & 0 \\
> 0 & 0 & \frac 1 4
> \end{bmatrix}
> $$

> [!example]
> $$
> A =
> \begin{bmatrix}
> 2 & 0 & 0 \\
> 0 & 0 & 0 \\
> 0 & 0 & 4
> \end{bmatrix}
> $$
> Then $f([x, y, z]) = 2x + 0y + 4z$, but there is no function that composes with $f$ to produce $id_y$, so $A$ is not invertible.

> [!tip]
> Slowing down and doing the matrix-vector multiplication helped me understand why the previous examples hold

> [!example]
> $$
> A =
> \begin{bmatrix}
> 1 & 0 & 0 \\
> 2 & 1 & 0 \\
> 0 & 0 & 1
> \end{bmatrix}
> $$
> $f([x, y, z]) = [x_1, 2x_1 + x_2, x_3]$. Then $g([x, y, z]) = [x_1, x_2 - 2x_1, x_3]$, so then
>
> $$
> A^{-1} =
> \begin{bmatrix}
>  1 & 0 & 0 \\
> -2 & 1 & 0 \\
>  0 & 0 & 1
> \end{bmatrix}
> $$

> [!todo]
> Transcribe more examples later

## Uses of Matrix Inverse

We prove a property that holds if two matrices are inverses of one another

> [!abstract] Theorem.
> If the $R \times C$ matrix $A$ has an inverse, then $AA^{-1}$ is the identity matrix.
>
> Proof.
> Suppose $A^{-1}$ is the $C \times R$ inverse of $A$. Then by [[Matrices and Functions|definition of linear function]], $f_A(x) = A * x$ and $f_{A^{-1}}(x) = A^{-1} * x$. Then by [[Matrix Multiplication#Function Composition|composition of linear functions]] $f_A \circ f_{A^{-1}} = f_{AA^{-1}} = AA^{-1}$. By definition of composition of inverses, $AA^{-1} = id(x)$ which is the identity matrix.
>
> $\blacksquare$