class Dog():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

    def bark(self):
        print("GIVE ME BUTTER FATHER")


class Cat():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

    def meow(self):
        print("Mewo")


myDog = Dog()

myDog.name = "Dog with butter"
myDog.weight = 40
myDog.age = 12
myDog.bark()

myCat = Cat()

myCat.name = "Cat"
myCat.weight = 1234
myCat.age = 21
myCat.meow()
