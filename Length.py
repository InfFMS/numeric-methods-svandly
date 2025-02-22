import numpy as np
import math
import matplotlib.pyplot as plt
pi = math.pi
# print(pi)

f = np.linspace(0, pi, 1000)
y = np.cos(f)
y1 = np.cos(f) + 0.1*f**2
y2 = -np.tanh(f-(pi/2))

y3 = -0.2*(f - pi)**3 + 0.5*(f - pi)**2 + 1
plt.plot(f, y)
plt.plot(f, y1)
plt.plot(f, y2)
plt.plot(f, y3)

plt.title("Зависимость Y от X")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

ggg = 0
hhh = 0.01
saratov = 0
saratov2 = 0
saratov3 = 0
saratov52 = 0

jjj = 0
while jjj < pi:
    dlina1 = (((jjj + 0.01) - jjj)**2 + (np.cos(jjj) - np.cos(jjj + 0.01))**2) ** 0.5
    dlina2 = (((jjj + 0.01) - jjj)**2 + abs(((np.cos(jjj) + 0.1*(jjj**2)) - (np.cos(jjj+0.01) + 0.1*(jjj+0.01)**2)))**2) ** 0.5
    dlina3 = (((jjj + 0.01) - jjj)**2 + (-0.2*(jjj - pi)**3 + 0.5*(jjj - pi)**2 + 1 - (-0.2*((jjj+0.01) - pi)**3 + 0.5*((jjj+0.01) - pi)**2 + 1))**2)**0.5
    dlina52 = (((jjj + 0.01) - jjj)**2 + (-np.tanh(jjj-(pi/2)) - -np.tanh((jjj+0.01)-(pi/2)))**2)**0.5
    saratov = saratov + dlina1
    saratov2 = saratov2 + dlina2
    saratov3 = saratov3 + dlina3
    saratov52 = saratov52 + dlina52
    jjj += 0.01

# for i in f:
#     dlina1 = (((i+1)- i) + (np.cos(i)- np.cos(i+1)))**0.5
#     dlina2 = (((i + 1) - i) + ((np.cos(i) + 0.1*i**2) - (np.cos(i+1) + 0.1*(i + 1)**2))) ** 0.5
#     saratov = saratov + dlina1
#     saratov2 = saratov2 + dlina2
print(saratov, saratov2, saratov3, saratov52)