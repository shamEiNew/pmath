import plain_message as pm

def create_playfair_msg():
    
    plain_text = pm.plain_text().upper()
    plain_text = plain_text.replace('J', 'I')
    print(plain_text)
    plain_text_stripped = [plain_text[i] for i in range(0,len(plain_text))]
    playfair_message = []
    i = 0 
    while i < len(plain_text_stripped):
        if i == len(plain_text_stripped)-1:
            playfair_message.append(plain_text_stripped[i]+"X")
            i += 1

        elif plain_text_stripped[i]!=plain_text_stripped[i+1]:
            playfair_message.append(plain_text_stripped[i]+plain_text_stripped[i+1])
            i+=2
        else:
            playfair_message.append(plain_text_stripped[i]+"X")
            i+=1
    return playfair_message

def create_playfair_key(key): 
    key = key.upper()
    playfair_keys = []
    key_modi = ""
    for k in key:
        if k not in key_modi:
            key_modi+= k
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in key_modi:
        alphabets = alphabets.replace(letter, "")
    alphabets_reordered = key_modi+alphabets
    playfair_keys.extend(alphabets_reordered)
    playfair_keys.remove('J')
    playfair_key=[playfair_keys[i:i+5] for i in range(0, len(playfair_keys), 5)]
    return playfair_key

def transpose(playfair_key):
    playfair_key_transpose = []
    for i in range(0, len(playfair_key)):
        temp = []
        for j in range(0, len(playfair_key)):
            temp.append(playfair_key[j][i])
        playfair_key_transpose.append(temp)
    return playfair_key_transpose


def encrypt_message(playfair_message=None, a=1):
    enc = []

    for j in playfair_message:

        for i in range(0, len(playfair_key)):

            if (j[0] in playfair_key[i] and j[1] in playfair_key[i]):
                enc.append(
                    playfair_key[i][(playfair_key[i].index(j[0])+a)%5]
                    +
                    playfair_key[i][(playfair_key[i].index(j[1])+a)%5]
                    )


            elif(
                j[0] in playfair_key_transpose[i]
                and 
                j[1] in playfair_key_transpose[i]
                ):
                enc.append(
                    playfair_key_transpose[i][(playfair_key_transpose[i].index(j[0])+a)%5]
                    +
                    playfair_key_transpose[i][(playfair_key_transpose[i].index(j[1])+a)%5]
                    )
            else:
                if(
                    j[0] in playfair_key[i]
                    and
                    j[1] not in playfair_key[i]
                    ):

                    for _ in range(0, len(playfair_key_transpose)):

                        if j[0] in playfair_key_transpose[_] and j[1] not in playfair_key_transpose[_]:

                            for k in range(0, len(playfair_key)):
                                if(
                                    j[1] in playfair_key[k]
                                    ):

                                    row_number_1 = k
                                    column_number_1 = playfair_key[i].index(j[0])

                                    row_number_0 = i
                                    column_number_0 = playfair_key[k].index(j[1])

                                    enc.append(
                                        playfair_key[row_number_0][column_number_0]
                                        +
                                        playfair_key[row_number_1][column_number_1]
                                        )
    return enc

if __name__=="__main__":
    playfair_message = create_playfair_msg()
    playfair_key = create_playfair_key(pm.playfair_key())
    playfair_key_transpose = transpose(playfair_key)
    enc = encrypt_message(playfair_message = playfair_message)
    p = encrypt_message(playfair_message = enc, a=-1)
    print("".join(enc).lower())
    print("".join(p).lower())