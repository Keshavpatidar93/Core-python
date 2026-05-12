import threading

def Hello():
    for i in range(1,11):
        print("Hello",i)

def Hi():
    for i in range(1,11):
        print("Hi",i)

t1 = threading.Thread(target=Hello)
t2 = threading.Thread(target=Hi)

t1.start()
t2.start()