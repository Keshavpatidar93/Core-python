list = [10,20,30,66,4,20,77,20,50]
number = 88
count = 0
for i in list:
    if i == number:
        count +=1
if count > 0:
    print("Number exist ")
else:
    print("Number does not exist")