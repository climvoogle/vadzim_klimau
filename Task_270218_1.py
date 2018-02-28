matrix = [[1,2,3],[4,5,6],[7,8,9]]

mysum = 0
counter = 0

for i in matrix:
    for j in i:
        mysum += j
        counter += 1

aver = mysum/counter

print('Cреднее арифметическое значение элементов матрицы: ', round(aver))



