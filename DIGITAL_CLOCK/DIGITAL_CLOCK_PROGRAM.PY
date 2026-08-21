import tkinter as tk
from time import strftime

# Main Window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("700x400")
root.configure(bg="#121212")
root.resizable(False, False)

# Title
title_label = tk.Label(
    root,
    text="DIGITAL CLOCK",
    font=("Arial", 20, "bold"),
    bg="#121212",
    fg="white"
)
title_label.pack(pady=(30, 10))


# Clock Function
def time():
    current_time = strftime("%I:%M:%S")
    current_date = strftime("%A, %d %B %Y")
    am_pm = strftime("%p")

    time_label.config(text=current_time)
    ampm_label.config(text=am_pm)
    date_label.config(text=current_date)

    root.after(1000, time)


# Time
time_label = tk.Label(
    root,
    font=("Consolas", 70, "bold"),
    bg="#121212",
    fg="#00FFCC"
)
time_label.pack(pady=(20, 0))


# AM / PM
ampm_label = tk.Label(
    root,
    font=("Arial", 18, "bold"),
    bg="#121212",
    fg="#FFD700"
)
ampm_label.pack()


# Date
date_label = tk.Label(
    root,
    font=("Arial", 18),
    bg="#121212",
    fg="white"
)
date_label.pack(pady=20)


# Footer
footer_label = tk.Label(
    root,
    text="Digital Clock By MANSI",
    font=("Arial", 10),
    bg="#121212",
    fg="gray"
)
footer_label.pack(side="bottom", pady=15)


# Start Clock
time()

root.mainloop()