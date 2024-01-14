# Integration of the Trigonometric Functions

$$
\begin{align}
&\int_a^b \sin x \; dx = -(\cos b - \cos a) \\
&\int_a^b \cos x \; dx = \sin b - \sin a
\end{align}
$$

We establish an inequality which demonstrates the integral of the sine function. We use this integral to then show the formula for the definite integral of the cosine.

> [!warning]
> This proof is a beast. Proceed slowly and carefully.

> [!abstract] Theorem 2.4
> For $0 \leqslant a \leqslant \frac \pi 2$ and $n \geqslant 1$
> $$
> \frac a n \sum_{k=1}^{n} \cos \frac {ka} n \lt
> \sin a \lt
> \frac a n \sum_{k=0}^{n-1} \cos \frac {ka} n
> $$
>
> Proof.
> First we establish an equivalent inequality which lets us leverage the [[Trig Functions#Basic Identities]] of the sine and cosine.
>
>> [!abstract] Lemma
>> For any real $x$ and $n \geqslant 1$:
>> $$
>> 2\sin \frac x 2 \sum_{k=1}^n \cos kx = \sin (n-1)x - \sin \frac x 2
>> $$
>>
>> Proof.
>> Let $a = k + \frac 1 2, b = k - \frac 1 2$, then $a + b = 2kx, a - b = x$. By the difference formula we have:
>> $$
>> 2 \sin \frac x 2 \cos kx = \sin (k + \frac 1 2)x - \sin (k - \frac 1 2)x
>> $$
>>
>> Taking $k = 1, 2, \dots, n$ and adding the respective terms we have:
>>
>> $$
>> \begin{align}
>> 2\sin \frac x 2 \sum_{k=1}^n \cos kx &= \sin (n + \frac 1 2)x - \sin (\frac x 2) &\text{Telescoping Sum} \\
>> &= \sum_{k=1}^n \cos kx = \frac {\sin (n + \frac 1 2)x - \sin (\frac x 2)} {2\sin \frac x 2} \\
>> &= \sum_{k=0}^{n-1} \cos kx = \frac {\sin ((n-1) + \frac 1 2)x - \sin (\frac x 2)} {2\sin \frac x 2} + 1 &\text{$\cos 0 = 1$} \\
>> &= \sum_{k=0}^{n-1} \cos kx = \frac {\sin (n - \frac 1 2)x + \sin (\frac x 2)} {2\sin \frac x 2} \\ \\
>> &&\blacksquare
>> \end{align}
>> $$
>
> Letting $x = \frac a n$, $0 \lt a \lt \frac \pi 2$,
> $$
> \sum_{k=0}^{n-1} \cos \frac {ka} n = \frac {\sin (n - \frac 1 2)\frac a n + \sin (\frac {ka} {2n})} {2\sin \frac {ka} {2n}}
> $$
>
> Thus we have:
> $$
> \begin{align}
> &\frac a n \sum_{k=1}^{n} \cos \frac {ka} n \lt
> \sin a \lt
> \frac a n \sum_{k=0}^{n-1} \cos \frac {ka} n  \iff \\ \\
> &\frac a n \frac {\sin (n + \frac 1 2)\frac a n - \sin (\frac {a} {2n})} {2\sin \frac {a} {2n}} \lt
> \sin a \lt
> \frac a n \frac {\sin (n - \frac 1 2)\frac a n + \sin (\frac {a} {2n})} {2\sin \frac {a} {2n}}
> \end{align}
> $$
>
> Where this inequality holds due to the fact that cosine is monotonically decreasing over the interval. Dividing both sides by $\frac a n$ and multiplying by $2\sin \frac a {2n}$:
> $$
> \sin (n + \frac 1 2) \frac a n - \sin (\frac a {2n}) \lt
> \sin a (\frac {2\sin \frac a {2n}} {\frac a n}) \lt
> \sin (n - \frac 1 2)\frac a n + \sin (\frac a {2n})
> $$
>
> Now let $\theta = \frac a {2n}$ (and so $\frac a n = 2\theta$, $a = 2n \theta$):
> $$
> \sin (2n + 1) \theta - \sin \theta \lt
> \sin 2n\theta (\frac {\sin \theta} \theta) \lt
> \sin (2n - 1)\theta + \sin \theta
> $$
>
> We first show the left side of the inequality holds by noticing
> $$
> \sin (2n + 1)\theta = \sin 2n\theta \cos \theta + \cos 2n\theta \sin \theta \lt \sin 2n\theta \frac {\sin \theta} \theta + \sin \theta
> $$
> Using the fact that:
> - $\cos \theta \lt \frac {\sin \theta} \theta$ (Property 4)
> - $0 < \sin \theta$
> - $0 \lt \cos 2n\theta \leqslant 1$
>
> Now taking the right inequality and again applying the addition formula for sine:
> $$
> \begin{align}
> &\sin (2n - 1)\theta = \sin 2n\theta \cos \theta - \cos 2n\theta \sin \theta \iff \\
> &\sin(2n - 1)\theta + \sin \theta = \sin 2n\theta \cos \theta - \cos 2n\theta \sin \theta + \sin \theta \iff \\
> &\sin (2n - 1) + \sin \theta = \sin 2n\theta(\cos \theta + \sin \theta \frac {1 - \cos2n\theta} {\sin 2n\theta}) &\text{Factoring}
> \end{align}
> $$
> Finally, applying the trig identities:
> - $1 -\cos 2x = 2\sin^2 x$
> - $\sin 2x = 2\sin x \cos x$
>
> $$
> \frac {1 - \cos 2n\theta} {\sin 2n\theta} = \frac {2 \sin^2n\theta} {2\sin \theta \cos \theta} = \frac {\sin n \theta} {\cos n \theta}
> $$
> And so we have:
> $$
> \begin{align}
> \sin (2n - 1) + \sin \theta &= \sin 2n\theta(\cos \theta + \sin \theta \frac {\sin n \theta} {\cos n\theta}) \\ \\
> &= \sin 2n\theta(\frac {\cos \theta \cos n\theta + \sin \theta \sin n \theta} {\cos n \theta}) &\text{Property 2, $(n - 1)\theta$} \\ \\
> &= \sin 2n\theta (\frac {\cos (n-1)\theta} {\cos n \theta})
> \end{align}
> $$
>
> Recalling the inequality above, we want to show:
> $$
> \sin 2n\theta (\frac {\sin \theta} \theta) < \sin 2n\theta (\frac {\cos (n-1)\theta} {\cos n \theta}) \iff \frac {\sin \theta} \theta < \frac {\cos (n-1)\theta} {\cos n \theta}
> $$
>
> Applying the addition formula for the cosine:
> $$
> \begin{align}
> \cos n\theta &= \cos((n-1) + 1)\theta = \cos(n-1)\theta \cos\theta
> - \sin(n-1)\theta \sin\theta  \\
> &\lt \cos(n-1)\theta \cos \theta \lt
> \cos(n-1)\theta \frac \theta {\sin \theta} \\
> &\iff \cos \theta \lt \frac \theta {\sin \theta}
> \end{align}
> $$
>
> Where the final property follows from the inequality in property 4.
>
> $\blacksquare$