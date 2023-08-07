The dot product is the **scalar** result of adding the component-wise products of two vectors:

>[!info] Definition Dot Product:
>Given $n$-vectors $u, v$,
>$$
>u \cdot v = \sum_{k \in D} u[k] \times v[k]
>$$

>[!example]- Example $[1, 1, 1] \cdot [10, 20, 30]$
>$$
>= 10 + 20 + 30 = 60
>$$

Dot products are a central idea in [[Linear Equations]].

> [!example] Total Cost and Benefit
> Suppose $D$ is a set of foods:
> $$
> D = \{hops, malt, water, yeast\}
> $$
> We are given the following vectors:
> - $cost = \{hops : 2.50/oz, malt : 1.50/lb, water: 0.006/gallon, yeast: 0.45/g\}$
> - $quantity = \{hops: 6oz, malt: 14lbs, water: \text{7 gallons}, yeast: 11g\}$
> - $value = \{hops: 0, malt: 960, water: 0, yeast: 3.25\}$
> 
> We can compute *total cost*:
> $$
> cost \cdot quantity = 2.50 * 6 + 1.50 * 14 + 0.006 * 7 + 0.45 * 11 = 40.992
> $$
> and caloric content per pound:
> $$
> value \cdot quantity = 0 * 6 + 960 * 14 + 7 * 0 + 3.25 * 11 
> = 13475.75
> $$

## Miscellaneous Applications

- Measuring Similarity
	- Audio Samples
	- Voting Records
	- Plagiarism Detection
- Parity (number of ones is odd) of an integer
- Challenge-Response Authentication
	- Attacking weak security by solving a system of equations
 
## Algebraic Properties

> [!info] Commutativity
> $$
> u \cdot v = v \cdot u
> $$
> > [!abstract] Proof.
> > $$
> > \begin {align}
> > u \cdot v &= \sum_{k \in D} u[k] \times v[k] \\
> > &= \sum_{k \in D} v[k] * u[k] \\
> > &= v \cdot u
> > \end{align}
> > $$
> > $\blacksquare$
>  

>[!info] Homogeneity
>$$
>(\alpha u) \cdot v = \alpha (u \cdot v)
>$$
>>[!abstract] Proof.
>>$$
>>\begin{align}
>>(\alpha u) \cdot v &= \alpha [u_1, u_2, \dots, u_n] \cdot v \\
>>&= [\alpha u_1, \alpha u_2, \dots, \alpha u_n] \cdot v \\
>>&= \sum_{k \in D} \alpha u[k] \times v[k] \\
>>&= \alpha \sum_{k \in D} u[k] \times v[k] \\
>>&= \alpha (u \cdot v) \\
>>\end{align}
>>$$
>>$\blacksquare$

>[!info] Distributivity
>$$
>(u + v) \cdot w = u \cdot w + v \cdot w
>$$
>> [!abstract] Proof.
>> $$
>> \begin {align}
>> (u + v) \cdot w &= \sum_{k \in D} (u + v)[k] \times w[k] \\
>> &= \sum_{k \in D} (u[k] + v[k]) \times w[k] \\
>> &= \sum_{k \in D} (u[k] * w[k]) + (v[k] \times w[k]) \\
>> &= \sum_{k \in D} (u[k] * w[k]) + \sum_{k \in D}(v[k] \times w[k]) \\
>> &= (u \cdot w) + (v \cdot w)
>> \end{align}
>> $$
>> $\blacksquare$

