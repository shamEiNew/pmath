
def plain_text():
    text = input("Enter the message to be encrypted\n")
    text = "".join(e for e in text if e.isalpha())
    return text

def playfair_key():
    text = input("Enter the key for encryption\n").strip()
    text = "".join(e for e in text if e.isalpha())
    return text