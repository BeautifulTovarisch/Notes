
## Fundamental Properties of Sine and Cosine

These properties are used heavily in Calculus to manipulate integrals involving the trig functions.

1. **Domain**: $\sin$ and $\cos$ are defined everywhere on $\mathbb{R}$
2. $\cos 0 = \sin \pi / 2 = 1$, $\cos \pi = -1$
3. $\cos(y - x) = \cos y \cos x + \sin y \sin x$
4. For $0 \lt x \lt \pi / 2$, $0 \lt \cos x \lt \frac {\sin x} x \lt \frac 1 {\cos x}$

We use these "axioms" to develop the following theorem:

### Basic Identities

> [!abstract] Theorem (2.3)
> $$
> \begin{align}
> &\cos^2 x + \sin^2 x = 1 &\text{Pythagorean} \\ \\
> &\sin 0 = \cos {\pi / 2 } = \sin \pi = 0 &\text{Special Values} \\ \\
> &\cos(-x) = \cos x, \; \sin(-x) = -\sin x &\text{Even, Odd} \\ \\
> &\sin(x + \pi/2) = \cos x, \; \cos(x + \pi/2) = -\sin x &\text{Co-Relations} \\ \\
> &\sin(x + 2\pi) = \sin x, \; \cos(x + 2\pi) = \cos x &\text{Periodicity} \\ \\
> &\cos(x+y) = \cos x \cos y - \sin x \sin y &\text{Additivity} \\
> &\sin(x+y) = \sin x \cos y + \cos x \sin y \\ \\
> &\sin a - \sin b = 2 \sin \frac {a-b} 2 \cos \frac {a+b} 2
> &\text{Difference Formulas} \\
> &\cos a - \cos b = -2 \sin \frac {a-b} 2 \sin \frac {a+b} 2 \\ \\
> &\text{Over $[0, \pi/2]$, sine strictly increasing, cosine strictly decreasing}&\text{Monotonicity}
> \end{align}
> $$

### Proofs of the Basic Identities

> [!abstract] Pythagorean Identity
> $\sin^2x + \cos^2x = 1$
>
> Proof.
> Using property #2 and letting $y = x$ we have:
> $$
> \begin{align}
> \cos(y - x) &= \cos 0 \\
> &= \cos y \cos x + \sin y \sin x &\text{Property 3} \\
> &= \cos^2 x + \sin^2 x \\
> &= 1 &\text{Property 2} \\ \\
> &&\blacksquare
> \end{align}
> $$

> [!abstract] Special Values
> $\sin 0 = cos\frac \pi 2 = \sin \pi = 0$
>
> Proof.
> Letting $x = 0, x = \pi/2, x = \pi$ and applying the Pythagorean Identity:
> $$
> \begin{align}
> \sin^2 0 + \cos^2 0
> &= \sin^2 \pi/2 + \cos^2 \pi/2
> = \sin^2 \pi + \cos^2 \pi = 1 \\
> &= \sin^2 0 + 1
> = \cos^2 \pi/2 + 1
> = \sin^2 \pi - 1 &\text{Property 2} \\
> &= \sin^2 0 = \cos^2 \pi/2 = \sin^2 \pi = 0 \\
> &= \sin 0 = \cos \pi/2 = \sin \pi = 0 \\ \\
> &&\blacksquare
> \end{align}
> $$

> [!abstract] Even and Odd
> $\cos (-x) = \cos x$
> $\sin (-x) = -\sin x$
>
> Proof.
> We establish another formula and use it to prove the evenness of cosine and oddness of sine:
>
>> [!abstract] Lemma
>> $\cos(\pi/2 - x) = \sin x$
>>
>> Proof.
>> Using property 2 and Special Values, we have:
>> $$
>> \cos(\pi/2 - x) = \cos \pi/2 \cos x + \sin \pi/2 \sin x \\
>> = \sin x \; \blacksquare
>> $$
>
> Now we let $x = \pi/2 - x$ in the formula above:
> $$
> \begin{align}
> \sin (-x) &= \cos (\pi/2 + x) \\
> &= \cos(\pi - (\pi/2 - x)) \\
> &= \cos \pi \cos(\pi/2 - x) - \sin \pi \sin (\pi/2 - x) &\text{Property 3} \\
> &= -\sin(x) &\text{Special Values, Lemma}
> \end{align}
> $$
>
> Finally, let $y = 0$ and see that:
> $$
> \begin{align}
> \cos (y - x) &= \cos(-x) \\
> &= \cos 0 \cos(x) + \sin 0 \sin(x) &\text{Propery 3} \\
> &= \cos x &\text{Special Values}
> \end{align}
> $$
>
> $\blacksquare$

