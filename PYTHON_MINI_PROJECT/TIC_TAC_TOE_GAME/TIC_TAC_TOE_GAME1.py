import tkinter as tk
from tkinter import messagebox


def check_winner():
    global winner

    # All possible winning combinations
    for combo in [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]:

        # Check if all three buttons have the same value
        if (
            buttons[combo[0]]["text"]
            == buttons[combo[1]]["text"]
            == buttons[combo[2]]["text"]
            != ""
        ):

            # Change winning buttons to green
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")

            # Show winner
            messagebox.showinfo(
                "TIC-TAC-TOE",
                f"PLAYER {buttons[combo[0]]['text']} WINS!"
            )

            winner = True
            return


def button_click(index):
    global current_player

    # Only allow empty buttons to be clicked
    # and don't allow moves after someone wins
    if buttons[index]["text"] == "" and not winner:

        buttons[index]["text"] = current_player

        check_winner()

        # Change player only if game is not over
        if not winner:
            toggle_player()


def toggle_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    label.config(text=f"Player {current_player}'s turn")


# Create main window
root = tk.Tk()
root.title("TIC-TAC-TOE")


# Create 9 buttons
buttons = []

for i in range(9):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 25),
        width=6,
        height=2,
        command=lambda i=i: button_click(i)
    )

    buttons.append(button)


# Arrange buttons in 3 × 3 grid
for i, button in enumerate(buttons):
    button.grid(
        row=i // 3,
        column=i % 3
    )


# Starting player
current_player = "X"

# Game winner status
winner = False


# Player turn label
label = tk.Label(
    root,
    text=f"Player {current_player}'s turn",
    font=("Arial", 16)
)

label.grid(
    row=3,
    column=0,
    columnspan=3
)


# Start the application
root.mainloop()