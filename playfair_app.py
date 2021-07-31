import streamlit as st
from pymath.numtheory import _playfair as playfair



def plain_message():
    #Plain message for conversion and also check whether it is alpha numeric.

    message = st.text_input("Enter text to be encrypted:",value="There is going to be attack on titan.", help="Note this values must be only letters")
    
    if 'msg' not in st.session_state:
        st.session_state['msg'] = message
    st.session_state['msg'] = message
    st.write(f"Entered message: {st.session_state.msg}")
    message = "".join(e for e in message if e.isalpha())

    key = st.text_input("Enter key:",value="Humanoids", help="Note this values must be only letters")

    if 'key' not in st.session_state:
        st.session_state['key']=key
    st.session_state['key'] = key
    st.write(f"Entered key: {st.session_state.key}")

    key = "".join(e for e in key if e.isalpha())
    if (message and key):
        return message, key
    return None, None

def playfair_encrypt():
    #generate key message pair
    message, key = plain_message()

    #key and message if not none pre-process them for encryption
    try:
        message, key = playfair.create_playfair_msg(message), playfair.create_playfair_key(key)
        key_transpose = playfair.transpose(key)
    except:
        st.markdown("Enter message and key value for for encryption")


    #After preprocess encrypt using the key matrix.
    try:

        encrypted_message = playfair.encrypt_message(key, key_transpose,message, 1)
        st.markdown(f'Encrypted Message: {"".join(s for s in encrypted_message)}')
        msg_decrypted = playfair.encrypt_message(key, key_transpose,encrypted_message, -1)
       
        if st.button("Decrypt"):
            st.markdown(f'Decrypted Message:{"".join(s for s in msg_decrypted)}')
    except:
        st.markdown("Enter valid values, if the error still exits it will be logged.")

def main():
    columns =  st.beta_columns(2)

    with columns[0]:
        st.header("Playfair Cipher")
        st.markdown("""From Wiki:""")
        st.markdown("""\n The Playfair cipher or 
        Playfair square or Wheatstone–Playfair cipher is
        a manual symmetric encryption technique and was
        the first literal digram substitution cipher.
        The scheme was invented in 1854 by Charles Wheatstone,
        but bears the name of Lord Playfair for promoting its use.""")
        st.write("[Playfair Cipher](https://en.wikipedia.org/wiki/Playfair_cipher)")
    with columns[1]:
        playfair_encrypt()