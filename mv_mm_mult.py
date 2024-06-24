matrix = [[1,2,3],[1,2,3],[1,2,3]]
matrix1 = [[1,2,3],[1,2,3],[1,2,3]]
matrix2 = [[2,3,4],[2,3,4],[2,3,4]]
vector = [1,2,3]


#the lines 8-23 calculate the matrix with a vector mulitplication if it is allowed
results = []

if len(matrix) == len(vector):
    #creating empty list for the resulting vector
    results = []
    for i in range(len(matrix)):
        #variable for each row of action
        items = 0
        for j in range(len(vector)):
            #adding the result of matrix vector itemwise multiplication
            items += matrix[i][j] * vector[j]
        results.append(items)
else: 
    print("The matrix and vector aren't compatible.")
    
print(results)


#the lines 27-41 calculate the matrix with a matrix mulitplication if it is allowed
resultsmxm = []

if len(matrix1) == len(matrix2):
    for i in range(len(matrix1)):
        rows = []
        for j in range(len(matrix2)):
            items2 = 0
            for k in range(len(matrix1)):
                items2 += matrix1[i][k] * matrix2[k][j]
            rows.append(items2)
        resultsmxm.append(rows)
else:
    print("These matrices aren't compatible.")

print(resultsmxm)