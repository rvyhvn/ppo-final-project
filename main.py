from dijkstra import Dijkstra
from pso_1_var import PsoOneVar
from pso_2_var import PsoTwoVar

import random

# DJIKSTRA NOMOR 1
graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'D': 7},
    'C': {'D': 1},
    'D': {}
}

# dijkstra = Dijkstra(graph)
# dijkstra.route('A', 'D')
# print(dijkstra.distance)  # Shortest distances from 'A' to all nodes
# print(dijkstra.path)      # Shortest path from 'A' to 'D'
# print(dijkstra.display_result())

# PSO NOMOR 1
# a.

print("""
      PSO NOMOR 1 a.
""")
x_1_var = [0, 1, 2]
v_1_var = [0, 0, 0]
r_1_var = [0.5, 0.5]
c_1_var = [0.5, 1]
w_1_var = 1

pso_1_var = PsoOneVar(x_1_var, v_1_var, r_1_var, c_1_var, w_1_var)
pso_1_var.iter(3)
pso_1_var.plot_iteration(3)
# PSO NOMOR 1
# b.
print("""
      PSO NOMOR 1 b.
""")

array_x0 = [random.randint(-5, 5) for i in range(10)]
# array_x1 = [random.randint(-5, 5) for i in range(10)]
# array_x2 = [random.randint(-5, 5) for i in range(10)]
c = [0.5, 1]
w = 1

for i in range(len(array_x0)):
    x0 = array_x0[i]
    # x1 = array_x1[i]
    # x2 = array_x2[i]
    v = [0, 0, 0]
    # , "x1 =", x1, "x2 =", x2)
    print("Perulangan ke-", i + 1, "dengan nilai x0 =", x0)
    r1 = random.random()
    r2 = random.random()
    r = [r1, r2]
    x = [x0, 1, 2]
    pso = PsoOneVar(x, v, c, r, w)
    pso.iter(3)
    pso.plot_iteration(3)

# PSO NOMOR 2
# a.

print("""
      PSO NOMOR 2 a.
""")
x_2_var = [0, 1, 2]
y_2_var = [0, 1, -1]
v_2_var = [0, 0, 0]
c_2_var = [1, 0.5]
r_2_var = [1, 1]
w_2_var = 1

pso_2_var = PsoTwoVar(x_2_var, y_2_var, v_2_var, c_2_var, r_2_var, w_2_var)
pso_2_var.iter(3)

# PSO NOMOR 2
# b.

print("""
      PSO NOMOR 2 b.
""")
array_x0_2_var = [random.randint(-10, 10) for i in range(10)]
array_y0_2_var = [random.randint(-10, 10) for i in range(10)]

c = [1, 0.5]
w = 1

for i in range(len(x_1_var)):
    x0 = array_x0_2_var[i]
    y0 = array_y0_2_var[i]
    v = [0, 0, 0]
    r1 = random.random()
    r2 = random.random()
    r = [r1, r2]
    x = [x0, 1, 2]
    y = [y0, 1, -1]
    pso_2_var_x_y = PsoTwoVar(x, y, v, c, r, w)
    pso_2_var_x_y.iter(3)
