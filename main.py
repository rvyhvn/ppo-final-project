from dijkstra import Dijkstra
from pso_1_var import PsoX
from pso_2_var import PsoXy

import numpy as np

graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'D': 7},
    'C': {'D': 1},
    'D': {}
}

dijkstra = Dijkstra(graph)
dijkstra.route('A', 'D')
print(dijkstra.distance)  # Shortest distances from 'A' to all nodes
print(dijkstra.path)      # Shortest path from 'A' to 'D'
# print(dijkstra.display_result())
print()

x_1_var = np.array([0, 1, 2])
v_1_var = np.array([0, 0, 0])
r_1_var = [1/2, 1/2]
c_1_var = [1/2, 1]
w_1_var = 1

# Membuat objek PSO dan menjalankan iterasi
pso_1_var = PsoX(x_1_var, v_1_var, r_1_var, c_1_var, w_1_var)
pso_1_var.iter(3)  # 3 iterasi
