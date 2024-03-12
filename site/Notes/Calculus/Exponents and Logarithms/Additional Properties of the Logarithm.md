# Additional Properties of the Logarithm

From our [[The Natural Logarithm#Properties of the Natural Logarithm]] in combination with our original [[Journey to the Natural Log#A Functional Equation]] we can deduce additional properties of the logarithm.

## Consequences of Logarithmic Additivity

Recall that $f(ab) = f(a) + f(b)$. We would like to show that $\ln(x)$ is unbounded and simultaneously prove another property of the logarithm.

> [!abstract] Theorem.
> For every $M \in \mathbb{R}$, $\ln(x) \gt M$ for some $x$.
>
> Proof.
>
> We first consider a straightforward lemma (which reveals a property of logarithms that'll come in handy later) which allows us to use our functional equation to show $ln(x)$ is unbounded.
>
>> [!abstract] Lemma.
>> Let $a \neq 0$ be a real number and $n$ be an integer. Then we have
>> $$
>> \ln(a^n) = n \ln(a)
>> $$
>>
>> Proof.
>>
>> By induction, notice that from the properties of the natural logarithm we have $\ln(a^0) = \ln(1) = 0 \ln(a) = 0$. Now assume the hypothesis for $N \geqslant 0$ and consider $N = n + 1$:
>> $$
>> \begin{align}
>> \ln(a^{n+1}) = \ln(a * a^n) = \ln(a) + n\ln(a) = (n+1)\ln(a)
>> \end{align}
>> $$
>>
>> Thus for every integer $n$, the hypothesis is shown.
>>
>> $\blacksquare$
>
>Using the above lemma, we can manipulate $\ln(a^n), \; a \neq 1$ and show that $\ln$ has no upper or lower bound.
>
> From above, we have $\ln(a^n) = n\ln(a)$. Assume some real number $M$ and notice by the archimedean property we may choose an $n$ such that
> $$
> \ln(a^n) = n\ln(a) \implies n \gt \frac M {\ln(a)} \; a \neq 1
> $$
>
> Similarly, consider $\ln(\frac 1 a)$. Then we may take $n = -1$ and notice from the above inequality:
> $$
> \ln(\frac 1 a) = -\ln(a) \lt -M
> $$
> which shows $\ln$ has no lower bound.
>
> $\blacksquare$

## Bijectivity of the Logarithm

Previously, we had shown our functional equation was monotonic. We now use this property to show that the logarithm is uniquely defined over its domain.

> [!abstract] Theorem.
> For every $a \in \mathbb{R}, a \gt 0$, $\exists! b \in \mathbb{R}^+$ such that
> $$
> \ln(a) = b
> $$
>
> Proof.
> We want to establish first that $\ln(a)$ takes on some value $b$ over some interval. If $b \gt 0$, choose some $n \gt \frac b {\ln(a^n)}$ and notice that over $[1, a^n]$, $\ln(1) = 0 \lt b \lt n\ln(a) = \ln(a^n)$. By the [[Values of Continuous Functions#Intermediate Value Theorem]] (we know $\ln$ is continuous because it is differentiable) $\ln$ must take on $b$ as a value in the interval.
>
> Now we show that this $b$ is unique. Assume by way of contradiction that there is some $\ln(a') = \ln(a) = b$ where $a \neq a'$. But by monotonicity of $ln$, either $\ln(a) \lt \ln(a')$ or vice versa, contradicting the assumption that $\ln(a) = \ln(a')$. Thus there must be only one $a$ whose logarithm is $b$.
>
> $\blacksquare$

## Bases of the Logarithm

Previously we sought a function $f$ which exhibited the following properties:

1. $f$ is a solution to $f(xy) = f(x) + f(y)$,
2. is positive, and
3. differentiable

which is given by the formula:

$$
f(x) = c \log(x)
$$

Since we have established all solutions to our functional equation differ by a constant, we would like to relate $f$ to $c$ somehow. The subsequent relationship is called the **base of the logarithm of x**.

Let $c = \frac 1 {\log(b)}$, then

$$
f(x) = c \log(x) = \frac {\log(x)} {\log(b)} = \log_b(x)
$$

This shows an alternative proof to the change of base [[Exponents and Logarithms#Logarithmic Identities]]:

$$
\log_b x = \frac {\log x} {\log b}
$$