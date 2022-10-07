# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():

    start = time.perf_counter() #needed for some reason not sure why
    print("cpu count:", cpu_count()) #Shows how many CPUs we got

    a = Process(target=counter, args=(500000000,)) #comma in args is to differentiate from an expression since we only have one argument
    b = Process(target=counter, args=(500000000,)) #uses two cpus to count. Each gets half the total amount

    a.start() #Starts child process
    b.start()

    print("processing...")

    a.join()
    b.join()

    print("Done!")
    print("finished in:", time.perf_counter() - start, "seconds")


if __name__ == '__main__': #needed for windows. Child process will be copied but not executed
    main()