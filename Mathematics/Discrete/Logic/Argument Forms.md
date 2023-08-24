An argument is a sequence of [[Logical Propositions]]. Arguments allow a more sophisticated composition of logical deduction than a single, large proposition.

## Argument

> [!info] Definitions:
> - Argument - Sequence of propositions
> - Argument Form - Sequence of proposition forms
> - Premises - All but the last argument in an argument form
> - Conclusion - The last argument in an argument form

Arguments are considered **valid** or **invalid**. An argument is **valid** if and only if all premises and the conclusion are **True**.

> [!example] Basic argument
> $$
> \begin{align}
> &p \implies q \\
> &p \\
> &\therefore q \\
> \end{align}
> $$
> Here, we have **premises:** $p \implies q$ and $p$ which lead to **conclusion** $q$.

## Critical Rows

Consider the logical form:

$$
\begin{align}
&p \implies q \\
&p \\
&\therefore q
\end{align}
$$

represented by the truth table:

| $p$ | $q$ | $p \implies q$ | $q$ |
| :-: | :-: | :------------: | :-: |
| T   | T   | T              | T   |
| T   | F   | F              | F   |
| F   | T   | T              | T   |
| F   | F   | T              | F   |

Row 1 is considered a **critical row** because all premises are true. We see that the argument is **valid** because the conclusion, $q$ is also true. 

> [!info] Validity using Critical Rows
> If even **one** critical row leads to a false conclusion, the argument is **invalid**.

### Invalid Argument Example

Suppose the following argument:

$$
\begin{align}
&p \implies q \\
&q \\
&\therefore p
\end{align}
$$

and consider its truth table:

| $p$ | $q$ | $p \implies q$ | $p$ |
| :-: | :-: | :------------: | :-: |
| T   | T   | T              | T   |
| T   | F   | F              | T   |
| F   | T   | T              | F   |
| F   | F   | T              | T   |

The first and third row are critical rows, and while the first row is valid, the third row proves that the argument leads to a false conclusion, and is therefore invalid.