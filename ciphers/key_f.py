"""STILL UNDER PROCESS TRYING TO GET A BEST METHOD. Since I want to modify string and eliminate all
repetitive elements exept the first one"""

def create_playfair_key(key): 
    key = key.upper()
    playfair_keys = []
    key_modi = ""
    for k in key:
        if k not in key_modi:
            key_modi+= k
    print(key_modi)
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in key_modi:
        print(letter, end=' ')
        alphabets = alphabets.replace(letter, "")
    alphabets_reordered = key_modi+alphabets
    playfair_keys.extend(alphabets_reordered)
    playfair_keys[playfair_keys.index('I')]= 'I J'
    playfair_keys.remove('J')
    print(playfair_keys)
    playfair_key=[playfair_keys[i:i+5] for i in range(0, len(playfair_keys), 5)]
    #alphabets_reordered = alphabets_reordered.replace("I", "IJ")
    return playfair_key

create_playfair_key('playfair')