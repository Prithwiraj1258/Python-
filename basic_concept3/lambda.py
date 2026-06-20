# lambda

#  def doubled(x):
#   return x*2

# doubled =lambda num : num *2 # short-cut of def function
# squared =lambda num: num*num 
# result =doubled (44)    
# output =squared  (9)
# #print(result,output)
# add =lambda x,y : x+y
# #sum =add(11,33)

# numbers =[12,56,98,78,56]
# doubled_nums=map (doubled,numbers)
# print(numbers)
# print(list(doubled_nums))
actors = [
    {'name':'sabana','age':65},
    {'name':'sabnoor','age':45},
    {'name':'sabila noor','age':30},
    {'name':'sabana','age':47},
]

juniors = filter(lambda actor: actor['age'] < 40, actors)
print(list(juniors))