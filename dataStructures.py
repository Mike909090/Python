#list
d2 = ['isaac', 15, '20', ('isaac', 15), ['isaac', 2]]
d2[1] = 60
#add an item in a dictionary
d2.append('pooki')
#remove an item in a dictionary
del d2[3]
print(d2)
#clear an item in a dictionary
d2.clear()
print(d2)
print(''' ''')

#tuple
d1 = ('isaac', 15, '20', ['isaac', 2])
print(d1)
del d1
try:
 print(d1)
except:
    print('At least you tried')
print(''' ''')

#dictionary
d = {
    "john": 40,
    "petter": 45
}
#delete an item in a dictionary
del d['john']
#add an item in a dictionary
d["isaac"] = 19
print(d)
#clear a dictionary
d.clear()
print(d)
