# Vectors over GF(2)

>[!todo] Link this to GF(2) notes

We can represent $n$-[[The Vector|vectors]] in $GF(2)$ as $n$-bit binary strings

> [!example] Binary String
> Let $u = 1101$, $v = 0111$ over $GF(2)$ then
> $$
> u + v = [1, 1, 0, 1] + [0, 1, 1, 1] = [1, 0, 1, 0]
> $$

## Perfect Secrecy Revisited

We want to send a 10-bit plain-text document $p$ from Alice to Bob.

### Vernam's Cipher

Alice and Bob agree ahead of time on a $k$-bit cipher represented by a $k$-vector in $GF(2)$. Alice computes the following:
$$\begin{align}
&\text{ Encryption } &c = p + k \\
&\text{ Decryption } &p = c - k
\end{align}$$
> [!example]
> Let $k = 0110100001, \; p = 0001110101$. Then $c = p + k = 0111010100$

### Lights Out Puzzle

The objective of the "Lights Out"  puzzle is to find a sequence of button presses such that, given any initial configuration of lights on or off, all lights are turned off at the end of the sequence. We can model this puzzle using vectors over $GF(2)$:
$$
\begin{array}{c}
1 & 1 & 1 & 1 & 0 \\
1 & 1 & 1 & 0 & 1 \\
1 & 1 & 1 & 0 & 1 \\
0 & 0 & 0 & 1 & 1 \\
1 & 1 & 0 & 1 & 1
\end{array}
$$
Where 1 and 0 represent "On" and "Off", respectively. Pushing a button (cell) inverts its (non-diagonal) neighbors. We use a vector in $GF(2)$ to represent the **state change** of the puzzle:
$$
\left[ \begin{array}{cc}
1 & 1 & 1 & 1 & 0 \\
1 & 1 & 1 & 0 & 1 \\
1 & 1 & 1 & 0 & 1 \\
0 & 0 & 0 & 1 & 1 \\
1 & 1 & 0 & 1 & 1
\end{array} \right]
+
\underbrace{\left[ \begin{array}{cc}
(0, 0):1 & (0, 1):1 & (1, 0):1
\end{array} \right]}_\text{Button Push vector}
=
\left[ \begin{array}{cc}
0 & 0 & 1 & 1 & 0 \\
0 & 0 & 1 & 0 & 1 \\
1 & 1 & 1 & 0 & 1 \\
0 & 0 & 0 & 1 & 1 \\
1 & 1 & 0 & 1 & 1
\end{array} \right]
$$
>[!info]
>This is modeled by normal vector addition in $GF(2)$

We can think of the solution to this problem as the solution to the following:
$$
\begin{align}
s + v_0 + v_1 + \dots + v_n = 0
\end{align}
$$
where $s$ represents the initial state of the puzzle and $v_0 \to v_n$ represent a sequence of button push vectors. This ends up reducing to the problem of solving a [[Linear Equations|linear system].