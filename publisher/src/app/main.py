#!usr/bin/python3

from scheduler.schedule_jobs import *
import time

if __name__ == "__main__":
    print("Starting Publisher ")
    while True:
        print("Sending Data ")
        run_jobs()
        time.sleep(5)