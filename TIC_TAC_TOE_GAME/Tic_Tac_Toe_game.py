import tkinter as tk
import random

from sounds import (
    play_player_move,
    play_computer_move,
    play_win_sound,
    play_draw_sound
)


# ==========================================================
# COLORS
# ==========================================================

WOOD_DARK = "#3B2114"
WOOD = "#5A321D"

# Empty box
EMPTY_BOX = "#C89563"

# Player X box
X_BOX = "#8B4513"

# Computer O box
O_BOX = "#704214"

# X text color
X_COLOR = "#FFE4B5"

# O text color
O_COLOR = "#FFF8DC"

# Winning boxes
WIN_COLOR = "#D4AF37"

WHITE = "#FFF8E7"

GOLD = "#F4C542"

# Hover color
BUTTON_HOVER = "#D8A875"


# ==========================================================
# GAME VARIABLES
# ==========================================================

game_running = True

player_score = 0

computer_score = 0

draw_score = 0


# ==========================================================
# WINNING COMBINATIONS
# ==========================================================

winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],

    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],

    [0, 4, 8],
    [2, 4, 6]
]


# ==========================================================
# MAIN WINDOW
# ==========================================================

root = tk.Tk()

root.title("Tic-Tac-Toe")

root.geometry("600x750")

root.resizable(False, False)

root.configure(
    bg=WOOD_DARK
)


# ==========================================================
# TITLE
# ==========================================================

title = tk.Label(
    root,
    text="TIC - TAC - TOE",
    font=("Arial", 30, "bold"),
    bg=WOOD_DARK,
    fg=GOLD
)

title.pack(
    pady=(25, 5)
)


# ==========================================================
# SUBTITLE
# ==========================================================

subtitle = tk.Label(
    root,
    text="YOU  VS  COMPUTER",
    font=("Arial", 12, "bold"),
    bg=WOOD_DARK,
    fg=WHITE
)

subtitle.pack()


# ==========================================================
# SCORE BOARD
# ==========================================================

score_frame = tk.Frame(
    root,
    bg=WOOD
)

score_frame.pack(
    pady=20,
    padx=30,
    fill="x"
)


# ----------------------------------------------------------
# PLAYER SCORE
# ----------------------------------------------------------

player_label = tk.Label(
    score_frame,
    text="YOU\n0",
    font=("Arial", 16, "bold"),
    bg=WOOD,
    fg=WHITE,
    width=10
)

player_label.pack(
    side="left",
    padx=20,
    pady=10
)


# ----------------------------------------------------------
# DRAW SCORE
# ----------------------------------------------------------

draw_label = tk.Label(
    score_frame,
    text="DRAW\n0",
    font=("Arial", 16, "bold"),
    bg=WOOD,
    fg=GOLD,
    width=10
)

draw_label.pack(
    side="left",
    padx=20
)


# ----------------------------------------------------------
# COMPUTER SCORE
# ----------------------------------------------------------

computer_label = tk.Label(
    score_frame,
    text="COMPUTER\n0",
    font=("Arial", 16, "bold"),
    bg=WOOD,
    fg=WHITE,
    width=10
)

computer_label.pack(
    side="left",
    padx=20
)


# ==========================================================
# TURN LABEL
# ==========================================================

turn_label = tk.Label(
    root,
    text="YOUR TURN  •  X",
    font=("Arial", 15, "bold"),
    bg=WOOD_DARK,
    fg=WHITE
)

turn_label.pack(
    pady=10
)


# ==========================================================
# GAME BOARD
# ==========================================================

board_frame = tk.Frame(
    root,
    bg=WOOD,
    padx=12,
    pady=12
)

board_frame.pack()


# ==========================================================
# HOVER EFFECT
# ==========================================================

def button_enter(event):

    if (
        event.widget["text"] == ""
        and game_running
    ):

        event.widget.config(
            bg=BUTTON_HOVER
        )


def button_leave(event):

    if (
        event.widget["text"] == ""
        and game_running
    ):

        event.widget.config(
            bg=EMPTY_BOX
        )


# ==========================================================
# CREATE 9 BUTTONS
# ==========================================================

buttons = []


for i in range(9):

    button = tk.Button(
        board_frame,

        text="",

        font=("Arial", 38, "bold"),

        width=4,

        height=2,

        bg=EMPTY_BOX,

        fg=WOOD_DARK,

        activebackground=EMPTY_BOX,

        relief="flat",

        bd=0,

        cursor="hand2",

        command=lambda i=i: player_move(i)
    )

    button.grid(
        row=i // 3,
        column=i % 3,
        padx=5,
        pady=5
    )

    button.bind(
        "<Enter>",
        button_enter
    )

    button.bind(
        "<Leave>",
        button_leave
    )

    buttons.append(button)


