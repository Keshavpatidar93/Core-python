dict = {'name':"Keshav Patidar",'age':19,'marks': 99.5}
print("dictionary : ",dict)       #  print dictionary

print(type(dict))    #   printing the type of the dict

dict.update({"roll_no" : "0827CS241119"})  #  it adds the value into the last
print(dict)

dict.update({"roll_no" : "1119"})  # also it updates the value
print(dict)

print(len(dict))   # it prints the length of the dictionary


dict.setdefault('address','Indore')  # it adds the value in last into the dictionary
print("dictionary : ",dict)

print(dict.get('name')) # it return the value according to the key

print(dict.pop('age')) # it works as the get function

print(dict.keys())  # it print all the keys

print(dict.values())    #it print all the values

print(dict.items())  # print all the key values pairs

copy = dict.copy()    # it makes a copy of the dictionary
print("Copy of the dictionary is : ",copy)

print(dict.popitem())   # it pop the key : value into the last

print(len(dict))

print(dict.fromkeys(['x','y','z'],"hello"))

print(dict)