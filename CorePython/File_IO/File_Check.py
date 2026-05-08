def Checking_file():
    file = open("C:/Users/KESHAV PATIDAR/OneDrive/Desktop/Hello.txt")
    print("The file name is :",file.name)    # gives the file name
    print("The file mode is :",file.mode)    # by default the mode of file is reading mode
    print("Is file is closed ? :",file.closed)   # true if file is closed
    file.close()
    print("Is file is closed ? :",file.closed)

Checking_file()