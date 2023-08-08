We want to be able to determine whether a function can be expressed in terms of a matrix-vector multiplication, in other words, if such a function is **linear**.

> [!info] Linear Function (Linear Transformation)
> Let $U, V$ be vector spaces over a field $\mathbb{F}$. A function $f: U \to V$ is called a **linear function** (or **linear transformation**) if it satisfies the following properties:
> 1. For any $u \in U, \alpha \in \mathbb{F}$, $f(\alpha u) = \alpha f(u)$
> 2. For any $u, v \in U$, $f(u + v) = f(u) + f(v)$.
> 
> We note the similarities to [[Multiplying Matrices and Vectors#Algebraic Properties]] of matrix multiplication.

Using the above definition, we want to proof the following proposition.

> [!abstract] Theorem.
> For any matrix $M$, $x \mapsto M * x$ is linear function.
> 
> Proof.
> Let $M$ be an $R \times C$ matrix over $\mathbb{F}$ and defined $f: \mathbb{F}^C \to \mathbb{F}^R$ by $f(x) = M * x$. By algebraic properties under matrix multiplication, we see $f$ satisfies both properties required to be a linear function. $\blacksquare$

We use this theorem to proof another important result:

> [!abstract] Theorem.
> For any $C$-vector $a$ over $\mathbb{F}$, defined $f: \mathbb{F}^C \to \mathbb{F}$ by $f(x) = a * x$, where $x$ is a vector. The function $f$ is a linear function.
> 
> Proof.
> Let $M$ be the matrix comprised entirely of $a$, (i.e):
> $$
> M = 
> \begin{bmatrix}
> a_1 & a_2 & \dots & a_C
> \end{bmatrix}
> $$
> 
> Then $f(x) = M * x$, and by previous theorem, $f$ is linear. $\blacksquare$

## Bilinearity of the Dot Product

For any vector $w$, $x \mapsto w * x$ is a linear function (with $w = M$) and so it is linear. Additionally, by [[Dot Product#Algebraic Properties|commutativity]] of the dot product, $x \mapsto x * w$ is also linear. We say that the dot product is **bilinear** in both of its arguments.

> [!example] bilinearity of vector addition
> By [[The Vector#Vector Addition]] for vectors $x, y$, $x \mapsto x + y$ is bilinear in both of its arguments by commutativity.

## Linear Functions and the 0 Vector

We build up the foundation of the **kernel** of a linear function.

> [!abstract] Lemma.
> If $f: U \to V$ is a linear function, then $f$ maps the zero vector of $U$ to the zero vector of $V$.
> 
> Proof.
> Let $u_0, v_0$ be zero vectors in $U, V$ respectively. Then,
> $$
> f(u_0) = f(u_0 + u_0) = f(u_0) + f(u_0)
> $$
> Subtracting $f(u_0)$ from both sides:
> $$
> 0 = f(u_0) \iff v_0 = f(u_0)
> $$

We use this finding to define the **kernel** of $f$:

> [!info] Kernel of Linear Function
> We define the **kernel** of a linear function $f$ to be $\{ v: f(v) = 0 \}$, denoted Ker $f$.

> [!abstract] Lemma.
> Ker $f$ is a [[Vector Spaces|vector space]].
> 
> Proof.
> We must show that Ker $f$ satisfies the three properties of a vector space. To see that the kernel contains the zero vector, let $v$ be a vector in Ker $f$. By linearity of $f$, we have $f(v - v) = f(v) - f(v) = 0 = f(0)$ so then Ker $f$ contains the zero vector.
> 
> Next, suppose $v$ is a vector in Ker $f$ and $\alpha \in \mathbb{F}$. Then again by linearity of $f$, $\alpha f(v) = \alpha 0 = 0 = f(\alpha v)$. So the kernel is closed under scalar multiplication.
> 
> Finally, suppose $v, u$ are in the kernel of $f$, so then $f(u + v) = f(u) + f(v) = 0 + 0$ by definition of the kernel, and so Ker $f$ is closed under vector addition, and thus it is a vector space.
> 
> $\blacksquare$

## Bijectivity of a Linear Function

We show now that a linear function is bijective if its kernel is a trivial vector space (consisting of only the zero vector).

### Injectivity

> [!abstract] Lemma
>  A linear function is injective if and only if its kernel is a trivial vector space.
>
>Proof.
>Suppose a linear function $f$ is injective and suppose some non-zero vector $v$ is in Ker $f$. Since Ker $f$ is a vector space, it contains the zero vector. But then if $f(0) = f(v)$, then $f$ is not injective.
>
>Now suppose Ker $f$ is a trivial vector space, and let $v_1, v_2$ be any vectors such that $f(v_1) = f(v_2)$. Then $f(v_1) - f(v_2) = 0$ and by linearity of $f$, $v1 - v2$ is in Ker $f$ so then $v_1 = v_2 = 0$ by assumption and so $f$ is injective.
>
>$\blacksquare$

We use this finding to reason about the uniqueness of solutions to a matrix-vector multiplication (and hence to an arbitrary [[Linear Systems]]).

> [!tip] Uniqueness of the Pre-Image of a Linear Function
> Consider $f(x) = M * x = b$. Then we can consider the task of finding $x$ as that of finding a pre-image of $b$ under $f$. If $f$ is 1-1, we know this **pre-image is unique**.

### Surjectivity

> We can't prove this completely, yet, but we can prove the forward direction.

> [!abstract] Lemma
> If $f : U \to W$, $f$ is onto if and only if $\{ f(u) : u \in U \} = W$. That is, the image of $f$ is a subspace of $W$.
> 
> Proof (->).
> By definition of Image, $f(U) \subseteq W$, so we must show that the image of $f$ is a vector space. By previous lemma, $f$ maps the zero vector of $U$ to that of $W$, so the zero vector of $W$ is in $f(U)$.
> Next, by linearity of $f$, we have $u_1, u_2 \in U$ such that $f(u_1 + u_2) = f(u_1) + f(u_2)$ both in $W$, so the image of $f$ is closed under vector addition. Finally, choose some scalar $\alpha$ and notice again by linearity of $f$, $\alpha f(U) = f(\alpha U) \subseteq \alpha W$ and so $f(U)$ is closed under scalar multiplication.
> 
> $\blacksquare$

### Inverse

If a linear function is a bijection then it has an [[Functions#Inverse]] and that inverse also is linear.

> [!abstract] Theorem.
> If $f$ is a linear function and $g$ is its inverse, then $g$ is also linear.
> 
> Proof.
> We must show $g$ satisfies linearity.
> 
> 1. Suppose $y_1, y_2$ are in the domain of $g$. By definition of inverse, $g^{-1}(y_1) = x_1$ and $g^{-1}(y_2) = x_2$. By by linearity of $f$, we know that $f(x_1) + f(x_2) = f(x_1 + x_2)$ and so:
> $$
> \begin{align}
> g(f(x_1) + f(x_2)) &= g(f(x_1 + x_2)) \\
> &= g(y_1 + y_2) \\
> &= x_1 + x_2 &\text{Def. of Inverse} \\
> &= g(y_1) + g(y_2) \\ \\
> &&\blacksquare 
> \end{align}
> $$
> 
> 2. Now suppose $\alpha$ is a scalar and $y$ is in the domain of $g$. Then
> $$
> \begin{align}
> g(\alpha y) &= \\
> &= g(\alpha f(x)) \\
> &= g(f(\alpha x)) &\text{Linearity of $f$} \\
> &= \alpha x &\text{Def. of Inverse} \\
> &= \alpha g(y) \\ \\
> &&\blacksquare 
> \end{align}
> $$