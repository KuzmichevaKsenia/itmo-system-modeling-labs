from math import log2, sin, cos, pi


def generator(n, xsi=1650755800):
    a = 630360016
    m = 2147483647
    res = []
    for i in range(n):
        res.append(xsi / m)
        xsi = (a * xsi) % m
    return res


def func_method(f, a, b, m, n):
    g = generator(n * 6)
    x = []
    i = 0
    while len(x) < n:
        mu1 = a + g[i] * (b - a)
        mu2 = m * g[i + 1]
        if mu2 <= f(mu1):
            x.append(mu1)
        i += 2
    return x


def box_muller_method_2_2(n):
    n = int(n / 2)
    mu = 2
    sigma = 2 ** 0.5
    g1 = generator(n, 284255903)
    g2 = generator(n, 186734714)
    x = []
    for i in range(n):
        x.append(mu + sigma * (-2 * log2(g1[i])) ** 0.5 * sin(2 * pi * g2[i]))
        x.append(mu + sigma * (-2 * log2(g1[i])) ** 0.5 * cos(2 * pi * g2[i]))
    return x
