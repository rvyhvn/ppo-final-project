import numpy as np

# Fungsi yang ingin dioptimalkan
def f(x):
    return (x**4 - 16 * x**2 + 5 * x) / 2

class PsoX:
    def __init__(self, x, v, r, c, w):
        self.x = x
        self.vx = v.copy()
        self.r = r
        self.c = c
        self.w = w

        self.old_x = x.copy()
        self.x_p_best = self.x.copy()
        self.x_g_best = self.x[np.argmin([f(x) for x in self.x])]
        self.f_values = [f(x_i) for x_i in self.x]  # Menyimpan nilai f(x) untuk setiap x

    def find_p_best(self):
        for i in range(len(self.x)):
            val = f(self.x[i])
            if val < f(self.x_p_best[i]):
                self.x_p_best[i] = self.x[i]

    def find_g_best(self):
        self.x_g_best = self.x[np.argmin(self.f_values)]

    def update_v(self):
        for i in range(len(self.x)):
            r1, r2 = np.random.rand(), np.random.rand()
            self.vx[i] = self.w * self.vx[i] + self.c[0] * r1 * (self.x_p_best[i] - self.x[i]) + self.c[1] * r2 * (self.x_g_best - self.x[i])

    def update_x(self):
        for i in range(len(self.x)):
            self.x[i] += self.vx[i]
            self.f_values[i] = f(self.x[i])  # Mengupdate nilai f(x) setelah pembaruan x

    def iter(self, n):
        print("Iterasi 0")
        print(f"x = {self.x}")
        print(f"v = {self.vx}")
        # print(f"f(x) = {self.f_values}")
        print()
        for i in range(n):
            print(f"Iterasi ke: {i+1}")
            print("======================")
            self.find_p_best()
            self.find_g_best()
            self.update_v()
            self.update_x()
            print(f"x = {[round(val, 3) for val in self.x]}")
            print(f"v = {[round(val, 3) for val in self.vx]}")
            print(f"f(x) = {[round(val, 3) for val in self.f_values]}")
            print(f"x_p_best = {[round(val, 3) for val in self.x_p_best]}")
            print(f"x_g_best = {round(self.x_g_best, 3)}")
            print()
