import Exp as ft


a, index, index1, delmass, maxdel, n, delmin, f = [], 0, 0, [], 1, 0, [], True
x = input("\033[34m{}" .format('Вводите числа в строку через пробел: '))
a = ft.split(x, a)
b = ft.gen(a, index)
for i in a:
    print('\t', "\033[37m{} [{}]: {}{}" .format('Делители числа', i, '1,', ft.out(b[index1])))
    index1 += 1
a = sorted(a)
delmin = ft.asort(a[0], delmin)
for del2 in delmin:
    n = 0
    for i in b:
        for j in range(len(i)):
            if i[j] == del2:
                n += 1
    if n == len(b):
        f = False
        delmass.append(del2)
if len(delmass) > 0:
    maxdel = delmass[len(delmass) - 1]
print(ft.output(a, maxdel, f))


