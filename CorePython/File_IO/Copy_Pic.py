import shutil

source = "C://Users//KESHAV PATIDAR//OneDrive//Desktop//Video1//RamJiVedio.mp4"
target = "C://Users//KESHAV PATIDAR//OneDrive//Desktop//Video2//RamJiVedio.mp4"         # only at the time of copy from one file to another we use double lines (//) rest of all places we use single(/) line
# here in place of source and target we will write any name as well
shutil.copyfile(source,target)
print("your",source,"     <=== is copied to ===>       ",target)