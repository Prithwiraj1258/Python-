class Gadjet:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = origin

    def run(self):
        return f'Running laptop: {self.brand}'
    
    def coding(self):
        return f'learning python and practicing'
class laptop:
    def __init__(self,memory,ssd):
        self.memory=memory
        self.ssd=ssd
        
class Phone(Gadjet):#inherit hocche
    def __init__(self, brand,price,origin,color,dual_sim) -> None:

        self.dual_sim = dual_sim
        super(). __init__(brand,price,color,origin)
    
    def run(self):
        return f'phone tipa tipi kore'
    
    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with: {text}'
    def __repr__(self):
        return f'phone:{self.brand}{self.price}{self.dual_sim}'
class Camera:
    def __init__(self, brand, price, color, pixel) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.pixel = pixel

# 
my_phone=Phone('Iphone',120000,'silver','china',True)
print(my_phone.brand)
print(my_phone)