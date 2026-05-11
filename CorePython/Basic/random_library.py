# import random
# for i in range(5):
#     print(random.choice(['Ram','Shyam','jay','viru','keshav','chetan','golu']))

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
even = 0
count1 = 0
count2 = 0
odd = 0
for i in list :
    if i%2 == 0:
        even +=i
        count1 +=1
        if count1 == 5:
            break
for i in list:
    if i % 2 != 0:
        odd += i
        count2 +=1
        if count2 == 5:
            break

print("The average of first 5 even numbers is:",even/5)
print("The average of first 5 odd numbers is:",odd/5)
