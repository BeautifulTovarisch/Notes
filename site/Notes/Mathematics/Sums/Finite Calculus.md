# Finite Calculus

We develop discrete methods analogous to the methods of integration and differentiation in order to [[Manipulation|manipulate sums]] when we don't know how to deal with them.

## Notation

Finite calculus offers method analogous to [[The Derivative]] and [[Integrals of more General Functions|Integration]] for a large classification of problems.

### Finite Difference

We begin by defining the finite **difference operator** which bears resemblance to the [[The Derivative#Formal Definition]] of a derivative

> [!info] Finite Difference
> Let $f$ be a function and consider the limit of the difference quotient from Calculus:
> $$
> \lim_{h \to 0} \frac {f(x + h) - f(x)} h
> $$
> We define the **finite difference** operator as the difference quotient under the restriction that $h \in \mathbb{Z}^+$, thus we have:
> $$
> \Delta f(x) = \lim_{h \to 1} \frac {f(x + h) - f(x)} h = f(x + 1) - f(x)
> $$

> [!example]
> Let $f(x) = x^3$. Then
> $$
> \Delta (x^3) = (x + 1)^3  - x^3 = 3x^2 + 3x + 1
> $$

This functions as a "finite" derivative which can be readily applied to polynomials expressed in terms of Rising and Falling factorials.

#### Shift Operator

Knuth also introduces a "shift" operator (for some reason) which signifies the $(x + 1)$ term in the difference operator. This is used in some more complicated [[Worked Examples]] to develop an analog for "integration by parts".

> [!info] Shift Operator
> $$
> E f(x) = f(x + 1)
> $$

### Rising and Falling Factorials

Knuth introduces notation indicating whether the terms of a factorial product are increasing or decreasing by one, with the corresponding number determining the total number of terms.

> [!info] Rising and Falling Factorial
> Let $m \in \mathbb{Z}, \; m \gt 0$. We define the **rising** and **falling** factorial of $x \in \mathbb{R}$ as follows:
> $$
> \begin{align}
> &x^{\overline m} = (x)(x+1)\dots(x+m-1) &\text{Rising Factorial} \\ \\
> &x^{\underline m} = (x)(x-1)\dots(x-m+1) &\text{Falling Factorial}
> \end{align}
> $$
> When $m \lt 0$ we have $x^{\underline m} = 1 / {x^{\overline m}}$.
>>[!tip]
>>$(x + m - 1 - x) + 1 = (x - (x - m + 1)) + 1 = m \; \text{terms}$

### Finite Derivative

We can compute the finite derivative of a term raised to a rising or falling factorial in exactly the same way as we would a power function:

> [!abstract] Finite Derivative of a Power Function
> Let $f(x) = x^{\underline m}$. Then the finite derivative of $f = \Delta(x^{\underline m}) = m x^{\underline {m-1}}$
>
> Proof.
> By definition of the finite difference operator we have:
> $$
> \begin{align}
> \Delta(x^{\underline m}) &= (x + 1)^{\underline m} - x^{\underline m} \\ \\
> &= (x+1)(x)(x-1)\dots(x-m+2) - (x)(x-1)\dots(x-m+2)(x-m+1) \\ \\
> &= (x)(x-1)\dots(x-m+2)(x + 1 - (x-m+1)) \\ \\
> &= m(x)(x-1)\dots(x-m+2) \\ \\
> &= m x^{\underline {m-1}} \\ \\
> &&\blacksquare
> \end{align}
> $$

### Finite Integral

By the Fundamental Theorem of Calculus, we find that the integral is the inverse of the derivative operator. We can define a "Finite Integral" (not to be confused with "Definite Integral") using summation notation:

> [!info] Finite Integral
> Let $f(x)$ be some function and $g(x)$ be the finite derivative of $f$, that is, $g(x) = \Delta f(x)$. We denote the **finite inverse** of $f$ to be:
> $$
> \sum g(x) \delta x = f(x) + C \; \text{Indefinite Sum}
> $$
> We denote the **definite summation**:
> $$
> \sum_a^b g(x) \delta x = f(x) \mid_b^a = f(b) - f(a)
> $$
> With the **critical difference** that this summation is taken over a half-open interval: $[a, b)$.
>> [!warning]
>> Remember that this means the limits of the summation are from $a \to b-1$

Next for posterity we prove the relationship between  "normal" summation and the finite integral:

> [!abstract] Theorem
> Let $g(x) = \Delta f(x)$ be defined over an interval $[a, b)$, then $\sum_a^b g(x) \delta x = f(b) - f(a)$.
>
> Proof.
> We see immediately that the summation of the difference operator is telescoping:
> $$
> \sum_a^b g(x) \delta x
> = f(a + 1) - f(a) + f(a+2) - f(a+1) + \dots + f(b) - f(b-1)
> = f(b) - f(a)
> $$

We can use this fact when taking the finite integral of certain terms:

> [!example]
> $$
> \sum_{0 \leqslant k \lt n} k^{\underline m}
> = \sum_0^n x^{\underline m}
> = \frac {x^{\underline {m+1}}} {m + 1} \mid_0^n
> = \frac {n^{\underline {m+1}}} {m + 1}
> $$

Thus we see the basic operations of finite calculus allow us to manipulate sums in an analogous way.