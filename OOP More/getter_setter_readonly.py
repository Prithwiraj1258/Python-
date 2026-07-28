# read only --> you can not set the value. value can not be changed
# getter --> get a value of a property through a method. Most of the time, you will get the value of a private attribute.
# setter --> set a value of a property through a method. Most of the time, you will set the value of a private property.

class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money
    
    # getter without any setter is readonly attribute
    @property
    def age(self):
        return self._age

    # getter 
    @property
    def salary(self):
        return self.__money
    
    # setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            return 'salary can not be negative'
        self.__money += value

samsu = User('Kopa', 21, 12000)
harry=User('kane',33,20000000)
#print(samsu.__money)
print(samsu.age) 
# samsu.age=25
# print(samsu.age)#getter e eki class e multiple time kono attribute access kora jabe na
print(harry.age) 
print(harry.salary)#setter kane be accesed for multiple constructors
# harry.salary=100000
# print(harry.salary)
samsu.salary = 4500
print(samsu.salary)