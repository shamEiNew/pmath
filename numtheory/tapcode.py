import winsound
import time
from numtheory import playfair
from numtheory import _hybrid_polybius as h


def tap(polybius_message):
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    for letter in polybius_message:
        for _ in range(int(letter[0])): winsound.Beep(frequency, duration)
        time.sleep(0.5)
        for _ in range(int(letter[1])): winsound.Beep(frequency, duration)
        time.sleep(2)

def encrypt_to_playfair():
    playfair_message = playfair.create_playfair_msg()
    playfair_key = playfair.create_playfair_key()
    playfair_key_transpose = playfair.transpose(playfair_key)
    enc = playfair.encrypt_message(playfair_key, playfair_key_transpose, playfair_message = playfair_message)
    print("".join(enc).lower())
    p = playfair.encrypt_message(playfair_key, playfair_key_transpose, playfair_message = enc, a=-1)
    print("".join(p).lower())
    hybrid_message = h.hybrid_polybius("".join(enc), playfair_key)
    print("".join(hybrid_message))
    tap(hybrid_message)

encrypt_to_playfair()

