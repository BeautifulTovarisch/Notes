# The Inverse Trigonometric Functions

In order to define an inverse for the [[Trig Functions]], we need to restrict the domain to an interval which is strictly monotonic (in order to preserve injectivity). For $\sin$ this is conventionally $[-\pi/2, \pi/2]$, for $\cos$, $[0, \pi]$.

## The Inverse Sine Function

From the results proved in [[Derivatives of Inverse Functions]], we know that the derivative of the inverse of $\sin$ (denoted with $\arcsin$) must be of the form:

$$
\frac d {dx} \arcsin x = \frac 1 {\cos x}
$$

Now we apply some [[Trig Functions#Fundamental Properties of Sine and Cosine]] in order to produce a function in terms of $x$:

$$
D \arcsin = \frac 1 {\cos x} = \frac 1 {\sqrt{1 - \sin^2 x}} = \frac 1 {\sqrt{1 - x^2}}
$$

defined for $|x| < 1$.

By the Fundamental Theorem of Calculus, we obtain an analytical definition for $\arcsin$.

$$
\arcsin = \int_0^x \frac 1 {\sqrt{1 - x^2}} \; dx
$$

> [!tip] Analytical Trigonometry
> The integral definition of $\arcsin$ can be used to develop trigonometry without reference to geometry.

## The Inverse Cosine Function

By the same process we derive a formula for the inverse cosine function, $\arccos x$:

$$
D \arccos x = \frac 1 {D \cos x} = - \frac 1 {\sin x} = - \frac 1 {\sqrt{1 - x^2}}
$$

Hence, we may define $\arccos x$ in terms of its antiderivative:

$$
\arccos x = - \int_0^x \frac 1 {\sqrt{1 - x^2}} \; dx
$$

## The Inverse Tangent Function

Finally, we compute the inverse tangent function. The inverse tangent function is particularly important when integrating by the method of partial fractions.

$$
D \arctan x = \frac 1 {\sec^2 x} = \frac 1 {\frac 1 {\cos^2 x}} = \frac 1 {1 + \tan^2 x} = \frac 1 {1 + x^2}
$$

Thus, $\arctan$ is again defined using the Fundamental Theorem of Calculus:

$$
\arctan x = \int_0^x \frac 1 {1 + x^2} \; dx
$$