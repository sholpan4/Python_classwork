import threading
import time

def my_func():
    print("Yoooo")
    time.sleep(3)
    print("Woke up")

my_thread = threading.Thread(target=my_func) #args=(items)
my_thread.start()

print("prodoljaetsya")


my_thread.join()
print("End")