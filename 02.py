import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np


# [1] Частина надана безпосредньо у ДЗ


# Визначення функції та межі інтегрування
def f(x):
    return x**2


a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, "r", linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
plt.grid()
plt.show()

# [/1]


# Обчислення значення інтеграла функції за допомогою методу Монте-Карло
def mc_integration(points):
    # Знаходження максимального значення функції на інтервалі
    x_range = np.linspace(a, b, 1000)
    max_y = max(f(x_range))

    # Генерація випадкових точок
    random_x = np.random.uniform(a, b, points)
    random_y = np.random.uniform(0, max_y, points)

    # Обчислення кількості точок, які потрапили під криву
    points_under_curve = sum(random_y <= f(random_x))

    # Обчислення площі прямокутної області та інтегралу методом Монте-Карло
    total_area = (b - a) * max_y
    integral_by_mc = total_area * (points_under_curve / points)

    return integral_by_mc


def main():
    # [2] Обчислення інтеграла за допомогою quad() надано у ДЗ
    result, error = spi.quad(f, a, b)
    print("Інтеграл за допомогою quad(): ", result, error)
    # [/2]

    # Обчислення інтеграла за допомогою методу Монте-Карло
    points_test_array = [10, 100, 1000, 10000, 100000]

    print("Інтеграл за допомогою методу Монте-Карло: ")
    for points in points_test_array:
        result_mc = mc_integration(points)
        print(
            f"Кількість точок: {points}\t Інтеграл: {result_mc}\t Похибка: {abs(result - result_mc):.4f}"
        )


if __name__ == "__main__":
    main()
