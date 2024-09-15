import time

import pyautogui

# The entire region for the game is (1676, 167, 2522, 1220)

# game_region is given as (x, y, w, h)
game_region = (1676, 167, 846, 1053)
# These are given as (x1, y1, x2, y2)
tableau_region = (1676, 366, 2522, 1211)
foundation_region = (1676, 185, 2155, 240)
waste_region = (2176, 190, 2392, 253)

current_tableau = {}
current_foundation = {}
waste = {}


def solve(card_order, region=current_tableau):
    print("SOLVING")
    time.sleep(0.2)
    # for card in current_tableau:
    #     if "Ace" in card:
    #         pyautogui.click(current_tableau[card])
    #     else:
    #         if "Hearts" in card or "Diamonds" in card:
    #             black_index = card_order["Red"].index(card) + 1
    #
    #             try:
    #                 black_card = card_order["Black"][black_index] in current_tableau.keys()
    #
    #                 if black_card:
    #                     pyautogui.click(current_tableau[card_order["Black"][black_index]])
    #
    #                 else:
    #                     black_card = card_order["Black"][black_index + 13] in current_tableau.keys()
    #                     if black_card:
    #                         pyautogui.click(current_tableau[card_order["Black"][black_index + 13]])
    #             except IndexError:
    #                 black_card = card_order["Black"][black_index - 13] in current_tableau.keys()
    #                 if black_card:
    #                     pyautogui.click(current_tableau[card_order["Black"][black_index - 13]])
    #
    #         elif "Clubs" in card or "Spades" in card:
    #             red_index = card_order["Black"].index(card) + 1
    #
    #             try:
    #                 red_card = card_order["Red"][red_index] in current_tableau.keys()
    #
    #                 if red_card:
    #                     pyautogui.click(current_tableau[card_order["Red"][red_index]])
    #
    #                 else:
    #                     red_card = card_order["Red"][red_index + 13] in current_tableau.keys()
    #                     if red_card:
    #                         pyautogui.click(current_tableau[card_order["Red"][red_index + 13]])
    #             except IndexError:
    #                 red_card = card_order["Red"][red_index - 13] in current_tableau.keys()
    #                 if red_card:
    #                     pyautogui.click(current_tableau[card_order["Red"][red_index - 13]])
    #
    #         else:
    #             print("UNKNOWN CARD.")
    #
    #     # if card_order["Red"].index(card) - 1 in current_tableau.keys():
    #     #     pyautogui.click(card)
    #     #
    #     # elif card_order["Black"].index(card) - 1 in current_tableau.keys():
    #     #     pyautogui.click(card)

    for card in region:
        if "Ace" in card and region != current_foundation:
            pyautogui.click(region[card])
        else:
            try:
                card_index, color = card_order["Red"].index(card), "Red"
            except ValueError:
                card_index, color = card_order["Black"].index(card), "Black"

            if region == current_foundation:
                card_index -= 1

                card_fetched = card_order[color][card_index]

                if card_fetched in current_tableau.keys():
                    pyautogui.click(current_tableau[card_fetched])
                elif card_fetched in waste.keys():
                    pyautogui.click(waste[card_fetched])


def update_cards(cards, region=game_region):
    # Gets a new card from the stock
    pyautogui.click(2456, 258, interval=0.15, clicks=1)

    # Creates a PIL.Image, allowing for faster processing.
    ss = pyautogui.screenshot(region=region)

    for card in cards:
        try:
            # Gets the coords of the image based on the region "haystackImage."
            check_for_card = pyautogui.center(
                pyautogui.locate(haystackImage=ss, needleImage=cards[card], confidence=0.965))

            # Offsets the given coords so that it matches with the location of the card.
            check_for_card = (check_for_card[0]+region[0], check_for_card[1]+region[1])

            # If the card's coords are inbetween x1, x2 of "foundation_region", and y1, y2 of "foundation_region",
            # place the card under "current_foundation"
            in_foundation = (foundation_region[0] <= check_for_card[0] <= foundation_region[2] and
                             foundation_region[1] <= check_for_card[1] <= foundation_region[3])

            # If the card's coords are inbetween x1, x2 of "tableau_region", and y1, y2 of "tableau_region",
            # place the card under "current_tableau"
            in_tableau = (tableau_region[0] <= check_for_card[0] <= tableau_region[2] and
                          tableau_region[1] <= check_for_card[1] <= tableau_region[3])

            if in_foundation:
                current_foundation[card] = check_for_card

            elif in_tableau:
                current_tableau[card] = check_for_card

            else:
                waste[card] = check_for_card

        # If no result is returned, just ignore it.
        except pyautogui.ImageNotFoundException:
            pass

    # Debugging
    print("Current Foundation: ")
    print(current_foundation)
    print("Current Tableau: ")
    print(current_tableau)
    print("Current Waste: ")
    print(waste)
