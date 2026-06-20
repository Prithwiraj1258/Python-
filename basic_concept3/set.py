# set : unique items collection
#list --> []
#tupple->()
#set ->{}
#set: unique items collectiom.NO duplicates
numbers=[12,56,98,78,56,12,6,98]
numbers_set=set(numbers)
print(numbers_set)
numbers_set.add(55)# frequently ekta jagay add korbe
# numbers_set[1]=5
# print(numbers_set) evabe change kora jay na
numbers_set.remove(6)
print(numbers_set) 
A={1,3,5,7,9}
B={1,2,3,4,5}

print(A & B)
print(A | B)
# NOTE : Tuple e common value thakte pare, Set e kono common value thakbe na
