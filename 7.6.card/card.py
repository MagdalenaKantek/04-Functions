def hide(card_number):
    result = card_number[:2] + "*" * 10 + card_number[-4:]
    return result