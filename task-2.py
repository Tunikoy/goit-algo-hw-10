import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Функція для обчислення інтегралу
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Точний інтеграл за допомогою SciPy
exact_integral, error = spi.quad(f, a, b)
print(f'Точне значення інтегралу: {exact_integral}, похибка: {error}')

# Інтеграл методом Монте-Карло
N = 10000
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)
points_under_curve = np.sum(y_random < f(x_random))
monte_carlo_area = (b - a) * f(b)
monte_carlo_integral = monte_carlo_area * (points_under_curve / N)
print(f'Інтеграл методом Монте-Карло: {monte_carlo_integral}')

# Висновки
with open('readme.md', 'w') as f:
    f.write(f'Точний інтеграл: {exact_integral}\n')
    f.write(f'Інтеграл методом Монте-Карло: {monte_carlo_integral}\n')
    f.write(f'Порівняння показує, що інтеграл методом Монте-Карло має невелику похибку.\n')
