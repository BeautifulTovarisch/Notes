> [!info] Definition: Linear Equation
> A **linear equation** is an equation of the form:
> $$
> \alpha \cdot x = \beta
> $$
> where
> $$
> \begin{align}
> \alpha \; &\text{is a vector} \\
> x \; &\text{is a vector variable} \\
> and \; \beta \; &\text{is a scalar} 
> \end{align}
> $$

Generally we are presented with the [[Vectors over GF(2)#Lights Out Puzzle|problem]] of finding a vector(s) that satisfy the equation.

>[!example] Sensor Node Energy Utilization
>Define $D = \{radio, sensor, memory, cpu\}$
>and consider the following vectors:
> - $rate = \{memory:0.06W, radio:0.1W, sensor:0.004W, CPU: 0.0025W\}$
> - $duration = \{memory: 1s, radio: 0.25s, sensor:0.5s, CPU: 1s\}$ 
> 
> Then the *total* energy consumed by the sensor is given by:
> $$
> \text{total energy} = rate \cdot duration = 0.0845J
> $$

If we are given the duration and energy output over multiple trials, we can construct a linear equation:
$$
\left\{
\begin{array}{c}
duration_1 \cdot rate = \beta_1 \\
duration_2 \cdot rate = \beta_2 \\
duration_3 \cdot rate = \beta_3
\end{array}
\right .
$$
## System of Equations

>[!info] Definition: System of Linear Equations
>A *system* of *linear equations* (*linear system*) is a collection of equations:
>$$
>\begin{array}{c}
>a_1 \cdot x = \beta_1 \\
>a_2 \cdot x = \beta_2 \\
>\vdots \\
>a_n \cdot x = \beta_n
>\end{array}
>$$
>with a solution $\hat x$ that satisfies all equations.

>[!question] Uniqueness of $\hat x$
>For a given system of linear equations, how can we tell if there is a unique solution?

### Solving a Triangular Linear System

A special case of linear systems are called triangular:
$$
\begin{cases}
[a_{11}, a_{12}, \dots, a_{1n}] &\cdot x &= \beta_1 \\
[0, a_{22}, \dots, a_{2n}] &\cdot x &= \beta_2 \\
[0, 0, a_{33}, \dots, a_{3n}] &\cdot x &= \beta_3 \\
\cdots \\
[0, 0, \dots, 0, a_{nn}] &\cdot x &= \beta_n \\
\end{cases}
$$

>[!example] Triangular Linear System
>$$
>\left\{
>\begin{aligned}
>x_1 + \frac 12 x_2 - 2 x_3 + 4 x_4 &= -8 \\
>3 x_2 + 3 x_3 + 2 x_4 &= 3 \\
>x_3 + 5 x_4 &= -4 \\
>2 x_4 &= 6 \\
>\end{aligned}
>\right .
>$$

We can solve triangular linear systems trivially using "Backwards Substitution"

#### Backwards Substitution

The main idea is to "solve backwards", finding the last component first and deriving the others in tow.

> [!example] Solving with Backwards Substitution
> $$
> \left\{
> \begin{aligned}
> x_1 + \frac 12 x_2 - 2 x_3 + 4 x_4 &= -8 \\
> 3 x_2 + 3 x_3 + 2 x_4 &= 3 \\
> x_3 + 5 x_4 &= -4 \\
> 2 x_4 &= 6 \\
> \end{aligned}
> \right .
> $$
> First we notice that $x_4 = 3$. From there we can work backwards:
> $$
> \begin{align}
> x_4 = 3 &\implies x_3 = -19 \\
> &\implies x_2 = 18 \\
> &\implies x_1 = -67
> \end{align}
> $$
> So our solution is the vector: $[-67, 18, -19, 3]$

We can describe the general algorithm of backwards substitution as follows:
1. Initialize $x := \text{zero vector}$
2. Compute $x_i$ by computing the dot product of $x$ and the current sub-expression
3. Move to sub-expression $i-1$ 

The value computed in step two is given by the formula:
$$
x_i = \frac {\beta_i - expr} {a_{ii}}
$$

The Python procedure solves a triangular system with the notable constraint that `r[i][i] != 0` for a given $i$ (this avoids a division by zero):

```Python
triangular_solve_n(rowlist, b):
	'''
	Solves the linear equation described by [rowlist] and [b].

	Parameters:
	    rowlist vector[]: A list of n-vectors comprising the LHS of the system
	    b vector: An n-vector representing the RHS (B1, B2, ...) of the system

	Returns:
	    The unique vector satisfying the equation.

	Example:
		rowlist = [
			[1, -3, -2],
			[0, 2, 4],
			[0, 0, -10]
		]

		b = [7, 4, 12]

		triangular_solve_n(rowlist, b) = [17.8, 4.4, -1.2] 
	'''
	
	x = zero_vec
	n = len(rowlist[0])

	# n-1 to 0
	for i in reversed(range(n)):
		x[i] = b[i] - dot(rowlist[i], x) / rowlist[i][i]
```
