c = {}
l = [1,2,3,4,1,1,2]

for i in l:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
print('Максимальное значение элемента: {}, количество повторений элемента: {}'.format(*max(c.items(), key=lambda x: x[1])))
