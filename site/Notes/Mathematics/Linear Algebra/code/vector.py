"""
Vector

This module implements common vector utilities such as scalar multiplication
and dot product. A vector is assumed to use an iterable and indexable structure.

NOTE: These implementation prioritize clarity and education over efficiency.
"""

def zero_vec(n):
  '''
  zero_vec return an [n]-vector with all entries zero.

  Paramters:
    n (int): The dimension of the vector

  Output:
    A list of size [n] with all entries zero.

  Example:
    zero_vec(3)
    => [0, 0, 0]
  '''
  return [0 for _ in range(n)]

def add(u, v):
	'''
	vadd(u, v) computes the vector obtaining by adding [u] + [v]

	Parameters:
		u,v (list): Lists representing vectors of some space.

	Output:
		The vector u + v

	Example:
		vadd([1, 2], [3, 4])
		=> [4, 6]
	'''
	return [u[k] + v[k] for k in range(len(u))]


def scale(a, v):
	'''
	scale(a, v) computes the scalar multiplication of [a] * [v]

	Parameters:
		a (int): A scalar value
		v (list): A list representing a vector

	Output:
		A vector whose elements have been scaled by [a].

	Example:
		scale(10, [1, 2, 3])
		=> [10, 20, 30]
	'''
	return [a * e for e in v]

def dot(u, v):
	'''
	dot(u, v) computes the dot product of vectors u and v.

	Parameters:
		u, v (list): Vectors under some field F.

	Output:
		Scalar value of u * v

	Example:
		dot([1, 2, 3], [4, 5, 6])
		=> 4 + 10 + 18
		=> 32
	'''
	return sum([u[k] * v[k] for k in range(len(u))])
