k = []
r = []
c = []
sum  = 0

test_cases = int(input())


for i in range(test_cases):
    sum = 0
    duplicateRow = 0
    duplicateColumn = 0
    matrix_size = int(input())
    matrix = []
    matrixC = []
    for j in range(matrix_size):
        row = list(map(int, input().split(maxsplit=matrix_size)))
        matrix.append(row)
    for i in range(matrix_size):
        sum += matrix[i][i]
    k.append(sum)
    #check duplicate element in a row
    for i in range(matrix_size):
        for j in range(matrix_size):
            if matrix[i].count(matrix[i][j]) > 1:
                hasDuplicate = True
                break
            else:
                hasDuplicate = False
        if hasDuplicate:
            duplicateRow += 1
    r.append(duplicateRow)
    #check duplicate element in a column
    a = 0
    for i in range(matrix_size):
        column = []
        for j in range(matrix_size):
            column.append(matrix[j][a])
        a += 1
        matrixC.append(column)
    for i in range(matrix_size):
        for j in range(matrix_size):
            if matrixC[i].count(matrixC[i][j]) > 1:
                hasDuplicate = True
                break
            else:
                hasDuplicate = False
        if hasDuplicate:
            duplicateColumn += 1
    c.append(duplicateColumn)

for i in range(test_cases):
    print('Case #{0}: {1} {2} {3}'.format(i+1, k[i], r[i], c[i]))
        
