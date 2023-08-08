"""
Matrix

This module implements common matrix utilities including matrix-vector product
and transpose

NOTE: These implementation prioritize clarity and education over efficiency.
"""

from vector import scale, dot, add, zero_vec

def transpose(M):
  '''
  transpose(M) computes the transpose of M.

  Parameters:
    M (list[]): An R x C matrix

  Output:
    A C x R matrix with columns equal to [M]'s rows and vice versa

  Example:
    M = [
      [1, 3, 7],
      [2, 9, 4]
    ]

    transpose(M)
    => [
      [1, 2],
      [3, 9],
      [7, 4]
    ]
  '''
  R = len(M)
  C = len(M[0])

  return [[M[i][j] for i in range(R)] for j in range(C)]

def mvMultDot(M, v):
	'''
	mvMultDot(M, v) computes the matrix-vector multiplication [M] * [v]

	Parameters:
		M (list[]): An R x C matrix
		v (list): A C-vector in the same field as [M]

	Output:
		An R-vector whose entries are the result of M * v

  Example:
    M = [[1, 2, 3], [10, 20, 30]]
    v = [7, 0, 4]

    mvMultDot(M, V)
    => [19, 190]
	'''
	return [dot(M[r], v) for r in range(len(M))]

def mv(f):
    '''
    mv(f) produces a function that performs matrix-vector multiplication
    using [f] to provide the appropriate vector addition for a particular field.

    Parameters:
        f (list * list -> list): a function that performs vector addition for the
        desired field.

    Output:
        A function (list[] * list) -> list that performs matrix-vector multiplication

    Example:
        # R
        mv(add)

        # GF(2)
        mv(gfadd)
    '''
    def mvMult(M, v):
        '''
        mvMult(M, v) computes the product [M] * [v]

        Parameters:
            M (list[]) an R x C matrix in GF(2)
            v (list) a C vector in GF(2)

        Output:
            An R-vector obtained by matrix-vector multiplication of [M] and [v]
        '''
        # Need to operate on the columns of M
        T = transpose(M)
        out = zero_vec(len(M))

        # Produce linear combination of row[i] of T and v[i]
        for i in range(len(T)):
            out = f(out, scale(v[i], T[i]))

        return out

    return mvMult

def mm(dotfn):
  '''
  mm(dotfn) produces a function that performs matrix-matrix multiplication
  using [dotfn] to provide the appropriate dot product for a particular field.

  Parameters:
    dotfn ('a list * 'a list -> 'a): a function that computes the dot product
    of two vectors in a desired field.

  Output:
    A function ('a list list * 'a list list) -> 'a list list that performs
    matrix-matrix multiplication

  Example:
    # R
    mm(vdot)

    # GF(2)
    mm(gfdot)
  '''
  def matMultiply(A, B):
    '''
    matMultiply(A, B) peforms matrix-matrix multiplication of [A] * [B].

    Paramters:
      A (list[]) an R x S matrix
      B (list[]) an S x T matrix

    Output:
      An R x T matrix obtained by the product [A][B]

    Example:
      A = [
        [1, 2],
        [-1, 1]
      ]

      B = [
        [4, 2, 0],
        [3, 1, -1]
      ]

      matMultiply(A, B)
      => [
        [10, 4, -2],
        [-1, -1, -1]
      ]
    '''
    bT = transpose(B)

    R = len(A)
    T = len(bT)

    out = [[0 for _ in range(T)] for _ in range(R)]

    for r in range(R):
      for t in range(T):
        out[r][t] = dotfn(A[r], bT[t])

    return out

  return matMultiply
