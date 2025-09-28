sLine = input()

matrix = list(map(int, sLine.split()))

sB = input()

B = list(map(int, sB.split()))


# [0, 1, 2      [a, b, c
#  3, 4, 5       d, e, f
#  6, 7, 8]      g, h, i]

def determ():
    a,b,c,d,e,f,g,h,i = matrix
    detM = a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
    if (detM == 0):
        return False
    else:
        return True
    

def row_swop(Ra, Rb):
    temp = []
    for i in range(Ra-1, 3*Ra):
        temp.append(matrix[i])
        matrix[i] = matrix[i + 3*(Rb-1)]
        matrix[i + 3*(Rb-1)] = temp[i]
    #solution vector swop for consistency
    tempB = B[Ra-1]
    B[Ra-1] = B[Rb-1]
    B[Rb-1] = tempB
    

def check_pivot():
    if (matrix[0] == 0):
        if (abs(matrix[3]) > abs(matrix[6])):
            row_swop(1,2)
        else:
            row_swop(1,3)
    if (matrix[4] == 0):
        row_swop(2,3)
    
def gauss():
    #get it into form

    for i in range(2): #pivot element
        for j in range(i+1,3): #rows below pivot
            m = matrix[i + j*3]/matrix[i+i*3]
            for col in range(0+i,3):                
                matrix[j*3+col] = matrix[j*3+col] - m*matrix[i*3+col]
            B[j] -= m * B[i] #update B

    print(matrix)
    #finding solution
    sol = [0]*3
    for n in range(2, -1, -1):
        #perform summation
        s = 0
        for c in range(n+1,3):
            s += matrix[n*3+c]*sol[c]
        sol[n] = (B[n]-s)/matrix[n*3+n] 
    
    print(sol)


if determ():
    print("matrix has a unique solution")
    check_pivot()
    gauss()
else:
    print("matrix does not have a unique solution")
