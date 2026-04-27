def update(list):
    list.append(555555)
    print('Updated list is : ',list)

l = [140,52,697,75,779,5496]
print("the list is : ",l)
update(l)  # pass by refernce

print("After the update : ",l)



