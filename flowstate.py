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
    bg.pack(anchor=tk.CENTER, expand=True)

    return bg


def play_button(canvas: tk.Canvas):
    """
    Displays a functional play button that starts the stopwatch.
    """

    button = canvas.create_oval(
        (145, 220),
        (215, 290),
        fill="gray"
    )
    triangle = canvas.create_polygon(
        (168, 235),
        (168, 275),
        (200, 255),
        fill="lightgray"
    )

    canvas.tag_bind(
        button,
        "<Button-1>",
        lambda e: TimeText.first_update(TimeText())
    )

    canvas.tag_bind(
        triangle,
        "<Button-1>",
        lambda e: TimeText.first_update(TimeText())
    )


class TimeText:
    """
    The text for the stopwatch.
    """
    def __init__(self) -> None:
        self.focus_sec = 0
        self.focused = False
        self.label = tk.Label(
            root,
            bg="white",
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

    def first_update(self) -> None:
        """
        Waits one second before updating the time.
        """
        self.focused = True
        self.label.after(1000, self.update)

    def update(self) -> None:
        """
        Updates the label to display the new time.
        """
        if self.focused:
            self.label.configure(text=self.time_string())
            self.label.after(1000, self.update)

    def stop_updates(self) -> None:
        """
        Stop the time from updating.
        """
        self.focused = False


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

    canvas = place_canvas()

    play_button(canvas)

    TimeText()

    settings_menu()

    root.mainloop()


if __name__ == "__main__":
    main()
