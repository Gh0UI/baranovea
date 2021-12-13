import foo

while True:
        try:
            a = int(input("Число: "))
            b = int(input("Степень числа: "))   
            break               
        except ValueError:
            print("Вы ввели не число. Повторите ввод")

print(f'Число в степени: {foo.pow(a, b)}')