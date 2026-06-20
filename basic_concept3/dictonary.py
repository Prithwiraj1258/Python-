numbers=[1,2,3,4,5,98,45]
person1=['kala chan','kalipur',23,'student']
#key value pair
#dictionary
#object
#hash table 
# overlap with set
person={'name':'kala Pakhi','address':'kaliapur','age':23,'job':'facebooker'}
# print(person)
# print(person['job'])#->facebooker
# #print(person.keys())#->(['name', 'address', 'age', 'job'])
# print(person.values())#->sudhu man gulo print korbedict_values(['kala Pakhi', 'kaliapur', 23, 'facebooker'])
# person['language']='python'#new update possible
# print(person)
# del person['age']#age deleted
# print(person)
for key,value in person.items():
    print(key,value)