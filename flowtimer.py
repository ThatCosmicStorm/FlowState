import time
from math import floor
from datetime import timedelta

N = "\n\n"
LINE = "*" * 20
N_LINE = f"\n{LINE}\n"
v = ""
q = True
idle_sec = 0
focus_num = 0
break_num = 0
break_sec = 0
session_s = ""
break_s = ""
tot_focus_sec = 0
tot_break_sec = 0


def pretty(x):
    y = floor(x) % 60
    return y


def display_time(x):
    return f"{pretty(x / 60 / 60)}h, {pretty(x / 60)}m, {pretty(x)}s"


def q_enter():
    global v
    v = input("Type Q and press ENTER to end FlowTimer and get stats.")


print(f"{N * 3}Welcome to FlowTimer!\n")
print("What do you plan to focus on today?\n")
main_topic = input("I plan to focus on... ")

print(N_LINE)
print("Press ENTER to start a focus session.")

while v.lower() != "q":

    focus_start = time.time()

    focus_num += 1

    print(N_LINE)
    print(f"Focus Session #{focus_num} has STARTED!\n")
    print("You are being TIMED.\n")
    print(f"Remember: your focus is on {(main_topic).upper()}.\n")
    v = input("Press ENTER to end this focus session.")

    focus_sec = time.time() - focus_start
    tot_focus_sec += focus_sec

    print(N_LINE)
    print(f"Focus Session #{focus_num} has ENDED!")
    print("\nSession length:")
    print(f"{display_time(focus_sec)}{N}{LINE}")

    if focus_num > 1:
        print("\nTOTAL time spent in focus sessions:")
        print(f"{display_time(tot_focus_sec)}{N}{LINE}")

    if focus_sec < 10*60: break_sec = 1*60
    elif focus_sec < 25*60: break_sec = 5*60
    elif focus_sec < 50*60: break_sec = 10*60
    elif focus_sec < 1.5*60*60: break_sec = 15*60
    else: break_sec = 20*60

    if focus_num%4 == 0: break_sec *= 3*60

    print(f"\nYou deserve a {int(break_sec / 60)} minute break!")

    if focus_num%4 == 0:
        print("\nYou have completed four focus sessions, so you get a longer"
              " break!")

    idle = time.time()

    print("\nPress ENTER to begin your break.")
    q_enter()

    if v.lower() == "q":
        break

    idle_sec += time.time() - idle

    tot_break_sec += break_sec

    break_num += 1

    print(N_LINE)
    print(f"Break #{break_num} has STARTED!\n")
    print("Break time left:")

    timer_sec = break_sec

    while timer_sec > -1:
        timer = timedelta(seconds=timer_sec)
        print(timer, end="\r")
        time.sleep(1)
        timer_sec -= 1
        # Actual timer

    print("\n"+N_LINE)
    print(f"Break #{break_num} has ENDED!\n")

    idle = time.time()

    # Break timer
    print("Press ENTER to start a new focus session.")
    q_enter()

    idle_sec += time.time() - idle


def done_read():
    print("Done reading?")
    input("Press ENTER to fully end FlowTimer.\n")


if focus_num > 0:
    if focus_num > 1: session_s = "s"
    if break_num > 1: break_s = "s"

    print(N_LINE)
    print(f"FlowTimer Stats:\n")
    print(f"Your main focus was on {(main_topic).upper()}.\n")
    print(f"You focused for {display_time(tot_focus_sec)} over {focus_num}"
          f" focus session{session_s}.\n")
    print(f"And you spent {display_time(tot_break_sec)} over {break_num} break"
          f"{break_s}.\n")
    done_read()


else:
    print(N + N_LINE)
    print("No stats to show.\n")
    done_read()