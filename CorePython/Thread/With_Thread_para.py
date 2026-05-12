import threading

def Hello(name):
    for i in range(1,11):
        print("Hello :",name,i)

def Hi(name):
    for i in range(1,11):
        print("Hi :",name,i)

t1 = threading.Thread(target= Hello,args=("keshav",))   # here the , is used because the interpreter knows there is no any other argument
t2 = threading.Thread(target= Hi,args=("Anshu",))

t1.start()
t2.start()