import numpy as np
#positive definite and symmetric

A = np.array([[4,12,-16],[12,37,-43],[-16,-43,98]])

n = len(A)

L = np.eye(n)

#cholesky factorisation
def cholesky():
    for i in range(n):
        for j in range(i,n):
            if (i == j):
                s = sum(L[j][k]*L[j][k] for k in range(j))
                L[i][j] = (A[i][j]-s)**(1/2)
            else:
                s = sum(L[j][k]*L[i][k] for k in range(j))
                L[j][i] = (A[i][j]-s)/L[i][i]

Lt = L.T

cholesky()
print("L = \n", L, "\n LT = \n", Lt)
