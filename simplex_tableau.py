#the below code produces a simplex tableau given initial data:
# systems of equations A = b
# constraints c

import numpy as np

#c = np.array([36,30,-3,-4],float)
#A = np.array([[1,1,-1,0], [6,5,0,-1]], float)
#b = np.array([5,10], float)

def makeTableau(c, A, b):
    numRows = np.size(A, 0)  #num of rows in A
    tableau = np.zeros((numRows, np.size(A,1)))
    tableau = A
    slack = np.eye(np.size(A,0))
    tableau = np.concatenate((tableau, slack), axis = 1) #joining the rows
    b = np.vstack(b) # making b a vertical matrix
    tableau = np.concatenate((tableau, b), axis = 1) #joining rows
    c = -c
    c = np.concatenate((c, np.zeros(np.size(A,0)+1)))
    c = np.array([c])
    tableau = np.concatenate((c, tableau), axis = 0)
    
    basis = np.array([i for i in range(np.size(A,1),np.size(tableau, 1)-1)])

    return tableau, basis

def getPivotColumn(tableau):
    min = tableau[0][0]
    min_pos = 0
    neg = False
    if (tableau[0][0] < 0):
        neg = True
    for i in range(np.size(tableau[0][0:-1])):
        if (tableau[0][i] < min):
            min = tableau[0][i]
            min_pos = i
        if (tableau[0][i] < 0):
            neg = True
    if not neg:
        return -1
    return min_pos

def getPivotRow(tableau, pivotCol):
    min = 1000000
    min_pos = 0
    none = True
    for i in range(1, np.size(tableau, 0)):
        el = tableau[i][pivotCol]
        if (el > 0):
            if (tableau[i][-1]/el < min):
                min = tableau[i][-1]/el
                min_pos = i-1
            none = False
    
    if (none):
        return -1
    
    return min_pos

def getPivotElement(tableau):
    pivotCol = getPivotColumn(tableau)
    pivotRow = getPivotRow(tableau, pivotCol)
    if (pivotCol == -1):
        return -1
    if (pivotRow == -1):
        return 0
    pos = np.array([pivotRow, pivotCol])
    return pos

def updateBasis(basis, pivotElement):
    newBasis = np.copy(basis)
    newBasis[pivotElement[0]] = pivotElement[1]

    return newBasis

def updateTableauRow(pivotRow, tableauRow, pivotCol):
    newRow = np.copy(tableauRow)
    multiplier = tableauRow[pivotCol]
    newRow = newRow - pivotRow*multiplier

    return newRow

def updateTableau(tableau, basis, pivotElement):
    newTableau = np.copy(tableau)
    pivotRow = pivotElement[0] +1
    pivotCol = pivotElement[1]
    newTableau[pivotRow, :] = newTableau[pivotRow, :]/newTableau[pivotRow, pivotCol]
    for i in range(np.size(newTableau,0)):
        if (i != pivotRow):
            newTableau[i] = updateTableauRow(newTableau[pivotRow, :], newTableau[i], pivotCol)
    newBasis = updateBasis(basis, pivotElement)

    return newTableau, newBasis

def readSolution(A, tableau, basis):
    x = np.zeros(np.size(A, 1))
    i = 1
    for el in basis:
        if (el < np.size(A, 1)):
            x[el] = tableau[i][-1]
        i += 1
        
    y = tableau[0][0:-1]
    #z = sum(x * y)
    z = tableau[0][-1]
    return x, z

def readMultipleSols(A, tableau, basis):
    x = np.zeros(np.size(A, 1))
    i = 1
    for el in basis:
        if (el < np.size(A, 1)):
            x[el] = tableau[i][-1]
        i += 1
        
    y = tableau[0][0:-1]
    return x

def pivotElMultipleSolutions(tableau, basis):
    tableau[0, basis] = 1
    pivotCol = np.argmin(tableau[0, :-1])
    if tableau[0, pivotCol] > 0:
        pivotElement = -1
    else:
        pivotRow = getPivotRow(tableau, pivotCol)
        if pivotRow == -1:
            pivotElement = -1
        else:
            pivotElement = np.array([pivotRow, pivotCol])
    
    return pivotElement

def simplexMethod(c, A, b):
    tableau, basis = makeTableau(c, A, b)
    
    while (np.any(tableau[0,:] < 0)):
        if type(getPivotElement(tableau)) is int:
            if getPivotElement(tableau) == 0:
                return 0
        pivotElement = getPivotElement(tableau)
        tableau, basis = updateTableau(tableau, basis, pivotElement)
    if type(pivotElMultipleSolutions(tableau, basis)) is not int:
            solution1 = readMultipleSols(A, tableau, basis)
            pivotElement = pivotElMultipleSolutions(tableau, basis)
            tableau, basis = updateTableau(tableau, basis, pivotElement)
            solution2 = readMultipleSols(A, tableau, basis)
            return solution1, solution2, tableau[0][-1]

    return readSolution(A, tableau, basis)


#print(simplexMethod(c, A, b))
