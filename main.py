import os
from pathlib import Path
import multiprocessing

import pyautogui
import time

import card_manipulation

cards_path = "C:\\Users\\Sqidy\\PycharmProjects\\pythonProject\\card_imgs\\"
cards = {}
card_order = {"Red": [], "Black": []}

regions = [
    (1676, 366, 122, 845),
    (1798, 366, 120, 845),
    (1918, 366, 120, 845),
    (2038, 366, 121, 845),
    (2159, 366, 121, 845),
    (2280, 366, 120, 845),
    (2400, 366, 122, 845)]


# def main():
#     while True:
#         print(pyautogui.position())
#         time.sleep(2)


def set_card_key_to_value():
    for card in os.listdir(cards_path):
        cards[Path(cards_path + card).stem] = cards_path + card


def set_card_order():
    for card in open("CardOrder.txt", "r"):
        if "Hearts" in card or "Diamonds" in card:
            card_order["Red"].append(card.strip())
        elif "Clubs" in card or "Spades" in card:
            card_order["Black"].append(card.strip())


if __name__ == "__main__":
    set_card_key_to_value()
    set_card_order()

    card_manipulation.update_cards(cards)

# import multiprocessing
# import time
#
#
# def task():
#     print('Sleeping for 0.5 seconds')
#     time.sleep(0.5)
#     print('Finished sleeping')
#
#
# if __name__ == "__main__":
#     start_time = time.perf_counter()
#     processes = []
#
#     # Creates 10 processes then starts them
#     for i in range(10):
#         p = multiprocessing.Process(target=task)
#         p.start()
#         processes.append(p)
#
#     # Joins all the processes
#     for p in processes:
#         p.join()
#
#     finish_time = time.perf_counter()
#
#     print(f"Program finished in {finish_time - start_time} seconds")
