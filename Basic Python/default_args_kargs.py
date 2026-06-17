# def sum(num1,num2,num3=0,num4=0):
#     result = num1+num2+num3
#     return result
# total=sum(99,11,5) 
# print('total : ',total)
#args 
def all_sum(*numbers):#"*" dile kannakati korbe na(tapple banay (array er moto)
    print(numbers)
    sum=0
    for num in numbers:
        print(num)
        sum=sum+num
   
