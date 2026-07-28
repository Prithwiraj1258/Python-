class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):#add_to_cart na thakle protibar alada kore object er item gulo declare korte hoto
        product = {
            'item': item,
            'price': price,
            'quantity': quantity
        }
        self.cart.append(product)

    def checkout(self, amount):
        total = 0

        for item in self.cart:
            print(item)
            total += item['price'] * item['quantity']

        print("Total price:", total)

        if amount < total:
            print(f"Please provide {total - amount} more")
        else:
            extra = amount - total
            print(f"Here is your extra money {extra}")


swapan = Shopping('Alan Swapon')

swapan.add_to_cart('alu', 50, 6)
swapan.add_to_cart('dim', 10, 16)
swapan.add_to_cart('rice', 50, 6)

print(swapan.cart)

swapan.checkout(600)