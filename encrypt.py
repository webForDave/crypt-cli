import sys
from alphabet import alphabet

exit_string = "\nProgram interupted with the keyboard\n"

def get_key():
    try:
        print("\nEnter encryption key (number)")
        user_input = int(input("> "))

        if user_input:
            if user_input == 0:
                sys.exit("Zero isn't valid")
            if user_input< 0:
                sys.exit("\nKey must be a positive integer\n")
            else:
                return user_input
        else:
            raise ValueError
    except ValueError:
        sys.exit("\nInvalid Key, must be an integer\n")
    except KeyboardInterrupt:
        sys.exit(exit_string)


def get_message():
    try:
        print("\nEnter your message")
        user_input = input("> ").strip()

        if user_input:
            return user_input
        else:
            sys.exit("\nYou need to input a message\n")
    except ValueError:
        sys.exit("\nMessage cannot be a number\n") 
    except KeyboardInterrupt:
        sys.exit(exit_string)


def message_and_key():
    try:
        message = get_message()
        if message:
            key = get_key()
            if message and key:
                return [message, key]
    except KeyboardInterrupt:
        sys.exit(exit_string)


def encrypt():
    return message_and_key()
    