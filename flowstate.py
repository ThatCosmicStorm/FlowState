"""
Contains the functions that run FlowState.
"""

import os
import tkinter as tk

PADDING = "-200+200"

root = tk.Tk()


def img(image) -> tk.PhotoImage:
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
    screen_width =root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    bg = tk.Canvas(
        root,
        width=screen_width,
        height=screen_height,
        bg="navy",
        highlightthickness=0
    )
    bg.place(x=0, y=0)

    return bg


def settings_menu():
    """
    settings_menu
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


def main():
    """
    main program
    """
    root.title("FlowState")
    root.geometry(f"360x360{PADDING}")
    root.resizable(False, False)
    root.attributes("-topmost", 1)

    place_canvas()

    settings_menu()

    root.mainloop()


if __name__ == "__main__":
    main()
