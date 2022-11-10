import Classes
import helper_functions as hf


def chapter_1():
    # Initialize player
    player1 = Classes.Player("Ricardo")

    # Read line and then choice
    hf.read_line_helper("Chapter 1")
    response = input()
    if response.lower().strip() == "yes":
        chapter_2(player1)
    else:
        chapter_3(player1)


def chapter_2(player):
    # Prints the text
    hf.read_line_helper("Chapter 2")

    # Assigns weapon
    player.assign_weapon(Classes.Pistol(6, 1))

    # Choice
    response = input()
    if response.lower().strip() == "no":
        hf.read_line_helper("Chapter 3")
    else:
        chapter_4(player)


def chapter_3(player):
    hf.read_line_helper("Chapter 3")


def chapter_4(player):
    hf.read_line_helper("Chapter 4")


if __name__ == '__main__':
    chapter_1()
