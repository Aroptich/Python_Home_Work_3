# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def reversed_fibonacci(n):
    if n in (1, 2):
        return 1
    return reversed_fibonacci(n + 2) - reversed_fibonacci(n + 1)


def negafibonacci() -> list:
    a = []
    b = []
    try:
        n = int(input("Введите число для последовательности Фибоначчи:"))
        if type(n) in [int]:
            for i in range(-n, n + 1):
                if i > 0:
                    a.append((fibonacci(i)))
                else:
                    b.append(reversed_fibonacci(i))
            return f'- для k={n} список будет выглядеть так: {b + a}'
    except ValueError as e:
        print(e)
        return negafibonacci()


print(negafibonacci())