> [!abstract] Co-Relations
> $\cos (x + \pi/2) = -\sin x$
> $\sin (x + \pi/2) = \cos x$
>
> Proof.
> Using the formula shown by the lemma in the proof of Even and Odd properties, first let $x = -x$:
> $$
> \begin{align}
> \cos (\pi/2 + x) &= \cos (\pi/2 - (-x))  \\
> &= \cos \pi/2 \cos(-x) + \sin \pi/2 \sin(-x) &\text{Property 3} \\
> &= \sin(-x) &\text{Special Values, Property 2} \\
> &= -\sin x &\text{Odd Property of the Sine} \\ \\
> &&\blacksquare
> \end{align}
> $$
>
> And now letting $x = \pi/2 + x$:
> $$
> \begin{align}
> \cos x &= \cos(-x) \\
> &= \cos(\pi/2 - (\pi/2 + x)) \\
> &= \cos \pi/2 \cos (\pi/2 + x) + \sin \pi/2 \sin (\pi/2 + x) &\text{Property 3} \\
> &= \sin (\pi/2 + x) &\text{Special Values} \\ \\
> &&\blacksquare
> \end{align}
> $$

> [!abstract] Periodicity
> $\cos (x + 2\pi) = \cos x$
> $\sin (x + 2\pi) = \sin x$
>
> Proof.
> Repeatedly using Co-Relations and "iterating" through $2\pi$ in increments of $\pi/2$ we have:
> $$
> \begin{align}
> \cos(x + 2\pi) &= \cos((x + 3\pi / 2) + \pi / 2) \\
> &= -\sin (x + 3\pi/2) \\
> &= -\cos (x + \pi) \\
> &= \sin (x + \pi/2) \\
> &= \cos x \\ \\
> \sin(x + 2\pi) &= \sin((x + 3\pi / 2) + \pi/2) \\
> &= \cos (x + 3\pi / 2) \\
> &= -\sin (x + \pi) \\
> &= -\cos (x + \pi / 2) \\
> &= \sin x \\ \\
> &&\blacksquare
> \end{align}
> $$

> [!abstract] Addition Formulas
> $$
> \cos (x + y) = \cos x \cos y - \sin x \sin y
> $$
> $$
> \sin (x + y) = \sin x \cos y + \cos x \sin y
> $$
>
> Proof.
> $$
> \begin{align}
> \cos (x + y) &= \cos(y - (-x)) \\
> &= \cos y \cos (-x) + \sin y \sin (-x) \\
> &= \cos x \cos y - \sin x \sin y &\text{Even and Odd} \\ \\
>
> \sin (x + y) &= -\cos((x+y) + \pi/2) &\text{Co-Relations} \\
> &= -[\cos x \cos (y + \pi/2) - \sin x \sin (y + \pi/2)] &\text{Cosine Addition} \\
> &= -[-\cos x \sin y - \sin x \cos y] &\text{Co-Relations} \\
> &= \cos x \sin y + \sin x \cos y
> &&\blacksquare
> \end{align}
> $$

> [!abstract] Difference Formulas
> $$
> \sin a - \sin b = 2\sin (\frac {a-b} 2) \cos (\frac {a+b} 2 )
> $$
> $$
> \cos a - \cos b = -2\sin (\frac {a-b} 2) \sin (\frac {a+b} 2)
> $$
>
> Proof.
>
> Notice that for $x = \frac {a+b} 2$, $y = \frac {a-b} 2$ we have $x + y = a$, $x - y = b$. Using the addition formulas for sine and cosine:
> $$
> \begin{align}
> \cos(x + y) - \cos(x - y) &= \cos a - \cos b \\
> &= \cos x \cos y - \sin x \sin y \\
> & - \cos x \cos y - \sin x \sin y &\text{Addition, Odd Property} \\
> &= -2 \sin x \sin y \\
> &= -2 \sin (\frac {a+b} 2) \sin (\frac {a-b} 2) \\ \\
> \sin(x + y) - \sin(x - y) &= \sin a - \sin b \\
> &= \sin x \cos y + \cos x \sin y \\
> &- \sin x \cos y + \cos x \sin y &\text{Addition, Odd, Even Properties} \\
> &= 2\sin y \cos x \\
> &= 2\sin (\frac {a-b} 2) \cos (\frac {a+b} 2) \\ \\
> &&\blacksquare
> \end{align}
> $$

> [!abstract] Monotonicity
> Over the interval $[0, \pi/2]$:
> - $\cos$ is strictly **decreasing**
> - $\sin$ is strictly **increasing**
>
> Proof.
> We use Property 4 and the difference formula to show that for $0 \lt b \lt a \lt \frac \pi 2$ $\sin a - \sin b \gt 0$ and $\cos a - \cos b \lt 0$. By property #4, $\sin$ and $\cos$ are positive over the entire interval. Let $x = \frac {a+b} 2$ and $y = \frac {a-b} 2$. We see by the difference formulas that $\sin a - \sin b$ is 2 times some positive real and $\cos a - \cos b$ is -2 times some positive real, hence $\sin a - \sin b \gt 0 \implies \sin a > \sin b$ and $\cos a - \cos b \lt 0 \implies \cos a < \cos b$ and hence the respective definitions of strict monotonicity are satisfied.
>
> $\blacksquare$