"""input содержит количество атомов C H O
необходимых для создания молекулы спирата
выводит количество полученных молекул 
"""

with open('input.txt', 'r') as f:
    """чтение из файла"""
    text=f.read()

try:  
    """проверка ввода только чисел"""
    test=text.replace(" ", "")
    test=int(test)

except ValueError:
    print('ошибка ввода')
    exit()



text=str(text)
list=(text.split(' '))

for elem in list:
    print(elem)
"""определение количества молекул"""
c=int(list[0])//2   
h=int(list[1])//6
o=int(list[2])//1

min=min(c,h,o)
out=(f"минимальное количество молекул равно {min}")

with open('output.txt', 'w') as fp:
    fp.write(out)