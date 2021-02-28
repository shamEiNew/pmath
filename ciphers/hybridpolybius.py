def create_playfair_msg():

    plain_text = "HELLO WORLD"
    plain_text = plain_text.replace(" ","")
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
        print(letter, end=' ')
        alphabets = alphabets.replace(letter, "")
    alphabets_reordered = key_modi+alphabets
    playfair_keys.extend(alphabets_reordered)
    playfair_keys[playfair_keys.index('I')]= 'IJ'
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

    
playfair_message = create_playfair_msg()
print(playfair_message)
playfair_key = create_playfair_key('PLAYFAIR')
print(playfair_key)
playfair_key_transpose = transpose(playfair_key)
print(playfair_key_transpose)

enc = []

for j in range(0, len(playfair_message)):
    flag = 0
    for i in range(0, len(playfair_key)):

        if (
            playfair_message[j][0] in playfair_key[i]
            and 
            playfair_message[j][1] in playfair_key[i]
            ):
            enc.append(
                playfair_key[i][(playfair_key[i].index(playfair_message[j][0])+1)%5]
                +
                playfair_key[i][(playfair_key[i].index(playfair_message[j][1])+1)%5]
                )


        elif(
            playfair_message[j][0] in playfair_key_transpose[i]
            and 
            playfair_message[j][1] in playfair_key_transpose[i]
            ):
            enc.append(
                playfair_key_transpose[i][(playfair_key_transpose[i].index(playfair_message[j][0])+1)%5]
                +
                playfair_key_transpose[i][(playfair_key_transpose[i].index(playfair_message[j][1])+1)%5]
                )
        else:
            if(
                playfair_message[j][0] in playfair_key[i]
                and
                playfair_message[j][1] not in playfair_key[i]
                ):
                for _ in range(0, len(playfair_key_transpose)):
                    if playfair_message[j][0] in playfair_key_transpose[_] and playfair_message[j][1] not in playfair_key_transpose[_]:
                        for k in range(0, len(playfair_key)):
                            if(
                                playfair_message[j][1] in playfair_key[k]
                                ):

                                row_number_1 = k
                                column_number_1 = playfair_key[i].index(playfair_message[j][0])

                                row_number_0 = i
                                column_number_0 = playfair_key[k].index(playfair_message[j][1])

                                enc.append(
                                    playfair_key[row_number_0][column_number_0]
                                    +
                                    playfair_key[row_number_1][column_number_1]
                                    )
                            flag+=1
                            if j == 2: print(f"alla{flag}")
    


                
    #print(f"The element is {j} and flag is {flag}")    
print(enc)