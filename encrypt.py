import sys
from alphabet import alphabet

def get_key():
    while True:
        try:
            print("\nEnter encryption key (number)")
            user_input = int(input("> "))

            if user_input:
                if user_input< 0:
                    sys.exit("Invalid Key")
                else:
                    return user_input
            else:
                raise ValueError
        except ValueError:
            break
        except KeyboardInterrupt:
            break


def get_message():
    while True:
        try:
            print("\nEnter your message")
            user_input = input("> ").strip()

            if user_input:
                if any(char.isdigit() for char in user_input):
                   sys.exit("Message can only contain alphabet")
                else:
                    return user_input
            else:
                break
        except ValueError:
            continue 
        except KeyboardInterrupt:
            break


def message_and_key():
    while True:
        try:
            message = get_message()
            if message:
                key = get_key()
                if message and key:
                    return [message, key]
                else:
                    return "Invalid"
            else:
                return "Invalid"

        except KeyboardInterrupt:
            break


def encrypt():
    user = message_and_key()
    new_list = []
    mmm = []

    if "Invalid" in user:
        return "\nEncryption process failed"
    else:
        text = user[0]
        key = user[1]

        for i in text:
            if i == " ":
                new_list.append(" ")         
            elif i.lower() in alphabet:
                index_of_element = alphabet.index(i)
                new_list.append(index_of_element + key) 
            else:
                new_list.append(index_of_element)

        for j in new_list:
            if j == " ":
                mmm.append(" ")
            else:
                mmm.append(alphabet[j])

        return "".join(mmm)

    