# Divide and Conquer

Divide and conquer algorithms are characterized by a procedure which breaks a problem into distinct subproblems (divide) and produces the solution to the overall problem by combining the results of the subproblems (conquer).

This paradigm differs from [[Dynamic Programming]] in that the divide operation is not concerned with determining the optimality of previous subproblems.

## MergeSort

Probably the most famous divide and conquer algorithm. The core idea behind MergeSort is to repeatedly bisect an array until reaching a trivial sorting problem of one element and then recursively merge each subarray, placing the element in ascending order in the final output.

```pseudo
	\begin{algorithm}
	\caption{MergeSort}
	\begin{algorithmic}
	\Procedure{Merge}{$A, B$}
	\State $i = 0$
	\State $j = 0$
	\For{$k = 0$ \To $n-1$}
	\If{$A[i] < B[j]$}
	\State $C[k] = A[i]$
	\State $i = i + 1$
	\Else
	\State $C[k] = B[j]$
	\State $j = j + 1$
	\EndIf
	\EndFor
	\Return $C$
    \EndProcedure

	\Procedure{MergeSort}{$A$}
	\If{$len(A) == 1$}
	\Return $A[0]$
	\EndIf
	\State $L =$ \Call{MergeSort}{left half of $A$}
	\State $R =$ \Call{MergeSort}{right half of $A$}
	\Return \Call{Merge}{$L, R$}
    \EndProcedure
	\end{algorithmic}
	\end{algorithm}
```

### Analysis

## Karatsuba Multiplication

## Counting Array Inversions