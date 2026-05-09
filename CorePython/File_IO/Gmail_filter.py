import re # Regular Expression

def readline():
    input_file1 =   open("C:\\Users\\KESHAV PATIDAR\\OneDrive\\Desktop\\File_Handling\\File_filter.txt","r")
    output_file1 = open("C:\\Users\\KESHAV PATIDAR\\OneDrive\\Desktop\\File_Handling\\gmail_only","w")

    input_file2 =   open("C:\\Users\\KESHAV PATIDAR\\OneDrive\\Desktop\\File_Handling\\File_filter.txt","r")
    output_file2 = open("C:\\Users\\KESHAV PATIDAR\\OneDrive\\Desktop\\File_Handling\\yahu_only", "w")

    input_file3 =   open("C:\\Users\\KESHAV PATIDAR\\OneDrive\\Desktop\\File_Handling\\File_filter.txt","r")
    output_file3 = open("C:\\Users\\KESHAV PATIDAR\\OneDrive\\Desktop\\File_Handling\\acro_only", "w")

    for line in input_file1:
        if re.search("@gmail.com",line):
            output_file1.write(line)
            print(line)

    for line in input_file2:
        if re.search("@yahuu.com",line):
            output_file2.write(line)
            print(line)

    for line in input_file3:
        if re.search("@acropolis.com",line):
            output_file3.write(line)
            print(line)


    input_file1.close()
    input_file2.close()
    input_file3.close()
    output_file1.close()
    output_file2.close()
    output_file3.close()


readline()