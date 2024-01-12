We want to find a compact representation of a [[Linear Functions]]. We use [[Generators#Standard Generators]] under the image of the function to produce a matrix.

> [!info] Matrix Representation of a Linear Function
>  Suppose $f: \mathbb{F}^C \to \mathbb{F}^R$ is a linear function. Let $M$ be an $R x C$ matrix defined such that $M_{,c} = f(e_c)$, where $e_c$ is a standard generator under $\mathbb{F}^C$. Then for $f(x) = M * x$ we have by definition of [[Multiplying Matrices and Vectors#Matrix-Vector Multiplication#Linear Combination]]:
>  $$
>  \begin{align}
>  f(x) &= \sum_{c \in C} x[c] * f(e_c) \\
>  &= \sum_{c \in C} x[c] * M_{,c}
>  \end{align}
> $$

> [!warning] Review
> I don't completely understand the reasoning here. Review in another LinAlg book in the future.

