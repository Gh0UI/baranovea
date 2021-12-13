from random import randint
"""операции над множествами, состоящих из 2 списков со случайными значениями(0-100)"""
count = 15
list1 = []
list2 = []
for i in range(count):
    
    list1.append(randint(1, 100))
    list2.append(randint(1, 100))

numbers1 = set(list1)
numbers2 = set(list2)
print(f"первое множество:\n{numbers1}\nвторое множество:\n{numbers2}"
      f"\nобщие элементы:\n{numbers1.intersection(numbers2)}\n"
      f"вход в первое, но не во второе:\n{numbers1.difference(numbers2)}\n"
      f"вход во второе, но не в перове:\n{numbers2.difference(numbers1)}"
      f"\nвходит в первое или второе, но не в оба одновременно:\n{numbers1.symmetric_difference(numbers2)}\n")