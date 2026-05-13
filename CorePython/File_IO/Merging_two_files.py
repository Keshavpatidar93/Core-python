var = ""
var1 = ""

def read():
    f = open("C:\\Users\\KESHAV PATIDAR\\OneDrive\\Desktop\\File_Handling\\list.txt","r")
    var = f.read()
    # print(var)

    f1 = open("C:\\Users\\KESHAV PATIDAR\\OneDrive\\Desktop\\File_Handling\\keyboardtofile.txt","r")
    var1 = f1.read()
    # print(var1)

    file = open("C:\\Users\\KESHAV PATIDAR\\OneDrive\\Desktop\\File_Handling\\Merging.txt","w")
    file.write(var)
    file.write("\n")
    file.write(var1)
    file.close()
    f1.close()
    f.close()

read()
