def keyboardtofile():
    file = open("C:/Users//KESHAV PATIDAR//OneDrive//Desktop/keyboardtofile.txt", "w")
    text = input("Enter your message : ")
    while(text != "Quit"):
        file.write(text)
        file.write("\n")
        text = input()
    file.close()

keyboardtofile()