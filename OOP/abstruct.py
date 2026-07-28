from abc  import ABC,abstractmethod
#abstruct base class
class Animal(ABC):
    @abstractmethod #enforce all derived class to have a eat method
    def eat(self):
        print('I need food')
    @abstractmethod
    def move(self):
        print('hanging')
class Monkey(Animal):
    def __init__(self,name)->None:
        self.category='Monkey'
        self.name=name
        super().__init__()
    
    def eat(self):
        print('hey nana !,I am eating banana')
    def move(self):
        print('Hanging on the branches')
layka= Monkey('lucky')
layka.eat()