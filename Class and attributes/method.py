def call():
    print('calling some one i dont know')
    return 'call done'
class Phone:
    price =19000
    color='blue'
    brand ='samsung'
    features=['camera','speaker','hammer']

    def call(self):#self dile jekono jaga diye class er moddher function(method) access kora jabe
        print('calling one person')
    def send_sms(self,phone,sms):
       text =f'sending SMS to :{phone} and message : {sms}'
       return text

my_phone = Phone()
print(my_phone.features)
my_phone.call()
result =my_phone.send_sms(41524,'I forgot to miss you')
print(result)