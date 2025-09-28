iString = input()

A = list(map(int,iString.split()))

#computing L

L = [0] * 9
L[0] = 1
L[4] = 1
L[8] = 1
L[3] = A[3]/A[0]
L[6] = A[6]/A[0]
#L[1],[2] and [5] should remain 0

#computing U

U = [0] * 9

U[0] = A[0]
U[1] = A[1]
U[2] = A[2]
#U[3], [6], [7] should all remain 0
U[4] = A[4] - L[3]*U[1]
U[5] = A[5] - L[3]*U[2]

L[7] = (A[7]-L[6]*U[1])/U[4]
U[8] = A[8] - L[6]*A[2] - L[7]*U[5]

print("L: ")
print(L)
print("U: ")
print(U)

iString1 = input()

b = list(map(int,iString1.split()))

#solving for y

y = [0] * 3

y[0] = b[0]
y[1] = b[1] - y[0]*L[3]
y[2] = b[2] - y[1]*L[7] - y[0]*L[6]

#solving for x

x = [0] * 3

x[2] = y[2]/U[8]
x[1] = (y[1] - x[2]*U[5])/U[4]
x[0] = (y[0] - x[2]*U[2] - x[1]*U[1])/U[0]


print("y: ")
print(y)
print("x: ")
print(x)