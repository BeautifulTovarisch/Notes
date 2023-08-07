This section defines several representations of multiplication involving a matrix and vector.

> A "mnemonic" I like for remembering legal operations:
> 
> - MvC: $M * v \implies v \text{ is a } C$-vector
> - vMR: $v * M \implies v \text{ is an } R$-vector
> 
> Whether the operation happens against the columns or rows follows naturally from the dimension of the resulting vector. 

For each "direction" (M-v or v-M), we can represent the operation as a [[Linear Combination]] or [[Dot Product]].

## Matrix-Vector Multiplication

When the vector is on the **right**, it must have the same length/domain as the **columns** of $M$.

$$
M * v = a
$$

### Linear Combination

> [!info] Linear Combination
> Let $M$ be an $R \times C$ matrix over $\mathbb{F}$. Let $v$ be a $C$-vector of $\mathbb{F}$. Then $M * v$ is the linear combination:
> $$
> r = \sum_{c \in C} v[c] * M_{,c}
> $$
> 
> Where $r$ is an $R$-vector. In other words, the elements of $v$ act as the scalar values in a **linear combination** over $M$'s columns.
> $$
> \begin{bmatrix}
> a_{11} & a_{12} & \dots & a_{1C} \\
> a_{21} & a_{22} & \dots & a_{2C} \\
> \vdots & \vdots & \dots & \vdots \\
> a_{R1} & a_{R2} & \dots & a_{RC}
> \end{bmatrix} 
> * [x_1, x_2, \dots, x_C] 
>$$
>$$ 
> r = x_1 [a_{11}, a_{21}, \dots, a_{R1}]
> + x_2 [a_{12}, a_{22}, \dots, a_{R2}]
> + \dots
> + x_C [a_{1C}, a_{2C}, \dots, a_{RC}]
> $$

> [!example]
> Let
> $$
> M = 
> \begin{bmatrix}
> 1 & 2 & 3 \\
> 10 & 20 & 30
> \end{bmatrix},
> v = [7, 0, 4]
> $$
> 
> Then, 
> $$
> \begin{align}
> M * v &= 
> \begin{bmatrix}
> 1 & 2 & 3 \\
> 10 & 20 & 30
> \end{bmatrix}
> * [7, 0, 4] \\
> &= 7[1, 10] + 0[2, 20] + 4[3, 30] \\
> &= [7, 70] + [12, 120] \\
> &= [19, 190]
> \end{align}
> $$

### Dot Product

> [!info] Dot Product
> If $M$ is an $R \times C$ matrix and $u$ is an $C$-vector, then $M * u$ is the $R$-vector $v$ such that $v[r]$ is the **dot product** of $u$ and $M_{r,}$.
> 
> $$
> \begin{bmatrix}
> a_{11} & a_{12} & \dots & a_{1C} \\
> a_{21} & a_{22} & \dots & a_{2C} \\
> \vdots & \vdots & \dots & \vdots \\
> a_{R1} & a_{R2} & \dots & a_{RC}
> \end{bmatrix} 
> * [x_1, x_2, \dots, x_C] 
>$$
>$$ 
> r = [(x_1 * a_{11} + x_2 * a_{12} + \dots x_C * a_{1C}), (x_1 * a_{21} + \dots + x_C * a_{2C}), \dots, (x_1 * a_{R1} + \dots + x_C * a_{RC})]
> $$

> [!example]
> $$
> \begin{align}
> M =
> \begin{bmatrix}
> 1 & 2 \\
> 3 & 4 \\
> 10 & 0
> \end{bmatrix}, u = [3, 4]
> \end{align}
> $$ 
> then,
> $$
> \begin{align}
> M * u &= 
> \begin{bmatrix}
> 1 & 2 \\
> 3 & 4 \\
> 10 & 0
> \end{bmatrix} * [3, 4] \\ \\
> &= [(3 * 1 + 4 * 2), (3 * 3 + 4 * 4), (3 * 10 + 4 * 0)] \\
> &= [11, 25, 30]
> \end{align}
> $$

## Vector-Matrix Multiplication

When the vector is on the **left**, $v$ must have length/domain equal to the **rows** of $M$. 

$$
v * M = a
$$

### Linear Combination

> [!info] Linear Combination
> Let $M$ be an $R \times C$ matrix. Then $v * M$ is the **linear combination** 
> $$
> c = \sum_{r \in R} v[r] * M_{r,}
> $$
> 
> Where $c$ is a $C$-vector. In other words, the elements of $v$ are scalars in a linear combination over the rows of $M$.

> [!example]
> $$
> \begin{align}
> [3, 4] *
> \begin{bmatrix}
> 1 & 2 & 3 \\
> 10 & 20 & 30
> \end{bmatrix}
> &= 3[1, 2, 3] + 4[10, 20, 30] \\
> &= [3, 6, 9] + [40, 80, 120] \\
> &= [43, 86, 129]
> \end{align}
> $$

### Dot Product

> [!info] Dot Product
> If $M$ is an $R \times C$ matrix and $u$ is an $R$-vector, then $u * M$ is the $C$-vector $v$ such that $v[c]$ is the **dot product** of $u$ and $M_{,c}$.

> [!example]
> $$
> \begin{align}
> M =
> \begin{bmatrix}
> 1 & 2 \\
> 3 & 4 \\
> 10 & 0
> \end{bmatrix}, u = [1, 2, 3]
> \end{align}
> $$ 
> then,
> $$
> \begin{align}
> u * M &= [1, 2, 3] * 
> \begin{bmatrix}
> 1 & 2 \\
> 3 & 4 \\
> 10 & 0
> \end{bmatrix} \\ \\
> &= [(1 * 1 + 2 * 3 + 3 * 10), (1 * 2 + 2 * 4 + 3 * 0)] \\
> &= [37, 10]
> \end{align}
> $$


## Algebraic Properties

We use the Dot Product representation in order to prove some helpful properties about matrix multiplication:

> [!abstract] Theorem.
> Let $M$ be an $R \times C$ matrix. Then,
> 1. For any $C$-vector $v$ and scalar $\alpha$,
> $$
> M * (\alpha v) = \alpha (M * v)
> $$
> 2. For any $C$-vectors $u, v$,
> $$
> M * (u + v) = M * u + M * v
> $$
> 
> Proof (1):
> By definition of matrix-vector multiplication as a dot-product, we have
> $$
> \begin{align}
> M * (\alpha v) &= M * [\alpha v_1, \alpha v_2, \dots, \alpha v_C] \\
> &= [M_1 \cdot \alpha v_1, \dots, M_R \cdot \alpha v_C] \\
> &= [\alpha (M_1 \cdot v_1), \dots, \alpha (M_R \cdot v_C)] &\text{Hom. of Dot Product} \\
> &= \alpha (M * v)
> \end{align}
> $$
> 
> Proof (2):
> Again by the definition of dot-product we have:
> $$
> \begin{align}
> M * (u + v) &= [M_1 \cdot (u + v), \dots, M_R \cdot (u + v)] \\
> &= [M_1 \cdot u + M_1 \cdot v, \dots, M_R \cdot u + M_R \cdot v] &\text{Dist. of Dot Product} \\
> &= M * u + M * v
> \end{align}
> $$
> 
> $\blacksquare$