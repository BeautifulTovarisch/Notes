This section contains some basic algorithms and nicely transitions to proofs of correctness for algorithms later on.

> [!info] Algorithm
> An **algorithm** is a series of steps operating on an input which produces an output that is the solution to some problem

## Long Division

> [!todo] 
> Express this as a mathematical algorithm and rewrite to be cleaner.

```Python
def longdiv(divisor, dividend, N):
	result = remainder = 0
	i = N - 1
	
	while dividend > 0:
		remainder = remainder * 10 + (dividend // (10 ** i))
		quotient = remainder // divisor
		product = quotient * divisor
		result = result * 10 + quotient
		remainder = remainder - product
		
		dividend = dividend % (10 ** i)
		
		i -= 1
	
	return (result, remainder)

# longdiv(8, 3521, 4) == (440, 1)
```

## Powerset 

Computing the powerset involves appending those subsets containing a given $a \in A$ and those without. The powerset in this manner is built up [[Induction|inductively]] starting with the null set as a basis.

I include two algorithms here, one is hopelessly convoluted (from the book). The other is one I wrote (which could be simplified using list comprehensions).

```Python
# Book Version
def powerset(S):
	rem = S
	powset = [[]]

	while len(rem):
		powadd = []
		remPSet = powset
		cur = rem[0]

		while len(remPSet):
			curSubSet = remPSet[0]
			powadd = [[cur] + curSubSet] + powAdd
			remPSet = remPSet[1:]

		powset = powset + powadd
		rem = rem[1:]

	return powset
```