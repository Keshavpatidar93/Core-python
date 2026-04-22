name = "my name is keshav patidar"
alphabates = "abcdefghijklmnopqrstuvwxyz"
for i in alphabates:
    count=0
    for j in name:
        if i == j:
            count +=1
    if count>0:
        print(i ,"Count = ",count)