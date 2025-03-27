import time
from math import floor
from datetime import timedelta

v = ""
n = "\n\n"
line = "*" * 20
idle_sec = 0
focus_num = 0
break_num = 0
break_min = 0
tot_break_min = 0
no_break = False

v = input(f"{n * 3}Welcome to FlowTimer!{n}Press ENTER to start a focus"
          f" session.{n}Type Q and press ENTER to end FlowTimer and get your"
          " statistics.\n")

flow_start = time.time()
# Takes a snapshot of the time at the start of the FIRST focus session


while v.lower() != "q":
    # As long as Q has not been entered, the flowtimer will work

    if v.lower() == "q":
        break
        # Loop stop

    focus_start = time.time()
    # Takes a snapshot of the time at the start of the CURRENT focus session

    v = input(f"{line}{n}Focus Session #{focus_num + 1} has STARTED!{n}You"
              f" are CURRENTLY being timed.{n}Press ENTER to end this focus"
              " session.\n")

    if v.lower() == "q":
        break

    focus_num += 1
    focus_sec = time.time() - focus_start
    focus_min = focus_sec / 60
    focus_hours = focus_min / 60

    tot_focus_sec = ((time.time() - flow_start) - (break_min * 60)
                     - (idle_sec))
    tot_focus_min = tot_focus_sec / 60
    tot_focus_hours = tot_focus_min / 60

    print(f"{line}{n}Focus Session #{focus_num} has ENDED!")

    def pretty24(x):
        y = str((floor(x) % 24))
        return y

    def pretty60(x):
        y = str((floor(x) % 60))
        return y

    idle = time.time()

    if focus_num == 1:
        print("\nSession length:")
        print(f"{pretty24(focus_hours)}h, {pretty60(focus_min)}m, "
              f"{pretty60(focus_sec)}s{n}{line}")

    else:
        print("\nSession length:")
        print(f"{pretty24(focus_hours)}h, {pretty60(focus_min)}m, "
              f"{pretty60(focus_sec)}s{n}TOTAL time spent in focus sessions:")
        print(f"{pretty24(tot_focus_hours)}h, {pretty60(tot_focus_min)}m, "
              f"{pretty60(tot_focus_sec)}s{n}{line}")

    idle_sec += time.time() - idle

    if focus_hours < 1:
        if focus_min < 10:
            break_min = 1
        elif 10 < focus_min < 25:
            break_min = 5
        elif 25 <= focus_min < 50:
            break_min = 10
        elif 50 <= focus_min < 60:
            break_min = 15

    else:
        if focus_min < 30:
            break_min = 15
        elif focus_min >= 30:
            break_min = 20

    if focus_num % 4 == 0:
        break_min *= 3

    tot_break_min += break_min

    if focus_num % 4 != 0:
        print(f"\nYou deserve a {break_min} minute break!")

    else:
        print(f"\nYou have completed four focus sessions, so you get a"
              f"longer break!{n}You deserve a {break_min} minute break!")

    idle = time.time()

    v = input(f"\nPress ENTER to begin your break.")

    if v.lower() == "q":
        no_break = True
        break

    idle_sec += time.time() - idle

    break_num += 1

    print(f"\n{line}{n}Break #{break_num} has STARTED!{n}Break Time Left:")

    timer_sec = break_min * 60

    while timer_sec > 0:
        timer = timedelta(seconds=timer_sec)
        print(timer, end="\r")
        time.sleep(1)
        timer_sec -= 1
        # Actual timer

    print(f"{n}{line}{n}Break #{break_num} has ENDED!")

    idle = time.time()

    v = input("\nPress ENTER to start a new focus session.\n")
    # Break timer

    if v.lower() == "q":
        break

    idle_sec += time.time() - idle


if focus_num > 0:

    if no_break:
        tot_break_min -= break_min

    tot_break_hours = tot_break_min / 60

    if focus_num == 1:
        session_s = ""
    else:
        session_s = "s"

    if break_num == 1:
        break_s = ""
    else:
        break_s = "s"

    print(f"\n{line}\n")
    input(f"FlowTimer Stats:{n}You focused for {pretty24(tot_focus_hours)}h, "
          f"{pretty60(tot_focus_min)}m, {pretty60(tot_focus_sec)}s over "
          f"{focus_num} focus session{session_s}.{n}You spent "
          f"{pretty24(tot_break_hours)}h, {pretty60(tot_break_min)}m, 0s over "
          f"{break_num} break{break_s}.{n}Done reading?\nPress ENTER to fully"
          " end FlowTimer.\n")


elif focus_num == 0:
    input(f"\n{n}{line}{n}No stats to show.{n}Done reading?\nPress ENTER to"
          " fully end FlowTimer.\n")