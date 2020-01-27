import time
import sys

use_seconds = 'seconds' in sys.argv
print(use_seconds)

print("-----------------Task Timer-----------------")

print(f"Times are in {'seconds' if use_seconds else 'minutes'}.")

work_time_duration = float(input("How long do you want to work? "))
break_time_duration = float(input("How long do you want the breaks? "))

if not use_seconds:
    work_time_duration *= 60
    break_time_duration *= 60


def start():
    print('Start working!')
    time.sleep(work_time_duration)
    print('Take a break')
    time.sleep(break_time_duration)
    print("Break's over")

    start()


start()
