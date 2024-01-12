# The Exponential Function

[[Additional Properties of the Logarithm#Bijectivity of the Logarithm|Previously]] we showed that the logarithm is bijective, and therefore has an inverse. We define this inverse as follows:

> [!info] The Exponential Function
> For all real $x$, we define the **exponential function** at $x$ to be the $y$ whose logarithm is $x$. In other words:
> $$
> \log_b y = x \iff b^x = y
> $$

The exponential function has properties analogous to the logarithm.

## Properties of the Exponential Function

> [!abstract] Special Values
> $e^0 = 1$, $e^1 = e$
>
> Proof.
> This property follows immediately from writing the exponential function in terms of the logarithm:
> $$
> \log_b 1 = 0 \implies b^0 = 1 = e^0
> $$
> $$
> \ln(e) = 1 \implies e^1 = e
> $$
> In other words, the number whose logarithm base $e$ is 1 is $e$ itself.

> [!abstract] Additivity
> $e^{a + b} = e^a e^b$
>
> Proof.
> To show this, we take advantage of the fact that $\ln x$ and $e^x$ are inverses.
> Let $x = e^a, y = e^b$, then $xy = e^a e^b$ and notice $\ln(xy) = \ln x + \ln y$. So then letting $\exp = e^x$
> $$
> \begin{align}
> xy &= \exp(ab) \\
> &= \exp(\ln(xy)) \\
> &= \exp(\ln(x) + \ln(y)) \\
> &= \exp(a + b) \\
> &= \exp(a) \exp(b)
> && \blacksquare
> \end{align}
> $$

> [!abstract] Identity under Differentiation
> $(e^x)' = e^x$
>
> Proof.
> We start by using the additive property of the exponential function to manipulate the difference quotient:
> $$
> \frac d {dx} e^x
> = \lim_{h \to 0} \frac {e^{x + h} - e^x} h \\ \\
> = \lim_{h \to 0} e^x \frac {e^h - 1} h
> $$
>
> Thus, in order to prove the property, we must show that $\lim_{h \to 0} \frac {e^h - 1} h = 1$. Let $k = e^h - 1$ and notice that $h = \ln(e^h) = \ln(k + 1)$. We write:
> $$
> \lim_{h \to 0} \frac k {\ln(k+1)} =
> \lim_{h \to 0} \frac k {\ln(k + 1) - \ln 1} =
> \frac 1 {\ln'(1)} =
> 1
> $$
>
> Where the rightmost expression comes from the fact that $k \to 0$ as $h \to 0$.
>
> $\blacksquare$

## Exponentials as Powers of $e$

We would like to establish some properties of exponential functions in a similar manner to those of the logarithm. We start by using a functional equation (proved previously):

$$
E(a+b) = E(a)E(b)
$$

To show that $E(r) = e^r$ for all rational numbers.

> [!abstract] Theorem.
> $E(r) = e^r$ where $r \in \mathbb{Q}$.
>
> Proof.
> By induction. Consider $b = -a$ in the equation. Then we have:
> $$
> E(a - b) = E(-a)E(a) = E(0) = 1 = e^0
> $$
>
> From this we see that $E(-a) = \frac 1 {E(a)}$. Now let $N = n+1$ and notice:
> $$
> \begin{align}
> E((n+1)a) &= E(na + a) \\
> &= E(na)E(a) \\
> &= e^{na}e^a &\text{IH} \\
> &= e^{na + a} &\text{properties of $e$} \\
> &= e^{(n+1)a} \\
> &&\blacksquare
> \end{align}
> $$
>
> A similar proof follows for $a = \frac 1 n$. In particular, for $a = \frac 1 m, b = n$, we have $E(\frac n m) = e^{n/m}$