class Algorithms:
# 1) Пошук мінімального елементу масиву позитивних чисел
    def min_positive(arr):
        if not arr:
            raise ValueError("Масив порожній")

        mn = arr[0]
        if mn <= 0:
            raise ValueError("Усі числа мають бути > 0")

        for x in arr:
            if x <= 0:
                raise ValueError("Усі числа мають бути > 0")
            if x < mn:
                mn = x
        return mn

# 2) Розрахунок суми елементів масиву, який може складатися лише з від’ємних чисел
    def sum_negative_only(arr):
        if not arr:
            raise ValueError("Масив порожній")

        s = 0
        for x in arr:
            if x >= 0:
                raise ValueError("Усі числа мають бути < 0")
            s += x
        return s

# 3) Алгоритм розрахунку N-го елементу послідовності Фібоначчі
    def fibonacci_n(n):
        if n < 0:
            raise ValueError("n має бути >= 0")
        if n == 0:
            return 0
        if n == 1:
            return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# 4) Алгоритм розрахунку сили струму на ділянці кола
    def current(U, R):
        if R == 0:
            raise ValueError("Опір R не може бути 0")
        return U / R