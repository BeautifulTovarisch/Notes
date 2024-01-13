# The Natural Logarithm

Recall from [[Journey to the Natural Log#A Closer Look at Our Formula]] the general form of the solution we'd like to see:

$$
g(x) = \int_1^x \frac 1 t \; dt
$$

> [!todo]
> Plots

and define the **Natural Logarithm** as follows:

> [!info] Definition of the Natural Logarithm
> If $x$ is a positive real, we define $\ln(x)$ (or $\log(x)$ to be:
> $$
> \ln(x) = \int_1^x \frac 1 t \; dt
> $$

## Properties of the Natural Logarithm

Immediately from our groundwork we can conclude a few important properties of the natural logarithm:

> [!abstract] Properties of the Natural Log
> $$
> \begin{align}
> &(a) &\ln(1) = 0 \\ \\
> &(b) &\ln'(x) = \frac 1 x \\ \\
> &(c) &\ln(ab) = \ln(a) + \ln(b)
> \end{align}
> $$
>
> Proof.
> Property $(a)$ follows immediately from the definition of the natural log:
> $$
> \ln(1) = \int_1^1 \frac 1 t \; dt = 0
> $$
>
> Using the first fundamental theorem of calculus, we find $\frac d {dx} \int_1^x \frac 1 t \; dt = \frac 1 x$, which shows property $(b)$.
>
> Finally, using the [[Properties of the Integral of a Step Function|additive property of the integral]], we find:
> $$
> \begin{align}
> \ln(ab) = \int_1^{ab} \frac 1 t \; dt &= \int_1^a \frac 1 t \; dt + \int_a^{ab} \frac 1 t \; dt \\ \\
> &= \ln(a) + \int_a^{ab} \frac 1 t \; dt \\ \\
> &= \ln(a) + a \int_1^b \frac 1 t \; dt \\ \\
> &= \ln(a) + \int_1^b \frac 1 u \; du &(u = \frac t a, du = \frac 1 a) \\ \\
> &= \ln(a) + \ln(b) \\ \\
> &&\blacksquare
> \end{align}
> $$