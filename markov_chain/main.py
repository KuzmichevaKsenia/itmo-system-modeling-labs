from numpy.linalg import linalg

from markov_chain.functions import get_states, generator
from terminaltables import AsciiTable
import matplotlib.pyplot as plt

g = [[0.2, 0.6, 0.2, 0],
     [0.4, 0.4, 0, 0.2],
     [0.2, 0, 0.5, 0.3],
     [0.1, 0, 0.5, 0.4]]

n = 1000

values = generator(n)

tableData = [['γ'] + values]
states_list = [st for st in range(len(g))]
for i in states_list:
    states = get_states(g, i, values)
    tableData.append(['st. (from st. ' + str(i) + ')'] + states)
    plt.title("Вероятность пребывания в состояниях (начальное состояние=" + str(i) + ")")
    plt.xlabel("state")
    plt.ylabel("p")
    plt.bar(states_list, [states.count(st)/n for st in states_list], 1)
    plt.xticks(states_list)
    plt.grid()
    plt.show()
resultTable = AsciiTable(tableData)
resultTable.inner_heading_row_border = True
resultTable.outer_border = False
resultTable.inner_row_border = False
print(resultTable.table)

print('Стационарное состояние:')
print(linalg.matrix_power(g, 100)[0])
