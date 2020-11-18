from math import exp


# генерирует список из n чисел от 0 до 1
def generator(n, xsi=1148216685):
    a = 630360016
    m = 2147483647
    res = []
    for i in range(n):
        res.append(xsi / m)
        xsi = (a * xsi) % m
    return res


# сопоставляет каждому x интервал вероятности
def make_table(x, p):
    res = {}
    cnt = 0
    for i in range(len(x)):
        right = round(cnt + p[i], 4)
        res.update({x[i]: [cnt, right]})
        cnt = right
    return res


# получает набор xi по попаданиям сгенерированных чисел в интервалы вероятности
def make_discrete(xp, gen):
    res = []
    for g in gen:
        for x, p in xp.items():
            if p[0] <= g <= p[1]:
                res.append(x)
                break
    return res


# методом обратной функции получает набор дискретных величин
def inverse_transform_sampling(x, p, n=1000):
    xp = make_table(x, p)
    gen_list = generator(n)
    return make_discrete(xp, gen_list)


# получает набор дискретных величин методом Пуассона
def puasson_method(lmbd, n=1000):
    a = exp(-lmbd)
    x = []
    xsi = 1148216685
    for i in range(n):
        g = generator(lmbd * 4, xsi+i)
        j = 1
        b = g[j]
        while b > a:
            if j == len(g):
                print("unknown error")
                return
            j += 1
            b *= g[j]
        x.append(j-1)
    return x
