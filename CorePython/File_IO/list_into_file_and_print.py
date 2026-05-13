list = [10,20,30,40,50,60,70]
def write():
    file = open("C:\\Users\\KESHAV PATIDAR\\OneDrive\\Desktop\\File_Handling//list.txt","w")
    file.write(str(list)) #the write function doesn't take list so we convert it into string
    file.close()

def read():
    file = open("C:\\Users\\KESHAV PATIDAR\\OneDrive\\Desktop\\File_Handling//list.txt","r")
    text = file.read()
    print("The list into the file is ....",text)
    file.close()

write()
read()
