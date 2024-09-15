import os
from pathlib import Path

from PIL import Image

import card_manipulation

cards_path = "C:\\Users\\Sqidy\\PycharmProjects\\pythonProject\\card_imgs\\"
cards = {}
card_order = {"Red": [], "Black": []}


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


# Sets the order of how the cards in the game are supposed to be ordered.
# Allows for figuring out what cards go together.
def set_card_order():
    # Read every line in CardOrder.txt.
    for card in open("CardOrder.txt", "r"):
        # If it's Hearts or Diamonds, put it into the Red key.
        if "Hearts" in card or "Diamonds" in card:
            card_order["Red"].append(card.strip())
        # If it's Clubs or Spades, put it into the Black key.
        elif "Clubs" in card or "Spades" in card:
            card_order["Black"].append(card.strip())


if __name__ == "__main__":
    set_card_key_to_value()
    set_card_order()

    card_manipulation.update_cards(cards)
    card_manipulation.solve(card_order, region=card_manipulation.current_foundation)

    # main()
