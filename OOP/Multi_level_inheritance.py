class Vehicle:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __repr__(self)->str:
        return f'{self.name}{self.price}'
class bus(Vehicle):
    def __init__(self, name, price,seat):
        self.seat=seat
        super().__init__(name, price)
    def __repr__(self)->str:
         return f'{self.name}{self.price}{self.seat}'
class truck(Vehicle):
    def __init__(self, name, price,licence_number):
        self.licence_number=licence_number
        super().__init__(name, price)
class ACbus(bus):
    def __init__(self, name, price, seat,temp):
        self.temp=temp
        super().__init__(name, price, seat)
    def __repr__(self)->str:
        return f'matite akash er choya :{self.name}\nppp: {self.price}\ntotal seats : {self.seat}\ntemperature : {self.temp}'

sakura=ACbus('Sakura Paribahan',750,40,16)
print(sakura)