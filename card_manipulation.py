import pyautogui

# The entire region for the game is (1676, 167, 2522, 1485)
tableau_region = (1676, 366, 846, 845)
foundation_region = (1676, 185, 2155, 240)
waste_region = (2176, 190, 2392, 253)

current_tableau = {}


def update_cards(cards):
    # TODO: Check entire game for card. if it exists, check if it is in the tableau or foundation.
    # Two birds with one stone!!

    for card in cards:
        try:
            check_for_card = pyautogui.locateCenterOnScreen(image=cards[card], region=tableau_region, confidence=0.965)

            # if region[0] <= check_for_card[0] <= region[2] and region[1] <= check_for_card[1] <= region[3]:
            current_tableau[card] = check_for_card

        except pyautogui.ImageNotFoundException:
            pass

    print(current_tableau)
