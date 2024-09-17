import os
from pathlib import Path

from PIL import Image

import card_manipulation

cards_path = "C:\\Users\\Sqidy\\PycharmProjects\\Solitare-AI\\card_imgs\\"
cards = {}
card_order_temp = {"Red": [], "Black": []}
card_order = {}


# def main():
#     import time
#     import pyautogui
#
#     while True:
#         print(pyautogui.position())
#         time.sleep(2)


# Sets the key to the images, the names, and the value which is what Image.open is returning.
def set_card_key_to_value():
    for card in os.listdir(cards_path):
        # cards[Path(cards_path + card).stem] gets the name. Image.open opens the image into memory, allowing for
        # exponentially higher speeds, with the downside of more ram usage.
        cards[Path(cards_path + card).stem] = Image.open("card_imgs\\"+card)


# Connects each card with its corresponding card
# e.g. EightOfHearts to NineOfClubs and NineOfSpades
def set_card_connections(color):
    opp = ""

    # For every card that's red or black
    for card in range(26):
        # Get the reversed color
        if color == "Red":
            opp = "Black"
        else:
            opp = "Red"

        # Set the key equal to the card the computer is going to associate
        key = card_order_temp[color][card]
        # Get the card it associates to
        value = card_order_temp[opp][card - 1]

        # Ignore any King or Ace cards as to not associate the two
        if "King" in key or "Ace" in key:
            pass
        else:
            # Add the card and give it its corresponding card
            card_order[key] = [value]

            try:
                # Since there are two red or black cards it can connect to,
                # check for one twelve positions down. It will return an error
                # if the card associated as value is already a Diamonds or Spades.
                value = card_order_temp[opp][card + 12]

                card_order[key].append(value)

            except IndexError:
                # If it's already a Diamonds or Spades, get the other card (Hearts or Clubs)
                value = card_order_temp[opp][card - 14]

                card_order[key].append(value)


# Sets the order of how the cards in the game are supposed to be ordered.
# Allows for figuring out what cards go together.
def set_card_order():
    # Read every line in CardOrder.txt.
    for card in open("CardOrder.txt", "r"):
        # If it's Hearts or Diamonds, put it into the Red key.
        if "Hearts" in card or "Diamonds" in card:
            card_order_temp["Red"].append(card.strip())
        # If it's Clubs or Spades, put it into the Black key.
        elif "Clubs" in card or "Spades" in card:
            card_order_temp["Black"].append(card.strip())

    # Associates a card with its corresponding values.
    # e.g. EightOfHearts to NineOfClubs and NineOfSpades
    set_card_connections("Red")
    set_card_connections("Black")


if __name__ == "__main__":
    set_card_key_to_value()
    set_card_order()
