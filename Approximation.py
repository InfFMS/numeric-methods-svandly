import numpy as np
import math

f = np.linspace(-4,4,1000)
nol = np.random.randint(0, 1, size=(1000))

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 6))

# x_1 = np.linspace(1,366,365)
x1 = f
def def1(x):
    return x**3 - x + 1

def def2(x):
    return x**3 - x**2 - 9*x + 9

def def3(x):
    return x**2 - np.exp(x)

def def4(x):
    return 5*x - 6 * np.log10(x) - 7

def def5(x):
    return np.cos(x) + 2*x - 3


y = x1**3 - x1 + 1
y2 = x1**3 - x1**2 - 9*x1 + 9
y3 = x1**2 - np.exp(x1)
y4 = 5*x1 - 6 * np.log10(x1) - 7
y5 = np.cos(x1) + 2*x1 - 3

plt.plot(x1, y)
plt.plot(x1, nol)
plt.plot(x1, y2)
plt.plot(x1, y3)
plt.plot(x1, y4)
plt.plot(x1, y5)
plt.title("Зависимость Y от X")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

def solve_ddd(f, a, b, eps = 0.01):
    while (b-a)/2 >= eps:
        c = (a + b)/2
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    return c

root = [solve_ddd(def1, -2, 2), solve_ddd(def2, -4, -2), solve_ddd(def2, 0, 2), solve_ddd(def2, 2, 4),
        solve_ddd(def3, -2, 0), solve_ddd(def4, 0, 1), solve_ddd(def4, 1, 3), solve_ddd(def5, 0, 3)]
print(root)

for i in root:
    d = i//0.01 / 100
    print(d)
