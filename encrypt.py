from input import message_and_key 
from alphabet import alphabet

def encrypt():
    user = message_and_key()
    message = user[0]
    key = user[1]
    index_store = []
    new_string = []

    for char in message:
        if char == " ":
            index_store.append(" ")
        elif char not in alphabet:
            index_store.append(char)
        if char in alphabet:
            index_store.append(alphabet.index(char) + key)

    for char in index_store:
        if type(char) == str:
            new_string.append(char)
        else:
            new_string.append(alphabet[char%len(alphabet)])

    return f"Here's your encrypted message:\n{''.join(new_string)}"
