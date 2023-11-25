import math

def f(x):
    return (math.pow(x, 4) - 16 * math.pow(x, 2) + 5 * x) / 2

class PsoOneVar:
    def __init__(self, x_vals, v_vals, c_vals, r_vals, w_val):
        self.x = x_vals
        self.v = v_vals
        self.c = c_vals
        self.r = r_vals
        self.w = w_val
        self.oldX = self.x.copy()
        self.pBest = self.x.copy()
        self.gBest = 0.0

    def findPBest(self):
        for i in range(len(self.x)):
            if f(self.x[i]) < f(self.pBest[i]):
                self.pBest[i] = self.x[i]
            else:
                self.pBest[i] = self.oldX[i]

    def findGBest(self):
        minVal = f(self.x[0])
        minIndex = 0
        for i in range(1, len(self.x)):
            fx = f(self.x[i])
            if fx < minVal:
                minVal = fx
                minIndex = i
        self.gBest = self.x[minIndex]

    def updateV(self):
        for i in range(len(self.x)):
            self.v[i] = (self.w * self.v[i]) + (self.c[0] * self.r[0] * (self.pBest[i] - self.x[i])) + (self.c[1] * self.r[1] * (self.gBest - self.x[i]))

    def updateX(self):
        for i in range(len(self.x)):
            self.oldX[i] = self.x[i]
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
            self.findPBest()
            self.findGBest()
            print("pBest =", [round(val, 3) for val in self.pBest])
            print("gBest =", round(self.gBest, 3), "\n")
            self.updateV()
            self.updateX()
            print("Updated x =", [round(val, 3) for val in self.x])
            print("Updated v =", [round(val, 3) for val in self.v], "\n")
