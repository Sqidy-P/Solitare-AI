import pyautogui

# The entire region for the game is (1676, 167, 2522, 1485)
tableau_region = (1676, 366, 846, 845)
foundation_region = (1676, 185, 479, 55)
waste_region = (2176, 190, 216, 63)

current_tableau = {}


def update_cards(cards, region):
    # Creates a PIL.Image, allowing for faster processing.
    ss = pyautogui.screenshot(region=region)

    for card in cards:
        try:
            # Gets the coords of the image based on the region "haystackImage."
            check_for_card = pyautogui.center(pyautogui.locate(needleImage=cards[card], haystackImage=ss, confidence=0.965))

            # Offsets the given coords so that it matches with the location of the card.
            check_for_card = (check_for_card[0]+region[0], check_for_card[1]+region[1])

            # Adds it to current_tableau in the form of "card" as name and "check_for_card" as coords.
            current_tableau[card] = check_for_card

        # If no result is returned, just ignore it.
        except pyautogui.ImageNotFoundException:
            pass

    print(current_tableau)
