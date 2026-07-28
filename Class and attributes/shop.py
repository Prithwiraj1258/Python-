class Shop:
    cart=[]# class attribute
    def __init__(self,buyer):
        self.buyer = buyer
    def add_to_cart(self,item):
        self.cart.append(item)
        
mehjaben=Shop('Mezjabeen')
mehjaben.add_to_cart('shoe')
mehjaben.add_to_cart()
print(mehjaben.cart)
nisho=Shop('nishi night er nisho')
nisho.add_to_cart('hat')
nisho.add_to_cart('watch')
print(nisho.cart)
