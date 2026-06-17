numbers=[122,45,98,68]
numbers.append(56)
print(numbers)
numbers.insert(0,71)#0 index e 71 add
print(numbers)
if 8 in numbers :
 numbers.remove(8)
print(numbers)
if 98 in numbers :
  numbers.remove(98)
last = numbers.pop()#last = last value
print(last,numbers)
if 122 in numbers:
   index=numbers.index(122)
   print(index)
   numbers.reverse()
   print(numbers)
  