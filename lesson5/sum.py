list1=[]
num=1
print("Введите число:\n0-выход\n")
while num!=0:
        try:
            num = int(input())
            if num == 0: break
            list1.append(num)
        except ValueError:
            print("Вы ввели не число. Повторите ввод")


def sum(list1):
    """сумма чисел с бесконечным количеством операндов"""
    i = 0
    sum = 0
    while i < len(list1):       
        sum += list1[i]
        i += 1
    print('Cумма числел равна:', sum)

sum((list1))
