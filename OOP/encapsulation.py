#encapsulation -->hide details
class Bank:
    def __init__(self,holder_name,initial_deposit)->None:
        self.holder_name=holder_name#public attribute
        self.__balance=initial_deposit#private
        self._brance="banani 11"#protected
    def deposit(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance #this returns 10000 not 0
    def withdraw(self,amount):
        if amount<self.__balance:
            self.__balance=self.__balance-amount
            return amount
        else:
            return f"Fokira taka nai"
rafsun =Bank('Chooto bro',10000)
print(rafsun.holder_name)
rafsun.holder_name='boro vai'
# print(rafsun.holder_name)
rafsun.__balance=0 #not accesible in the private attribute
print(rafsun.deposit(500))#deposit returns nothing
print(rafsun.get_balance())
print(rafsun.holder_name)
print(rafsun._brance)
print(dir(rafsun))
print(rafsun._Bank__balance)#আসল private balance, mangled নাম দিয়ে access
# _ClassName__attributename