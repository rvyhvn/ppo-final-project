import math

def f(x, y):
    return (math.pow(x, 4) - 16 * math.pow(x, 2) + 5 * x + math.pow(y, 4) - 16 * math.pow(y, 2) + 5 * y) / 2

class PsoTwoVar:
    def __init__(self, x_vals, y_vals, v_vals, c_vals, r_vals, w_val):
        self.x = x_vals
        self.y = y_vals
        self.vx = v_vals  # vx untuk x
        self.vy = v_vals  # vy untuk y
        self.c = c_vals
        self.r = r_vals
        self.w = w_val
        self.oldX = self.x.copy()
        self.oldY = self.y.copy()
        self.pBestX = self.x.copy()  # pBest untuk x
        self.pBestY = self.y.copy()  # pBest untuk y
        self.gBestX = 0.0  # gBest untuk x
        self.gBestY = 0.0  # gBest untuk y

    # Metode lainnya tetap sama

    def findPBest(self):
        for i in range(len(self.x)):
            if f(self.x[i], self.y[i]) < f(self.pBestX[i], self.pBestY[i]):
                self.pBestX[i] = self.x[i]
                self.pBestY[i] = self.y[i]
            else:
                self.pBestX[i] = self.oldX[i]
                self.pBestY[i] = self.oldY[i]

    def findGBest(self):
        minVal = f(self.x[0], self.y[0])
        minIndex = 0
        for i in range(1, len(self.x)):
            fx = f(self.x[i], self.y[i])
            if fx < minVal:
                minVal = fx
                minIndex = i
        self.gBestX = self.x[minIndex]
        self.gBestY = self.y[minIndex]

    def updateV(self):
        for i in range(len(self.x)):
            self.vx[i] = (self.w * self.vx[i]) + (self.c[0] * self.r[0] * (self.pBestX[i] - self.x[i])) + (self.c[1] * self.r[1] * (self.gBestX - self.x[i]))
            self.vy[i] = (self.w * self.vy[i]) + (self.c[0] * self.r[0] * (self.pBestY[i] - self.y[i])) + (self.c[1] * self.r[1] * (self.gBestY - self.y[i]))

    def updateXy(self):
        for i in range(len(self.x)):
            self.oldX[i] = self.x[i]
            self.oldY[i] = self.y[i]
            self.x[i] += self.vx[i]  # Update x
            self.y[i] += self.vy[i]  # Update y

    def iter(self, n):
        print("Inisialisasi")
        print("x =", self.x)
        print("y =", self.y)
        print("vx =", self.vx)
        print("vy =", self.vy, "\n")
        for i in range(n):
            print("Iterasi ke-", i + 1)
            print("==================")
            print("x =", self.x)
            print("y =", self.y)
            print("vx =", self.vx)
            print("vy =", self.vy)
            print("f(x, y) =", [f(self.x[j], self.y[j]) for j in range(len(self.x))])
            self.findPBest()
            self.findGBest()
            print("pBestX =", self.pBestX)
            print("pBestY =", self.pBestY)
            print("gBest =", self.gBestX)
            print("gBestY =", self.gBestY, "\n")
            self.updateV()
            self.updateXy()
            print("Updated x =", self.x)
            print("Updated y =", self.y)
            print("Updated vx =", self.vx)
            print("Updated vy =", self.vy, "\n")
