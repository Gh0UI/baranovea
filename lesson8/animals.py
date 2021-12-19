class Animal:
    def __init__(self, gender, height, weight):
        self.gender = gender
        self.height = height
        self.weight = weight

    def info(self):
        print(f'okay. i`m animal :)')

class mammals(Animal):
    def __init__(self, gender, height, weight, wool ): 
        super().__init__(gender, height, weight)
        self.wool=wool

    def milk(self):
        print(f'yeaaa. i have a milk ^^')

class human(mammals):
    def __init__(self, gender, height, weight, wool, age, name ): 
        super().__init__(gender, height, weight, wool)
        self.age=age
        self.name=name
    def say(self):
        print(f'I can speak')

class cat(mammals):
    def __init__(self, gender, height, weight, wool, name ): 
        super().__init__(gender, height, weight, wool)
        self.name=name

    def say(self):
        print(f'meow')

class dog(mammals):
    def __init__(self, gender, height, weight, wool, name ): 
        super().__init__(gender, height, weight, wool)
        self.name=name
        
    def say(self):
        print(f'wow')


Biba=human("male",180, 60, None, 20, "Biba")
print(Biba.name)
print(Biba.gender)
print(Biba.height)
print(Biba.weight)
Biba.info()
Biba.milk()
Biba.say()

Barsik=cat("cat",50, 2, 'white',"Barsik")
print(Barsik.name)
print(Barsik.gender)
print(Barsik.height)
print(Barsik.weight)
Barsik.info()
Barsik.milk()
Barsik.say()

muhtar=dog("kobel",90, 20, 'black',"muhtar")
print(muhtar.name)
print(muhtar.gender)
print(muhtar.height)
print(muhtar.weight)
muhtar.info()
muhtar.milk()
muhtar.say()