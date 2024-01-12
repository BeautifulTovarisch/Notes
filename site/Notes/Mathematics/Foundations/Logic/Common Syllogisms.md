Several [[Argument Forms]] are very common:

Modus Ponens:

$$
\begin{align}
&p \implies q \\
&p \\
&\therefore q
\end{align}
$$

Modus Tollens:

$$
\begin{align}
&p \implies q \\
&\lnot q \\
&\therefore \lnot p
\end{align}
$$

Generalization:

$$
\begin{align}
&p \\
&\therefore p \lor q
\end{align}
$$

Specialization:

$$
\begin{align}
&p \land q \\
&\therefore p
\end{align}
$$

Elimination:

$$
\begin{align}
&p \lor q \\
&\lnot p \\
&\therefore q
\end{align}
$$

Transitivity:

$$
\begin{align}
&p \implies q \\
&q \implies r \\
&\therefore p \implies r
\end{align}
$$

Division into Cases:

$$
\begin{align}
&p \lor q \\
&p \implies r \\
&q \implies r \\
&\therefore r
\end{align}
$$

Contradiction:

$$
\begin{align}
&p \implies F \\
&\therefore \lnot p
\end{align}
$$

## Example Deduction

Consider the following argument form:

- a) $\lnot p \land \lnot r \implies s$
- b) $p \implies \lnot q$
- c) $\lnot t$
- d) $t \lor \lnot s$
- e) $r \implies \lnot q$
- f) $\therefore \lnot q$

we can reduce the premises a-e using logical equivalences and knowledge of common syllogism:

> [!abstract] Verification of an argument form.
> We prove the logical deduction in the argument form above.
> 1. Using (c), (d) applying Division into cases:
>
> $$
> \begin{align}
> &t \lor \lnot s \\
> &\lnot t \\
> &\therefore \lnot s
> \end{align}
> $$
>
> 2. Using (1), (a) applying Modus Tollens
>
> $$
> \begin{align}
> &\lnot p \land \lnot r \implies s \\
> &\lnot s \\
> &\therefore \lnot (\lnot p \land \lnot r)
> \end{align}
> $$
>
> 3. Applying DeMorgan's  to (2)
>
> $$
> \begin{align}
> &\lnot (\lnot p \land \lnot r) \\
> &\equiv p \lor r
> \end{align}
> $$
>
> 4. Dividing (3) into cases over $\lnot q$:
>
> $$
> \begin{align}
> &p \lor r \\
> &p \implies \lnot q \\
> &r \implies \lnot q \\
> &\therefore \lnot q
> \end{align}
> $$