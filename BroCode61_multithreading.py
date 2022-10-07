# ****************************************************
# Python threading tutorial
# ****************************************************
# thread =  a flow of execution. Like a separate order of instructions.
#                  However, each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock), (only one thread can run at any one time
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing
# Multithreading is useful for when there is one big process that eats a lot of time
# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading. Example would be if there was a timer for user input. one thread for user input and one for countdown timer

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_milk():
    time.sleep(4)
    print("You drank milk")


def clothes():
    time.sleep(5)
    print("You put clothes on")


x = threading.Thread(target=eat_breakfast, args=()) #args for it function has parameters
x.start()

y = threading.Thread(target=drink_milk, args=())
y.start()

z = threading.Thread(target=clothes, args=())
z.start()

x.join() #these cause the main thread to wait for these threads to complete before it starts. Will cause  active count to return 1
y.join()
z.join()

#these make it so that we run multiple threads at once

print(threading.active_count()) #How many threads are running?
print(threading.enumerate()) #Which threads are running? One thread in charge of running program is main thread
print(time.perf_counter()) #Returns how long it takes main thread to complete.
                            # The main threads job is to call the three threads and use the active count enumerate and perf counter functions