# ==========================================================
# CHECK WINNER
# ==========================================================

def check_winner():

    for combo in winning_combinations:

        a = buttons[combo[0]]["text"]

        b = buttons[combo[1]]["text"]

        c = buttons[combo[2]]["text"]


        # Check whether all 3 are same
        if (
            a == b == c
            and a != ""
        ):

            # Change winning boxes to GOLD
            for index in combo:

                buttons[index].config(
                    bg=WIN_COLOR
                )

            return a

    return None


# ==========================================================
# CHECK TIE
# ==========================================================

def check_tie():

    return all(
        button["text"] != ""
        for button in buttons
    )


# ==========================================================
# PLAYER MOVE
# ==========================================================

def player_move(index):

    global game_running


    # ------------------------------------------------------
    # Don't allow player to move while computer is thinking
    # ------------------------------------------------------

    if not game_running:

        return


    # ------------------------------------------------------
    # Don't allow clicking an occupied box
    # ------------------------------------------------------

    if buttons[index]["text"] != "":

        return


    # ======================================================
    # PLAYER PLAYS X
    # ======================================================

    buttons[index].config(
        text="X",

        fg=X_COLOR,

        # IMPORTANT:
        # Color changes IMMEDIATELY
        bg=X_BOX
    )


    # ======================================================
    # PLAY PLAYER WATER DROP SOUND
    # ======================================================

    play_player_move()


    # ======================================================
    # CHECK PLAYER WIN
    # ======================================================

    winner = check_winner()


    if winner == "X":

        end_game(
            "YOU WIN!",
            "Congratulations! You won! 🎉"
        )

        return


    # ======================================================
    # CHECK DRAW
    # ======================================================

    if check_tie():

        end_game(
            "GAME DRAW",
            "Nobody wins this round."
        )

        return


    # ======================================================
    # COMPUTER TURN
    # ======================================================

    game_running = False


    turn_label.config(
        text="COMPUTER IS THINKING..."
    )


    # Computer waits 700 milliseconds
    root.after(
        700,
        computer_move
    )


# ==========================================================
# COMPUTER MOVE
# ==========================================================


def computer_move():

    global game_running

    # ======================================================
    # GET EMPTY BOXES
    # ======================================================

    empty_positions = [
        i
        for i in range(9)
        if buttons[i]["text"] == ""
    ]

    # Safety check
    if not empty_positions:
        return


    # ======================================================
    # COMPUTER DIFFICULTY
    # ======================================================

    # 60% = smart move
    # 40% = random mistake
    #
    # This makes the computer more human-like.

    smart_move = random.random() < 0.60

    move = None


    # ======================================================
    # SMART MOVE
    # ======================================================

    if smart_move:

        # --------------------------------------------------
        # 1. COMPUTER TRIES TO WIN
        # --------------------------------------------------

        move = find_winning_move("O")


        # --------------------------------------------------
        # 2. COMPUTER BLOCKS PLAYER
        # --------------------------------------------------

        if move is None:

            move = find_winning_move("X")


        # --------------------------------------------------
        # 3. TAKE CENTER
        # --------------------------------------------------

        if move is None:

            if buttons[4]["text"] == "":

                move = 4


        # --------------------------------------------------
        # 4. TAKE A CORNER
        # --------------------------------------------------

        if move is None:

            corners = [
                0,
                2,
                6,
                8
            ]

            empty_corners = [
                i
                for i in corners
                if buttons[i]["text"] == ""
            ]

            if empty_corners:

                move = random.choice(
                    empty_corners
                )


    # ======================================================
    # RANDOM / HUMAN-LIKE MISTAKE
    # ======================================================

    if move is None:

        move = random.choice(
            empty_positions
        )


    # ======================================================
    # COMPUTER PLAYS O
    # ======================================================

    buttons[move].config(
        text="O",
        fg=O_COLOR,
        bg=O_BOX
    )


    # ======================================================
    # COMPUTER SOUND
    # ======================================================

    play_computer_move()


    # ======================================================
    # CHECK COMPUTER WIN
    # ======================================================

    winner = check_winner()

    if winner == "O":

        end_game(
            "COMPUTER WINS!",
            "The computer won this round! 🤖"
        )

        return


    # ======================================================
    # CHECK DRAW
    # ======================================================

    if check_tie():

        end_game(
            "GAME DRAW",
            "Nobody wins this round."
        )

        return


    # ======================================================
    # PLAYER TURN
    # ======================================================

    game_running = True

    turn_label.config(
        text="YOUR TURN  •  X"
    )


