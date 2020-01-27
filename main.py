import time
import sys
from playsound import playsound

use_seconds = 'seconds' in sys.argv

print("-----------------Task Timer-----------------")

print(f"Times are in {'seconds' if use_seconds else 'minutes'}.")

work_time_duration = float(input("How long do you want to work? "))
break_time_duration = float(input("How long do you want the breaks? "))
to_do_list = input("Enter the list of things to do separated by a comma: ")
to_do_list = to_do_list.split(", ")

if not use_seconds:
    work_time_duration *= 60
    break_time_duration *= 60


def alarm():
    playsound("alarm.wav")


def start():
    for to_do_list_item in to_do_list:
        print(f"Time for: ", to_do_list_item)
        time.sleep(work_time_duration)
        print('Take a break')
        alarm()
        time.sleep(break_time_duration)
        print("Break's over")
        alarm()

    print("Congratulations! You did it!")


start()
