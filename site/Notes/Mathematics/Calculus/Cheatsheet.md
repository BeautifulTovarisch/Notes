# Cheatsheet

Important derivations and/or results that I forget all the time.

## Basic  Integrals

| $f$       | $f'$         | $\int f$        |
| :-------: | :---------: | :------------: |
| $\sin x$   | $\cos x$     | $-\cos x$       |
| $\cos x$   | $-\sin x$    | $\sin x$        |
| $\tan x$   | $\sec^2 x$   | $-\log (\cos x)$ |
| $\cot x$   | $-\csc^2 x$  | $\log(\sin x)$   |
| $\log x$   | $\frac 1 x$  | $x\log x - x$    |

## Table of Integrals

| $f$      | $\int f$                               |
| :------: | :------------------------------------: |
| $x \cos x$   | $x \sin x + \cos x$                   |
| $x \sin x$   | $\sin x - x \cos x$ |
| $x^2 \cos x$   | $x^2\sin x + 2(x \cos x - \sin x)$ |
| $x^2 \sin x$   | $2(x \cos x + \cos x) - x^2\cos x$ |
| $x^3 \cos x$   | $x \sin x(x^2 - 6) + 3\cos x(x^2 - 2)$ |
| $x^3 \sin x$   | $x \cos x(6 - x^2) + 3\sin x(x^2 - 2)$ |
| $\sin x \cos x$   | $\frac 1 2 \sin^2 x$ |
| $x \sin x \cos x$   | $\frac 1 8 (\sin 2x - 2x \cos 2x)$ |
| $\sin^2x$ | $\frac 1 2 x - \frac 1 4 \sin (2x)$ |
|| $-\sin x\cos x + \int \cos^2 x \; dx$ |

| $f$       | $\int f$ |
| :-----:   | -------: |
| $\log^2 x$   | $x(\log^2 x -2 \log x + 2)$ |
| $x \log x$   | $\frac 1 2 x^2(\log x - \frac 1 2)$ |
| $x \log^2 x$   | $\frac 1 2 x^2 \log^2 x - \frac 1 2 x^2(\log x - \frac 1 2)$ |
| $x^n \log ax$   | $\frac {x^{n+1}} {n+1}(\log ax - \frac 1 {n+1})$ |
| $x^2 \log^2 x$   | $\frac {x^3} 3 \log^2 x - \frac 2 9 x^3 \log x + \frac 2 {27} x^3$ |
| $\frac 1 {x \log x}$   | $\log \log x$ |

| $f$       | $\int f$ |
| :-----:   | -------: |
| $\arctan x$   | $x\arctan x - \frac 1 2 \log(1 + x^2)$ |
| $\arccos x$   | $x\arccos x - \sqrt{1 - x^2}$ |
| $\arcsin x$   | $x\arccos x + \sqrt{1 - x^2}$ |

## Logarithmic Differentiation

This is used so seldom that I forget the technique.

Suppose $g(x) = \ln(f(x))$, that is $(\ln \circ f)$. By the chain rule:

$$
g'(x) = (\ln(f(x)))' = f'(x) * \ln'(f(x)) = \frac {f'(x)} {f(x)}
$$

Then we have from the above formula that $g'(x)f(x) = f'(x)$. This is generally useful when we would like to break apart an ugly function using the properties of the logarithm.

> [!example]-
> $$
> f(x) = x^2 \cos x (1 + x^4)^{-7}
> $$
>
> Taking the $\log$ of $f$ we have:
> $$
> \begin{align}
> g(x) = \log(f(x)) &= \log(x^2) + \log(\cos x) + \log((1 + x^4)^{-7}) \\ \\
> &= 2\log(x) + \log(\cos x) - 7\log(1 + x^4) \\ \\
> \end{align}
> $$
>
> Taking the derivative
> $$
> g'(x)
> = \frac 2 x - \frac {\sin x} {\cos x} - \frac {28x^3} {1 + x^4}
> = \frac {f'(x)} {f(x)}
> $$
>
> Solving for $f'(x)$ we have:
> $$
> \begin{align}
> g'(x)f(x)
> &= \frac 2 x - \frac {\sin x} {\cos x} - \frac {28x^3} {1 + x^4}
> * (x^2 \cos x (1+x^4)^{-7}) \\ \\
> &= \frac {2x\cos x} {(1+x^4)^{7}} - \frac {x^2 \sin x} {(1+x^4)^{7}} + \frac {28x^5\cos x} {(1+x^4)^{8}}
> \end{align}
> $$

## Taylor Polynomials

$$
\begin{array}{c l r}
f(x) & P(x) & o \\ \\

\frac 1 {1-x}
& 1 + x + x^2 + \dots + x^n + \frac {x^{n+1}} {1 - x}
& o(x^n) \\ \\

\log(1 + x)
& x - \frac {x^2} 2 + \frac {x^3} 3 - \dots + (-1)^{n-1} \frac {x^n} n
& o(x^n) \\ \\

e^x
& 1 + x + \frac {x^2} 2 + \frac {x^3} {3!} + \dots + \frac {x^n} {n!}
& o(x^n) \\ \\

\sin x
& x - \frac {x^3} {3!} + \frac {x^5} {5!} + \dots + (-1)^{n-1} \frac {x^{2n}} {(2n)!}
& o(x^{2n}) \\ \\

\cos x
& 1 - \frac {x^2} {2!} + \frac {x^4} {4!} + \dots + (-1)^n \frac {x^{2n+1}} {(2n+1)!}
& o(x^{2n+1}) \\ \\

\tan x
& x + \frac {x^3} 3 + \frac {x^5} 5 + \dots + \frac {x^{2n+1}} {2n+1}
& o(x^{2n+1}) \\ \\

\arctan x
& x - \frac {x^3} 3 + \frac {x^5} 5 - \dots + (-1)^{n-1} \frac {x^{2n-1}} {2n-1}
& o(x^{2n}) \\ \\

\end{array}
$$

## Miscellaneous

> [!tip] Formula
> $$
> \begin{align}
> \int \sin^n x \; dx &= -\cos x \sin^{n-1} x + (n-1)\int \sin^{n-2} x \cos^2 x \; dx \\ \\
> &= \frac {-\cos x \sin^{n-1}} n + \frac {(n-1)} n \int \sin^{n-2} x \; dx
> \end{align}
> $$

> [!tip]  Formula
> $$
> \begin{align}
> \int \cos^n x \; dx &= \sin x \cos^{n-1} x - (n-1) \int \sin^2 x \cos^{n-2} x \; dx \\
> &= \frac {\sin x \cos^{n-1} x} n - \frac {n-1} n \int \cos^{n-2} x \; dx
> \end{align}
> $$

> [!tip]  Formula
> $$
> \int x^m \log^n x \; dx = \frac {x^{m+1} \log^n x} {m+1} - \frac n {m+1} \int x^m \log^{n-1} \; dx
> $$

> [!tip] Formula
> $$
> \begin{align}
> &\cot^{-1} x = \frac \pi 2 - \arctan x \\
> &\sec^{-1} x = \arccos \frac 1 x \\
> &\csc^{-1} x = \arcsin \frac 1 x
> \end{align}
> $$