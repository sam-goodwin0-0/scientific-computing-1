import numpy as np 

A = np.array([[1,-1,3],[3,-3,1],[1,1,0]])
b = np.array([[2],[-1],[3]])

n = len(A)

for i in range(n-1,0,-1):
    if A[i][i] == 0: #check pivot
            A[[i,i-1],:] = A[[i-1,i],:]
            b[[i,i-1]] = b[[i-1,i]]
    for j in range(i-1,-1,-1):
        m = A[j,i]/A[i,i]
        A[j,:] = A[j,:] - A[i,:]*m
        b[j] = b[j] - b[i]*m


print(f"A' = \n{A}\nb'=\n{b}")

#solving
x = np.zeros((n,1))

for i in range(n):
    s = sum(A[i,k]*x[k] for k in range(n))
    x[i]= (b[i] - s)/A[i,i]

print("x = \n", x)
