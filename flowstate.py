"""
Contains the functions that run FlowState.
"""

import os
import tkinter as tk
from datetime import timedelta

PADDING = "-200+200"

root = tk.Tk()


def img(image: str) -> tk.PhotoImage:
    """
    Load an image and return it as a PhotoImage object.
    """
    if os.name == "nt":
        directory = f".\\Images\\{image}"
    else:
        directory = f"./Images/{image}"

    return tk.PhotoImage(file=directory)


def place_canvas() -> tk.Canvas:
    """
    Places a background canvas.
    """
    bg = tk.Canvas(
        root,
        width=360,
        height=360,
        bg="white",
        highlightthickness=0
    )

    bg.place(x=0, y=0)

    return bg


class TimeText:
    """
    The text for the stopwatch.
    """
    def __init__(self) -> None:
        self.focus_sec = 0
        self.label = tk.Label(
            root,
            text="0:00:00",
            font=("Tahoma", 64)
        )

        self.label.place(x=180, y=150, anchor="center")

    def time_string(self) -> str:
        """
        Adds a second to the timer and styles it with timedelta.
        """
        self.focus_sec += 1
        display_time = timedelta(seconds=self.focus_sec)
        return str(display_time)

    def update(self) -> None:
        """
        Updates the label to display the new time.
        """
        self.label.configure(text=self.time_string())
        self.label.after(1000, self.update)


def settings_menu() -> None:
    """
    Adds settings menu with options.
    """
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    settings = tk.Menu(menubar, tearoff=False)

    settings.add_command(
        label="Proportional"
    )
    settings.add_command(
        label="Incremental"
    )

    menubar.add_cascade(
        label="Settings",
        menu=settings
    )


def main() -> None:
    """
    The main program.
    """
    root.title("FlowState")
    root.geometry(f"360x360{PADDING}")
    root.resizable(False, False)
    root.attributes("-topmost", 1)

    place_canvas()

    settings_menu()

    stopwatch = TimeText()
    stopwatch.label.after(1000, stopwatch.update)

    root.mainloop()


if __name__ == "__main__":
    main()
