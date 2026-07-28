#base class,parent class,common attribute+functionality class
# derived class,child class,uncommon attribute+dunctionality class
class Device :
    def __init__(self,brand,price,color,origin)->None:
         self.brand=brand
         self.price=price
         self.color=color
         self.origin=origin
    def run(self):
        return f'phone tipa tipi kore'
    
class Laptop:
    def __init__(self,memory,ssd)->None:
        self.memory=memory
        self.ssd =ssd
    def run(self):
        return f'Running laptop :{self.brand}'
    
    
class Phone():
    def __init__(self,dual_sim)->None:
        self.dual_sim=dual_sim
    def run(self):
        return f'phone tipa tipi kore'
    def phone_call(self,number,text):
        return f'sending SMS to: {number}with : {text}'
    def __repr__(self)->str:
        return f'phone : {self.dual_sim}'
class Camera :
    def __init__(self,pixel)->None:
        self.pixel=pixel
   
   #inheritance
my_phone=Phone(True)
print(my_phone)
