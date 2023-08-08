There are a few strategies for computing the product of two matrices. We revisit the representations in [[Multiplying Matrices and Vectors]] and reduce the problem to either a matrix-vector or vector-matrix multiplication over the respective dimensions of the matrices.

> [!info] Legal Multiplication
> Let $A$ be an $R \times S$ matrix and $B$ by an $S \times T$ matrix. Then $A * B$ (often written $AB$) is legal and an $R \times T$ matrix.
> > [!warning]
> > In general, matrix multiplication is **not commutative**.

## Vector-Matrix

We can compute a matrix-matrix multiplication by repeated vector-matrix multiplication choosing each **row** of $A$ as a vector.

> [!info] Vector-Matrix Representation 
> For each $r \in R$ of $A$, we compute $AB_r = A_r * B$ where $A$ is an $R \times S$ matrix and $B$ is an $R \times T$ matrix.
> $$
> A = 
> \begin{bmatrix}
> a_{11} & a_{12} & \dots & a_{1S} \\
> a_{21} & a_{22} & \dots & a_{2S} \\
> \vdots & \vdots & \dots & \vdots \\
> a_{R1} & a_{R2} & \dots & a_{RS}
> \end{bmatrix}
> 
> B = 
> \begin{bmatrix}
> b_{11} & b_{12} & \dots & b_{1T} \\
> b_{21} & b_{22} & \dots & b_{2T} \\
> \vdots & \vdots & \dots & \vdots \\
> b_{S1} & b_{S2} & \dots & b_{ST}
> \end{bmatrix}
> $$
> Then the product $AB$ is given by:
> $$
> \begin{align}
> &AB_1 = A_{1,} * B = a_{11} [b_{11}, b_{12}, \dots, b_{1T}] + \dots + a_{1S} [b_{S1}, \dots, b_{ST}] \\
> &AB_2 = A_{2,} * B = a_{21} [b_{11}, b_{12}, \dots, b_{1T}] + \dots + a_{2S} [b_{S1}, \dots, b_{ST}] \\
> &\dots \\
> &AB_{R} = A_{R,} * B = a_{R1} [b_{11}, b_{12}, \dots, b_{1T}] + \dots + a_{RS} [b_{S1}, \dots, b_{ST}] 
> \end{align}
> $$

> [!example]
> Suppose 
> $$
> A = 
> \begin{bmatrix}
> 1 & 0 & 0 \\
> 2 & 1 & 0 \\
> 0 & 0 & 1
> \end{bmatrix}
> B = 
> \begin{bmatrix}
> b_1 \\
> b_2 \\
> b_3
> \end{bmatrix}
> $$
> Then using the linear combination approach
> $$
> AB = 
> \begin{bmatrix}
> 1b_1 + 0b_2 + 0b_3 \\
> 2b_1 + 1b_2 + 0b_3 \\
> 0b_1 + 0b_2 + 1b_3
> \end{bmatrix}
> = 
> 
> \begin{bmatrix}
> b_1 \\
> 2b_1 + b_2 \\
> b_3
> \end{bmatrix}
> $$
> 
> Aside: We call $A$ an **elementary row-addition matrix** since it is an identity matrix with **one** non-diagonal entry nonzero.

## Matrix-Vector

Similarly, we can define the operation as repeated matrix-vector multiplications against by choosing each column of $B$ as as vector multiplied against $A$.

> [!info] Matrix-Vector Representation 
> For each $t \in T$ of $B$, we compute $AB_t = A * B_t$ where $A$ is an $R \times S$ matrix and $B$ is an $R \times T$ matrix.
> $$
> A = 
> \begin{bmatrix}
> a_{11} & a_{12} & \dots & a_{1S} \\
> a_{21} & a_{22} & \dots & a_{2S} \\
> \vdots & \vdots & \dots & \vdots \\
> a_{R1} & a_{R2} & \dots & a_{RS}
> \end{bmatrix}
> 
> B = 
> \begin{bmatrix}
> b_{11} & b_{12} & \dots & b_{1T} \\
> b_{21} & b_{22} & \dots & b_{2T} \\
> \vdots & \vdots & \dots & \vdots \\
> b_{S1} & b_{S2} & \dots & b_{ST}
> \end{bmatrix}
> $$
> Then the product $AB$ is given by:
> $$
> \begin{align}
> &AB_{,1} = A * B_{,1} = b_{11} [a_{11}, a_{21}, \dots, a_{R1}] + \dots + b_{S1} [a_{1S}, \dots, a_{RS}] \\
> &AB_{,2} = A * B_{,2} = b_{12} [a_{11}, a_{21}, \dots, a_{R1}] + \dots + b_{S2} [a_{1S}, \dots, a_{RS}] \\
> &\dots \\
> &AB_{,T} = A * B_{,T} = b_{1T} [a_{11}, a_{21}, \dots, a_{R1}] + \dots + b_{ST} [a_{1S}, \dots, a_{RS}] 
> \end{align}
> $$

