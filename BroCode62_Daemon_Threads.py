# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes

import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")


x = threading.Thread(target=timer, daemon=True) #Daemon has to be true otherwise daemon thread will keep going despite user input`
x.start()

# x.setDaemon(True) #changes thread but does not work if the thread is running. It would have to use before a start function
# print(x.isDaemon()) #Tells us if a thread is a daemon or not

answer = input("Do you wish to exit?")