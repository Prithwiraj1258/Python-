numbers=[45,87,65,43,85,14,26,61]
odds=[]
for num in numbers:
    if num %2 == 1 and num%5==0:
        odds.append(num)

print(odds)
odd_nums=[num for num in numbers if num%2==1 if num %5 ==0]
print(odd_nums)
players =['sakib','mushfik','mustafiz']
ages=[38,38,32]
for player in players:
    print('player:',player)