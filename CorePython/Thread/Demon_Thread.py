import threading
import time

def first_thread(name):
    for i in range(11):
        time.sleep(4)         # demon thread
        print(name,i)

def second_thread():
    for i in range(11):
        time.sleep(2)         # main thread
        print("Main Thread",i)

t1 = threading.Thread(target=first_thread,args=("Demon Thread",),daemon=True) # in demon thread the arguments are into the brackets()
t2 = threading.Thread(target=second_thread)

t1.start()
# time.sleep(2)
t2.start()