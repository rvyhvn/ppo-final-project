from dijkstra import Dijkstra
from pso_1_var import PsoOneVar
from pso_2_var import PsoTwoVar

import random
import numpy as np
import math

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
x_1_var = [0, 1, 2]
v_1_var = [0, 0, 0]
r_1_var = [0.5, 0.5]
c_1_var = [0.5, 1]
w_1_var = 1

# Membuat objek  PsoOneVar dan menjalankan iterasi
pso_1_var =  PsoOneVar(x_1_var, v_1_var, r_1_var, c_1_var, w_1_var)
pso_1_var.iter(3)  # 3 iterasi

# PSO NOMOR 1
# b.
array_x0 = [random.randint(1, 50) for i in range(10)]
v = [0, 0, 0]
c = [0.5, 1]
r = [0.5, 0.5]
w = 1

for i in range(len(array_x0)):
    x0 = array_x0[i]
    x = [x0, 1, 2]
    pso = PsoOneVar(x, v, c, r, w)
    pso.iter(3)
