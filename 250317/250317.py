a = [1,2,[3,4]]
b = []

for i in range(len(a)):
    if isinstance(a[i], list):
        list = []
        for k in range(len(a[i])):
            list.append(a[i][k])
        b.append(list)
    else:
        b.append(a[i])

b[2][0] = 99
