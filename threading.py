import threading

def print_one():
	for i in range(32):
		print(9)
def print_two():
	for i in range(1000):
		print(51)
    
# create threads
thread1 = threading.Thread(target=print_one)
thread2 = threading.Thread(target=print_two)
# start thread 1
thread1.start()
# start thread 2
thread2.start()
# wait until thread 1 is completely executed
thread1.join()
# wait until thread 2 is completely executed
thread2.join()
# both threads completely executed
print("DONE!!!")
