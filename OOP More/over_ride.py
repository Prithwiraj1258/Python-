class Person:
    def __init__(self,name,age,height,weight)->None:
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        

    def eat(self):
        print('vat mangso polau korma')
    def exerxise():
        raise NotImplementedError
class Cricketer(Person):
    def __init__(self, name, age, height, weight,team)->None:
        self.team=team
        super().__init__(name, age, height, weight)
    #override
    def eat(self):
        print('vegetables')
    def exercise(self):
      
      print('gym e poisa diya hudai gham jhorai')
    # + sign operator overload
    def __add__(self, other):
        return self.age+other.age
     # * sign operator overload
    def __mul__(self, other):
        return self.weight * other.weight
    #len overload
    def __len__(self):
       return self.height
    # > operator overload
    def __gt__(self, other):
        return self.age >other.age


sakib = Cricketer('sakib',38,68,91,'80')
mushi= Cricketer('mushi',36,65,78,'80')
sakib.eat()#vegetables
sakib.exercise()
#plus sign overload
print(45+63)
print('Sakib'+'Rakib')
print(sakib+mushi)
print(sakib * mushi)
print(len(sakib))
print(sakib>mushi)