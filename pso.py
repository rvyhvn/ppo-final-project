import numpy as np

def f(x, y):
    return ((2 - x) ** 2) + (200 * (y - x ** 2) ** 2)

class Pso:
    def __init__(self, x, y, v, r, c, w):
        self.x = x
        self.y = y
        self.vx = v.copy()
        self.vy = v.copy()
        self.r = r
        self.c = c
        self.w = w

        self.old_x = x.copy()
        self.old_y = y.copy()
        self.x_p_best = self.x.copy()
        self.y_p_best = self.y.copy()
        self.x_g_best = self.x[np.argmin([f(x, y) for x, y in zip(self.x, self.y)])]
        self.y_g_best = self.y[np.argmin([f(x, y) for x, y in zip(self.x, self.y)])]

    def find_p_best(self):
        for i in range(len(self.x)):
            val = f(self.x[i], self.y[i])
            if val < f(self.x_p_best[i], self.y_p_best[i]):
                self.x_p_best[i] = self.x[i]
                self.y_p_best[i] = self.y[i]

    def find_g_best(self):
        self.x_g_best = self.x[np.argmin([f(x, y) for x, y in zip(self.x, self.y)])]
        self.y_g_best = self.y[np.argmin([f(x, y) for x, y in zip(self.x, self.y)])]

    def update_v(self):
        for i in range(len(self.x)):
            r1, r2 = np.random.rand(), np.random.rand()
            self.vx[i] = self.w * self.vx[i] + self.c[0] * r1 * (self.x_p_best[i] - self.x[i]) + self.c[1] * r2 * (self.x_g_best - self.x[i])
            self.vy[i] = self.w * self.vy[i] + self.c[0] * r1 * (self.y_p_best[i] - self.y[i]) + self.c[1] * r2 * (self.y_g_best - self.y[i])

    def update_x(self):
        for i in range(len(self.x)):
            self.x[i] += self.vx[i]
            self.y[i] += self.vy[i]

    def iter(self, n):
        print(f"Iterasi 0")
        print(f"x = {self.x}")
        print(f"v = {self.v}")

        for i in range(n):
            print(f"Iterasi ke: {i+1}")
            self.find_p_best()
            self.find_g_best()
            self.update_v()
            self.update_x()
            print(f"x = {self.x}")
            print(f"v = {self.v}")
