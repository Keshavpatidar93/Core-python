list = [30,28,10,50,70,60]
for i in range(0,len(list)):
    for j in range(i+1, len(list)-1):
        if list[i] > list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j]=temp


print(list,end=" ")

