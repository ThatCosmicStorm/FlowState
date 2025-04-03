import time
import os
from pygame import mixer
from datetime import timedelta, datetime
from math import floor

N = "\n\n"
LINE = "*" * 20
N_LINE = f"\n{LINE}\n"
v = ""
idle_sec = 0
focus_num = 0
break_num = 0
break_sec = 0
session_s = "s"
break_s = "s"
tot_focus_sec = 0
tot_break_sec = 0
you_did = {}
you_spent = {}
alarm_path = __file__[:-12] + "breakalarm.wav"

mixer.init()

breakalarm = mixer.Sound(alarm_path)

def clear_and_print(text):
    os.system("cls" if os.name == "nt" else "clear")
    return print(text)


def pretty_print(x):
    return LINE + N + x


def print2(x):
    return clear_and_print(pretty_print(x))


def display(x):
    return floor(x) % 60


def display_time(x):
    return (f"{display(x / 60 / 60)}h, {display(x / 60)}m, {display(x)}s")


def q_enter():
    global v
    v = input("Type Q and press ENTER to end FlowTimer and get stats.")

print2(
    f"Welcome to FlowTimer!{N}"
    f"What do you plan to focus on today?{N}"
    "I plan to focus on..."
)

main_topic = input()

print2("Press ENTER to start a focus session.")

v = input()

while v.lower() != "q":

    focus_start = time.time()

    focus_num += 1

    print2(
        f"Focus Session #{focus_num} has STARTED!\n"
        f"You are being TIMED.{N}"
        f"Remember: your focus is on {(main_topic).upper()}.{N}"
        "Press ENTER to end this focus session."
    )

    v = input()

    focus_sec = floor(time.time() - focus_start)
    tot_focus_sec += focus_sec

    print2(
        f"Focus Session #{focus_num} has ENDED!{N}"
        "Session length:\n"
        f"{display_time(focus_sec)}"
    )

    if focus_num > 1:
        print("\nTOTAL time spent in focus sessions:")
        print(display_time(tot_focus_sec) + N + LINE)

    print("\nWhat did you do during the focus session?")

    if focus_num == 1:
        print("Ex. studied for unit exam, took notes of lectures, etc.\n")

    you_spent[focus_num] = display_time(focus_sec)
    you_did[focus_num] = input("During the focus session, I... ")

    if focus_sec < 10*60: break_sec = 1*60
    elif focus_sec < 25*60: break_sec = 5*60
    elif focus_sec < 50*60: break_sec = 10*60
    elif focus_sec < 1.5*60*60: break_sec = 15*60
    else: break_sec = 20*60

    if focus_num%4 == 0: break_sec *= 3*60

    print2(f"You deserve a {int(break_sec / 60)} minute break.")

    if focus_num%4 == 0:
        print(
            "\nYou have completed four focus sessions,"
            "so you get a longer break!"
        )
        
    print("\nPress ENTER to begin your break.")
    q_enter()

    if v.lower() == "q": break

    tot_break_sec += break_sec

    break_num += 1

    print2(
        f"Break #{break_num} has STARTED!{N}"
        f"WARNING: DO NOT PRESS ENTER UNTIL BREAK HAS ENDED.{N}"
        "Break time left:"
    )

    timer_sec = break_sec

    while timer_sec > -1:
        timer = timedelta(seconds=timer_sec)
        print(timer, end="\r")
        time.sleep(1)
        timer_sec -= 1
        # Actual timer

    mixer.Sound.play(breakalarm)

    print2(
        f"Break #{break_num} has ENDED!{N}"
        "Press ENTER to start a new focus session."
    )

    q_enter()


def done_read():
    print("Done reading?")
    input("Press ENTER to fully end FlowTimer.\n")


if focus_num > 0:

    print2(
        f"Would you like to save your stats in a new text file?{N}"
        "Type Y and press ENTER to save. Just press ENTER to not save."
    )

    save_stats = input().lower()

    if save_stats == "y":
        new_file = datetime.isoformat(datetime.now())
        new_file = new_file[:19].replace(":",".").replace("T","_") + ".txt"
        file = open(new_file, "a")
        print2(f"{new_file} has been created.\n")

    def write(x):
        if save_stats == "y": file.write(x)
        return print(x)

    if focus_num == 1: session_s = ""
    if break_num == 1: break_s = ""

    write(
        f"{LINE}{N}TOTAL Stats:{N}"
        f"You focused for {display_time(tot_focus_sec)} over {focus_num}"
        f" focus session{session_s}.\n"
        f"And you spent {display_time(tot_break_sec)} over {break_num} break"
        f"{break_s}.\n"
        f"{N_LINE}\n"
        f"Session-by-session Stats:{N}"
        f"Your main focus was on {(main_topic).upper()}.{N}"
    )

    for session in range(1, focus_num + 1):
        write(
            f"Focus Session #{session}:\n"
            f"You focused for {you_spent[session]} during this session.\n"
            f"You wrote down \"I {you_did[session]}\".{N}"
        )

    if save_stats == "y":
        file.close()
        print(f"{LINE}{N}All stats have been recorded and stored in {new_file}\n")

    done_read()


else:
    print2("No stats were recorded.\n")
    done_read()