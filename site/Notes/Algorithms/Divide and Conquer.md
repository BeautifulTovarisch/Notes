# Divide and Conquer

Divide and conquer algorithms are characterized by a procedure which breaks a problem into distinct subproblems (divide) and produces the solution to the overall problem by combining the results of the subproblems (conquer).

This paradigm differs from [[Dynamic Programming]] in that the divide operation is not concerned with determining the optimality of previous subproblems.

## Master Theorem

The master theorem is a concise summary of the runtime of certain specific recurrences which come about naturally in divide-and-conquer algorithms. This is mainly a shortcut to avoid the verbose computation of determining the value of a geometric series.

Let $T(n)$ be a recurrence with upper bound defined as follows:

$$
T(n) \leqslant a \cdot T(\frac n b) + O(n^d)
$$

Then we have,

$$
T(n) =
\begin{cases}
O(n^d \log n) & \text{if $a = b^d$} \\
O(n^d) & \text{if $a < b^d$} \\
O(n^{\log_b a}) & \text{if $a > b^d$} \\
\end{cases}
$$

Where
- $a$ Is the number of recursive calls,
- $b$ Is the decrease in the size of a subproblem in a recursive call, and
- $d$ Is the order of the work performed for each subproblem

The runtimes follow naturally from reasoning about the upper bound in each case.

### Proof

TODO

## MergeSort

Probably the most famous divide and conquer algorithm. The core idea behind MergeSort is to repeatedly bisect an array until reaching a trivial sorting problem of one element and then recursively merge each subarray, placing the element in ascending order in the final output.

```pseudo
	\begin{algorithm}
	\caption{MergeSort}
	\begin{algorithmic}
	\Procedure{Merge}{$A, B$}
	\State $i = 0, j = 0$
	\State $C = []$ \\\\
	\For{$k = 0$ \To $n-1$}
	\If{$A[i] < B[j]$}
	\State $C[k] = A[i]$
	\State $i = i + 1$ 
	\Else
	\State $C[k] = B[j]$
	\State $j = j + 1$ \\\\
	\EndIf
	\EndFor
	\Return $C$ \\\\
	\EndProcedure

	\Procedure{MergeSort}{$A$}
	\If{$len(A) \leqslant 1$}
	\Return $A$ \\\\
	\EndIf
	\State $L =$ \Call{MergeSort}{left half of $A$}
	\State $R =$ \Call{MergeSort}{right half of $A$} \\\\
	\Return \Call{Merge}{$L, R$}
	\EndProcedure
	\end{algorithmic}
	\end{algorithm}
```

### Analysis

From the pseudocode, we see there are 2 recursive calls per iteration, each dividing the input in half. Additionally, the `Merge` routine performs linear work per call, leading to the following recurrence:

$$
T(n) \leqslant 2 \cdot T(\frac n 2) + O(n)
$$

Applying the master theorem with $a = 2 = 2^1 = b^d$, we arrive at a runtime of $O(n\log n)$.

## Counting Array Inversions

Array inversions are the number of "out of place" element with respect to the sorted list. For example,

```python
A = [3, 1, 2]
```

has 2 inversions. The trivial brute-force solution involves comparing every element against the rest of the $n-1$ items, leading to a quadratic runtime.

The divide-and-conquer approach employs the generally useful idea of counting the inversions in the left and right subhalves as well as those than span the middle of the array. The following strategy sorts each subarray, counting the split inversions during the combine step.

```pseudo
	\begin{algorithm}
	\caption{Count Inversions}
	\begin{algorithmic}
	\Procedure{CountSplitInv}{$A, B$}
	\State i = j = 0
	\State inv = 0
	\State Out = [] \\\\
	\For{$k$ \To $n-1$}
	\Comment{No Inversion}
	\If{A[i] < B[j]}
	\State Out[k] = B[j]
	\State i = i + 1
	\Else
	\State Out[k] = A[j]
	\State j = j + 1
	\State inv = inv + (n - i) \\\\
    \EndIf
    \EndFor
    \Return (Out, inv) \\\\
    \EndProcedure
	\Procedure{CountInv}{$A$}
	\If{$n \leqslant 1$}
	\Return (A, 0) \\\\
    \EndIf
	\State (L, leftInv) = \Call{CountInv}{left half of $A$}
	\State (R, rightInv) = \Call{CountInv}{right half of $A$}
	\State (Merged, splitInv) = \Call{CountSplitInv}{L, R} \\\\
	\Return (Merged, leftInv + rightInv + splitInv)
    \EndProcedure
	\end{algorithmic}
	\end{algorithm}
```

### Analysis

Similar to `MergeSort`, we see two recursive calls and linear work per recursive iteration:

$$
T(n) \leqslant 2 \cdot T(\frac n 2) + O(n)
$$

And therefore `CountInv` has a runtime of $O(n \log n)$ as well.

## Karatsuba Multiplication

Anatoly Karatsuba invented this algorithm as a faster way to multiply very large integers. This happens to be the multiplication algorithm used by Python. The idea behind the algorithm is to recursively split apart each integer into halves until they are small enough to be multiplied in constant time with the normal `*` operator.

The combine step involves some manipulation of the quadratic identity.

```pseudo
	\begin{algorithm}
	\caption{Karatsuba}
	\begin{algorithmic}
	\Require $x$ and $y$ have the same number of digits
	\end{algorithmic}
	\end{algorithm}
```
