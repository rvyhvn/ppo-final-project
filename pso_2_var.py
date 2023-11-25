import math

def f(x, y):
    return (math.pow(x, 4) - 16 * math.pow(x, 2) + 5 * x + math.pow(y, 4) - 16 * math.pow(y, 2) + 5 * y) / 2

class PsoTwoVar:
    def __init__(self, x_vals, y_vals, v_vals, c_vals, r_vals, w_val):
        self.x = x_vals
        self.y = y_vals
        self.v = v_vals
        self.c = c_vals
        self.r = r_vals
        self.w = w_val
        self.oldX = self.x.copy()
        self.oldY = self.y.copy()
        self.pBest = self.x.copy()
        self.pBestY = self.y.copy()
        self.gBest = 0.0

    def findPBest(self):
        for i in range(len(self.x)):
            if f(self.x[i], self.y[i]) < f(self.pBest[i], self.pBestY[i]):
                self.pBest[i] = self.x[i]
                self.pBestY[i] = self.y[i]
            else:
                self.pBest[i] = self.oldX[i]
                self.pBestY[i] = self.oldY[i]

    def findGBest(self):
        minVal = f(self.x[0], self.y[0])
        minIndex = 0
        for i in range(1, len(self.x)):
            fx = f(self.x[i], self.y[i])
            if fx < minVal:
                minVal = fx
                minIndex = i
        self.gBest = self.x[minIndex]
        self.gBestY = self.y[minIndex]

    def updateV(self):
        for i in range(len(self.x)):
            self.v[i] = (self.w * self.v[i]) + (self.c[0] * self.r[0] * (self.pBest[i] - self.x[i])) + (self.c[1] * self.r[1] * (self.gBest - self.x[i])) + (self.c[2] * self.r[2] * (self.gBestY - self.y[i]))

    def updateX(self):
        for i in range(len(self.x)):
            self.oldX[i] = self.x[i]
            self.oldY[i] = self.y[i]
            self.x[i] += self.v[i]
            self.y[i] += self.v[i]

    def iter(self, n):
        print("Inisialisasi")
        print("x =", self.x)
        print("y =", self.y)
        print("v =", self.v, "\n")
        for i in range(n):
            print("Iterasi ke-", i + 1)
            print("x =", self.x)
            print("y =", self.y)
            print("v =", self.v)
            print("f(x, y) =", [f(self.x[j], self.y[j]) for j in range(len(self.x))])
            self.findPBest()
            self.findGBest()
            print("pBest =", self.pBest)
            print("pBestY =", self.pBestY)
            print("gBest =", self.gBest)
            print("gBestY =", self.gBestY, "\n")
            self.updateV()
            self.updateX()
            print("Updated x =", self.x)
            print("Updated y =", self.y)
            print("Updated v =", self.v, "\n")
