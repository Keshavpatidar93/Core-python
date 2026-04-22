name = "Keshav Patidar Pathrad"
str = name.split() # the str becomes list = ['keshav','patidar','pathrad']
for i in str:
    reverse = " "
    for ch in i:
        reverse = ch + reverse
    print(reverse,end="")
