def fibonacci(n):
    if n <= 0:
        return "Число повинно бути більше 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b


n = int(input("Введіть номер числа Фібоначчі, яке хочете отримати: "))
print(f"{n}-е число Фібоначчі: {fibonacci(n)}")
