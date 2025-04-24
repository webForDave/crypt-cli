import sys

exit_string = "\nProgram interupted with the keyboard\n"

def get_user_key():
    while True:
        try:
            print("\nEnter encryption key (number)")
            user_key = int(input("> "))

            if user_key:
                if user_key == 0 or user_key < 0:
                    print("Invalid number")
                    get_another_number = input("\nDo you want to use another number? Y/N ").lower().strip()

                    if get_another_number in ["yes", "y"]:
                        continue
                    elif get_another_number in ["no", "n"]:
                        print("Program successfully aborted")
                        break
                    else:
                        print("Invalid input")
                        break
                else:
                    return user_key
            else:
                raise ValueError
        except ValueError:
            print("\nInvalid, key must be an integer\n")
            break
        except KeyboardInterrupt:
            sys.exit(exit_string)


def get_user_message():
    while True:
        try:
            print("\nEnter your message")
            user_message = input("> ").strip()

            if user_message:
                if any(char.isdigit() for char in user_message):
                    raise ValueError
                return user_message
            else:
                print("\nYou need to input a message\n")
                continue
        except ValueError:
            print("\nMessage cannot contain a number\n") 
            get_another_text = input("Do you want to input another text? Y/N ").strip().lower()
            if get_another_text in ["yes", "y"]:
                continue
            elif get_another_text in ["no", 'n']:
                print("Program successfully aborted")
                break
            else:
                break
        except KeyboardInterrupt:
            sys.exit(exit_string)


def message_and_key():
    message = get_user_message()
    if message:
        key = get_user_key()
        if key:
            return [message, key]

