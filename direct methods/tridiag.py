import numpy as np

A = np.array([[4,1,0,0],[1,4,1,0],[0,1,4,1],[0,0,1,4]])
n = len(A)
L = np.eye(n)
U = np.zeros((n,n))

for i in range(n):
    #setting U
    for j in range(i,n):
        s = sum(L[i][k]*U[k][j] for k in range(j))
        U[i][j] = (A[i][j] - s)/L[i][i]
    
    #setting L
    for j in range(i,n):
        if (j != i):
            s = sum(U[i][k]*L[k][j] for k in range(j))
            L[j][i] = (A[i][j] - s)/U[i][i]

print("L = \n", L, "\nU = \n", U)
