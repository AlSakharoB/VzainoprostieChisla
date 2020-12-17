def out(mass):
    retstr = ''
    for i in range(len(mass) - 1):
        retstr += str(mass[i]) + ','
    return retstr + str(mass[len(mass) - 1])


def split(str2, mass):
    str2 += ' '
    strdop = ''
    for i in str2:
        if i != ' ':
            strdop += i
        if i == ' ':
            mass.append(int(strdop))
            strdop = ''
    return mass


def output(main, maxdel, f):
    delstr = str(maxdel)
    length = 36 + len(delstr)
    if len(main) == 2:
        print('\t', 'Максимальный общий делитель "МОД" -', maxdel)
        print("\033[34m{}".format('Ответ программы: '))
        if f == False:
            length = 22
            print("\033[31m {}".format('=' * length))
            print("\033[31m {}".format('Числа невзаимнопростые'))
        if f == True:
            length = 20
            print("\033[32m {}".format('=' * length))
            print("\033[32m {}".format('Числа взаимнопростые'))
    else:
        print("\033[34m{}".format('Ответ программы: '))
        print("\033[34m {}".format('=' * length))
        print(' Максимальный общий делитель "МОД" -', maxdel)
    return(" {}" .format('=' * length))


def gen(a, index):
    b = [[] for i in range(len(a))]
    for i in a:
        for j in range(2, i + 1):
            if i % j == 0:
                b[index].append(j)
        index += 1
    return b


def asort(a, delmin):
    for i in range(2, a + 1):
        if a % i == 0:
            delmin.append(i)
    return delmin
