Linear Combinations, such as [[Line Segments#Convex Combinations]] are defined as follows:

> [!info] Linear Combination
> $$
> 	\alpha_1 v_1 + \alpha_2 v_2 + \dots + \alpha_n v_n
> $$
> 
> where $\alpha_1, \dots, \alpha_n$ are scalars and $v_1, \dots, v_n$ are vectors. We call the set of scalars the **coefficients** of the linear combination. If all coefficients of the linear combination are $0$, it is called the **trivial combination**.

> [!example]
> $$
> -5[2, 3.5] + 2[4, 10]
> $$

> [!example] Minimum Cost Diet
> Suppose we have 77 9-vectors, $v_i$ where each $i$ corresponded to a particular food and each vector was comprised of 9 nutrients of interest. We could construct a linear combination of these vectors in order to maximize nutrition and minimize cost.

## Linear Combinations to Coefficients

> [!abstract] Computational Problem
> Expressing a given vector as a linear combination of other vectors.
> - **input**: A vector $b$ and a list of vectors $[v_1, v_2, \dots, v_n]$
> - **output**: A list of coefficients $[\alpha_1, \alpha_2, \dots, \alpha_n]$ such that
> $$
> b = \alpha_1 v_1 + \alpha_2 v_2 + \dots + \alpha_n v_n
> $$
> or proof that none exists.

### Lights Out Problem

Revisiting the [[Vectors over GF(2)#Lights Out Puzzle]], we can consider the solution to this puzzle a linear combination of form:

$$
s = a_{0,0} v_{0,0} + \dots + a_{n-1, n-1} v_{n-1, n-1}
$$

in which the coefficients are either 0 or 1 (indicating whether we press the button or not).

> [!todo] Learn mathematical diagrams in LaTeX
> See notes for an example of a given configuration expressed as a linear combination of button presses.