# ==========================================================
# FIND WINNING MOVE
# ==========================================================

def find_winning_move(player):

    for i in range(9):

        # Only check empty box
        if buttons[i]["text"] == "":


            # ----------------------------------------------
            # Temporarily place symbol
            # ----------------------------------------------

            buttons[i].config(
                text=player
            )


            winning = False


            # ----------------------------------------------
            # Check winning combinations
            # ----------------------------------------------

            for combo in winning_combinations:

                if (
                    buttons[combo[0]]["text"]
                    == buttons[combo[1]]["text"]
                    == buttons[combo[2]]["text"]
                    == player
                ):

                    winning = True

                    break


            # ----------------------------------------------
            # Remove temporary symbol
            # ----------------------------------------------

            buttons[i].config(
                text="",

                bg=EMPTY_BOX
            )


            # ----------------------------------------------
            # Found winning position
            # ----------------------------------------------

            if winning:

                return i


    return None


# ==========================================================
# END GAME
# ==========================================================

def end_game(
    title_text,
    message_text
):

    global game_running

    global player_score

    global computer_score

    global draw_score


    # Stop game
    game_running = False


    # ======================================================
    # UPDATE SCORE
    # ======================================================

    if title_text == "YOU WIN!":

        player_score += 1

        # Victory sound
        play_win_sound()


    elif title_text == "COMPUTER WINS!":

        computer_score += 1

        # Victory sound
        play_win_sound()


    else:

        draw_score += 1

        # Draw sound
        play_draw_sound()


    # ======================================================
    # UPDATE SCOREBOARD
    # ======================================================

    player_label.config(
        text=f"YOU\n{player_score}"
    )


    computer_label.config(
        text=f"COMPUTER\n{computer_score}"
    )


    draw_label.config(
        text=f"DRAW\n{draw_score}"
    )


    # ======================================================
    # SHOW RESULT POPUP
    # ======================================================

    root.after(
        300,
        lambda: show_result(
            title_text,
            message_text
        )
    )


# ==========================================================
# RESULT POPUP
# ==========================================================

def show_result(
    title_text,
    message_text
):

    popup = tk.Toplevel(root)


    popup.title(
        "Game Result"
    )


    popup.geometry(
        "400x300"
    )


    popup.resizable(
        False,
        False
    )


    popup.configure(
        bg=WOOD_DARK
    )


    # Keep popup above main window
    popup.transient(root)

    popup.grab_set()


    # ======================================================
    # POPUP TITLE
    # ======================================================

    tk.Label(
        popup,

        text=title_text,

        font=("Arial", 26, "bold"),

        bg=WOOD_DARK,

        fg=GOLD
    ).pack(
        pady=(40, 10)
    )


    # ======================================================
    # POPUP MESSAGE
    # ======================================================

    tk.Label(
        popup,

        text=message_text,

        font=("Arial", 17, "bold"),

        bg=WOOD_DARK,

        fg=WHITE
    ).pack(
        pady=15
    )


    # ======================================================
    # NEW GAME BUTTON
    # ======================================================

    tk.Button(
        popup,

        text="NEW GAME",

        font=("Arial", 13, "bold"),

        bg=GOLD,

        fg=WOOD_DARK,

        activebackground="#FFD966",

        relief="flat",

        padx=30,

        pady=10,

        cursor="hand2",

        command=lambda:
        close_popup_and_reset(popup)

    ).pack(
        pady=20
    )


# ==========================================================
# CLOSE POPUP AND RESET
# ==========================================================

def close_popup_and_reset(popup):

    popup.destroy()

    reset_game()


# ==========================================================
# RESET GAME
# ==========================================================

def reset_game():

    global game_running


    # ======================================================
    # CLEAR ALL BOXES
    # ======================================================

    for button in buttons:

        button.config(
            text="",

            bg=EMPTY_BOX,

            fg=WOOD_DARK
        )


    # ======================================================
    # START NEW GAME
    # ======================================================

    game_running = True


    turn_label.config(
        text="YOUR TURN  •  X"
    )


# ==========================================================
# START APPLICATION
# ==========================================================

root.mainloop()