class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance #ekhane getter method apply kora hoyeche

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'Fokira! You cannot withdraw below {self.min_withdraw}.')
        elif amount > self.max_withdraw:
            print(f'Bank fokir hoye jabe! Maximum withdraw {self.max_withdraw}.')
        else:
            self.balance -= amount
            print(f'Here is your money: {amount}')


brac = Bank(15000)

brac.withdraw(25)
brac.withdraw(50000000)
brac.withdraw(1000)

print(brac.get_balance())#ekhane getter method final self.balance return kore (15000-1000)

dbbl = Bank(500)

dbbl.deposit(2000)
dbbl.deposit(2000)

print(dbbl.get_balance())