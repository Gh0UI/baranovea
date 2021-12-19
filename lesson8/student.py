class Human:
    def __init__(self, gender, name, age, height, weight): #конструктор
        self.gender = gender
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
       



class student(Human):
    def __init__(self, gender, name, age, height, weight, clas, countt): #конструктор
        super().__init__(gender, name, age, height, weight)
        self.countt = countt
        self.clas = clas

    def count(self):
        print(f'у меня сдано {self.countt} работ')
    
vasja=student('м','вася пупкин',15,178,70,'8а', 15)
print(vasja.name)
print(vasja.gender)
print(vasja.age)
print(vasja.height)
print(vasja.weight)
print(vasja.clas)
vasja.count()