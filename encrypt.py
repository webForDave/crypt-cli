import sys

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
            user_input = input("> ")

            if user_input:
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

    if "Invalid" in user:
        return "\nEncryption process failed"
    else:
        pass
             