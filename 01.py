from pulp import LpProblem, LpMaximize, LpVariable


def main():
    # Створюємо модель оптимізації
    model = LpProblem(name="Production_Optimization", sense=LpMaximize)

    # Оголошуємо змінні рішення
    x1 = LpVariable(name="лимонад", lowBound=0, cat="Integer")
    x2 = LpVariable(name="фруктовий сік", lowBound=0, cat="Integer")

    # Цільова функція для максимізації загального виробництва
    model += x1 + x2, "Total_Production"

    # Додаємо обмеження ресурсів згідно з ДЗ, формат: вираз цільової функції, назва цільової функції
    # Вода (2 од. на лимонад + 1 од. на сік) та маємо її 100 од.
    # Цукор (1 од. на лимонад), 50 од.
    # Лимонний сік (1 од. на лимонад), 30 од.
    # Фруктове пюре (2 од. на сік), 40 од.

    model += 2 * x1 + x2 <= 100, "Вода"
    model += x1 <= 50, "Цукор"
    model += x1 <= 30, "Лимонний сік"
    model += 2 * x2 <= 40, "Фруктове пюре"

    # Розв'язуємо задачу
    model.solve()

    # Результати
    print("\nРезультати:")
    print(f"Оптимальна кількість лимонаду:\t\t{int(x1.value())} од.")
    print(f"Оптимальна кількість фруктового соку:\t{int(x2.value())} од.")
    print(f"Загальна кількість продуктів:\t\t{int(model.objective.value())} од.")

    # Використання ресурсів
    print("\nВикористання ресурсів:")
    print(f"Вода:\t\t{2 * int(x1.value()) + int(x2.value())}/100 од.")
    print(f"Цукор:\t\t{int(x1.value())}/50 од.")
    print(f"Лимонний сік:\t{int(x1.value())}/30 од.")
    print(f"Фруктове пюре:\t{2 * int(x2.value())}/40 од.")


if __name__ == "__main__":
    main()
