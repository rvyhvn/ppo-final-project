import math
import matplotlib.pyplot as plt


def f(x):
    return (math.pow(x, 4) - 16 * math.pow(x, 2) + 5 * x) / 2


class PsoOneVar:
    def __init__(self, x_vals, v_vals, c_vals, r_vals, w_val):
        self.x = x_vals
        self.v = v_vals
        self.c = c_vals
        self.r = r_vals
        self.w = w_val
        self.old_x = self.x.copy()
        self.p_best = self.x.copy()
        self.g_best = 0.0

    def find_p_best(self):
        for i in range(len(self.x)):
            if f(self.x[i]) < f(self.p_best[i]):
                self.p_best[i] = self.x[i]
            else:
                self.p_best[i] = self.old_x[i]

    def find_g_best(self):
        min_val = f(self.x[0])
        min_index = 0
        for i in range(1, len(self.x)):
            fx = f(self.x[i])
            if fx < min_val:
                min_val = fx
                min_index = i
        self.g_best = self.x[min_index]

    def update_v(self):
        for i in range(len(self.x)):
            self.v[i] = (self.w * self.v[i]) + (self.c[0] * self.r[0] * (self.p_best[i] -
                                                                         self.x[i])) + (self.c[1] * self.r[1] * (self.g_best - self.x[i]))

    def update_x(self):
        for i in range(len(self.x)):
            self.old_x[i] = self.x[i]
            self.x[i] += self.v[i]

    def iter(self, n):
        print("Inisialisasi")
        print("x =", [round(val, 3) for val in self.x])
        print("v =", [round(val, 3) for val in self.v], "\n")
        for i in range(n):
            print("Iterasi ke-", i + 1)
            print("==================")
            print("x =", [round(val, 3) for val in self.x])
            print("v =", [round(val, 3) for val in self.v])
            print("f(x) =", [round(f(val), 3) for val in self.x])
            self.find_p_best()
            self.find_g_best()
            print("Personal Best =", [round(val, 3) for val in self.p_best])
            print("Global Best =", round(self.g_best, 3), "\n")
            self.update_v()
            self.update_x()
            print("Updated x =", [round(val, 3) for val in self.x])
            print("Updated v =", [round(val, 3) for val in self.v], "\n")

    def plot_iteration(self, n):
        x_values = []
        v_values = []
        p_best_values = []
        g_best_values = []

        for i in range(n):
            x_values.append(self.x.copy())
            v_values.append(self.v.copy())
            p_best_values.append(self.p_best.copy())
            g_best_values.append(self.g_best)

            self.find_p_best()
            self.find_g_best()
            self.update_v()
            self.update_x()

        iterations = list(range(1, n + 1))

        fig, axs = plt.subplots(2, 2, figsize=(12, 8))
        axs[0, 0].plot(iterations, x_values)
        axs[0, 0].set_title('x per Iterasi')
        axs[0, 0].set_xlabel('Iterasi')
        axs[0, 0].set_ylabel('Nilai x')

        axs[0, 1].plot(iterations, v_values)
        axs[0, 1].set_title('v per Iterasi')
        axs[0, 1].set_xlabel('Iterasi')
        axs[0, 1].set_ylabel('Nilai v')

        axs[1, 0].plot(iterations, p_best_values)
        axs[1, 0].set_title('Personal Best per Iterasi')
        axs[1, 0].set_xlabel('Iterasi')
        axs[1, 0].set_ylabel('Nilai Personal Best')

        axs[1, 1].plot(iterations, g_best_values)
        axs[1, 1].set_title('Global Best per Iterasi')
        axs[1, 1].set_xlabel('Iterasi')
        axs[1, 1].set_ylabel('Nilai Global Best')

        plt.tight_layout()
        plt.show()
