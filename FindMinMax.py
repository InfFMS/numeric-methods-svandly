import numpy as np
import matplotlib.pyplot as plt

n1 = int(input())
n2 = int(input())
a = int(input())
b = int(input())
f = np.linspace(a,10,1000)
y = (-a)-n1*f
nol = np.linspace(0, 0, 1000)

def def1(x):
    return b-n1*x

def solve_ddd(f, a, b, eps = 0.01):
    while (b-a)/2 >= eps:
        c = (a + b)/2
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    return c

root = [solve_ddd(def1, -10, 10)]

max = float(root[0])

print(max)
buba = np.linspace(-10,0,1000)

f2 = np.linspace(0,10,1000)
y2 = -n2*f2

plt.plot(buba, y)
plt.plot(f2, y2)
plt.plot(f, nol)

plt.title("Зависимость Y от X")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()