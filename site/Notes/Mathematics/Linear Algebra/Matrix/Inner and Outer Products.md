We can treat vectors as "1-dimensional matrices" and perform a kind of multiplication between them.

## Inner Product

This definition is the most similar to [[Multiplying Matrices and Vectors#Matrix-Vector Multiplication]].

> [!info] Inner Product of two Vectors
> Let $u, v$ be two $D$-vectors and consider the "matrix-matrix" multiplication $u^Tv$. By the dot-product representation of matrix multiplication, we have $u^Tv = u \cdot v$. We call $u^Tv$ the **inner product** of $u$ and $v$.

> [!example]
> $$
> u = [1, 2, 3], v =
> \begin{bmatrix}
> 3 \\
> 2 \\
> 1
> \end{bmatrix}
> $$
> Then,
> $$
> u^Tv = [3*1 + 2*2 + 1*3] = [10]
> $$

## Outer Product

This definition is similar to the dot-product definition of matrix-matrix multiplication.

> [!info] Outer Product
> Let $u, v$ be any vectors not necessarily of the same domain. Then the **outer product**, $uv^T$, is defined as follows:
> $$
> uv^T_{st} = u_s * v_t
> $$

> [!example]
> $$
> u =
> \begin{bmatrix}
> u_1 \\
> u_2 \\
> u_3 \\
> \end{bmatrix},
> v = [v_1, v_2, v_3, v_4]
> $$
> Then
> $$
> uv^T =
> \begin{bmatrix}
> u_1v_1 & u_1v_2 & u_1v_3 & u_1v_4 \\
> u_2v_1 & u_2v_2 & u_2v_3 & u_2v_4 \\
> u_3v_1 & u_3v_2 & u_3v_3 & u_3v_4
> \end{bmatrix}
> $$