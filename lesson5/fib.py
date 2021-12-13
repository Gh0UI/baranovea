def fibonacci(n):
    """рекурсивная функция, возвращает число Фибоначчи"""
    cur = 1
    if n > 2:
        cur = fibonacci(n-1) + fibonacci(n-2)
    return cur

while True:
        try:
            num = int(input("Введите число\n"))
            break                    
        except ValueError:
            print("Вы ввели не число. Повторите ввод")

res=fibonacci(num)
print(f'{num} элемент последовательности равен {res}')