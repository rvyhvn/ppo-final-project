import math

def f(x, y):
    return (math.pow(x, 4) - 16 * math.pow(x, 2) + 5 * x + math.pow(y, 4) - 16 * math.pow(y, 2) + 5 * y) / 2

class PsoTwoVar:
    def __init__(self, x_vals, y_vals, v_vals, c_vals, r_vals, w_val):
        self.x = x_vals
        self.y = y_vals
        self.vx = v_vals
        self.vy = v_vals
        self.c = c_vals
        self.r = r_vals
        self.w = w_val
        self.old_x = self.x.copy()
        self.old_y = self.y.copy()
        self.p_best_x = self.x.copy()
        self.p_best_y = self.y.copy()
        self.g_best_x = 0.0
        self.g_best_y = 0.0

    def find_p_best(self):
        for i in range(len(self.x)):
            if f(self.x[i], self.y[i]) < f(self.p_best_x[i], self.p_best_y[i]):
                self.p_best_x[i] = self.x[i]
                self.p_best_y[i] = self.y[i]
            else:
                self.p_best_x[i] = self.old_x[i]
                self.p_best_y[i] = self.old_y[i]

    def find_g_best(self):
        min_val = f(self.x[0], self.y[0])
        min_index = 0
        for i in range(1, len(self.x)):
            fx = f(self.x[i], self.y[i])
            if fx < min_val:
                min_val = fx
                min_index = i
        self.g_best_x = self.x[min_index]
        self.g_best_y = self.y[min_index]

    def update_v(self):
        for i in range(len(self.x)):
            self.vx[i] = (self.w * self.vx[i]) + (self.c[0] * self.r[0] * (self.p_best_x[i] - self.x[i])) + (self.c[1] * self.r[1] * (self.g_best_x - self.x[i]))
            self.vy[i] = (self.w * self.vy[i]) + (self.c[0] * self.r[0] * (self.p_best_y[i] - self.y[i])) + (self.c[1] * self.r[1] * (self.g_best_y - self.y[i]))

    def update_x_and_y(self):
        for i in range(len(self.x)):
            self.old_x[i] = self.x[i]
            self.old_y[i] = self.y[i]
            self.x[i] += self.vx[i]
            self.y[i] += self.vy[i]

    def iter(self, n):
        print("Inisialisasi")
        print("x =", [round(val, 3) for val in self.x])
        print("y =", [round(val, 3) for val in self.y])
        print("vx =", [round(val, 3) for val in self.vx])
        print("vy =", [round(val, 3) for val in self.vy], "\n")
        for i in range(n):
            print("Iterasi ke-", i + 1)
            print("==================")
            print("x =", [round(val, 3) for val in self.x])
            print("y =", [round(val, 3) for val in self.y])
            print("vx =", [round(val, 3) for val in self.vx])
            print("vy =", [round(val, 3) for val in self.vy])
            print("f(x, y) =", [round(f(self.x[j], self.y[j]), 3) for j in range(len(self.x))])
            self.find_p_best()
            self.find_g_best()
            print("Personal Best X =", [round(val, 3) for val in self.p_best_x])
            print("Personal Best Y =", [round(val, 3) for val in self.p_best_y])
            print("Global Best X =", round(self.g_best_x, 3))
            print("Global Best Y =", round(self.g_best_y, 3), "\n")
            self.update_v()
            self.update_x_and_y()
            print("Updated x =", [round(val, 3) for val in self.x])
            print("Updated y =", [round(val, 3) for val in self.y])
            print("Updated vx =", [round(val, 3) for val in self.vx])
            print("Updated vy =", [round(val, 3) for val in self.vy], "\n")
