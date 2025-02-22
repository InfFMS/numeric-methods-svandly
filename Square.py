import numpy as np
import math
import matplotlib.pyplot as plt
pi = math.pi

f = np.linspace(0, pi, 1000)
y = np.sin(2*f) + 1
y1 = -0.2 * f**2 + 0.5

plt.plot(f, y)
plt.plot(f, y1)
# plt.plot(f, y2)
# plt.plot(f, y3)

plt.title("Зависимость Y от X")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

current_number = 0
next_number = 0.01
sum_plosh = 0

while current_number < pi:
    ploshad = (((np.sin(2 * current_number) + 1) - (-0.2 * current_number**2 + 0.5)) + ((np.sin(2 * next_number) + 1) - (-0.2 * next_number**2 + 0.5)))*0.01
    current_number += 0.01
    next_number = 0.01 + current_number
    sum_plosh = sum_plosh + ploshad
print(sum_plosh)



num = np.linspace(-(pi/2), (pi/2), 1000)
y2 = np.cos(num) + 1.2
y3 = -0.5 * num**2 + 0.7

plt.plot(num, y2)
plt.plot(num, y3)
# plt.plot(f, y2)
# plt.plot(f, y3)

plt.title("Зависимость Y от X")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

current_number = -(pi/2)
next_number = -(pi/2) + 0.01
sum_plosh2 = 0

while current_number < pi:
    ploshad2 = ((np.cos(current_number) + 1.2) - (-0.5 * current_number**2 + 0.7)) + ((np.cos(next_number) + 1.2) - (-0.5 * next_number**2 + 0.7))*0.01
    current_number += 0.01
    next_number = 0.01 + current_number
    sum_plosh2 = sum_plosh2 + ploshad2
print(sum_plosh2)


num1 = np.linspace(-2, 2, 1000)
y4 = np.exp(-(num1**2)) + 1
y5 = -0.3 * num1**3 + 0.5

plt.plot(num1, y4)
plt.plot(num1, y5)
# plt.plot(f, y2)
# plt.plot(f, y3)

plt.title("Зависимость Y от X")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

current_number = -2
next_number = -2 + 0.01
sum_plosh3 = 0

while current_number < pi:
    ploshad3 = (abs(np.exp(-(current_number**2)) + 1) - (-0.3 * current_number**3 + 0.5)) + abs((np.exp(-(next_number**2)) + 1) - (-0.3 * next_number**3 + 0.5))*0.01
    current_number += 0.01
    next_number = 0.01 + current_number
    sum_plosh3 = sum_plosh3 + ploshad3
print(sum_plosh3)

# это наверное можно красиво написать через функцию, что бы не переписывать 1000 раз, но я решила в тупую сделать((