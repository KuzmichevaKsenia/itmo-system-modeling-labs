from analog_randomizer.generator import func_method, box_muller_method_2_2
from analog_randomizer.analysis import expected_value, variance, scatter_plot, correlation_plot, \
    confidence_interval, plot_histogram, pirson
from terminaltables import AsciiTable

n = 1000


def analyze(g):
    #print(g)
    mx = expected_value(g)
    print("Оценка мат. ожидания: " + str(mx))

    dx = variance(g)
    print("Оценка дисперсии: " + str(dx))

    lm, rm = confidence_interval(g)
    print("Доверительный интервал мат. ожидания: (" + str(lm) + ", " + str(rm) + ")")

    correlation_plot(g, 1, 20)

    scatter_plot(g)

    resintervals, resh = plot_histogram(g)

    return g, resintervals, resh


def f(x):
    if 0 <= x < 2:
        return 0.3 * x
    if x == 2:
        return 0.4
    if 2 < x <= 4:
        return 0.2


a = 0
b = 4
m = 0.6
# мат ожидание 2
# дисперсия 1,47
print('Непрерывная случайная величину с заданной плотностью распределения вероятности')
analyze(func_method(f, a, b, m, n))
print()
print()

print('Метод Бокса-Мюллера: нормально распределенная случайная величина X ~ N(2, 2)')
g, intervals, h = analyze(box_muller_method_2_2(n))
xhi2, xhi2_theor, all_p, p = pirson(g, intervals, h)
print('x2 расчитанный: ' + str(xhi2))
print('x2 теоретический: ' + str(xhi2_theor))
tableData = [['P(X<=x)', 'P(a<x<b)', 'h'],
             [round(all_p[0], 4), '', '']]
for i in range(len(p)):
    tableData.append([round(all_p[i+1], 4), round(p[i], 4), h[i]])
resultTable = AsciiTable(tableData)
resultTable.inner_heading_row_border = True
resultTable.outer_border = False
resultTable.inner_row_border = False
print(resultTable.table)
