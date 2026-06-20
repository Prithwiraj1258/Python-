#mainly function theke ekadhik jinish return korte gele tuple use kora hoy
things ='pen','tripod','water bottle','sunglass'
print(type(things))#-> type=tuple
print(things[-2])#->tripod
print(things[3:4])
if 'tripod' in things:
    print('exists')#in condition hits then exists will be printed
for item in things:
    print(item)
#things[0]='wagin' elements can"t be changed
# print(things[0])
print(len(things))#->size of tuple
mega=([2,3,4],[6,8,9])
print(type(mega))#its a tuple
mega[0][1]=666# 1st list er 1th index
print(mega)#it can be changed

