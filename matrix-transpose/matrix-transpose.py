import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    pass
    a = np.asarray(A)
    rows, cols = a.shape
    transpose = np.zeros((cols, rows), dtype=a.dtype)

    for i in range(rows):
        for j in range(cols):
            transpose[j, i] = a[i,j]

    return transpose