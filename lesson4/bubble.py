from random import randint
 
count = 15
list = []
for i in range(count):
    list.append(randint(1, 100))
print(list)
 
for i in range(count-1):
    for j in range(count-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
 
print(list)