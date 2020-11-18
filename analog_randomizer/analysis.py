import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats.distributions import chi2


# мат. ожидание
def expected_value(g):
    return sum(g) / len(g)


# дисперсия
def variance(g):
    amount = 0
    n = len(g)
    mx = expected_value(g)
    for x in g:
        amount += (x - mx) ** 2
    return amount / (n - 1)


# доверительный интервал
def confidence_interval(g):
    k = 1.96 * (variance(g) / len(g)) ** 0.5
    mx = expected_value(g)
    return round(mx - k, 5), round(mx + k, 5)


# ковариация
def covariance(g, j):
    mx = expected_value(g)
    n = len(g)
    amount = 0
    for i in range(1, n - j):
        amount += (g[i] - mx) * (g[i + j] - mx)
    return amount / (n - j)


# корреляция
def correlation_plot(g, a, b):
    dx = variance(g)
    res = []
    interval = [x for x in range(a, b)]
    for i in interval:
        res.append(covariance(g, i) / dx)

    plt.title('График корелляции')
    plt.xlabel('i')
    plt.ylabel('ρ(i)')
    plt.scatter(interval, res, c="red")
    plt.grid()
    plt.show()


# рассеивание
def scatter_plot(g):
    plt.title('Диаграмма рассеивания')
    plt.xlabel('x(i)')
    plt.ylabel('x(i+1)')
    x_points = g[:len(g) - 1]
    y_points = g[1:]
    plt.scatter(x_points, y_points, c="red")
    plt.grid()
    plt.show()


def frequency_list(g, intervals):
    h = [0] * (len(intervals) - 1)
    for xi in g:
        for i in range(len(intervals) - 1):
            if intervals[i] <= round(xi, 5) < intervals[i + 1]:
                h[i] += 1
                break
            elif round(xi, 5) == intervals[-1]:
                h[-1] += 1
                break
    return h


# получение P(a<x<b) из P(X<=x)
def get_interval_p(all_p):
    p = []
    for i in range(1, len(all_p)):
        p.append(all_p[i] - all_p[i - 1])
    return p


# получение оси с отмеченными точками интервалов (от a до b k интервалов)
def get_interval_list(a, b, k):
    dx = (b - a) / k
    intervals = []
    i = a
    while i < b:
        intervals.append(round(i, 5))
        i += dx
    intervals.append(b)
    return intervals


# получение относительной частоты из абсолютной
def make_frequency_relative(h, n, dx):
    h_ = []
    for hi in h:
        h_.append(hi / n / dx)
    return h_


# построение гистограммы
def plot_histogram(g):
    n = len(g)
    k = int(round(1.72 * n ** (1 / 3), 0))
    a = min(g)
    b = max(g)
    dx = (b - a) / k
    intervals = get_interval_list(a, b, k)
    h = frequency_list(g, intervals)
    plt.title("Относительная частота")
    plt.xlabel("x")
    plt.ylabel("~h")
    plt.bar(intervals[1:], make_frequency_relative(h, n, dx), -dx, align='edge')
    plt.xticks([round(xi, 1) for xi in intervals])
    plt.grid()
    plt.show()
    return intervals, h


# метод Пирсона
def pirson(g, intervals, h):
    n = len(g)
    k = int(round(1.72 * n ** (1 / 3), 0))
    mu = expected_value(g)
    sigma = variance(g) ** (1/2)
    all_p = norm.cdf(intervals, mu, sigma)
    p = get_interval_p(all_p)
    xhi2_list = []
    for i in range(k):
        xhi2_list.append((h[i] - n * p[i]) ** 2 / n / p[i])
    return sum(xhi2_list), chi2.ppf(0.95, df=k-3), all_p, p
