

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, species):
        self.name = name
        self.species = species


    @abstractmethod
    def move(self):
        return 'Animals do migrate.'
    


class Mammal(Animal):
    def __init__(self, name, species, mammal):
        super().__init__(name, species)
        self.mammal = mammal

    def move(self):
        return 'Mammal can travel.'
    


class Dog(Mammal):


    def bark(self):
        return 'Dog can bark'

    
class Cat(Mammal):
    
    def bark(self):
        return 'cat can do meow'
    

my_dog = Dog('khalid','Husky','mammal')
print(my_dog.move())
print(my_dog.bark())


# my_cat = Cat('Bhola','catwoman','mammal')
# print(my_cat.move())
# print(my_cat.bark())
    


class Bird(Animal):
    def __init__(self, name, species, bird):
        super().__init__(name, species)
        self.bird = bird

    def move(self):
        return 'Bird can fly.'
class Eagle(Bird):

    def fly(self):
        return 'Eagle can fly very high.'
    
class penguin(Bird):

    def fly(self):
        return 'penguin can not fly.'
    



my_bird = Eagle('chill','carnivorous','bird')
print(my_bird.move())
print(my_bird.fly())
    





class Fish(Animal):
    def __init__(self, name, species, fish):
        super().__init__(name, species)
        self.fish = fish

    def move(self):
        return 'fish can swim.'
    
    
class Salmon(Fish):
    def swim(self):
        return 'Salmon can swim fast.'
    

macha = Salmon('goldy','fewa tal','macha')
print(macha.move())
print(macha.swim())









