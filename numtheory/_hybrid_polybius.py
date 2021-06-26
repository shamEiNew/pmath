from numtheory import playfair

def hybrid_polybius(playfair_cipher, playfair_key):
    hybrid = []
    for letter in playfair_cipher:
        for i in range(0, len(playfair_key)):
            for j in range(0, len(playfair_key)):
                if playfair_key[i][j]==letter:
                    hybrid.append(str(i+1)+str(j+1))
    return hybrid

def encrypt_to_playfair():
    playfair_message = playfair.create_playfair_msg()
    playfair_key = playfair.create_playfair_key()
    playfair_key_transpose = playfair.transpose(playfair_key)
    enc = playfair.encrypt_message(playfair_key, playfair_key_transpose, playfair_message = playfair_message)
    print("".join(enc).lower())
    p = playfair.encrypt_message(playfair_key, playfair_key_transpose, playfair_message = enc, a=-1)
    print("".join(p).lower())
    hybrid_message = hybrid_polybius("".join(enc), playfair_key)
    print("".join(hybrid_message))