from abc import ABC,abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("i can walk and run")
class snake(Animal):
    def move(self):
        print("just move")

H=Human()
H.move()
s=snake()
s.move()

