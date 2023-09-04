The validity of a logical construct comes from its **structure**, not its **contents**.

## Proposition

> [!info] Proposition:
> A statement that can be true or false.

### Logical Equivalence

> [!abstract] Theorem 5.1: Logical Equivalences.
> $$
> \begin{align}
> &\text{Commutativity} &p \land q \equiv q \land p \\ \\
> &\text{Associativity} &(p \land q) \land r \equiv p \land (q \land r) \\ \\
> &\text{Distributivity} &p \land (q \lor r) \equiv (p \land q) \lor (p \land r) \\ \\
> &\text{Absorption} &p \land (p \lor q) \equiv p, p \lor (p \land q) \equiv p \\ \\ 
> &\text{Idempotency} &p \land p \equiv p, p \lor p \equiv p \\ \\
> &\text{Double Negation} &\lnot \lnot p \equiv p \\ \\
> &\text{DeMorgan's} &\lnot (p \land q) \equiv \lnot p \lor \lnot q \\ \\
> &\text{Negation} &p \lor \lnot p \equiv T, p \land \lnot p \equiv F \\ \\
> &\text{Universal Bound} &p \lor T \equiv T, p \land F \equiv F \\ \\
> &\text{Identity} &p \lor T \equiv p \\ \\
> &\text{Tautology and Contradiction} &\lnot T \equiv F, \lnot F \equiv T 
> \end{align}
> $$

We verify the first half of the Absorption law below using a proof table as an exercise:

| $p$ | $q$ | $p \lor q$ | $p \land (p \lor q)$|
| :-: | :-: |:----------:|:-------------------:|
| T   | T   | T          | T                   |
| T   | F   | T          | T                   |
| F   | T   | T          | F                   |
| F   | F   | F          | F                   |

Some examples of verification by applying the equivalences from **Theorem 5.1**

> [!abstract] Verify 
> $$ 
> (q \land p) \lor \lnot (p \lor \lnot q) \equiv q
> $$
> Proof.
> $$
> \begin{align}
> &\; (q \land p) \lor \lnot (p \lor \lnot q) \\
> &\equiv (q \land p) \lor (\lnot p \land q) &\text{DeM.} \\
> &\equiv q \land (p \lor \lnot p) &\text{Dist.} \\
> &\equiv q \land T &\text{Identity} \\
> &\equiv q \\
> &&\blacksquare
> \end{align}
> $$

> [!abstract] Verify 
> $$
> \lnot (\lnot (p \land p) \lor (\lnot q \land T))
> $$
>Proof.
>$$
>\begin{align}
>& \lnot (\lnot (p \land p) \lor (\lnot q \land T)) \\
>&\equiv \lnot (\lnot p \lor (\lnot q \land T)) &\text{Idemp.} \\
>&\equiv p \land \lnot (\lnot q \land T) &\text{Dbl. Neg} \\
>&\equiv p \land (q \lor T) &\text{DeM.} \\
>&\equiv p \land q &\text{Univ. Bound} \\
>&&\blacksquare
>\end{align}
>$$ 

## Conditional Propositions

We write the truth tables below for interesting findings:

### Implication

| $p$ | $q$ | $p \implies q$ |
| :-: | :-: | :------------: |
| T   | T   | T              | 
| T   | F   | F              | 
| F   | T   | T              | 
| F   | F   | T              | 

> [!info] The third and fourth row are called "vacuously true".

A more interesting truth table suggesting an equivalence of implication:

| $p$ | $q$ | $p \lor q$ | $\lnot (p \lor q)$ | $q \lor \lnot (p \lor q)$ | $p \implies q$ |
| :-: | :-: | :--------: | :----------------: | :-----------------------: | :------------: |
| T   | T   | T          | F                  | T                         | T              |
| T   | F   | F          | F                  | F                         | F              |
| F   | T   | T          | F                  | T                         | T              |
| F   | F   | F          | T                  | T                         | T              |

### Negation

| $p$ | $q$ | $p \implies q$ | $\lnot (p \implies q)$ |
| :-: | :-: | :------------: | :--------------------: |
| T   | T   | T              | F                      |
| T   | F   | F              | T                      |
| F   | T   | T              | F                      |
| F   | F   | T              | F                      |

### Converse, Inverse, and Contrapositive


$$
\begin{align}
&p \implies q \\ \\
&\text{Converse} &q &\implies p \\
&\text{Inverse} &\lnot p &\implies \lnot q \\
&\text{Contrapositive} &\lnot q &\implies \lnot p \\
&\text{Biconditional} &p &\iff q \\
\end{align}
$$

> [!warning] 
> Neither the Converse nor the Inverse is logically equivalent!