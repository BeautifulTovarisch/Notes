"""
Matrix

This module implements common matrix utilities including matrix-vector product
and transpose

NOTE: These implementation prioritize clarity and education over efficiency.
"""

import scale, dot, add from vector

# Using the linear combination representation
def mvMult(M, v):
	'''
	mvMult(M, v) computes the matrix-vector multiplication [M] * [v]

	Parameters:
		M (list[]): An R x C matrix
		v (list): A C-vector in the same field as [M]

	Output:
		An R-vector whose entries are the result of M * v
	'''
	# TODO: since this requires transpose

def mvMultDot(M, v):
	'''
	mvMultDot(M, v) computes the matrix-vector multiplication [M] * [v]

	Parameters:
		M (list[]): An R x C matrix
		v (list): A C-vector in the same field as [M]

	Output:
		An R-vector whose entries are the result of M * v
	'''
	return [dot(M[r], v) for r in range(len(M))]
