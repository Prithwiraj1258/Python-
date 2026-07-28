class Shop:
    shopping_mall = 'Jamuna'#class attribue(same for all object)

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] #instance attribute(private for all)

    def add_to_cart(self, item):#self=mehjabin,item=shoe
        self.cart.append(item)

mehjaben = Shop('Mezjabeen')
mehjaben.add_to_cart('shoe')
mehjaben.add_to_cart('bag')
print(mehjaben.cart)

nisho = Shop('nishi night er nisho')
nisho.add_to_cart('hat')
nisho.add_to_cart('watch')
print(nisho.cart)