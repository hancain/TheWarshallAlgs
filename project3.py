# An import statement for copying so the original is not changed
import copy

# Warshall takes a matrix and returns the ajacency matrix to the input
def Warshall(matrix):
    # Copies the input in to an independent variable tempList (original
    # will not be modified)
    tempList = copy.deepcopy(matrix)

    # examines verts k, i, j and makes according relation calculations to
    # determine ajacency
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            for aja in range(len(matrix)):

                # if an ajacency is found, set [i][j] to 1
                if tempList[row][aja] == 1 or (tempList[row][col] == 1 and tempList[col][aja] == 1):
                    tempList[row][aja] = 1
    #returns the updated matrix
    return tempList

# Floyd Warshall takes a weighted matrix as an input and returns the "lightest"
# path when determining the ajacency paths
def Floyd_Warshall(matrix):
    # Copties input to independ vaiable so original is not modified in
    # calculation
    tempList = copy.deepcopy(matrix)
    # sets everything in tempList to "inf" for calculations to be done later
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if tempList[row][col] == 0:
                tempList[row][col]= float('inf')

# examines verts k, i, j and makes according calculations to find the lightest
# path between transitive verticies
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if tempList[i][k]+tempList[k][j] < tempList[i][j]:
                        tempList[i][j] = tempList[i][k]+tempList[k][j]
    #returns the updated matrix
    return tempList


print(Warshall([[1,1,0],[0,0,1],[0,1,0]]))
print(Warshall([[0,1,0,0],[0,0,0,1],[0,0,0,0],[1,0,1,0]]))
print(Warshall([[0,0,1,0],[1,0,0,1],[0,0,0,0],[0,1,0,0]]))
print(Floyd_Warshall([[0,7,0,5],[0,2,0,0],[0,3,0,4],[1,0,0,0]]))
print(Floyd_Warshall([[0,0,3,0], [2,0,0,0], [0,7,0,1], [6,0,0,0]]))
print(Floyd_Warshall([[0,-1,-2,0],[4,0,2,4],[5,1,0,2],[3,-1,1,0]]))