> [!example]
> $$
> A =
> \begin{bmatrix}
> 1 & 2 \\
> -1 & 1
> \end{bmatrix}
> B =
> \begin{bmatrix}
> 4 & 2 & 0 \\
> 3 & 1 & -1
> \end{bmatrix}
> $$
> Then $AB$ is given by
> $$
> \begin{align}
> AB_{,1} &= 4[1, -1] + 3[2, 1] = [10, -1] \\
> AB_{,2} &= 2[1, -1] + 1[2, 1] = [4, -1] \\
> AB_{,3} &= 0[1, -1] + -1[2, 1] = [-2, -1] \\ \\
> &= 
> \begin{bmatrix}
> 10 & 4 & -2 \\
> -1 & -1 & -1  
> \end{bmatrix}
> \end{align}
> $$

## Dot Product

Two matrices can also be computed as a [[Dot Product]]. An entry is given by the dot product of a row of $A$ and column of $B$.

> [!info] Dot Product
> Suppose $A$ is an $R \times S$ matrix and $B$ is an $S \times T$ matrix. Then entry $AB_{rt}$ is given by $A_r \cdot B_t$.
> $$
> A = 
> \begin{bmatrix}
> a_{11} & a_{12} & \dots & a_{1S} \\
> a_{21} & a_{22} & \dots & a_{2S} \\
> \vdots & \vdots & \dots & \vdots \\
> a_{R1} & a_{R2} & \dots & a_{RS}
> \end{bmatrix}
> 
> B = 
> \begin{bmatrix}
> b_{11} & b_{12} & \dots & b_{1T} \\
> b_{21} & b_{22} & \dots & b_{2T} \\
> \vdots & \vdots & \dots & \vdots \\
> b_{S1} & b_{S2} & \dots & b_{ST}
> \end{bmatrix}
> $$
> 
> $$
> \begin{align}
> &AB_{11} = A_{1,} \cdot B_{,1} = (a_{11} * b_{11}) + (a_{12} * b_{21}) + \dots + (a_{1S} * b_{S1}) \\
> &AB_{12} = A_{1,} \cdot B_{,2} = (a_{11} * b_{12}) + (a_{12} * b_{22}) + \dots + (a_{1S} * b_{S2}) \\
> &\dots \\
> &AB_{RT} = A_{R,} \cdot B_{,T} = (a_{R1} * b_{1T}) + \dots + (a_{RS} * b_{ST})
> 
> \end{align}
> $$

## Function Composition

We want to look at the composition of linear transformations and therefore define a function under matrix-matrix multiplication that represents such an operation. We define $f_{AB}(x) = (AB) * x$ and wish to prove that is it a composition of the linear functions defined by $f_A$ and $f_B$.

> [!abstract] Lemma
> $f_{AB} = f_A \circ f_B$
> 
> Proof.
> We must show that $f_A(x) \circ f_B(x) = f_AB(x)$. For any legal vector $x$ we write
> $$
> \begin{align}
> (f_A \circ f_B)(x) &= f_A(B * [x_1, x_2, \dots, x_n]) \\
> &= f_A(x_1 b_{,1} + x_2 b_{,2} + \dots + x_n b_{,n}) &\text{Linear Combination of M-v} \\
> &= x_1 f_A(b_{,1}) + x_2 f_A(b_{,2}) + \dots + x_n f_A(b_{,n}) &\text{Linearity} \\
> &= x_1 Ab_{,1} + x_2 Ab_{,2} + \dots + x_n Ab_{,n} &\text{Def. of $f_A$} \\
> &= x_1 AB_{,1} + x_2 AB_{,2} + \dots + x_n AB_{,n} &\text{M-v Def. of AB} \\
> &= (AB) * x &\text{Linear combination of M-v} \\
> &= f_{AB}
> \end{align}
> $$