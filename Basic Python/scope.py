balance = 3000  # global variable

def buy_things(item, price):
    #local scope variable
    #you can access global variable without using the global keyword
    global balance
    #but if you want to modify global variable ,yo have to use global variable keyword
    print("previous balance:", balance)

    balance = balance - price

    print(f'balance after buying {item}:', balance)

buy_things('sunglass', 1000)