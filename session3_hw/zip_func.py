def zipper(*num):
    result = []
    finale = []
    length = len(num[0])
    for i in num:
        if len(i) < length:
            length = len(i)
    for i in range(length):
        for n in num:
            result.append(n[i])
        finale.append(tuple(result))
        result = []
    return tuple(finale)


a = (1, 3, 4)
b = (5, 6, 7, 'r')
c = ('w', '4', '5')
print(zipper(a, b, c))
