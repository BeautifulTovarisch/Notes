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

---

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

## Miscellaneous

$$
\begin{align}
\int \sin^n x \; dx &= -\cos x \sin^{n-1} x + (n-1)\int \sin^{n-2} x \cos^2 x \; dx \\ \\
&= \frac {-\cos x \sin^{n-1}} n + \frac {(n-1)} n \int \sin^{n-2} x \; dx
\end{align}
$$

$$
\begin{align}
\int \cos^n x \; dx &= \sin x \cos^{n-1} x - (n-1) \int \sin^2 x \cos^{n-2} x \; dx \\
&= \frac {\sin x \cos^{n-1} x} n - \frac {n-1} n \int \cos^{n-2} x \; dx
\end{align}
$$

$$
\int x^m \log^n x \; dx = \frac {x^{m+1} \log^n x} {m+1} - \frac n {m+1} \int x^m \log^{n-1} \; dx
$$