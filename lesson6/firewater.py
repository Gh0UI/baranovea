with open('input.txt', 'r') as f:
    text=f.read()

try:  
    test=text.replace(" ", "")
    test=int(test)

except ValueError:
    print('ошибка ввода')
    exit()



text=str(text)
list=(text.split(' '))

for elem in list:
    print(elem)

c=int(list[0])//2   
h=int(list[1])//6
o=int(list[2])//1

min=min(c,h,o)
out=(f"минимальное количество молекул равно {min}")

with open('output.txt', 'w') as fp:
    fp.write(out)