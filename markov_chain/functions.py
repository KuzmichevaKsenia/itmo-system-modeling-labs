import matplotlib.pyplot as plt


def generator(n):
    a = 630360016
    m = 2147483647
    xsi = 1650755800
    res = []
    for i in range(n):
        res.append(round(xsi / m, 3))
        xsi = (a * xsi) % m
    return res


def get_state(row, value):
    amount = 0
    for i in range(len(row)):
        if value > amount + row[i]:
            amount += row[i]
        else:
            return i


def get_states(g, start_state, values):
    cur_state = start_state
    states = []
    for value in values:
        cur_state = get_state(g[cur_state], value)
        states.append(cur_state)
    plt.title("Диаграмма изменения состояния системы (начальное состояние=" + str(start_state) + ")")
    plt.grid()
    t = [i for i in range(len(values) + 1)]
    plt.step(t, [start_state] + states, where='post')
    t = []
    plt.xticks(t)
    plt.yticks(range(len(g)))
    plt.show()
    return states
