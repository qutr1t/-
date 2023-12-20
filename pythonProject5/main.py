import matplotlib.pyplot as plt
import numpy as np
import time

def gamma(d):
    x = 1.0000
    for _ in range(20):
        # Итерационная формула для вычисления gamma-функции
        x = x - (pow(x, d + 1) - x - 1) / ((d + 1) * pow(x, d) - 1)
    return x

d = 2  # количество осей координат
print('Введите количество точек: ')
n = int(input())  # количество точек
n = round(n + 3 - n % 3)
g = gamma(d)
z = np.zeros((n, d))  # Массив для хранения координат точек
colors = ['r', 'g', 'b']  # Цвета для разных групп точек
alpha = np.zeros((n, d))  # Массив для хранения alpha-значений

start_time = time.time()

for j in range(d):
    # Вычисление alpha-значений для каждой оси координат
    alpha[:, j] = pow(1 / g, j + 1) % 1

for k in range(3):
    counter = (n * k) // 3  # Определение начального индекса для k-той группы точек
    # Генерация координат точек по формуле
    z[counter:counter + n // 3] = (0.5 + alpha[counter:counter + n // 3] * np.arange(1, n // 3 + 1)[:, None] + alpha[counter:counter + n // 3] ** (k + 1)) % 1

plt.scatter(z[:, 0], z[:, 1], color=np.tile(colors, n // 3), marker='*')  # Нанесение точек на график

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")  # Вывод времени выполнения программы

plt.show()  # Отображение графика
