import time

print("-----------------Task Timer-----------------")
print("Times are in minutes.")
work_time_duration = int(input("How long do you want to work? ")) * 60
break_time_duration = int(input("How long do you want the breaks? ")) * 60


def start():
    print('Start working!')
    time.sleep(work_time_duration)
    print('Take a break')
    time.sleep(break_time_duration)
    print("Break's over")

    start()


start()
