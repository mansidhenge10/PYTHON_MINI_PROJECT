import winsound
import os


# ==========================================================
# SOUND FILE LOCATION
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


# ==========================================================
# PLAY SOUND WITHOUT OVERLAPPING
# ==========================================================

def play_sound(filename):

    sound_file = os.path.join(
        BASE_DIR,
        filename
    )

    if not os.path.exists(sound_file):

        print("Sound file not found:", sound_file)

        return

    # Stop previous sound
    winsound.PlaySound(
        None,
        0
    )

    # Start new sound immediately
    winsound.PlaySound(
        sound_file,
        winsound.SND_FILENAME |
        winsound.SND_ASYNC
    )


def play_player_move():
    pass


def play_computer_move():
    pass


def play_win_sound():
    pass


def play_draw_sound():
    pass