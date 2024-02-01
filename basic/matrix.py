import numpy as np
from scipy import sparse

matrix_np = np.eye(4)

print(matrix_np)

sci_arr = sparse.csr_matrix(matrix_np)

print(sci_arr)