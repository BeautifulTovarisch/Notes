# Little-o Notation

The little-oh $o$ notation is used to relate a function to another when we want to indicate the latter grows faster than the former as $x \to a$.

> [!info] Little-Oh Notation
> Let $f$ and $g$ be functions, $g(x) \neq 0$ for all $x$ in some interval containing $a$. For all $x \neq a$ let $x \to a$. We have:
> $$
> f(x) = o(g(x) \iff \lim_{x \to a} \frac {f(x)} {g(x)} = 0
> $$
>
> In other words, $f(x)$ is a **smaller order** than $g(x)$.

> [!examples] Simple Examples
> 1. $f(x) = o(1) \iff \lim_{x \to a} \frac {f(x)} 1 = 0 \implies f(x) = 0$
> 2. $f(x) = o(x) \iff \lim_{x \to a} \frac {f(x)} x = 0$
> 3. $f(x) = h(x) + o(g(x)) \iff \lim_{x \to a} \frac{f(x) - h(x)} {g(x)} = 0$

See [[Cheatsheet#Taylor Polynomials]] for the use of little-oh notation in Taylor series.

## Algebra of Little-oh

> [!abstract] Algebra of Little-oh Notation
> Let $x \to a$ and assume $g(x) \neq 0$. Then we have:
> $$
> \begin{align}
> &(a) &o(g(x)) \pm o(g(x)) = o(g(x)) \\
> &(b) &o(c g(x)) = o(g(x)) \\
> &(c) &f(x) \cdot o(g(x)) = o(f(x) g(x)) \\
> &(d) &o(o(g(x)) = o(g(x)) \\ \\
> &(e) &\frac 1 {1 + g(x)} = 1 - g(x) + o(g(x)), \; g(x) \to 0
> \end{align}
> $$
>
> Proof (a).
> Let $f_1(x) = o(g(x)), f_2(x) = o(g(x))$. Then by definition of $o(g(x))$ we have:
> $$
> \begin{align}
> f_1(x) + f_2(x) &= \lim_{x \to a} \frac {f_1(x)} {g(x)} \pm \lim_{x \to a} \frac {f_2(x)} {g(x)} \\ \\
>
> &= \lim_{x \to a} \frac {f_1(x) \pm f_2(x)} {g(x)} &\text{Limit Properties} \\ \\
> &= 0
> \end{align}
> $$
> Where final equality shows $o(g(x)) + o(g(x)) = o(g(x))$ by definition.
>
> $\blacksquare$
>
> Proof (b):
> Let $f(x) = o(c g(x))$. Then by definition we have:
> $$
> \lim_{x \to a} \frac {f(x)} {c g(x)} \iff \frac 1 c \lim_{x \to a} \frac {f(x)} {g(x)} \iff \lim_{x \to a} \frac {f(x)} {g(x)}
> $$
>
> $\blacksquare$
>
>> [!todo]
>> Proof (c), (d)
>
> Proof (e):
> Begin by noticing the algebraic identity:
> $$
> \frac 1 {1 + u} = 1 - u + u \frac u {1 + u}
> $$
> (Obtained from: $\frac 1 {1+u} = \frac {1 + u^2 - u^2} {1+u}$).
>
> Let $u = g(x)$ and let $h(x) = \frac u {1 + u}$. Then we see that the rightmost term is given by $g(x) h(x)$. Also notice that $g(x) \to 0 \implies h(x) \to 0$ and therefore:
> $$
> \lim_{x \to a} h(x) = \lim_{x \to a} \frac {g(x)h(x)} {g(x)} = 0
> $$
> Hence, by definition $g(x) \frac {g(x)} {1 + g(x)} = o(g(x))$ and the rest of the identity follows from simple substitution.
>
> $\blacksquare$

> [!example] $\tan x$
> We want to use the above theorem and the Taylor approximations for $\sin$ and $\cos$ to prove a formula for $\tan x$:
> $$
> \tan x = x - \frac {x^3} 3 + o(x^3)
> $$
>
> Proof.
> We have $\tan x = \frac {\sin x} {\cos x}$. We start by manipulating the Taylor expansion of $\frac 1 {\cos x}$ using property (e) and letting $g(x) = -\frac {x^2} 2$:
> $$
> \begin{align}
> \frac 1 {\cos x} &= \frac 1 {1 - \frac {x^2} 2 + o(x^3)} = 1 + \frac {x^2} 2 + o(-\frac {x^2} 2)
> \end{align}
> $$
>
> Now taking $\sin x = x - \frac {x^3} 6 + o(x^3)$, we have:
> $$
> \begin{align}
> \tan x &= (x - \frac {x^3} 6 + o(x^4))(1 + \frac {x^2} 2 + o(x^3)) \\
>
> &= x + \frac {x^3} 2 + o(x^4)
> - \frac {x^3} 6 - \frac {x^5} {12} + o(x^6)
> + o(x^4) + o(x^6) + o(x^7) \\ \\
>
> &= x + \frac {x^3} 3 - \frac {x^5} {12} + o(x^4) + o(x^6) + o(x^7) &\text{Property (a)} \\ \\
>
> &= x + \frac {x^3} 3 + o(x^3)
> \end{align}
> $$
>
> where the final simplification comes from the fact that the terms may be condensed into $o(x^3)$
>
> $\blacksquare$