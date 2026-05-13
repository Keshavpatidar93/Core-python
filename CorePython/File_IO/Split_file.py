def read():
    file = open("C:\\Users\\KESHAV PATIDAR\\OneDrive\\Desktop\\File_Handling\\File_filter.txt","r")
    text = file.read()

    f1 = open("C:\\Users\\KESHAV PATIDAR\\OneDrive\\Desktop\\File_Handling\\File_filter1.txt","w")
    for line in text:
        if line == "5":
            break
        else:
            f1.write(line)
    f1.close()

    f2 = open("C:\\Users\\KESHAV PATIDAR\\OneDrive\\Desktop\\File_Handling\\File_filter2.txt", "w")
    count = 0
    for line in text:
        if line == "5":
            count += 1
        if count > 0:
            f2.write(line)

    f2.close()
    file.close()

read()