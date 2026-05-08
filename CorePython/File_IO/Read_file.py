def read():
    file = open("C:/Users/KESHAV PATIDAR/OneDrive/Desktop/Reading.txt", "r")     # here in the place of the file we can write any name
    text = file.read()
    print("Your file data is..........")
    print(text)
    file.close()

read()