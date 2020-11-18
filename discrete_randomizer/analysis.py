import matplotlib.pyplot as plt


# теоретическое мат. ожидание
def theor_expected_value(x, p):
    amount = 0
    for i in range(len(x)):
        amount += x[i] * p[i]
    return amount


# теоретическая дисперсия
def theor_variance(x, p):
    sqrx = []
    for xi in x:
        sqrx.append(xi**2)
    return theor_expected_value(sqrx, p) - theor_expected_value(x, p)**2


# оценка мат. ожидания
def expected_value(g):
    return sum(g) / len(g)


# оценка дисперсии
def variance(g):
    amount = 0
    n = len(g)
    mx = expected_value(g)
    for x in g:
        amount += (x - mx)**2
    return amount / (n - 1)


# строит диаграмму рассеивания
def scatter_plot(g):
    plt.title('Диаграмма рассеивания')
    plt.xlabel('x(i)')
    plt.ylabel('x(i+1)')
    x_points = g[:len(g) - 1]
    y_points = g[1:]
    plt.scatter(x_points, y_points, c="red")
    plt.grid()
    plt.show()


# расчитывает ковариацию
def covariance(g, j):
    mx = expected_value(g)
    n = len(g)
    amount = 0
    for i in range(1, n-j):
        amount += (g[i] - mx) * (g[i+j] - mx)
    return amount/(n-j)


# строит график/диаграмму корелляции
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


# строит гистограмму относительной частоты появления x
def frequency_plot(g):
    freq = {}
    for x in g:
        if freq.get(x) is None:
            freq[x] = 1
        else:
            freq.update({x: freq.get(x) + 1})
    width = 1
    n = len(g)
    for key, value in freq.items():
        freq.update({key: value / n})
    plt.title("Относительная частота")
    plt.xlabel("x")
    plt.ylabel("~h")
    plt.bar(freq.keys(), freq.values(), width)
    plt.xticks(list(freq.keys()))
    plt.show()


# расчитывает доверительный интервал мат. ожидания
def confidence_interval(g):
    k = 1.96 * (variance(g) / len(g)) ** 0.5
    mx = expected_value(g)
    return round(mx - k, 5), round(mx + k, 5)
