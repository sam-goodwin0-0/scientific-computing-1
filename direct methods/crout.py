import numpy as np

A = np.array([[3,2,-1],[2,-2,4],[-1,0.5,-1]],dtype=float)
b = np.array([1,-2,0],dtype=float)

n = len(A)

U = np.eye(n)
L = np.zeros((n,n))

#factorising to get L and U

for i in range(n):
    for j in range(i,n):
        s = sum(L[j][k]*U[k][i] for k in range(i))
        L[j][i] = A[j][i]-s

    for j in range(i+1,n):
        s = sum(L[i][k]*U[k][j] for k in range(i))
        U[i][j] = (A[i][j] - s)/L[i][i]

print("L = \n",L)
print("U = \n",U)

            #solving by forward sub for y
y = np.zeros((n,1))

for i in range(n):
    s = sum(L[i][k]*y[k] for k in range(i))
    y[i] = (b[i]-s)/L[i][i]

            #solving by backward sub for x
x = np.zeros((n,1))

for i in reversed(range(n)):
    s = sum(U[i][k]*x[k] for k in range(n))
    x[i] = (y[i]-s)/U[i][i]


print(x)
