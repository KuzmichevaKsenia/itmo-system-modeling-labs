from discrete_randomizer.generator import *
from discrete_randomizer.analysis import *
from math import exp, factorial


def print_theor_x_p_mx_dx(x, p):
    print("x: " + str(x))
    print("p: " + str(p))
    print("Мат. ожидание: " + str(theor_expected_value(x, p)))
    print("Дисперсия: " + str(theor_variance(x, p)))


def show_report(discrete_gen_list):
    print("Полученные дискретные величины: " + str(discrete_gen_list))

    mx = expected_value(discrete_gen_list)
    print("Оценка мат. ожидания: " + str(mx))

    dx = variance(discrete_gen_list)
    print("Оценка дисперсии: " + str(dx))

    scatter_plot(discrete_gen_list)

    correlation_plot(discrete_gen_list, 1, 20)

    frequency_plot(discrete_gen_list)

    a, b = confidence_interval(discrete_gen_list)
    print("Доверительный интервал мат. ожидания: (" + str(a) + ", " + str(b) + ")")
    print("\n" + "-"*20 + "\n")
    return


# part 1
x_list_1 = [5, 8, 13, 16, 21, 24, 29]
p_list_1 = [0.1, 0.02, 0.25, 0.15, 0.35, 0.03, 0.1]
print_theor_x_p_mx_dx(x_list_1, p_list_1)
show_report(inverse_transform_sampling(x_list_1, p_list_1))

# part 2 - puasson
lmbd = 8

k = 20
x_list_2 = [xi for xi in range(k)]
p_list_2 = [(lmbd**i)*exp(-lmbd)/factorial(i) for i in range(k)]
print("lambda: " + str(lmbd))
show_report(inverse_transform_sampling(x_list_2, p_list_2))

print("lambda: " + str(lmbd))
show_report(puasson_method(lmbd))
